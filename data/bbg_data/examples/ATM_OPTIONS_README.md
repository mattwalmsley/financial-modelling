# 50-Delta Volatility Time Series Fetching

## Overview

The `fetch_50delta_vol_timeseries()` function fetches daily time series data for:

- **Underlying stock prices** (settlement)
- **50-delta implied volatility** for standard tenors (1M, 2M, 3M, 6M)

This approach uses Bloomberg's pre-calculated volatility surface fields, which is **much simpler and more efficient** than constructing ATM options manually (no need to find strikes, expiries, or filter option chains).

## How It Works

The function uses a single Bloomberg historical data request to fetch:

1. **Underlying settlement prices** for each date
2. **50-delta implied volatility** from Bloomberg's volatility surface

Bloomberg pre-calculates these values, eliminating the need for:

- Finding option chains
- Identifying ATM strikes
- Filtering by expiry dates
- Fetching individual option contracts

## Function Signature

```python
def fetch_50delta_vol_timeseries(
    underlying: str,
    start_date: date | str,
    end_date: date | str,
    tenor: str = "1M",
) -> Response[pd.DataFrame]
```

### Parameters

- **`underlying`** (`str`): Bloomberg ticker of the underlying security (e.g., `"NVDA US Equity"`)
- **`start_date`** (`date | str`): Start date, as `date` object or `"YYYY-MM-DD"` string
- **`end_date`** (`date | str`): End date, as `date` object or `"YYYY-MM-DD"` string
- **`tenor`** (`str`, optional): Volatility tenor - `"1M"`, `"2M"`, `"3M"`, or `"6M"` (default: `"1M"`)

### Returns

`Response[pd.DataFrame]` containing:

- **`data`**: DataFrame with the following columns:
  - `date`: Observation date
  - `security`: Underlying ticker
  - `settlement_price`: Underlying settlement price
  - `vol_50d_1m` (or `vol_50d_2m`, etc.): 50-delta implied volatility
- **`errors`**: List of any errors encountered (processing continues on errors)

## Usage Examples

### Basic Usage

```python
from datetime import date
from bbg_data.api import fetch_50delta_vol_timeseries

# Fetch 1-month 50-delta vol for Q4 2024
response = fetch_50delta_vol_timeseries(
    underlying="NVDA US Equity",
    start_date=date(2024, 10, 1),
    end_date=date(2024, 12, 31),
    tenor="1M"
)

df = response.data

if response.has_errors:
    print(f"Warning: {response.error_count} errors occurred")
    response.print_errors()

print(df.head())
```

### Using String Dates

```python
# Alternative using string dates
response = fetch_50delta_vol_timeseries(
    underlying="AAPL US Equity",
    start_date="2024-10-01",
    end_date="2024-10-31",
    tenor="3M"
)

df = response.data
print(df.describe())
```

### Compare Multiple Tenors

```python
# Fetch different tenors for term structure analysis
response_1m = fetch_50delta_vol_timeseries(
    "NVDA US Equity",
    start_date=date(2024, 10, 1),
    end_date=date(2024, 10, 31),
    tenor="1M"
)

response_3m = fetch_50delta_vol_timeseries(
    "NVDA US Equity",
    start_date=date(2024, 10, 1),
    end_date=date(2024, 10, 31),
    tenor="3M"
)

response_6m = fetch_50delta_vol_timeseries(
    "NVDA US Equity",
    start_date=date(2024, 10, 1),
    end_date=date(2024, 10, 31),
    tenor="6M"
)

# Combine the data
df_combined = response_1m.data[["date", "settlement_price", "vol_50d_1m"]].copy()
df_combined = df_combined.merge(
    response_3m.data[["date", "vol_50d_3m"]], on="date", how="left"
)
df_combined = df_combined.merge(
    response_6m.data[["date", "vol_50d_6m"]], on="date", how="left"
)

print(df_combined.head())
```

### Analyzing Volatility

```python
df = response.data

# Basic statistics
print(f"Average volatility: {df['vol_50d_1m'].mean():.2%}")
print(f"Volatility std dev: {df['vol_50d_1m'].std():.2%}")
print(f"Max volatility: {df['vol_50d_1m'].max():.2%}")
print(f"Min volatility: {df['vol_50d_1m'].min():.2%}")

# Calculate daily changes
df['price_change'] = df['settlement_price'].pct_change()
df['vol_change'] = df['vol_50d_1m'].diff()

# Correlation between price and vol
correlation = df[['settlement_price', 'vol_50d_1m']].corr()
print(correlation)
```

### Plotting Time Series

```python
import matplotlib.pyplot as plt

df = response.data

# Plot volatility and price
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.plot(df['date'], df['settlement_price'], 'b-', label='Price')
ax1.set_xlabel('Date')
ax1.set_ylabel('Price', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(df['date'], df['vol_50d_1m'], 'r-', label='50Δ 1M Vol')
ax2.set_ylabel('Implied Volatility', color='r')
ax2.tick_params(axis='y', labelcolor='r')

plt.title('NVDA: Price vs 50-Delta 1M Volatility')
plt.grid(True)
plt.show()
```

### Exporting to CSV

```python
# Save the data
df = response.data
df.to_csv('nvda_50delta_vol.csv', index=False)
```

## Advanced Usage with OptionChainFetcher

For more control, use the `OptionChainFetcher` class directly:

```python
from bbg_data.core.session import session
from bbg_data.api import OptionChainFetcher
from datetime import date

with session() as bbg_session:
    fetcher = OptionChainFetcher(bbg_session)
    
    # Fetch 50-delta vol timeseries
    response = fetcher.get_50delta_vol_timeseries(
        underlying="NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 10, 31),
        tenor="1M"
    )
    
    df = response.data
    print(df.head())
```

## Performance Considerations

- **Single API call**: Unlike the old ATM approach, this makes only **one** Bloomberg historical data request
- **Much faster**: No need to iterate through dates or fetch option chains
- **More reliable**: Uses Bloomberg's pre-calculated values
- **For a 3-month period**: Old approach ~200-300 API calls, new approach ~1 API call

## Bloomberg Fields Used

The function uses these Bloomberg volatility surface fields:

- `HIST_50D_IMP_VOL_1M` - 50-delta 1-month implied volatility
- `HIST_50D_IMP_VOL_2M` - 50-delta 2-month implied volatility
- `HIST_50D_IMP_VOL_3M` - 50-delta 3-month implied volatility
- `HIST_50D_IMP_VOL_6M` - 50-delta 6-month implied volatility

These fields represent the implied volatility at 50-delta (approximately ATM) for standard expiry tenors.

## Why 50-Delta Instead of ATM?

- **More stable**: 50-delta volatility is smoother than exact ATM volatility
- **Standard measure**: Used by traders and risk managers
- **Always available**: Bloomberg calculates these even when exact ATM strikes don't exist
- **Better interpolation**: Bloomberg's surface interpolation is more robust than manual strike selection

## Error Handling

The function returns a `Response` object that includes both data and errors:

```python
response = fetch_50delta_vol_timeseries(...)

if response.has_errors:
    print(f"{response.error_count} errors occurred")
    response.print_errors()  # Print detailed error information
    
# Data is still available even with errors
df = response.data
```

## See Also

- `fetch_option_chain()` - Fetch full option chains for building vol surfaces
- `OptionChainFetcher` class - Lower-level API for more control
- `examples/atm_option_timeseries.py` - Complete working example
