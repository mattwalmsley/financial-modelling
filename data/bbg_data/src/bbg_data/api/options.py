"""
Option chain data fetching functionality.

This module provides high-level functions for fetching option chain data from Bloomberg,
with support for filtering, batching, and extensible field selection.
"""

import logging
from datetime import date, datetime
from typing import Any

import blpapi
import pandas as pd

from bbg_data.api.requests import RequestBuilder, ResponseParser, to_dataframe
from bbg_data.core.enums import BloombergField, OptionType, ServiceType
from bbg_data.core.models import (
    HistoricalDataPoint,
    OptionChainFilter,
    OptionContract,
    OptionMarketData,
    ReferenceDataPoint,
)
from bbg_data.core.session import BloombergSession, session

logger = logging.getLogger(__name__)

# Default fields for option chain queries
DEFAULT_OPTION_FIELDS = [
    BloombergField.OPT_STRIKE_PX,
    BloombergField.OPT_PUT_CALL,
    BloombergField.OPT_EXPIRE_DT,
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
        chain_filter: OptionChainFilter | None = None,
    ) -> list[str]:
        """
        Get list of option tickers for an underlying security.

        Args:
            underlying: Bloomberg ticker of underlying (e.g., "NVDA US Equity")
            chain_filter: Optional filter criteria

        Returns:
            List of option ticker strings

        Example:
            >>> fetcher = OptionChainFetcher(session)
            >>> filter = OptionChainFilter(
            ...     expiry_start=date(2025, 11, 1),
            ...     expiry_end=date(2025, 12, 31)
            ... )
            >>> tickers = fetcher.get_option_chain("NVDA US Equity", filter)
        """
        logger.info(f"Fetching option chain for {underlying}")

        # Request OPT_CHAIN field
        request = self.request_builder.create_reference_request(
            securities=[underlying],
            fields=[BloombergField.OPT_CHAIN],
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

        # Apply filter if provided
        if chain_filter:
            all_tickers = self._filter_tickers(all_tickers, chain_filter, underlying)

        return all_tickers

    def get_option_market_data(
        self,
        tickers: list[str],
        fields: list[BloombergField] | None = None,
        as_of_date: date | None = None,
    ) -> list[OptionMarketData]:
        """
        Fetch market data for option contracts.

        Args:
            tickers: List of option Bloomberg tickers
            fields: Fields to fetch (uses defaults if None)
            as_of_date: Data as-of date (uses current if None)

        Returns:
            List of option market data objects

        Example:
            >>> tickers = ["NVDA US 11/21/25 C177.5 Equity"]
            >>> data = fetcher.get_option_market_data(tickers)
        """
        if fields is None:
            fields = DEFAULT_OPTION_FIELDS

        if as_of_date is None:
            as_of_date = date.today()

        logger.info(f"Fetching market data for {len(tickers)} options")

        all_data: list[ReferenceDataPoint] = []

        # Batch requests to avoid Bloomberg limits
        for i in range(0, len(tickers), self.batch_size):
            batch = tickers[i : i + self.batch_size]
            logger.debug(f"Processing batch {i // self.batch_size + 1} ({len(batch)} securities)")

            request = self.request_builder.create_reference_request(
                securities=batch,
                fields=fields,
            )

            self.session.send_request(request)

            # Collect responses
            while True:
                event = self.session.next_event()
                batch_data = ResponseParser.parse_reference_data(event)
                all_data.extend(batch_data)

                if event.eventType() == blpapi.Event.RESPONSE:
                    break

        # Convert to OptionMarketData objects
        return self._to_option_market_data(all_data, as_of_date)

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

        # Batch requests
        for i in range(0, len(tickers), self.batch_size):
            batch = tickers[i : i + self.batch_size]

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
                batch_data = ResponseParser.parse_historical_data(event)
                all_data.extend(batch_data)

                if event.eventType() == blpapi.Event.RESPONSE:
                    break

        # Convert to DataFrame
        return to_dataframe(all_data)

    def _filter_tickers(
        self,
        tickers: list[str],
        chain_filter: OptionChainFilter,
        underlying: str,
    ) -> list[str]:
        """Filter option tickers based on criteria."""
        # Parse tickers to contracts for filtering
        contracts = [self._parse_ticker(t, underlying) for t in tickers]
        filtered_tickers = [t for t, c in zip(tickers, contracts) if c and chain_filter.matches(c)]

        logger.info(f"Filtered to {len(filtered_tickers)} options matching criteria")
        return filtered_tickers

    def _parse_ticker(
        self,
        ticker: str,
        underlying: str,
    ) -> OptionContract | None:
        """
        Parse Bloomberg option ticker into OptionContract.

        Format: "NVDA US 11/21/25 C177.5 Equity"
        """
        try:
            parts = ticker.split()

            # Find date part (mm/dd/yy format)
            expiry_date = None
            for part in parts:
                if "/" in part:
                    try:
                        expiry_date = datetime.strptime(part, "%m/%d/%y").date()
                        break
                    except ValueError:
                        continue

            if not expiry_date:
                return None

            # Find option type and strike
            # Format: C177.5 or P150.0
            option_type = None
            strike = None
            for part in parts:
                if part and part[0] in ("C", "P"):
                    option_type = OptionType.CALL if part[0] == "C" else OptionType.PUT
                    try:
                        strike = float(part[1:])
                    except (ValueError, IndexError):
                        continue
                    break

            if not option_type or strike is None:
                return None

            return OptionContract(
                ticker=ticker,
                strike=strike,
                expiry=expiry_date,
                option_type=option_type,
                underlying=underlying,
            )

        except Exception as e:
            logger.debug(f"Failed to parse ticker {ticker}: {e}")
            return None

    def _to_option_market_data(
        self,
        data_points: list[ReferenceDataPoint],
        as_of_date: date,
    ) -> list[OptionMarketData]:
        """Convert ReferenceDataPoints to OptionMarketData objects."""
        results: list[OptionMarketData] = []

        for point in data_points:
            # Parse ticker to get contract info
            contract = self._parse_ticker(point.security, "")

            if not contract:
                logger.warning(f"Could not parse ticker: {point.security}")
                continue

            # Extract fields
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

        return results


def fetch_option_chain(
    underlying: str,
    expiry_date: str | date,
    fields: list[BloombergField] | None = None,
    strike_range: tuple[float | None, float | None] = (None, None),
) -> pd.DataFrame:
    """
    Convenience function to fetch option chain data for any underlying security.

    Args:
        underlying: Bloomberg ticker of underlying security (e.g., "NVDA US Equity")
        expiry_date: Target expiration date (e.g., "11/21/25" or date object)
        fields: Fields to fetch (uses defaults if None)
        strike_range: (min_strike, max_strike) tuple for filtering

    Returns:
        DataFrame with option market data

    Example:
        >>> df = fetch_option_chain("NVDA US Equity", "11/21/25")
        >>> df = fetch_option_chain("AAPL US Equity", "12/20/24", strike_range=(150.0, 200.0))
        >>> calls = df[df['option_type'] == 'CALL']
    """
    # Parse expiry date
    if isinstance(expiry_date, str):
        expiry_date = datetime.strptime(expiry_date, "%m/%d/%y").date()

    # Create filter
    chain_filter = OptionChainFilter(
        expiry_start=expiry_date,
        expiry_end=expiry_date,
        strike_min=strike_range[0],
        strike_max=strike_range[1],
    )

    with session() as bbg_session:
        fetcher = OptionChainFetcher(bbg_session)

        # Get option chain
        tickers = fetcher.get_option_chain(underlying, chain_filter)

        if not tickers:
            logger.warning(f"No options found for expiry {expiry_date}")
            return pd.DataFrame()

        # Get market data
        market_data = fetcher.get_option_market_data(tickers, fields)

        # Convert to DataFrame
        records: list[dict[str, Any]] = []
        for data in market_data:
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

        return df
