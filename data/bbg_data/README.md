# bbg_data

A type-safe Python library for fetching Bloomberg data via blpapi. Built with extensibility and maintainability in mind, using enums and dataclasses instead of string-based APIs.

## Features

- Type-safe API using enums and dataclasses
- Clean abstractions with extensible lower-level access
- Automatic session lifecycle management via context managers
- Modular sub-package architecture (core, api, data)
- Batch request handling for large queries
- Support for reference data, historical data, and option chains

## Installation

### Prerequisites

- Python 3.12+
- Bloomberg Terminal with API access
- UV package manager (recommended)

### Install Bloomberg API

The Bloomberg Python API must be installed from Bloomberg's repository:

```bash
python -m pip install --index-url=https://blpapi.bloomberg.com/repository/releases/python/simple/ blpapi
```

### Install bbg_data

From GitHub:

```bash
uv pip install git+https://github.com/ThanuK22/NvidiaBlackScholes.git#subdirectory=bbg_data
```

For local development:

```bash
cd bbg_data
uv pip install -e .
```

## Quick Start

### Fetch Option Chain

```python
from datetime import date
from bbg_data import session, OptionChainFetcher, OptionChainFilter

with session() as bbg:
    fetcher = OptionChainFetcher(bbg)
    
    # Create filter for specific criteria
    chain_filter = OptionChainFilter(
        expiry_start=date(2025, 11, 1),
        expiry_end=date(2025, 12, 31),
        strike_min=150.0,
        strike_max=200.0,
    )
    
    # Get option chain for any underlying
    tickers = fetcher.get_option_chain("NVDA US Equity", chain_filter)
    
    # Fetch market data
    market_data = fetcher.get_option_market_data(tickers)
    
    for data in market_data:
        print(f"{data.contract}: Settlement=${data.settlement_price}")
```

### Custom Field Selection

```python
from bbg_data import session, OptionChainFetcher, BloombergField

with session() as bbg:
    fetcher = OptionChainFetcher(bbg)
    
    fields = [
        BloombergField.OPT_STRIKE_PX,
        BloombergField.PX_SETTLE,
        BloombergField.IVOL_MID,
        BloombergField.OPT_DELTA,
    ]
    
    tickers = fetcher.get_option_chain("AAPL US Equity")
    market_data = fetcher.get_option_market_data(tickers, fields)
```

### Historical Data

```python
from datetime import date
from bbg_data import session, OptionChainFetcher, BloombergField

with session() as bbg:
    fetcher = OptionChainFetcher(bbg)
    
    df = fetcher.get_historical_option_data(
        tickers=["NVDA US 11/21/25 C177.5 Equity"],
        start_date=date(2024, 10, 1),
        end_date=date(2024, 10, 24),
        fields=[BloombergField.PX_SETTLE, BloombergField.VOLUME]
    )
```

## Package Structure

```
src/bbg_data/
├── core/               # Fundamental types and session management
│   ├── enums.py       # Type-safe Bloomberg field definitions
│   ├── models.py      # Dataclasses for contracts and market data
│   ├── session.py     # Bloomberg session management
│   └── utils.py       # Helper functions
├── api/               # High-level data fetching interfaces
│   ├── requests.py    # Request builders and response parsers
│   └── options.py     # Option chain fetching with filtering
└── data/              # Reserved for future data processing utilities
```

## Type-Safe Design

### Enums Instead of Strings

```python
from bbg_data import BloombergField, OptionType

# Type-safe field references with IDE autocomplete
fields = [
    BloombergField.PX_SETTLE,
    BloombergField.OPT_DELTA,
    BloombergField.IVOL_MID,
]

# Strongly-typed option types
option_type = OptionType.CALL  # or OptionType.PUT
```

### Dataclass Models

```python
from datetime import date
from bbg_data.core import OptionContract, OptionMarketData, OptionType

# Immutable contract specification
contract = OptionContract(
    ticker="NVDA US 11/21/25 C177.5 Equity",
    strike=177.5,
    expiry=date(2025, 11, 21),
    option_type=OptionType.CALL,
    underlying="NVDA US Equity"
)

# Mutable market data snapshot with calculated properties
market_data = OptionMarketData(
    contract=contract,
    as_of_date=date.today(),
    settlement_price=5.25,
    bid=5.20,
    ask=5.30,
)

mid_price = market_data.mid_price  # Auto-calculated from bid/ask
```

## Session Management

```python
from bbg_data import session
from bbg_data.core import ServiceType

# Recommended: context manager for automatic cleanup
with session() as bbg:
    service = bbg.get_service(ServiceType.REFDATA)
    # Automatically closed on exit

# Manual management for long-running applications
from bbg_data import BloombergSession

bbg = BloombergSession()
bbg.start()
try:
    service = bbg.get_service(ServiceType.REFDATA)
finally:
    bbg.stop()
```

## Advanced Usage

### Custom Request Builders

```python
from bbg_data import session, RequestBuilder, ResponseParser
from bbg_data.core import ServiceType, BloombergField
import blpapi

with session() as bbg:
    builder = RequestBuilder(bbg, ServiceType.REFDATA)
    
    request = builder.create_reference_request(
        securities=["NVDA US Equity", "AAPL US Equity"],
        fields=[BloombergField.PX_LAST, BloombergField.VOLUME]
    )
    
    bbg.send_request(request)
    
    while True:
        event = bbg.next_event()
        data = ResponseParser.parse_reference_data(event)
        
        for point in data:
            print(f"{point.security}: {point.fields}")
        
        if event.eventType() == blpapi.Event.RESPONSE:
            break
```

### Working with Multiple Underlyings

```python
from datetime import date
from bbg_data import session, OptionChainFetcher, OptionChainFilter

with session() as bbg:
    fetcher = OptionChainFetcher(bbg)
    
    underlyings = ["NVDA US Equity", "AAPL US Equity", "MSFT US Equity"]
    chain_filter = OptionChainFilter(
        expiry_start=date(2025, 11, 1),
        expiry_end=date(2025, 11, 30),
    )
    
    for underlying in underlyings:
        tickers = fetcher.get_option_chain(underlying, chain_filter)
        market_data = fetcher.get_option_market_data(tickers)
        print(f"{underlying}: {len(market_data)} options")
```

## Best Practices

- Use context managers (`with session()`) for automatic cleanup
- The library automatically batches large requests (default 50 securities per batch)
- Leverage type hints for better IDE autocomplete
- Check `ReferenceDataPoint.has_errors` for Bloomberg-reported errors
- Configure Python logging to see debug information: `logging.basicConfig(level=logging.INFO)`

## Development

### Installation

```bash
uv pip install -e ".[dev]"
```

### Run Tests

```bash
pytest
pytest --cov=bbg_data --cov-report=html
```

### Code Quality

```bash
ruff format .
ruff check .
pyright
```

## Dependencies

- Python 3.12+
- Bloomberg Terminal with API access
- blpapi
- pandas

## License

MIT License
