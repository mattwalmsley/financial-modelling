"""
Enumerations for Bloomberg data fields and types.

This module provides type-safe enumerations for Bloomberg field mnemonics,
reducing string-based errors and improving IDE autocomplete support.
"""

from enum import Enum


class BloombergField(str, Enum):
    """Bloomberg field mnemonics for reference and historical data requests."""

    # Price fields
    PX_LAST = "PX_LAST"
    PX_OPEN = "PX_OPEN"
    PX_HIGH = "PX_HIGH"
    PX_LOW = "PX_LOW"
    PX_SETTLE = "PX_SETTLE"
    PX_BID = "PX_BID"
    PX_ASK = "PX_ASK"
    PX_MID = "PX_MID"
    PX_VOLUME = "PX_VOLUME"

    # Option-specific fields
    OPT_STRIKE_PX = "OPT_STRIKE_PX"
    OPT_PUT_CALL = "OPT_PUT_CALL"
    OPT_EXPIRE_DT = "OPT_EXPIRE_DT"
    OPT_DELTA = "OPT_DELTA"
    OPT_GAMMA = "OPT_GAMMA"
    OPT_THETA = "OPT_THETA"
    OPT_VEGA = "OPT_VEGA"
    OPT_RHO = "OPT_RHO"
    OPT_CHAIN = "OPT_CHAIN"
    
    # Implied volatility
    IVOL_MID = "IVOL_MID"
    IVOL_BID = "IVOL_BID"
    IVOL_ASK = "IVOL_ASK"
    
    # Volume and open interest
    VOLUME = "VOLUME"
    OPEN_INT = "OPEN_INT"
    
    # Chain-related fields
    CHAIN_TICKERS = "CHAIN_TICKERS"
    
    # Option descriptive fields
    STRIKE = "STRIKE"
    CP_FLAG = "CP_FLAG"
    OPTION_TYPE = "OPTION_TYPE"
    
    # Dividend and corporate actions
    EQY_DVD_YLD = "EQY_DVD_YLD"
    
    # Risk-free rate proxies
    USGG3M = "USGG3M Index"
    USGG1Y = "USGG1Y Index"
    USGG5Y = "USGG5Y Index"
    USGG10Y = "USGG10Y Index"


class OptionType(str, Enum):
    """Option type: Call or Put."""
    
    CALL = "CALL"
    PUT = "PUT"
    
    @classmethod
    def from_bloomberg(cls, value: str | None) -> "OptionType | None":
        """
        Parse Bloomberg option type value.
        
        Args:
            value: Bloomberg field value (e.g., 'C', 'CALL', 'P', 'PUT')
            
        Returns:
            OptionType enum or None if unable to parse
        """
        if not value:
            return None
            
        value_upper = str(value).upper()
        if "C" in value_upper and "P" not in value_upper:
            return cls.CALL
        elif "P" in value_upper and "C" not in value_upper:
            return cls.PUT
        return None


class ServiceType(str, Enum):
    """Bloomberg API service types."""
    
    REFDATA = "//blp/refdata"
    MKTDATA = "//blp/mktdata"
    INSTRUMENTS = "//blp/instruments"


class RequestType(str, Enum):
    """Bloomberg request types."""
    
    REFERENCE_DATA = "ReferenceDataRequest"
    HISTORICAL_DATA = "HistoricalDataRequest"
    INTRADAY_TICK = "IntradayTickRequest"
    INTRADAY_BAR = "IntradayBarRequest"


class Periodicity(str, Enum):
    """Periodicity options for historical data requests."""
    
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    QUARTERLY = "QUARTERLY"
    SEMI_ANNUALLY = "SEMI_ANNUALLY"
    YEARLY = "YEARLY"
