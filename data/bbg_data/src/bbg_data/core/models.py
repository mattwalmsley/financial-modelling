"""
Data models for Bloomberg API requests and responses.

This module provides strongly-typed dataclasses for representing Bloomberg data,
ensuring type safety and reducing errors from string-based data handling.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Any

from bbg_data.core.enums import BloombergField, OptionType


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
