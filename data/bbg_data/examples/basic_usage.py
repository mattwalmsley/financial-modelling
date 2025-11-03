"""
Basic usage example for bbg_data library.

This script demonstrates the simplest way to fetch option chain data.
"""

from bbg_data import fetch_option_chain

# Fetch all NVIDIA options expiring on November 21, 2025
print("Fetching NVIDIA options for 11/21/25...")
df = fetch_option_chain("NVDA US Equity", "11/21/25")

print(f"\nFound {len(df)} options")

# Separate calls and puts
calls = df[df["option_type"] == "CALL"]
puts = df[df["option_type"] == "PUT"]

print(f"  Calls: {len(calls)}")
print(f"  Puts: {len(puts)}")

# Display first few options
print("\nFirst 10 Calls:")
print(calls[["strike", "settlement_price", "last_price", "implied_vol"]].head(10))

print("\nFirst 10 Puts:")
print(puts[["strike", "settlement_price", "last_price", "implied_vol"]].head(10))

# Save to CSV
output_file = "nvda_options_chain.csv"
df.to_csv(output_file, index=False)
print(f"\n✓ Data saved to {output_file}")
