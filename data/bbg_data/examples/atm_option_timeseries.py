"""
Example: Fetch 50-delta implied volatility time series

This example demonstrates how to fetch daily 50-delta implied volatility data
for an underlying stock using Bloomberg's pre-calculated volatility surface fields.
This is much simpler and more efficient than constructing ATM options manually.
"""

from datetime import date

from bbg_data.api import fetch_50delta_vol_timeseries


def main():
    """Fetch 50-delta vol time series for NVDA."""

    # Example 1: 1-month 50-delta vol over 3 months
    print("=" * 80)
    print("Example 1: 1-month 50-delta vol timeseries")
    print("=" * 80)

    response = fetch_50delta_vol_timeseries(
        underlying="NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 12, 31),
        tenor="1M",
    )

    # Check for errors
    if response.has_errors:
        print(f"\nWarning: Encountered {response.error_count} errors during fetch")
        response.print_errors()
    else:
        print("\nSuccessfully fetched all data with no errors")

    # Access the data
    df = response.data
    print(f"\nFetched {len(df)} days of data")

    print("\nDataFrame columns:")
    print(df.columns.tolist())

    print("\nFirst few rows:")
    print(df.head(10))

    # Example 2: Compare different tenors
    print("\n" + "=" * 80)
    print("Example 2: Compare 1M, 3M, and 6M volatilities")
    print("=" * 80)

    # Fetch different tenors
    response_1m = fetch_50delta_vol_timeseries(
        "NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 10, 31),
        tenor="1M",
    )

    response_3m = fetch_50delta_vol_timeseries(
        "NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 10, 31),
        tenor="3M",
    )

    response_6m = fetch_50delta_vol_timeseries(
        "NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 10, 31),
        tenor="6M",
    )

    # Combine the data

    df_combined = response_1m.data[["date", "settlement_price", "vol_50d_1m"]].copy()
    df_combined = df_combined.merge(response_3m.data[["date", "vol_50d_3m"]], on="date", how="left")
    df_combined = df_combined.merge(response_6m.data[["date", "vol_50d_6m"]], on="date", how="left")

    print("\nVolatility term structure:")
    print(df_combined.head(10))

    # Example 3: Using string dates
    print("\n" + "=" * 80)
    print("Example 3: String date formats")
    print("=" * 80)

    response_str = fetch_50delta_vol_timeseries(
        underlying="AAPL US Equity",
        start_date="2024-10-01",
        end_date="2024-10-31",
        tenor="2M",
    )

    df_str = response_str.data
    print(f"Fetched {len(df_str)} days of data for AAPL")
    print("\nSummary statistics:")
    print(df_str[["settlement_price", "vol_50d_2m"]].describe())

    if response_str.has_errors:
        print(f"\nNote: {response_str.error_count} errors occurred during fetch")

    # Example 4: Save to CSV
    output_file = "nvda_50delta_vol.csv"
    df.to_csv(output_file, index=False)
    print("\n" + "=" * 80)
    print(f"Data saved to {output_file}")

    # Example 5: Simple analysis
    print("\n" + "=" * 80)
    print("Example 5: Vol vs Price relationship")
    print("=" * 80)

    # Calculate correlation
    if not df.empty and "vol_50d_1m" in df.columns:
        valid_data = df.dropna(subset=["settlement_price", "vol_50d_1m"])
        if len(valid_data) > 1:
            correlation = valid_data[["settlement_price", "vol_50d_1m"]].corr()
            print("\nCorrelation matrix:")
            print(correlation)

            # Calculate daily changes
            valid_data = valid_data.copy()
            valid_data["price_change"] = valid_data["settlement_price"].pct_change()
            valid_data["vol_change"] = valid_data["vol_50d_1m"].diff()

            print("\nAverage daily volatility:", valid_data["vol_50d_1m"].mean())
            print("Volatility std dev:", valid_data["vol_50d_1m"].std())
            print("Max volatility:", valid_data["vol_50d_1m"].max())
            print("Min volatility:", valid_data["vol_50d_1m"].min())


if __name__ == "__main__":
    main()
