"""
Data models for Bloomberg API requests and responses.

This module provides strongly-typed dataclasses for representing Bloomberg data,
ensuring type safety and reducing errors from string-based data handling.
"""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Generic, TypeVar

from bbg_data.core.enums import BloombergField, OptionType


@dataclass
class ErrorDetail:
    """
    Represents an error that occurred during data fetching.

    Attributes:
        timestamp: When the error occurred
        error_type: Type of error (e.g., "BloombergAPIError", "ParsingError")
        message: Human-readable error message
        context: Additional context (e.g., security ticker, date, field name)
        exception: Original exception if available
    """

    timestamp: datetime
    error_type: str
    message: str
    context: dict[str, Any] = field(default_factory=dict)
    exception: Exception | None = None

    def __str__(self) -> str:
        """Return human-readable representation."""
        ctx_str = ", ".join(f"{k}={v}" for k, v in self.context.items()) if self.context else ""
        timestamp_str = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        base_msg = f"[{timestamp_str}] {self.error_type}: {self.message}"
        return base_msg + (f" ({ctx_str})" if ctx_str else "")


T = TypeVar("T")


@dataclass
class Response(Generic[T]):
    """
    Generic response wrapper that includes both data and error information.

    This allows functions to return partial results even when some errors occur,
    preventing loss of already-fetched data.

    Attributes:
        data: The actual data returned (can be partial if errors occurred)
        errors: List of errors encountered (empty if no errors)
        success: True if no errors occurred
    """

    data: T
    errors: list[ErrorDetail] = field(default_factory=list)

    @property
    def success(self) -> bool:
        """Check if operation completed without errors."""
        return len(self.errors) == 0

    @property
    def has_errors(self) -> bool:
        """Check if any errors occurred."""
        return len(self.errors) > 0

    @property
    def error_count(self) -> int:
        """Get count of errors."""
        return len(self.errors)

    def add_error(
        self,
        error_type: str,
        message: str,
        context: dict[str, Any] | None = None,
        exception: Exception | None = None,
    ) -> None:
        """
        Add an error to the response.

        Args:
            error_type: Type of error
            message: Error message
            context: Additional context information
            exception: Original exception if available
        """
        self.errors.append(
            ErrorDetail(
                timestamp=datetime.now(),
                error_type=error_type,
                message=message,
                context=context or {},
                exception=exception,
            )
        )

    def get_errors_by_type(self, error_type: str) -> list[ErrorDetail]:
        """Get all errors of a specific type."""
        return [e for e in self.errors if e.error_type == error_type]

    def print_errors(self) -> None:
        """Print all errors to console."""
        if not self.errors:
            print("No errors")
            return

        print(f"\n{len(self.errors)} error(s) occurred:")
        for i, error in enumerate(self.errors, 1):
            print(f"  {i}. {error}")


@dataclass(frozen=True)
class OptionContract:
    """
    Represents an option contract with its key characteristics.

    Attributes:
        ticker: Bloomberg ticker/security identifier
        strike: Option strike price
        expiry: Expiration date
        option_type: Call or Put
        underlying: Underlying security ticker
    """

    ticker: str
    strike: float
    expiry: date
    option_type: OptionType
    underlying: str

    def __str__(self) -> str:
        """Return human-readable representation."""
        return (
            f"{self.underlying} {self.expiry.strftime('%m/%d/%y')} "
            f"{self.option_type.value} @ {self.strike}"
        )


@dataclass
class OptionMarketData:
    """
    Market data for an option contract.

    Attributes:
        contract: The option contract
        settlement_price: Settlement price
        last_price: Last traded price
        bid: Bid price
        ask: Ask price
        volume: Trading volume
        open_interest: Open interest
        implied_vol: Implied volatility (mid)
        delta: Option delta
        gamma: Option gamma
        theta: Option theta
        vega: Option vega
        as_of_date: Data as-of date
        raw_data: Raw Bloomberg response data
    """

    contract: OptionContract
    as_of_date: date
    settlement_price: float | None = None
    last_price: float | None = None
    bid: float | None = None
    ask: float | None = None
    volume: float | None = None
    open_interest: float | None = None
    implied_vol: float | None = None
    delta: float | None = None
    gamma: float | None = None
    theta: float | None = None
    vega: float | None = None
    raw_data: dict[str, Any] = field(default_factory=dict)

    @property
    def mid_price(self) -> float | None:
        """Calculate mid price from bid/ask if available."""
        if self.bid is not None and self.ask is not None:
            return (self.bid + self.ask) / 2.0
        return None


@dataclass
class HistoricalDataPoint:
    """
    Single historical data point for a security.

    Attributes:
        security: Bloomberg ticker
        date: Date of the observation
        fields: Dictionary of field name to value
    """

    security: str
    date: date
    fields: dict[str, Any] = field(default_factory=dict)

    def get_field(self, field: BloombergField) -> Any:
        """
        Get field value by enum.

        Args:
            field: Bloomberg field enum

        Returns:
            Field value or None if not present
        """
        return self.fields.get(field.value)


@dataclass
class ReferenceDataPoint:
    """
    Reference (static) data for a security.

    Attributes:
        security: Bloomberg ticker
        fields: Dictionary of field name to value
        errors: List of error messages if any
    """

    security: str
    fields: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    def get_field(self, field: BloombergField) -> Any:
        """
        Get field value by enum.

        Args:
            field: Bloomberg field enum

        Returns:
            Field value or None if not present
        """
        return self.fields.get(field.value)

    @property
    def has_errors(self) -> bool:
        """Check if this data point has errors."""
        return len(self.errors) > 0


@dataclass
class OptionChainFilter:
    """
    Filtering criteria for option chain requests.

    Attributes:
        expiry_start: Minimum expiration date (inclusive)
        expiry_end: Maximum expiration date (inclusive)
        strike_min: Minimum strike price (inclusive)
        strike_max: Maximum strike price (inclusive)
        option_types: List of option types to include (None = all)
        min_volume: Minimum trading volume filter
        min_open_interest: Minimum open interest filter
    """

    expiry_start: date | None = None
    expiry_end: date | None = None
    strike_min: float | None = None
    strike_max: float | None = None
    option_types: list[OptionType] | None = None
    min_volume: float | None = None
    min_open_interest: float | None = None

    def matches(self, contract: OptionContract) -> bool:
        """
        Check if a contract matches this filter.

        Args:
            contract: Option contract to check

        Returns:
            True if contract matches all filter criteria
        """
        if self.expiry_start and contract.expiry < self.expiry_start:
            return False
        if self.expiry_end and contract.expiry > self.expiry_end:
            return False
        if self.strike_min is not None and contract.strike < self.strike_min:
            return False
        if self.strike_max is not None and contract.strike > self.strike_max:
            return False
        if self.option_types and contract.option_type not in self.option_types:
            return False
        return True


@dataclass
class ATMOptionDataPoint:
    """
    Combined underlying and ATM option data for a single date.

    Represents a point-in-time snapshot of the underlying security and its
    at-the-money option contract.

    Attributes:
        date: Observation date
        underlying_ticker: Bloomberg ticker of underlying security
        option_expiry: Option expiration date used for this observation
        underlying_settlement: Underlying settlement price
        underlying_last: Underlying last price
        underlying_bid: Underlying bid price
        underlying_ask: Underlying ask price
        call_option: ATM call option market data (None if not found)
        put_option: ATM put option market data (None if not found)
    """

    date: date
    underlying_ticker: str
    option_expiry: date | None = None
    underlying_settlement: float | None = None
    underlying_last: float | None = None
    underlying_bid: float | None = None
    underlying_ask: float | None = None
    call_option: OptionMarketData | None = None
    put_option: OptionMarketData | None = None

    @property
    def underlying_mid(self) -> float | None:
        """Calculate underlying mid price from bid/ask if available."""
        if self.underlying_bid is not None and self.underlying_ask is not None:
            return (self.underlying_bid + self.underlying_ask) / 2.0
        return None

    @property
    def atm_strike(self) -> float | None:
        """Get the ATM strike price (assumes call and put have same strike)."""
        if self.call_option:
            return self.call_option.contract.strike
        if self.put_option:
            return self.put_option.contract.strike
        return None

    @property
    def days_to_expiry(self) -> int | None:
        """Calculate days to expiry from observation date."""
        if self.option_expiry:
            return (self.option_expiry - self.date).days
        return None
