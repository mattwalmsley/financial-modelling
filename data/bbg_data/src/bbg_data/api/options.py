"""
Option chain data fetching functionality.

This module provides high-level functions for fetching option chain data from Bloomberg,
with support for filtering, batching, extensible field selection, and comprehensive
error handling.
"""

import logging
from datetime import date, datetime
from typing import Any

import blpapi
import pandas as pd

from bbg_data.api.requests import RequestBuilder, ResponseParser, to_dataframe
from bbg_data.core.enums import BloombergField, OptionType, ServiceType
from bbg_data.core.models import (
    ErrorDetail,
    HistoricalDataPoint,
    OptionContract,
    OptionMarketData,
    ReferenceDataPoint,
    Response,
)
from bbg_data.core.session import BloombergSession, session

logger = logging.getLogger(__name__)


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

    def get_50delta_vol_timeseries(
        self,
        underlying: str,
        start_date: date,
        end_date: date,
        tenor: str = "1M",
    ) -> Response[pd.DataFrame]:
        """
        Fetch 50-delta implied volatility time series using Bloomberg's volatility surface fields.

        This is a much simpler and more efficient approach than constructing ATM options manually.
        Bloomberg provides pre-calculated 50-delta implied volatility for standard tenors.

        Args:
            underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
            start_date: Start date (inclusive)
            end_date: End date (inclusive)
            tenor: Tenor for the volatility ("1M", "2M", "3M", or "6M")

        Returns:
            Response containing DataFrame with columns:
                - date: Observation date
                - security: Underlying ticker
                - settlement_price: Underlying settlement price
                - vol_50d: 50-delta implied volatility for the specified tenor

        Example:
            >>> from datetime import date
            >>> fetcher = OptionChainFetcher(session)
            >>> response = fetcher.get_50delta_vol_timeseries(
            ...     "NVDA US Equity",
            ...     start_date=date(2024, 10, 1),
            ...     end_date=date(2024, 12, 31),
            ...     tenor="1M"
            ... )
            >>> df = response.data
            >>> if response.has_errors:
            ...     response.print_errors()
        """
        # Map tenor to Bloomberg field
        tenor_field_map = {
            "1M": BloombergField.HIST_50D_IMP_VOL_1M,
            "2M": BloombergField.HIST_50D_IMP_VOL_2M,
            "3M": BloombergField.HIST_50D_IMP_VOL_3M,
            "6M": BloombergField.HIST_50D_IMP_VOL_6M,
        }

        if tenor not in tenor_field_map:
            raise ValueError(
                f"Invalid tenor '{tenor}'. Must be one of: {list(tenor_field_map.keys())}"
            )

        vol_field = tenor_field_map[tenor]

        logger.info(
            f"Fetching 50-delta {tenor} vol time series for {underlying} "
            f"from {start_date} to {end_date}"
        )

        fields = [
            BloombergField.PX_SETTLE,
            vol_field,
        ]

        # Use historical data request - much more efficient than daily reference requests
        all_data: list[HistoricalDataPoint] = []
        all_errors: list[ErrorDetail] = []

        try:
            request = self.request_builder.create_historical_request(
                securities=[underlying],
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
            logger.error(f"Error fetching 50-delta vol timeseries: {e}")
            return Response(
                data=pd.DataFrame(),
                errors=[
                    ErrorDetail(
                        timestamp=datetime.now(),
                        error_type="VolTimeseriesError",
                        message=f"Failed to fetch vol timeseries: {str(e)}",
                        context={
                            "underlying": underlying,
                            "start_date": str(start_date),
                            "end_date": str(end_date),
                            "tenor": tenor,
                        },
                        exception=e,
                    )
                ],
            )

        # Convert to DataFrame
        records = []
        for point in all_data:
            records.append(
                {
                    "date": point.date,
                    "security": point.security,
                    "settlement_price": point.get_field(BloombergField.PX_SETTLE),
                    f"vol_50d_{tenor.lower()}": point.get_field(vol_field),
                }
            )

        df = pd.DataFrame(records)

        if not df.empty:
            df = df.sort_values("date")

        logger.info(f"Fetched {len(df)} data points with {len(all_errors)} errors")

        return Response(data=df, errors=all_errors)


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


def fetch_50delta_vol_timeseries(
    underlying: str,
    start_date: date | str,
    end_date: date | str,
    tenor: str = "1M",
) -> Response[pd.DataFrame]:
    """
    Fetch 50-delta implied volatility time series using Bloomberg's volatility surface.

    This is a simple and efficient approach that uses Bloomberg's pre-calculated
    50-delta implied volatilities, avoiding the need to find strikes and expiries.

    Args:
        underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
        start_date: Start date (inclusive), as date object or "YYYY-MM-DD" string
        end_date: End date (inclusive), as date object or "YYYY-MM-DD" string
        tenor: Volatility tenor - "1M", "2M", "3M", or "6M" (default: "1M")

    Returns:
        Response containing DataFrame with columns:
            - date: Observation date
            - security: Underlying ticker
            - settlement_price: Underlying settlement price
            - vol_50d_1m (or vol_50d_2m, etc.): 50-delta implied volatility

    Example:
        >>> from datetime import date
        >>> # Fetch 1-month 50-delta vol timeseries
        >>> response = fetch_50delta_vol_timeseries(
        ...     "NVDA US Equity",
        ...     start_date=date(2024, 10, 1),
        ...     end_date=date(2024, 12, 31),
        ...     tenor="1M"
        ... )
        >>> df = response.data
        >>> if response.has_errors:
        ...     response.print_errors()
        >>> # Plot vol vs price
        >>> df.plot(x='date', y=['settlement_price', 'vol_50d_1m'], secondary_y=['vol_50d_1m'])
        >>>
        >>> # String dates work too
        >>> response = fetch_50delta_vol_timeseries(
        ...     "AAPL US Equity",
        ...     start_date="2024-10-01",
        ...     end_date="2024-10-31",
        ...     tenor="3M"
        ... )
    """
    response = Response(data=pd.DataFrame())

    try:
        # Parse dates
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, "%Y-%m-%d").date()

        logger.info(
            f"Fetching 50-delta {tenor} vol timeseries for {underlying} "
            f"from {start_date} to {end_date}"
        )

        with session() as bbg_session:
            fetcher = OptionChainFetcher(bbg_session)

            # Get vol timeseries (returns Response object)
            response = fetcher.get_50delta_vol_timeseries(
                underlying=underlying,
                start_date=start_date,
                end_date=end_date,
                tenor=tenor,
            )

    except Exception as e:
        logger.error(f"Error fetching 50-delta vol timeseries: {e}")
        response.add_error(
            error_type="VolTimeseriesFetchError",
            message=f"Failed to fetch 50-delta vol timeseries: {str(e)}",
            context={
                "underlying": underlying,
                "start_date": str(start_date),
                "end_date": str(end_date),
                "tenor": tenor,
            },
            exception=e,
        )

    return response
