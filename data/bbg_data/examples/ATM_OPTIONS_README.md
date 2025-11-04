# ATM Option Time Series Fetching

## Overview

The `fetch_atm_option_timeseries()` function fetches daily time series data for:

- **Underlying stock prices** (settlement, last, bid, ask)
- **ATM call option** metrics (settlement, last, bid, ask, implied volatility, Greeks, open interest, volume)
- **ATM put option** metrics (settlement, last, bid, ask, implied volatility, Greeks, open interest, volume)

## How It Works

The function implements a multi-step process for each date in the range:

1. **Fetch Underlying Prices** - Queries Bloomberg for the underlying security's prices as-of each date
2. **Get Option Chain** - Retrieves available option tickers for the specified expiry date, as-of each date
3. **Filter by Strike** - Limits options to those with strikes within a percentage range of the underlying price
4. **Find ATM Strike** - Identifies the strike closest to the underlying price (at-the-money)
5. **Fetch Option Data** - Queries market data for the ATM call and put options

## Function Signature

```python
def fetch_atm_option_timeseries(
    underlying: str,
    start_date: date | str,
    end_date: date | str,
    expiry_date: date | str,
    strike_range_pct: float = 0.1,
) -> pd.DataFrame
```

### Parameters

- **`underlying`** (`str`): Bloomberg ticker of the underlying security (e.g., `"NVDA US Equity"`)
- **`start_date`** (`date | str`): Start date, as `date` object or `"YYYY-MM-DD"` string
- **`end_date`** (`date | str`): End date, as `date` object or `"YYYY-MM-DD"` string
- **`expiry_date`** (`date | str`): Option expiration date, as `date` object or `"mm/dd/yy"` string
- **`strike_range_pct`** (`float`, optional): Percentage range around underlying price to search for options (default: 0.1 = ±10%)

### Returns

`pd.DataFrame` with the following columns:

#### Underlying Data

- `date`: Observation date
- `underlying_ticker`: Underlying security ticker
- `underlying_settlement`: Underlying settlement price
- `underlying_last`: Underlying last price
- `underlying_bid`: Underlying bid price
- `underlying_ask`: Underlying ask price
- `underlying_mid`: Underlying mid price (calculated from bid/ask)

#### General

- `atm_strike`: ATM strike price (same for call and put)

#### Call Option Data

- `call_ticker`: Bloomberg ticker of the call option
- `call_settlement`: Call settlement price
- `call_last`: Call last price
- `call_bid`: Call bid price
- `call_ask`: Call ask price
- `call_mid`: Call mid price (calculated from bid/ask)
- `call_volume`: Call trading volume
- `call_open_interest`: Call open interest
- `call_implied_vol`: Call implied volatility
- `call_delta`: Call delta
- `call_gamma`: Call gamma
- `call_theta`: Call theta
- `call_vega`: Call vega

#### Put Option Data

- `put_ticker`: Bloomberg ticker of the put option
- `put_settlement`: Put settlement price
- `put_last`: Put last price
- `put_bid`: Put bid price
- `put_ask`: Put ask price
- `put_mid`: Put mid price (calculated from bid/ask)
- `put_volume`: Put trading volume
- `put_open_interest`: Put open interest
- `put_implied_vol`: Put implied volatility
- `put_delta`: Put delta
- `put_gamma`: Put gamma
- `put_theta`: Put theta
- `put_vega`: Put vega

## Usage Examples

### Basic Usage

```python
from datetime import date
from bbg_data.api import fetch_atm_option_timeseries

# Fetch October 2024 data for NVDA with November expiry
df = fetch_atm_option_timeseries(
    underlying="NVDA US Equity",
    start_date=date(2024, 10, 1),
    end_date=date(2024, 10, 31),
    expiry_date="11/21/24"
)

print(df.head())
```

### Using String Dates

```python
# Alternative using string dates
df = fetch_atm_option_timeseries(
    underlying="AAPL US Equity",
    start_date="2024-10-01",
    end_date="2024-10-31",
    expiry_date="11/15/24",
    strike_range_pct=0.05  # Tighter ±5% range
)
```

### Analyzing Implied Volatility

```python
# Filter to rows with complete option data
valid_data = df.dropna(subset=["call_implied_vol", "put_implied_vol"])

# Calculate put-call IV skew
valid_data['iv_skew'] = valid_data['put_implied_vol'] - valid_data['call_implied_vol']

print(f"Mean Call IV: {valid_data['call_implied_vol'].mean():.2%}")
print(f"Mean Put IV: {valid_data['put_implied_vol'].mean():.2%}")
print(f"Mean IV Skew: {valid_data['iv_skew'].mean():.2%}")
```

### Plotting Time Series

```python
import matplotlib.pyplot as plt

# Plot implied volatility over time
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['call_implied_vol'], label='Call IV', marker='o')
plt.plot(df['date'], df['put_implied_vol'], label='Put IV', marker='s')
plt.xlabel('Date')
plt.ylabel('Implied Volatility')
plt.title('ATM Option Implied Volatility')
plt.legend()
plt.grid(True)
plt.show()

# Plot Greeks
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
df.plot(x='date', y='call_delta', ax=axes[0,0], title='Call Delta')
df.plot(x='date', y='call_gamma', ax=axes[0,1], title='Call Gamma')
df.plot(x='date', y='call_theta', ax=axes[1,0], title='Call Theta')
df.plot(x='date', y='call_vega', ax=axes[1,1], title='Call Vega')
plt.tight_layout()
plt.show()
```

### Exporting to CSV

```python
# Save the data
df.to_csv('atm_options_data.csv', index=False)
```

## Advanced Usage with OptionChainFetcher

For more control, use the `OptionChainFetcher` class directly:

```python
from bbg_data.core.session import session
from bbg_data.api import OptionChainFetcher
from datetime import date

with session() as bbg_session:
    fetcher = OptionChainFetcher(bbg_session)
    
    # Fetch data for a single date
    data_point = fetcher.get_atm_option_data(
        underlying="NVDA US Equity",
        target_date=date(2024, 10, 15),
        expiry_date=date(2024, 11, 21),
        strike_range_pct=0.10
    )
    
    print(f"Date: {data_point.date}")
    print(f"Underlying: {data_point.underlying_settlement}")
    print(f"ATM Strike: {data_point.atm_strike}")
    if data_point.call_option:
        print(f"Call IV: {data_point.call_option.implied_vol:.2%}")
    if data_point.put_option:
        print(f"Put IV: {data_point.put_option.implied_vol:.2%}")
```

## Performance Considerations

- Each date requires multiple Bloomberg API calls (underlying prices + option chain + option data)
- For a 20-day period, expect ~60-100 API calls total
- Consider using business days only to reduce API calls
- The `strike_range_pct` parameter helps limit the number of options queried

## Error Handling

The function is designed to be robust:

- If underlying data is missing for a date, that row will have `None` values
- If no options are found for a date, call/put columns will be `None`
- If only one of call/put is found, the other will be `None`
- The function continues processing even if individual dates fail

## See Also

- `fetch_option_chain()` - Fetch full option chains for a specific expiry
- `OptionChainFetcher` class - Lower-level API for more control
- `examples/atm_option_timeseries.py` - Complete working example
