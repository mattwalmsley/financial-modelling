"""
Advanced usage example with custom fields and filtering.

This script demonstrates type-safe field selection and filtering capabilities.
"""

from datetime import date

from bbg_data import OptionChainFetcher, session
from bbg_data.core import BloombergField, OptionChainFilter, OptionType

# Create a session
with session() as bbg:
    print("Connected to Bloomberg API")

    # Create fetcher
    fetcher = OptionChainFetcher(bbg, batch_size=50)

    # Define filter criteria
    chain_filter = OptionChainFilter(
        expiry_start=date(2025, 11, 1),
        expiry_end=date(2025, 11, 30),
        strike_min=150.0,
        strike_max=200.0,
        option_types=[OptionType.CALL],  # Only calls
    )

    print("\nFetching NVIDIA option chain with filters:")
    print(f"  Expiry: {chain_filter.expiry_start} to {chain_filter.expiry_end}")
    print(f"  Strike: ${chain_filter.strike_min} - ${chain_filter.strike_max}")
    print("  Type: Calls only")

    # Get filtered option tickers
    tickers = fetcher.get_option_chain("NVDA US Equity", chain_filter)
    print(f"\nFound {len(tickers)} matching options")

    # Define custom fields to fetch
    fields = [
        BloombergField.OPT_STRIKE_PX,
        BloombergField.OPT_PUT_CALL,
        BloombergField.OPT_EXPIRE_DT,
        BloombergField.PX_SETTLE,
        BloombergField.PX_BID,
        BloombergField.PX_ASK,
        BloombergField.IVOL_MID,
        BloombergField.OPT_DELTA,
        BloombergField.VOLUME,
        BloombergField.OPEN_INT,
    ]

    print(f"\nFetching market data with {len(fields)} fields...")

    # Fetch market data
    market_data = fetcher.get_option_market_data(tickers, fields)

    # Display results
    print(f"\nReceived data for {len(market_data)} options\n")
    print(f"{'Strike':<10} {'Settle':<10} {'IV':<10} {'Delta':<10} {'Volume':<10}")
    print("-" * 50)

    for data in market_data[:20]:  # Show first 20
        print(
            f"{data.contract.strike:<10.2f} "
            f"{data.settlement_price or 0:<10.2f} "
            f"{data.implied_vol or 0:<10.4f} "
            f"{data.delta or 0:<10.4f} "
            f"{data.volume or 0:<10.0f}"
        )

    # Find ATM option (closest to current price)
    # In real usage, you'd fetch the spot price
    spot_price = 177.5  # Example spot price
    atm_option = min(market_data, key=lambda x: abs(x.contract.strike - spot_price))

    print(f"\nClosest to ATM (spot ~${spot_price}):")
    print(f"  Contract: {atm_option.contract}")
    print(f"  Settlement: ${atm_option.settlement_price}")
    print(f"  Mid Price: ${atm_option.mid_price}")
    print(f"  Implied Vol: {atm_option.implied_vol:.2%}" if atm_option.implied_vol else "  IV: N/A")
    print(f"  Delta: {atm_option.delta:.4f}" if atm_option.delta else "  Delta: N/A")
