"""
Utility functions for common Bloomberg data operations.
"""

from datetime import date, datetime


def parse_bloomberg_date(value: str | date | datetime | None) -> date | None:
    """
    Parse various Bloomberg date formats into Python date object.

    Args:
        value: Date string, date, or datetime object

    Returns:
        Python date object or None if unable to parse
    """
    if value is None:
        return None

    if isinstance(value, date):
        return value

    if isinstance(value, datetime):
        return value.date()

    # Try common Bloomberg date formats
    formats = [
        "%Y-%m-%d",  # ISO format
        "%m/%d/%Y",  # US format
        "%m/%d/%y",  # Short US format
        "%Y%m%d",  # Compact format
    ]

    for fmt in formats:
        try:
            return datetime.strptime(str(value), fmt).date()
        except ValueError:
            continue

    return None


def format_ticker(
    underlying: str,
    expiry: date,
    option_type: str,
    strike: float,
    country: str = "US",
    security_type: str = "Equity",
) -> str:
    """
    Format a Bloomberg option ticker string.

    Args:
        underlying: Underlying symbol (e.g., "NVDA")
        expiry: Expiration date
        option_type: "C" for call, "P" for put
        strike: Strike price
        country: Country code (default: "US")
        security_type: Security type (default: "Equity")

    Returns:
        Bloomberg ticker string

    Example:
        >>> format_ticker("NVDA", date(2025, 11, 21), "C", 177.5)
        'NVDA US 11/21/25 C177.5 Equity'
    """
    expiry_str = expiry.strftime("%m/%d/%y")
    return f"{underlying} {country} {expiry_str} {option_type}{strike} {security_type}"


def split_dataframe_by_type(df, type_column: str = "option_type"):
    """
    Split options DataFrame into calls and puts.

    Args:
        df: DataFrame with option data
        type_column: Name of column containing option type

    Returns:
        Tuple of (calls_df, puts_df)
    """
    calls = df[df[type_column].str.upper().str.startswith("C")].copy()
    puts = df[df[type_column].str.upper().str.startswith("P")].copy()
    return calls, puts
