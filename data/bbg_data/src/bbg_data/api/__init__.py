"""
High-level API for Bloomberg data fetching.

This sub-package provides convenient interfaces for common data operations:
- Request builders and response parsers
- Option chain fetching with filtering
- Extensible for additional asset classes
"""

from bbg_data.api.options import OptionChainFetcher, fetch_option_chain
from bbg_data.api.requests import RequestBuilder, ResponseParser, to_dataframe

__all__ = [
    # Options API
    "OptionChainFetcher",
    "fetch_option_chain",
    # Request builders
    "RequestBuilder",
    "ResponseParser",
    "to_dataframe",
]
