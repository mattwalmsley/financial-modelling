"""
Example: Fetch ATM option time series with underlying prices

This example demonstrates how to fetch daily data for an underlying stock
and its at-the-money (ATM) options over a date range, with support for
auto-rolling to nearby expiries and comprehensive error handling.
"""

from datetime import date

from bbg_data.api import fetch_atm_option_timeseries


def main():
    """Fetch ATM option time series for NVDA with auto-rolling expiries."""

    # Example 1: Auto-roll to nearby expiries over 3 months
    print("=" * 80)
    print("Example 1: Auto-rolling expiries with error handling")
    print("=" * 80)

    response = fetch_atm_option_timeseries(
        underlying="NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 12, 31),
        # No expiry_date specified - will auto-find and roll to nearby expiries
        min_days_to_expiry=7,  # Avoid expiries less than 7 days out
        max_days_to_expiry=60,  # Target expiries 7-60 days out
        roll_days_before_expiry=5,  # Roll 5 days before expiry
        strike_range_pct=0.10,
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

    # Check when expiries changed
    print("\nExpiry dates used:")
    print(df.groupby("expiry_date").size())

    print("\nDataFrame columns:")
    print(df.columns.tolist())

    print("\nFirst few rows:")
    print(
        df[
            [
                "date",
                "expiry_date",
                "days_to_expiry",
                "underlying_settlement",
                "atm_strike",
                "call_implied_vol",
                "put_implied_vol",
            ]
        ].head(10)
    )

    # Example 2: Track a specific (fixed) expiry
    print("\n" + "=" * 80)
    print("Example 2: Fixed expiry date")
    print("=" * 80)

    response_fixed = fetch_atm_option_timeseries(
        underlying="NVDA US Equity",
        start_date=date(2024, 10, 1),
        end_date=date(2024, 10, 31),
        expiry_date="11/21/24",  # Fixed expiry
        strike_range_pct=0.10,
    )

    if response_fixed.success:
        print("Data fetched successfully!")
    else:
        print(f"Partial data fetched with {response_fixed.error_count} errors")

    df_fixed = response_fixed.data
    print(f"\nFetched {len(df_fixed)} days of data with fixed expiry")
    print(f"All rows use expiry: {df_fixed['expiry_date'].unique()}")

    # Example 3: Analyze implied volatility across expiry rolls
    print("\n" + "=" * 80)
    print("Example 3: Analyzing IV across expiry rolls")
    print("=" * 80)

    # Filter to rows where we have option data
    valid_data = df.dropna(subset=["call_implied_vol", "put_implied_vol"])

    if not valid_data.empty:
        print(f"\nFound {len(valid_data)} days with complete option data")

        # Group by expiry to see IV statistics for each contract period
        for expiry, group in valid_data.groupby("expiry_date"):
            print(f"\nExpiry: {expiry} ({len(group)} days)")
            days_range = f"{group['days_to_expiry'].min()}-{group['days_to_expiry'].max()}"
            print(f"  Days to expiry range: {days_range}")
            print(
                f"  Call IV - Mean: {group['call_implied_vol'].mean():.2%}, "
                f"Std: {group['call_implied_vol'].std():.2%}"
            )
            print(
                f"  Put IV  - Mean: {group['put_implied_vol'].mean():.2%}, "
                f"Std: {group['put_implied_vol'].std():.2%}"
            )

            # Calculate put-call IV skew
            group["iv_skew"] = group["put_implied_vol"] - group["call_implied_vol"]
            print(f"  IV Skew - Mean: {group['iv_skew'].mean():.2%}")

    # Example 4: Save to CSV
    output_file = "nvda_atm_options_autoroll.csv"
    df.to_csv(output_file, index=False)
    print("\n" + "=" * 80)
    print(f"Data saved to {output_file}")

    # Example 5: Using string dates
    print("\n" + "=" * 80)
    print("Example 5: String date formats")
    print("=" * 80)

    response_str = fetch_atm_option_timeseries(
        underlying="AAPL US Equity",
        start_date="2024-10-01",
        end_date="2024-10-10",
        # Auto-roll with tighter parameters
        min_days_to_expiry=5,
        max_days_to_expiry=45,
        strike_range_pct=0.05,  # Tighter ±5% range
    )

    df_str = response_str.data
    print(f"Fetched {len(df_str)} days of data for AAPL")
    print(f"Expiries used: {sorted(df_str['expiry_date'].dropna().unique())}")

    if response_str.has_errors:
        print(f"\nNote: {response_str.error_count} errors occurred during fetch")


if __name__ == "__main__":
    main()
