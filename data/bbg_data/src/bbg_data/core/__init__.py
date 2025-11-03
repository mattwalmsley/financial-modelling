"""
Core types, models, and session management.

This sub-package contains the fundamental building blocks:
- Enums for type-safe field references
- Dataclasses for structured data
- Session management with Bloomberg API
- Utility functions
"""

from bbg_data.core.enums import BloombergField, OptionType, Periodicity, RequestType, ServiceType
from bbg_data.core.models import (
    HistoricalDataPoint,
    OptionChainFilter,
    OptionContract,
    OptionMarketData,
    ReferenceDataPoint,
)
from bbg_data.core.session import BloombergSession, BloombergSessionError, session
from bbg_data.core.utils import format_ticker, parse_bloomberg_date, split_dataframe_by_type

__all__ = [
    # Enums
    "BloombergField",
    "OptionType",
    "Periodicity",
    "RequestType",
    "ServiceType",
    # Models
    "OptionContract",
    "OptionMarketData",
    "OptionChainFilter",
    "ReferenceDataPoint",
    "HistoricalDataPoint",
    # Session
    "session",
    "BloombergSession",
    "BloombergSessionError",
    # Utils
    "format_ticker",
    "parse_bloomberg_date",
    "split_dataframe_by_type",
]
