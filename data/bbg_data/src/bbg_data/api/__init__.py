"""
High-level API for Bloomberg data fetching.

This sub-package provides convenient interfaces for common data operations:
- Request builders and response parsers
- Option chain fetching with filtering
- ATM option time series with underlying prices
- Error handling with Response wrapper
- Extensible for additional asset classes
"""

from bbg_data.api.options import (
    OptionChainFetcher,
    fetch_atm_option_timeseries,
    fetch_option_chain,
)
from bbg_data.api.requests import RequestBuilder, ResponseParser, to_dataframe
from bbg_data.core.models import ErrorDetail, Response

__all__ = [
    # Options API
    "OptionChainFetcher",
    "fetch_option_chain",
    "fetch_atm_option_timeseries",
    # Request builders
    "RequestBuilder",
    "ResponseParser",
    "to_dataframe",
    # Error handling
    "ErrorDetail",
    "Response",
]
