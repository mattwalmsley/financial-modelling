"""
Option chain data fetching functionality.

This module provides high-level functions for fetching option chain data from Bloomberg,
with support for filtering, batching, extensible field selection, and comprehensive
error handling.
"""

import logging
from datetime import date, datetime, timedelta
from typing import Any

import blpapi
import pandas as pd

from bbg_data.api.requests import RequestBuilder, ResponseParser, to_dataframe
from bbg_data.core.enums import BloombergField, OptionType, ServiceType
from bbg_data.core.models import (
    ATMOptionDataPoint,
    ErrorDetail,
    HistoricalDataPoint,
    OptionContract,
    OptionMarketData,
    ReferenceDataPoint,
    Response,
)
from bbg_data.core.session import BloombergSession, session

logger = logging.getLogger(__name__)


def _is_third_friday(d: date) -> bool:
    """
    Check if a date is the third Friday of the month (monthly option expiration).

    Args:
        d: Date to check

    Returns:
        True if the date is the third Friday of the month
    """
    # Check if it's a Friday (weekday 4)
    if d.weekday() != 4:
        return False

    # Calculate which Friday of the month this is
    # Get the first day of the month
    first_day = d.replace(day=1)

    # Find the first Friday of the month
    days_until_friday = (4 - first_day.weekday()) % 7
    first_friday = first_day + timedelta(days=days_until_friday)

    # Third Friday is 14 days after first Friday
    third_friday = first_friday + timedelta(days=14)

    return d == third_friday


# Default fields for option chain queries
DEFAULT_OPTION_FIELDS = [
    BloombergField.OPT_STRIKE_PX,
    BloombergField.OPT_PUT_CALL,
    BloombergField.OPT_EXPIRE_DT,
    BloombergField.OPT_UNDL_TICKER,
    BloombergField.PX_SETTLE,
    BloombergField.PX_LAST,
    BloombergField.PX_BID,
    BloombergField.PX_ASK,
    BloombergField.IVOL_MID,
    BloombergField.OPT_DELTA,
    BloombergField.OPT_GAMMA,
    BloombergField.OPT_THETA,
    BloombergField.OPT_VEGA,
    BloombergField.VOLUME,
    BloombergField.OPEN_INT,
]


class OptionChainFetcher:
    """
    Fetches option chain data from Bloomberg.

    Provides methods for discovering option contracts and fetching market data
    with type-safe field specifications and filtering.
    """

    def __init__(
        self,
        session: BloombergSession,
        batch_size: int = 50,
    ) -> None:
        """
        Initialize option chain fetcher.

        Args:
            session: Active Bloomberg session
            batch_size: Number of securities per batch request (max typically 500)
        """
        self.session = session
        self.batch_size = batch_size
        self.request_builder = RequestBuilder(session, ServiceType.REFDATA)

    def get_option_chain(
        self,
        underlying: str,
        as_of_date: date | None = None,
    ) -> list[str]:
        """
        Get list of option tickers for an underlying security.

        This method returns the raw option chain from Bloomberg without any filtering.
        Use _get_option_contracts_from_reference_data to get contract details and filter.

        Args:
            underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
            as_of_date: Date to fetch option chain as-of (uses current date if None)

        Returns:
            List of option ticker strings (may be in human-readable or FIGI format)

        Example:
            >>> fetcher = OptionChainFetcher(session)
            >>> # Fetch current option chain
            >>> tickers = fetcher.get_option_chain("NVDA US Equity")
            >>> # Fetch option chain as of specific date
            >>> tickers = fetcher.get_option_chain("AAPL US Equity", date(2023, 8, 12))
        """
        logger.info(f"Fetching option chain for {underlying}")

        # Request OPT_CHAIN field
        overrides = None
        if as_of_date:
            overrides = {"SINGLE_DATE_OVERRIDE": as_of_date.strftime("%Y%m%d")}

        request = self.request_builder.create_reference_request(
            securities=[underlying],
            fields=[BloombergField.OPT_CHAIN],
            overrides=overrides,
        )

        self.session.send_request(request)

        # Collect all option tickers
        all_tickers: list[str] = []

        while True:
            event = self.session.next_event()

            for msg in event:
                if msg.messageType() == blpapi.Name("ReferenceDataResponse"):
                    sec_data_array = msg.getElement("securityData")

                    for i in range(sec_data_array.numValues()):
                        sec_data = sec_data_array.getValueAsElement(i)

                        if sec_data.hasElement("fieldData"):
                            field_data = sec_data.getElement("fieldData")

                            if field_data.hasElement("OPT_CHAIN"):
                                chain_element = field_data.getElement("OPT_CHAIN")

                                for j in range(chain_element.numValues()):
                                    option_element = chain_element.getValueAsElement(j)

                                    if option_element.hasElement("Security Description"):
                                        ticker = option_element.getElementAsString(
                                            "Security Description"
                                        )
                                        all_tickers.append(ticker)

            if event.eventType() == blpapi.Event.RESPONSE:
                break

        logger.info(f"Found {len(all_tickers)} total options in chain")

        return all_tickers

    def get_option_market_data(
        self,
        tickers: list[str],
        fields: list[BloombergField] | None = None,
        as_of_date: date | None = None,
    ) -> Response[list[OptionMarketData]]:
        """
        Fetch market data for option contracts with error handling.

        Always fetches contract identification fields (expiry, strike, put/call, underlying)
        in addition to requested market data fields to properly construct OptionContract objects.

        Args:
            tickers: List of option Bloomberg tickers (any format including FIGI)
            fields: Market data fields to fetch (uses defaults if None)
            as_of_date: Data as-of date (uses current if None)

        Returns:
            Response containing list of option market data objects and any errors

        Example:
            >>> tickers = ["NVDA US 11/21/25 C177.5 Equity"]
            >>> response = fetcher.get_option_market_data(tickers)
            >>> data = response.data
            >>> if response.has_errors:
            ...     response.print_errors()
        """
        if fields is None:
            fields = DEFAULT_OPTION_FIELDS.copy()
        else:
            fields = fields.copy()

        if as_of_date is None:
            as_of_date = date.today()

        logger.info(f"Fetching market data for {len(tickers)} options")

        all_data: list[ReferenceDataPoint] = []
        all_errors: list[ErrorDetail] = []

        # Batch requests to avoid Bloomberg limits
        for i in range(0, len(tickers), self.batch_size):
            batch = tickers[i : i + self.batch_size]
            logger.debug(f"Processing batch {i // self.batch_size + 1} ({len(batch)} securities)")

            try:
                overrides = None
                if as_of_date != date.today():
                    overrides = {"SINGLE_DATE_OVERRIDE": as_of_date.strftime("%Y%m%d")}

                request = self.request_builder.create_reference_request(
                    securities=batch,
                    fields=fields,
                    overrides=overrides,
                )

                self.session.send_request(request)

                # Collect responses
                while True:
                    event = self.session.next_event()
                    response = ResponseParser.parse_reference_data(event)
                    all_data.extend(response.data)
                    all_errors.extend(response.errors)

                    if event.eventType() == blpapi.Event.RESPONSE:
                        break

            except Exception as e:
                logger.error(f"Error fetching batch {i // self.batch_size + 1}: {e}")
                # Add error but continue with next batch
                err = ErrorDetail(
                    timestamp=datetime.now(),
                    error_type="BatchRequestError",
                    message=f"Failed to fetch batch {i // self.batch_size + 1}: {str(e)}",
                    context={"batch_index": i // self.batch_size, "batch_size": len(batch)},
                    exception=e,
                )
                all_errors.append(err)

        # Log summary of errors if any occurred
        if all_errors:
            logger.warning(f"Encountered {len(all_errors)} errors during data fetch")

        # Convert to OptionMarketData objects
        market_data = self._to_option_market_data(all_data, as_of_date)
        return Response(data=market_data, errors=all_errors)

    def get_historical_option_data(
        self,
        tickers: list[str],
        start_date: date,
        end_date: date,
        fields: list[BloombergField] | None = None,
    ) -> pd.DataFrame:
        """
        Fetch historical data for option contracts.

        Args:
            tickers: List of option Bloomberg tickers
            start_date: Start date (inclusive)
            end_date: End date (inclusive)
            fields: Fields to fetch (uses settlement price if None)

        Returns:
            DataFrame with historical option data

        Example:
            >>> from datetime import date
            >>> tickers = ["NVDA US 11/21/25 C177.5 Equity"]
            >>> df = fetcher.get_historical_option_data(
            ...     tickers,
            ...     start_date=date(2024, 10, 1),
            ...     end_date=date(2024, 10, 24)
            ... )
        """
        if fields is None:
            fields = [BloombergField.PX_SETTLE]

        logger.info(
            f"Fetching historical data for {len(tickers)} options from {start_date} to {end_date}"
        )

        all_data: list[HistoricalDataPoint] = []
        all_errors: list[ErrorDetail] = []

        # Batch requests
        for i in range(0, len(tickers), self.batch_size):
            batch = tickers[i : i + self.batch_size]

            try:
                request = self.request_builder.create_historical_request(
                    securities=batch,
                    fields=fields,
                    start_date=start_date,
                    end_date=end_date,
                )

                self.session.send_request(request)

                # Collect responses
                while True:
                    event = self.session.next_event()
                    response = ResponseParser.parse_historical_data(event)
                    all_data.extend(response.data)
                    all_errors.extend(response.errors)

                    if event.eventType() == blpapi.Event.RESPONSE:
                        break

            except Exception as e:
                logger.error(f"Error fetching historical batch {i // self.batch_size + 1}: {e}")
                # Add error but continue with next batch
                err = ErrorDetail(
                    timestamp=datetime.now(),
                    error_type="HistoricalBatchError",
                    message=f"Failed to fetch historical batch: {str(e)}",
                    context={
                        "batch_index": i // self.batch_size,
                        "start_date": str(start_date),
                        "end_date": str(end_date),
                    },
                    exception=e,
                )
                all_errors.append(err)

        # Log summary of errors if any occurred
        if all_errors:
            logger.warning(f"Encountered {len(all_errors)} errors during historical data fetch")

        # Convert to DataFrame
        return to_dataframe(all_data)

    def _get_option_contracts_from_reference_data(
        self,
        tickers: list[str],
        underlying: str,
        as_of_date: date | None = None,
    ) -> list[OptionContract]:
        """
        Fetch option contract details from Bloomberg reference data.

        This method is more robust than string parsing as it works with both
        human-readable tickers and FIGI format tickers. When using historical
        dates with SINGLE_DATE_OVERRIDE, Bloomberg may return FIGI tickers
        (e.g., 'BBG01QQKDSZ4 Equity') which cannot be parsed via string manipulation.

        Args:
            tickers: List of option Bloomberg tickers (any format)
            underlying: Bloomberg ticker of underlying security
            as_of_date: Date to fetch reference data as-of (uses current date if None)

        Returns:
            List of OptionContract objects with data from reference fields
        """
        if not tickers:
            return []

        logger.debug(f"Fetching reference data for {len(tickers)} tickers")

        # Fetch reference data for option-specific fields
        fields = [
            BloombergField.OPT_EXPIRE_DT,
            BloombergField.OPT_STRIKE_PX,
            BloombergField.OPT_PUT_CALL,
            BloombergField.OPT_UNDL_TICKER,
        ]

        overrides = None
        if as_of_date:
            overrides = {"SINGLE_DATE_OVERRIDE": as_of_date.strftime("%Y%m%d")}

        all_data: list[ReferenceDataPoint] = []

        # Batch requests to avoid Bloomberg limits
        for i in range(0, len(tickers), self.batch_size):
            batch = tickers[i : i + self.batch_size]

            try:
                request = self.request_builder.create_reference_request(
                    securities=batch,
                    fields=fields,
                    overrides=overrides,
                )

                self.session.send_request(request)

                # Collect responses
                while True:
                    event = self.session.next_event()
                    response = ResponseParser.parse_reference_data(event)
                    all_data.extend(response.data)

                    if event.eventType() == blpapi.Event.RESPONSE:
                        break

            except Exception as e:
                logger.error(f"Error fetching reference data batch {i // self.batch_size + 1}: {e}")

        # Convert reference data to OptionContract objects
        contracts: list[OptionContract] = []

        for point in all_data:
            try:
                expiry = point.get_field(BloombergField.OPT_EXPIRE_DT)
                strike = point.get_field(BloombergField.OPT_STRIKE_PX)
                put_call = point.get_field(BloombergField.OPT_PUT_CALL)

                if expiry is None or strike is None or put_call is None:
                    logger.debug(f"Missing required fields for {point.security}")
                    continue

                # Convert expiry to date if it's a datetime
                if isinstance(expiry, datetime):
                    expiry = expiry.date()

                # Parse option type from Bloomberg value (e.g., 'C', 'CALL', 'P', 'PUT')
                option_type = OptionType.from_bloomberg(put_call)
                if option_type is None:
                    logger.debug(f"Could not parse option type '{put_call}' for {point.security}")
                    continue

                contract = OptionContract(
                    ticker=point.security,
                    strike=float(strike),
                    expiry=expiry,
                    option_type=option_type,
                    underlying=underlying,
                )
                contracts.append(contract)

            except Exception as e:
                logger.debug(
                    f"Failed to create contract from reference data for {point.security}: {e}"
                )

        logger.debug(f"Created {len(contracts)} option contracts from reference data")
        return contracts

    def _to_option_market_data(
        self,
        data_points: list[ReferenceDataPoint],
        as_of_date: date,
    ) -> list[OptionMarketData]:
        """
        Convert ReferenceDataPoints to OptionMarketData objects.

        Uses reference data fields to determine contract details including underlying ticker.

        Args:
            data_points: Reference data points with option market data
            as_of_date: Date the data was fetched for
        """
        results: list[OptionMarketData] = []

        for point in data_points:
            # Extract contract details from reference data fields
            try:
                expiry = point.get_field(BloombergField.OPT_EXPIRE_DT)
                strike = point.get_field(BloombergField.OPT_STRIKE_PX)
                put_call = point.get_field(BloombergField.OPT_PUT_CALL)
                underlying = point.get_field(BloombergField.OPT_UNDL_TICKER)

                if expiry is None or strike is None or put_call is None or underlying is None:
                    logger.debug(f"Missing contract fields for {point.security}, skipping")
                    continue

                # Convert expiry to date if it's a datetime
                if isinstance(expiry, datetime):
                    expiry = expiry.date()

                # Parse option type
                option_type = OptionType.from_bloomberg(put_call)
                if option_type is None:
                    logger.debug(f"Could not parse option type '{put_call}' for {point.security}")
                    continue

                # Create contract
                contract = OptionContract(
                    ticker=point.security,
                    strike=float(strike),
                    expiry=expiry,
                    option_type=option_type,
                    underlying=underlying,
                )

                # Extract market data fields
                market_data = OptionMarketData(
                    contract=contract,
                    as_of_date=as_of_date,
                    settlement_price=point.get_field(BloombergField.PX_SETTLE),
                    last_price=point.get_field(BloombergField.PX_LAST),
                    bid=point.get_field(BloombergField.PX_BID),
                    ask=point.get_field(BloombergField.PX_ASK),
                    volume=point.get_field(BloombergField.VOLUME),
                    open_interest=point.get_field(BloombergField.OPEN_INT),
                    implied_vol=point.get_field(BloombergField.IVOL_MID),
                    delta=point.get_field(BloombergField.OPT_DELTA),
                    gamma=point.get_field(BloombergField.OPT_GAMMA),
                    theta=point.get_field(BloombergField.OPT_THETA),
                    vega=point.get_field(BloombergField.OPT_VEGA),
                    raw_data=point.fields,
                )

                results.append(market_data)

            except Exception as e:
                logger.debug(f"Failed to create market data for {point.security}: {e}")
                continue

        return results

    def find_atm_strike(
        self,
        underlying_price: float,
        available_strikes: list[float],
    ) -> float | None:
        """
        Find the strike price closest to the underlying price (ATM).

        Args:
            underlying_price: Current underlying price
            available_strikes: List of available strike prices

        Returns:
            Strike price closest to underlying price, or None if no strikes available

        Example:
            >>> strikes = [100.0, 105.0, 110.0, 115.0, 120.0]
            >>> fetcher.find_atm_strike(108.0, strikes)
            110.0
        """
        if not available_strikes:
            return None

        return min(available_strikes, key=lambda x: abs(x - underlying_price))

    def find_nearby_expiry(
        self,
        contracts: list[OptionContract],
        target_date: date,
        min_days_to_expiry: int = 7,
        max_days_to_expiry: int = 60,
        monthly_expiry_only: bool = True,
    ) -> date | None:
        """
        Find the nearby (front-month) option expiry date from a list of contracts.

        Searches for the nearest expiry that is at least min_days_to_expiry away
        but no more than max_days_to_expiry away from the target date.

        This method does not query Bloomberg - it works with pre-fetched contracts.

        Args:
            contracts: List of OptionContract objects to search
            target_date: Reference date to find expiry relative to
            min_days_to_expiry: Minimum days until expiry (to avoid expiration week)
            max_days_to_expiry: Maximum days until expiry (to stay in front month)
            monthly_expiry_only: If True, only consider monthly expiries (3rd Friday).
                                This filters out weekly and quarterly options. Default True.

        Returns:
            Expiry date, or None if no suitable expiry found

        Example:
            >>> from datetime import date
            >>> # First, get contracts
            >>> tickers = fetcher.get_option_chain("NVDA US Equity")
            >>> contracts = fetcher._get_option_contracts_from_reference_data(
            ...     tickers, "NVDA US Equity"
            ... )
            >>> # Find monthly expiry
            >>> expiry = fetcher.find_nearby_expiry(
            ...     contracts,
            ...     target_date=date(2024, 10, 15),
            ...     min_days_to_expiry=7,
            ...     monthly_expiry_only=True
            ... )
        """
        if not contracts:
            logger.warning("No contracts provided to find_nearby_expiry")
            return None

        # Get unique expiry dates
        expiry_dates = sorted({c.expiry for c in contracts})

        # Filter to monthly expiries if requested
        if monthly_expiry_only:
            expiry_dates = [d for d in expiry_dates if _is_third_friday(d)]
            logger.debug(f"Filtered to {len(expiry_dates)} monthly expiries (3rd Fridays)")

        # Filter expiries within the desired range
        valid_expiries = []
        for expiry in expiry_dates:
            days_to_expiry = (expiry - target_date).days
            if min_days_to_expiry <= days_to_expiry <= max_days_to_expiry:
                valid_expiries.append(expiry)

        if not valid_expiries:
            logger.warning(
                f"No {'monthly ' if monthly_expiry_only else ''}expiries found between "
                f"{min_days_to_expiry} and {max_days_to_expiry} days from {target_date}. "
                f"Available expiries: {expiry_dates[:5]}"
            )
            return None

        # Return the nearest expiry within the valid range
        nearby_expiry = valid_expiries[0]
        logger.debug(
            f"Found nearby expiry: {nearby_expiry} "
            f"({(nearby_expiry - target_date).days} days from {target_date})"
        )

        return nearby_expiry

    def get_atm_option_data(
        self,
        underlying: str,
        target_date: date,
        expiry_date: date | None = None,
        strike_range_pct: float = 0.1,
        min_days_to_expiry: int = 7,
        max_days_to_expiry: int = 60,
        monthly_expiry_only: bool = True,
    ) -> ATMOptionDataPoint:
        """
        Fetch underlying price and ATM option data for a specific date.

        This method:
        1. Fetches underlying settlement/last/bid/ask prices for the target date
        2. Finds nearby expiry if not provided (based on min/max days to expiry)
        3. Gets option chain as-of the target date
        4. Filters to specified expiry and options near the underlying price
        5. Identifies the ATM strike (closest to underlying price)
        6. Fetches market data for ATM call and put options

        Args:
            underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
            target_date: Date to fetch data for
            expiry_date: Option expiration date to use (if None, finds nearby expiry)
            strike_range_pct: Percentage range around underlying price to search for options
                            (e.g., 0.1 = ±10%)
            min_days_to_expiry: Minimum days until expiry when finding nearby (default: 7)
            max_days_to_expiry: Maximum days until expiry when finding nearby (default: 60)
            monthly_expiry_only: If True, only consider monthly expiries (3rd Friday)
                                when auto-finding expiry. Default True.

        Returns:
            ATMOptionDataPoint with underlying and option data

        Example:
            >>> from datetime import date
            >>> # With explicit expiry
            >>> data = fetcher.get_atm_option_data(
            ...     "NVDA US Equity",
            ...     target_date=date(2024, 10, 15),
            ...     expiry_date=date(2024, 11, 21)
            ... )
            >>> # Auto-find nearby monthly expiry
            >>> data = fetcher.get_atm_option_data(
            ...     "NVDA US Equity",
            ...     target_date=date(2024, 10, 15)
            ... )
            >>> print(f"Using expiry: {data.call_option.contract.expiry}")
        """
        # Find nearby expiry if not provided
        if expiry_date is None:
            # Need to fetch option chain to find contracts for expiry search
            tickers = self.get_option_chain(underlying, as_of_date=target_date)
            if not tickers:
                logger.warning(f"No options found for {underlying} on {target_date}")
                return ATMOptionDataPoint(
                    date=target_date,
                    underlying_ticker=underlying,
                )

            contracts = self._get_option_contracts_from_reference_data(
                tickers, underlying, target_date
            )

            expiry_date = self.find_nearby_expiry(
                contracts=contracts,
                target_date=target_date,
                min_days_to_expiry=min_days_to_expiry,
                max_days_to_expiry=max_days_to_expiry,
                monthly_expiry_only=monthly_expiry_only,
            )
            if expiry_date is None:
                logger.warning(f"Could not find nearby expiry for {underlying} on {target_date}")
                return ATMOptionDataPoint(
                    date=target_date,
                    underlying_ticker=underlying,
                )
            logger.info(f"Using nearby expiry: {expiry_date}")

        logger.info(
            f"Fetching ATM option data for {underlying} on {target_date} with expiry {expiry_date}"
        )

        # Step 1: Fetch underlying prices as-of target_date
        underlying_fields = [
            BloombergField.PX_SETTLE,
            BloombergField.PX_LAST,
            BloombergField.PX_BID,
            BloombergField.PX_ASK,
        ]

        overrides = {"SINGLE_DATE_OVERRIDE": target_date.strftime("%Y%m%d")}
        request = self.request_builder.create_reference_request(
            securities=[underlying],
            fields=underlying_fields,
            overrides=overrides,
        )

        self.session.send_request(request)

        # Collect underlying data
        underlying_data = None
        while True:
            event = self.session.next_event()
            data_points = ResponseParser.parse_reference_data(event)
            if data_points.data:
                underlying_data = data_points.data[0]

            if event.eventType() == blpapi.Event.RESPONSE:
                break

        if not underlying_data:
            logger.warning(f"No underlying data found for {underlying} on {target_date}")
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                option_expiry=expiry_date,
            )

        # Extract underlying prices
        underlying_settlement = underlying_data.get_field(BloombergField.PX_SETTLE)
        underlying_last = underlying_data.get_field(BloombergField.PX_LAST)
        underlying_bid = underlying_data.get_field(BloombergField.PX_BID)
        underlying_ask = underlying_data.get_field(BloombergField.PX_ASK)

        # Determine reference price for ATM calculation (prefer settlement, then last)
        ref_price = underlying_settlement or underlying_last
        if ref_price is None:
            logger.warning(f"No reference price found for {underlying} on {target_date}")
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                option_expiry=expiry_date,
                underlying_settlement=underlying_settlement,
                underlying_last=underlying_last,
                underlying_bid=underlying_bid,
                underlying_ask=underlying_ask,
            )

        # Step 2: Get option chain as-of target_date
        tickers = self.get_option_chain(underlying, as_of_date=target_date)

        if not tickers:
            logger.warning(f"No options found for {underlying} on {target_date}")
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                option_expiry=expiry_date,
                underlying_settlement=underlying_settlement,
                underlying_last=underlying_last,
                underlying_bid=underlying_bid,
                underlying_ask=underlying_ask,
            )

        # Step 3: Get contract details from reference data and filter
        contracts = self._get_option_contracts_from_reference_data(tickers, underlying, target_date)

        if not contracts:
            logger.warning("No valid option contracts found from reference data")
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                option_expiry=expiry_date,
                underlying_settlement=underlying_settlement,
                underlying_last=underlying_last,
                underlying_bid=underlying_bid,
                underlying_ask=underlying_ask,
            )

        # Filter to specified expiry and strike range
        strike_min = ref_price * (1 - strike_range_pct)
        strike_max = ref_price * (1 + strike_range_pct)

        filtered_contracts = [
            c for c in contracts if c.expiry == expiry_date and strike_min <= c.strike <= strike_max
        ]

        if not filtered_contracts:
            logger.warning(
                f"No options found for {underlying} on {target_date} "
                f"with expiry {expiry_date} in strike range [{strike_min:.2f}, {strike_max:.2f}]"
            )
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                option_expiry=expiry_date,
                underlying_settlement=underlying_settlement,
                underlying_last=underlying_last,
                underlying_bid=underlying_bid,
                underlying_ask=underlying_ask,
            )

        # Get unique strikes
        strikes = sorted(set(c.strike for c in filtered_contracts))

        # Step 4: Find ATM strike
        atm_strike = self.find_atm_strike(ref_price, strikes)

        if atm_strike is None:
            logger.warning("Could not determine ATM strike")
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                underlying_settlement=underlying_settlement,
                underlying_last=underlying_last,
                underlying_bid=underlying_bid,
                underlying_ask=underlying_ask,
            )

        logger.debug(
            f"Underlying price: {ref_price:.2f}, ATM strike: {atm_strike:.2f}, "
            f"Available strikes: {strikes}"
        )

        # Step 5: Get ATM call and put tickers
        atm_call_ticker = None
        atm_put_ticker = None

        for contract in filtered_contracts:
            if contract.strike == atm_strike:
                if contract.option_type == OptionType.CALL:
                    atm_call_ticker = contract.ticker
                elif contract.option_type == OptionType.PUT:
                    atm_put_ticker = contract.ticker

        # Step 6: Fetch market data for ATM options
        atm_tickers = [t for t in [atm_call_ticker, atm_put_ticker] if t is not None]

        if not atm_tickers:
            logger.warning(f"No ATM option tickers found for strike {atm_strike}")
            return ATMOptionDataPoint(
                date=target_date,
                underlying_ticker=underlying,
                option_expiry=expiry_date,
                underlying_settlement=underlying_settlement,
                underlying_last=underlying_last,
                underlying_bid=underlying_bid,
                underlying_ask=underlying_ask,
            )

        # Use reference request with date override instead of current market data
        option_market_data_response = self.get_option_market_data(
            atm_tickers,
            fields=DEFAULT_OPTION_FIELDS,
            as_of_date=target_date,
        )

        # Separate call and put data
        call_option = None
        put_option = None

        for opt_data in option_market_data_response.data:
            if opt_data.contract.option_type == OptionType.CALL:
                call_option = opt_data
            elif opt_data.contract.option_type == OptionType.PUT:
                put_option = opt_data

        return ATMOptionDataPoint(
            date=target_date,
            underlying_ticker=underlying,
            option_expiry=expiry_date,
            underlying_settlement=underlying_settlement,
            underlying_last=underlying_last,
            underlying_bid=underlying_bid,
            underlying_ask=underlying_ask,
            call_option=call_option,
            put_option=put_option,
        )

    def get_atm_timeseries(
        self,
        underlying: str,
        start_date: date,
        end_date: date,
        expiry_date: date | None = None,
        strike_range_pct: float = 0.1,
        min_days_to_expiry: int = 7,
        max_days_to_expiry: int = 60,
        roll_days_before_expiry: int = 5,
        monthly_expiry_only: bool = True,
    ) -> Response[list[ATMOptionDataPoint]]:
        """
        Fetch time series of underlying price and ATM option data with error handling.

        EFFICIENT ARCHITECTURE:
        1. Fetches option chain ONCE at the start (expensive operation done once)
        2. Gets all option contract details from reference data ONCE
        3. Iterates through each date, querying only:
           - Underlying settlement price for that date
           - Option market data for the single ATM contract for that date

        Errors for individual dates are logged and collected, but processing continues
        to preserve already-fetched data.

        Args:
            underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
            start_date: Start date (inclusive)
            end_date: End date (inclusive)
            expiry_date: Option expiration date to track (if None, auto-finds nearby expiry)
            strike_range_pct: Percentage range around underlying price to search for options
            min_days_to_expiry: Minimum days until expiry when finding nearby (default: 7)
            max_days_to_expiry: Maximum days until expiry when finding nearby (default: 60)
            roll_days_before_expiry: Days before expiry to roll to next contract (default: 5)
            monthly_expiry_only: If True, only consider monthly expiries (3rd Friday)
                                when auto-finding expiry. Default True.

        Returns:
            Response containing list of ATMOptionDataPoint objects and any errors

        Example:
            >>> from datetime import date
            >>> # Auto-roll to monthly expiries
            >>> response = fetcher.get_atm_timeseries(
            ...     "NVDA US Equity",
            ...     start_date=date(2024, 10, 1),
            ...     end_date=date(2024, 12, 31),
            ... )
        """
        logger.info(f"Fetching ATM time series for {underlying} from {start_date} to {end_date}")

        if expiry_date:
            logger.info(f"Using fixed expiry: {expiry_date}")
        else:
            logger.info(
                f"Auto-rolling expiry (targeting {min_days_to_expiry}-{max_days_to_expiry} "
                f"days out, rolling {roll_days_before_expiry} days before expiry, "
                f"monthly_only={monthly_expiry_only})"
            )

        response = Response(data=[])

        # STEP 1: Fetch option chain ONCE (expensive operation)
        logger.info(f"Fetching option chain for {underlying} (one-time operation)")
        tickers = self.get_option_chain(underlying, as_of_date=start_date)

        if not tickers:
            logger.warning(f"No options found for {underlying}")
            return response

        # STEP 2: Get all contract details ONCE (expensive operation)
        logger.info(f"Fetching contract details for {len(tickers)} options (one-time operation)")
        contracts = self._get_option_contracts_from_reference_data(tickers, underlying, start_date)

        if not contracts:
            logger.warning("No valid option contracts found")
            return response

        logger.info(f"Retrieved {len(contracts)} option contracts")

        # STEP 3: Iterate through each date, querying only prices
        current_expiry = expiry_date  # Will be None if auto-rolling
        current_date = start_date

        while current_date <= end_date:
            try:
                # Check if we need to roll to a new expiry (only if auto-rolling)
                if expiry_date is None:
                    if current_expiry is None:
                        # First iteration - find initial expiry from contracts
                        need_new_expiry = True
                    else:
                        # Check if we're too close to current expiry
                        days_to_expiry = (current_expiry - current_date).days
                        need_new_expiry = days_to_expiry < roll_days_before_expiry

                    if need_new_expiry:
                        logger.debug(
                            f"Finding new expiry for {current_date} from pre-fetched contracts"
                        )
                        current_expiry = self.find_nearby_expiry(
                            contracts=contracts,
                            target_date=current_date,
                            min_days_to_expiry=min_days_to_expiry,
                            max_days_to_expiry=max_days_to_expiry,
                            monthly_expiry_only=monthly_expiry_only,
                        )
                        if current_expiry:
                            logger.info(f"Rolled to new expiry: {current_expiry}")

                if current_expiry is None:
                    logger.warning(f"No suitable expiry found for {current_date}")
                    response.data.append(
                        ATMOptionDataPoint(
                            date=current_date,
                            underlying_ticker=underlying,
                        )
                    )
                    current_date += timedelta(days=1)
                    continue

                # Fetch underlying settlement price for this date
                underlying_fields = [
                    BloombergField.PX_SETTLE,
                    BloombergField.PX_LAST,
                    BloombergField.PX_BID,
                    BloombergField.PX_ASK,
                ]

                overrides = {"SINGLE_DATE_OVERRIDE": current_date.strftime("%Y%m%d")}
                request = self.request_builder.create_reference_request(
                    securities=[underlying],
                    fields=underlying_fields,
                    overrides=overrides,
                )

                self.session.send_request(request)

                # Collect underlying data
                underlying_data = None
                while True:
                    event = self.session.next_event()
                    data_points = ResponseParser.parse_reference_data(event)
                    if data_points.data:
                        underlying_data = data_points.data[0]

                    if event.eventType() == blpapi.Event.RESPONSE:
                        break

                if not underlying_data:
                    logger.warning(f"No underlying data for {current_date}")
                    response.data.append(
                        ATMOptionDataPoint(
                            date=current_date,
                            underlying_ticker=underlying,
                            option_expiry=current_expiry,
                        )
                    )
                    current_date += timedelta(days=1)
                    continue

                # Extract underlying prices
                underlying_settlement = underlying_data.get_field(BloombergField.PX_SETTLE)
                underlying_last = underlying_data.get_field(BloombergField.PX_LAST)
                underlying_bid = underlying_data.get_field(BloombergField.PX_BID)
                underlying_ask = underlying_data.get_field(BloombergField.PX_ASK)

                # Determine reference price for ATM calculation
                ref_price = underlying_settlement or underlying_last
                if ref_price is None:
                    logger.warning(f"No reference price for {current_date}")
                    response.data.append(
                        ATMOptionDataPoint(
                            date=current_date,
                            underlying_ticker=underlying,
                            option_expiry=current_expiry,
                            underlying_settlement=underlying_settlement,
                            underlying_last=underlying_last,
                            underlying_bid=underlying_bid,
                            underlying_ask=underlying_ask,
                        )
                    )
                    current_date += timedelta(days=1)
                    continue

                # Filter contracts to current expiry and strike range
                strike_min = ref_price * (1 - strike_range_pct)
                strike_max = ref_price * (1 + strike_range_pct)

                filtered_contracts = [
                    c
                    for c in contracts
                    if c.expiry == current_expiry and strike_min <= c.strike <= strike_max
                ]

                if not filtered_contracts:
                    logger.warning(
                        f"No options for {current_date} with expiry {current_expiry} "
                        f"in strike range [{strike_min:.2f}, {strike_max:.2f}]"
                    )
                    response.data.append(
                        ATMOptionDataPoint(
                            date=current_date,
                            underlying_ticker=underlying,
                            option_expiry=current_expiry,
                            underlying_settlement=underlying_settlement,
                            underlying_last=underlying_last,
                            underlying_bid=underlying_bid,
                            underlying_ask=underlying_ask,
                        )
                    )
                    current_date += timedelta(days=1)
                    continue

                # Find ATM strike
                strikes = sorted({c.strike for c in filtered_contracts})
                atm_strike = self.find_atm_strike(ref_price, strikes)

                if atm_strike is None:
                    logger.warning(f"Could not determine ATM strike for {current_date}")
                    response.data.append(
                        ATMOptionDataPoint(
                            date=current_date,
                            underlying_ticker=underlying,
                            option_expiry=current_expiry,
                            underlying_settlement=underlying_settlement,
                            underlying_last=underlying_last,
                            underlying_bid=underlying_bid,
                            underlying_ask=underlying_ask,
                        )
                    )
                    current_date += timedelta(days=1)
                    continue

                # Get ATM call and put tickers
                atm_call_ticker = None
                atm_put_ticker = None

                for contract in filtered_contracts:
                    if contract.strike == atm_strike:
                        if contract.option_type == OptionType.CALL:
                            atm_call_ticker = contract.ticker
                        elif contract.option_type == OptionType.PUT:
                            atm_put_ticker = contract.ticker

                # Fetch market data for ATM options on this date
                atm_tickers = [t for t in [atm_call_ticker, atm_put_ticker] if t is not None]

                if not atm_tickers:
                    logger.warning(
                        f"No ATM tickers found for strike {atm_strike} on {current_date}"
                    )
                    response.data.append(
                        ATMOptionDataPoint(
                            date=current_date,
                            underlying_ticker=underlying,
                            option_expiry=current_expiry,
                            underlying_settlement=underlying_settlement,
                            underlying_last=underlying_last,
                            underlying_bid=underlying_bid,
                            underlying_ask=underlying_ask,
                        )
                    )
                    current_date += timedelta(days=1)
                    continue

                # Fetch option market data for this date
                option_market_data_response = self.get_option_market_data(
                    atm_tickers,
                    fields=DEFAULT_OPTION_FIELDS,
                    as_of_date=current_date,
                )

                # Separate call and put data
                call_option = None
                put_option = None

                for opt_data in option_market_data_response.data:
                    if opt_data.contract.option_type == OptionType.CALL:
                        call_option = opt_data
                    elif opt_data.contract.option_type == OptionType.PUT:
                        put_option = opt_data

                # Create data point for this date
                response.data.append(
                    ATMOptionDataPoint(
                        date=current_date,
                        underlying_ticker=underlying,
                        option_expiry=current_expiry,
                        underlying_settlement=underlying_settlement,
                        underlying_last=underlying_last,
                        underlying_bid=underlying_bid,
                        underlying_ask=underlying_ask,
                        call_option=call_option,
                        put_option=put_option,
                    )
                )

            except Exception as e:
                logger.error(f"Error fetching data for {current_date}: {e}")
                # Add error and create empty data point to maintain date continuity
                response.add_error(
                    error_type="DateFetchError",
                    message=f"Failed to fetch data for {current_date}: {str(e)}",
                    context={
                        "date": str(current_date),
                        "underlying": underlying,
                        "expiry": str(current_expiry) if current_expiry else None,
                    },
                    exception=e,
                )
                # Still add a placeholder data point to maintain timeline
                response.data.append(
                    ATMOptionDataPoint(
                        date=current_date,
                        underlying_ticker=underlying,
                        option_expiry=current_expiry,
                    )
                )

            # Move to next day
            current_date += timedelta(days=1)

        logger.info(f"Fetched {len(response.data)} data points with {response.error_count} errors")
        return response


def fetch_option_chain(
    underlying: str,
    expiry_date: str | date,
    fields: list[BloombergField] | None = None,
    strike_range: tuple[float | None, float | None] = (None, None),
    as_of_date: date | None = None,
) -> Response[pd.DataFrame]:
    """
    Convenience function to fetch option chain data with error handling.

    Args:
        underlying: Bloomberg ticker of underlying security (e.g., "NVDA US Equity")
        expiry_date: Target expiration date (e.g., "11/21/25" or date object)
        fields: Fields to fetch (uses defaults if None)
        strike_range: (min_strike, max_strike) tuple for filtering
        as_of_date: Date to fetch option chain as-of (uses current date if None)

    Returns:
        Response containing DataFrame with option market data and any errors

    Example:
        >>> response = fetch_option_chain("NVDA US Equity", "11/21/25")
        >>> df = response.data
        >>> if response.has_errors:
        ...     response.print_errors()
        >>> calls = df[df['option_type'] == 'CALL']
    """
    response = Response(data=pd.DataFrame())

    try:
        # Parse expiry date
        if isinstance(expiry_date, str):
            expiry_date = datetime.strptime(expiry_date, "%m/%d/%y").date()

        with session() as bbg_session:
            fetcher = OptionChainFetcher(bbg_session)

            # Get full option chain
            all_tickers = fetcher.get_option_chain(underlying, as_of_date=as_of_date)

            if not all_tickers:
                logger.warning(f"No options found for {underlying}")
                response.add_error(
                    error_type="NoOptionsFound",
                    message=f"No options found for {underlying}",
                    context={
                        "underlying": underlying,
                        "expiry_date": str(expiry_date),
                        "strike_range": strike_range,
                    },
                )
                return response

            # Get contract details from reference data
            contracts = fetcher._get_option_contracts_from_reference_data(
                all_tickers, underlying, as_of_date
            )

            # Filter to requested expiry and strike range
            filtered_contracts = [
                c
                for c in contracts
                if c.expiry == expiry_date
                and (strike_range[0] is None or c.strike >= strike_range[0])
                and (strike_range[1] is None or c.strike <= strike_range[1])
            ]

            if not filtered_contracts:
                logger.warning(
                    f"No options found for expiry {expiry_date} with strike range {strike_range}"
                )
                response.add_error(
                    error_type="NoOptionsFound",
                    message=f"No options found for expiry {expiry_date}",
                    context={
                        "underlying": underlying,
                        "expiry_date": str(expiry_date),
                        "strike_range": strike_range,
                    },
                )
                return response

            # Extract tickers for filtered contracts
            tickers = [c.ticker for c in filtered_contracts]

            # Get market data (returns Response object)
            market_data_response = fetcher.get_option_market_data(
                tickers,
                fields=fields,
                as_of_date=as_of_date,
            )

            # Extend errors from market data fetch
            response.errors.extend(market_data_response.errors)

            # Convert to DataFrame
            records: list[dict[str, Any]] = []
            for data in market_data_response.data:
                record = {
                    "security": data.contract.ticker,
                    "strike": data.contract.strike,
                    "expiry": data.contract.expiry,
                    "option_type": data.contract.option_type.value,
                    "settlement_price": data.settlement_price,
                    "last_price": data.last_price,
                    "bid": data.bid,
                    "ask": data.ask,
                    "mid_price": data.mid_price,
                    "volume": data.volume,
                    "open_interest": data.open_interest,
                    "implied_vol": data.implied_vol,
                    "delta": data.delta,
                    "gamma": data.gamma,
                    "theta": data.theta,
                    "vega": data.vega,
                }
                records.append(record)

            df = pd.DataFrame(records)

            # Sort by option type and strike
            if not df.empty:
                df = df.sort_values(["option_type", "strike"])

            response.data = df

    except Exception as e:
        logger.error(f"Error fetching option chain: {e}")
        response.add_error(
            error_type="OptionChainFetchError",
            message=f"Failed to fetch option chain: {str(e)}",
            context={
                "underlying": underlying,
                "expiry_date": str(expiry_date),
                "strike_range": strike_range,
            },
            exception=e,
        )

    return response


def fetch_atm_option_timeseries(
    underlying: str,
    start_date: date | str,
    end_date: date | str,
    expiry_date: date | str | None = None,
    strike_range_pct: float = 0.1,
    min_days_to_expiry: int = 7,
    max_days_to_expiry: int = 60,
    roll_days_before_expiry: int = 5,
    monthly_expiry_only: bool = True,
) -> Response[pd.DataFrame]:
    """
    Fetch time series of underlying price and ATM option data with error handling.

    This function fetches daily data for:
    - Underlying stock prices (settlement, last, bid, ask)
    - ATM call option metrics (settle, last, bid, ask, implied vol, Greeks, OI, volume)
    - ATM put option metrics (settle, last, bid, ask, implied vol, Greeks, OI, volume)

    The function can either:
    1. Track a fixed expiry date (if expiry_date provided)
    2. Auto-roll to nearby expiries as they approach expiration (if expiry_date is None)

    When auto-rolling, the function:
    1. Iterates through each date in the range
    2. Finds the nearby expiry (min_days_to_expiry to max_days_to_expiry away)
    3. Rolls to the next expiry when current expiry is within roll_days_before_expiry
    4. Fetches underlying prices as-of each date
    5. Gets option chain as-of each date for the current expiry
    6. Identifies the strike closest to the underlying price (ATM)
    7. Fetches market data for ATM call and put options
    8. Returns combined data in a DataFrame with daily rows

    Errors for individual dates are logged and collected in the Response, but processing
    continues to preserve already-fetched data.

    Args:
        underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
        start_date: Start date (inclusive), as date object or "YYYY-MM-DD" string
        end_date: End date (inclusive), as date object or "YYYY-MM-DD" string
        expiry_date: Option expiration date, as date object or "mm/dd/yy" string.
                    If None, automatically finds and rolls to nearby expiries.
        strike_range_pct: Percentage range around underlying price to search for options
                         (e.g., 0.1 = ±10%, default)
        min_days_to_expiry: When auto-rolling, minimum days until expiry (default: 7)
        max_days_to_expiry: When auto-rolling, maximum days until expiry (default: 60)
        roll_days_before_expiry: When auto-rolling, roll to next expiry this many days
                                before current expiry (default: 5)
        monthly_expiry_only: If True, only consider monthly expiries (3rd Friday)
                            when auto-finding expiry. Default True.

    Returns:
        Response containing DataFrame with columns and any errors:
            - date: Observation date
            - underlying_ticker: Underlying security ticker
            - expiry_date: Option expiration date for this observation
            - days_to_expiry: Days from observation date to expiry
            - underlying_settlement: Underlying settlement price
            - underlying_last: Underlying last price
            - underlying_bid: Underlying bid price
            - underlying_ask: Underlying ask price
            - underlying_mid: Underlying mid price (calculated)
            - atm_strike: ATM strike price
            - call_ticker: Call option ticker
            - call_settlement: Call option settlement price
            - call_last: Call option last price
            - call_bid: Call option bid price
            - call_ask: Call option ask price
            - call_mid: Call option mid price
            - call_volume: Call option volume
            - call_open_interest: Call option open interest
            - call_implied_vol: Call option implied volatility
            - call_delta: Call option delta
            - call_gamma: Call option gamma
            - call_theta: Call option theta
            - call_vega: Call option vega
            - put_ticker: Put option ticker
            - put_settlement: Put option settlement price
            - put_last: Put option last price
            - put_bid: Put option bid price
            - put_ask: Put option ask price
            - put_mid: Put option mid price
            - put_volume: Put option volume
            - put_open_interest: Put option open interest
            - put_implied_vol: Put option implied volatility
            - put_delta: Put option delta
            - put_gamma: Put option gamma
            - put_theta: Put option theta
            - put_vega: Put option vega

    Example:
        >>> from datetime import date
        >>> # Auto-roll to nearby expiries over 3 months
        >>> response = fetch_atm_option_timeseries(
        ...     "NVDA US Equity",
        ...     start_date=date(2024, 10, 1),
        ...     end_date=date(2024, 12, 31),
        ... )
        >>> df = response.data
        >>> if response.has_errors:
        ...     response.print_errors()
        >>> # Check when expiries changed
        >>> print(df.groupby('expiry_date').size())
        >>>
        >>> # Track a specific expiry
        >>> response = fetch_atm_option_timeseries(
        ...     "NVDA US Equity",
        ...     start_date=date(2024, 10, 1),
        ...     end_date=date(2024, 10, 31),
        ...     expiry_date="11/21/24"
        ... )
        >>>
        >>> # Or using string dates
        >>> response = fetch_atm_option_timeseries(
        ...     "AAPL US Equity",
        ...     start_date="2024-10-01",
        ...     end_date="2024-10-31",
        ...     expiry_date="11/15/24",
        ...     strike_range_pct=0.05  # Tighter ±5% range
        ... )
        >>> df = response.data
        >>> # Analyze implied volatility over time
        >>> df.plot(x='date', y=['call_implied_vol', 'put_implied_vol'])
    """
    response = Response(data=pd.DataFrame())

    try:
        # Parse dates
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        if isinstance(expiry_date, str):
            expiry_date = datetime.strptime(expiry_date, "%m/%d/%y").date()

        if expiry_date:
            logger.info(
                f"Fetching ATM option time series for {underlying} from {start_date} to {end_date} "
                f"with fixed expiry {expiry_date}"
            )
        else:
            logger.info(
                f"Fetching ATM option time series for {underlying} from {start_date} to {end_date} "
                f"with auto-rolling expiries"
            )

        with session() as bbg_session:
            fetcher = OptionChainFetcher(bbg_session)

            # Get time series data (returns Response object)
            timeseries_response = fetcher.get_atm_timeseries(
                underlying=underlying,
                start_date=start_date,
                end_date=end_date,
                expiry_date=expiry_date,
                strike_range_pct=strike_range_pct,
                min_days_to_expiry=min_days_to_expiry,
                max_days_to_expiry=max_days_to_expiry,
                roll_days_before_expiry=roll_days_before_expiry,
                monthly_expiry_only=monthly_expiry_only,
            )

            # Extend errors from timeseries fetch
            response.errors.extend(timeseries_response.errors)

            # Convert to DataFrame
            records: list[dict[str, Any]] = []
            for point in timeseries_response.data:
                record = {
                    "date": point.date,
                    "underlying_ticker": point.underlying_ticker,
                    "expiry_date": point.option_expiry,
                    "days_to_expiry": point.days_to_expiry,
                    "underlying_settlement": point.underlying_settlement,
                    "underlying_last": point.underlying_last,
                    "underlying_bid": point.underlying_bid,
                    "underlying_ask": point.underlying_ask,
                    "underlying_mid": point.underlying_mid,
                    "atm_strike": point.atm_strike,
                }

                # Add call option data
                if point.call_option:
                    record.update(
                        {
                            "call_ticker": point.call_option.contract.ticker,
                            "call_settlement": point.call_option.settlement_price,
                            "call_last": point.call_option.last_price,
                            "call_bid": point.call_option.bid,
                            "call_ask": point.call_option.ask,
                            "call_mid": point.call_option.mid_price,
                            "call_volume": point.call_option.volume,
                            "call_open_interest": point.call_option.open_interest,
                            "call_implied_vol": point.call_option.implied_vol,
                            "call_delta": point.call_option.delta,
                            "call_gamma": point.call_option.gamma,
                            "call_theta": point.call_option.theta,
                            "call_vega": point.call_option.vega,
                        }
                    )
                else:
                    record.update(
                        {
                            "call_ticker": None,
                            "call_settlement": None,
                            "call_last": None,
                            "call_bid": None,
                            "call_ask": None,
                            "call_mid": None,
                            "call_volume": None,
                            "call_open_interest": None,
                            "call_implied_vol": None,
                            "call_delta": None,
                            "call_gamma": None,
                            "call_theta": None,
                            "call_vega": None,
                        }
                    )

                # Add put option data
                if point.put_option:
                    record.update(
                        {
                            "put_ticker": point.put_option.contract.ticker,
                            "put_settlement": point.put_option.settlement_price,
                            "put_last": point.put_option.last_price,
                            "put_bid": point.put_option.bid,
                            "put_ask": point.put_option.ask,
                            "put_mid": point.put_option.mid_price,
                            "put_volume": point.put_option.volume,
                            "put_open_interest": point.put_option.open_interest,
                            "put_implied_vol": point.put_option.implied_vol,
                            "put_delta": point.put_option.delta,
                            "put_gamma": point.put_option.gamma,
                            "put_theta": point.put_option.theta,
                            "put_vega": point.put_option.vega,
                        }
                    )
                else:
                    record.update(
                        {
                            "put_ticker": None,
                            "put_settlement": None,
                            "put_last": None,
                            "put_bid": None,
                            "put_ask": None,
                            "put_mid": None,
                            "put_volume": None,
                            "put_open_interest": None,
                            "put_implied_vol": None,
                            "put_delta": None,
                            "put_gamma": None,
                            "put_theta": None,
                            "put_vega": None,
                        }
                    )

                records.append(record)

            df = pd.DataFrame(records)

            # Sort by date
            if not df.empty:
                df = df.sort_values("date")

            response.data = df
            logger.info(f"Returned DataFrame with {len(df)} rows and {response.error_count} errors")

    except Exception as e:
        logger.error(f"Error fetching ATM option timeseries: {e}")
        response.add_error(
            error_type="ATMTimeseriesFetchError",
            message=f"Failed to fetch ATM option timeseries: {str(e)}",
            context={
                "underlying": underlying,
                "start_date": str(start_date),
                "end_date": str(end_date),
                "expiry_date": str(expiry_date) if expiry_date else None,
            },
            exception=e,
        )

    return response
