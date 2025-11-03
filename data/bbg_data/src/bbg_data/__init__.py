"""
bbg_data - A type-safe Python library for fetching Bloomberg data via blpapi.

This library provides a clean, Pythonic interface to Bloomberg's API with:
- Type-safe enums and dataclasses instead of string-based APIs
- Context-managed sessions with automatic cleanup
- High-level abstractions for common use cases
- Extensible architecture for custom queries

Package Structure:
    core: Fundamental types, models, and session management
    api: High-level data fetching interfaces
    data: (Reserved for future data processing utilities)

Quick Start:
    >>> from bbg_data import session, fetch_option_chain
    >>> from bbg_data.core import BloombergField
    >>>
    >>> # Fetch option chain for any underlying
    >>> df = fetch_option_chain("NVDA US Equity", "11/21/25")
    >>>
    >>> # Advanced usage: custom session and fields
    >>> with session() as bbg:
    ...     from bbg_data.api import OptionChainFetcher
    ...     fetcher = OptionChainFetcher(bbg)
    ...     tickers = fetcher.get_option_chain("NVDA US Equity")
    ...     data = fetcher.get_option_market_data(tickers)
"""

__version__ = "0.1.0"

# Import from sub-packages for convenience
from bbg_data.api import (
    OptionChainFetcher,
    RequestBuilder,
    ResponseParser,
    fetch_option_chain,
    to_dataframe,
)
from bbg_data.core import (
    BloombergField,
    BloombergSession,
    BloombergSessionError,
    HistoricalDataPoint,
    OptionChainFilter,
    OptionContract,
    OptionMarketData,
    OptionType,
    Periodicity,
    ReferenceDataPoint,
    RequestType,
    ServiceType,
    session,
)

__all__ = [
    # Version
    "__version__",
    # Core - Session
    "session",
    "BloombergSession",
    "BloombergSessionError",
    # Core - Enums
    "BloombergField",
    "OptionType",
    "Periodicity",
    "RequestType",
    "ServiceType",
    # Core - Models
    "OptionContract",
    "OptionMarketData",
    "OptionChainFilter",
    "ReferenceDataPoint",
    "HistoricalDataPoint",
    # API - Options
    "OptionChainFetcher",
    "fetch_option_chain",
    # API - Requests
    "RequestBuilder",
    "ResponseParser",
    "to_dataframe",
]
