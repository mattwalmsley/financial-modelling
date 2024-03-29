# Options

## Introduction

- Options are contracts between two counterparties that gives one counterparty *the right but not the obligation* to buy/sell a particular asset to/from the other counterparty at a price agreed to upon entering the contract.
  - An option to **buy** is called a **call**.
  - An option to **sell** is called a **put**.
  - The counterparty with the option is the **buyer** or **holder** and they will **exercise** the option upon deciding to buy or sell at the agreed price.
  - The counterparty which must accept the decision of the buyer is the **seller** or **writer** of the option.
- Option contracts will have a predefined **specification** that states the **underlying** asset, the **quantity** of that asset, the **type** (call/put), the **strike** price, and the **expiration** date of the contract.
  - The **strike price** is the price at which the underlying asset will be bought or sold should the option be exercised.
- The **option premium** is the price paid by the buyer of an option contract to the writer/seller, compensating the writer for the risks involved with issuing the associated rights.
  - Without an option premium, there would be an arbitrage opportunity as option buyers have no downside risk other than the price paid to enter into the option contract.
- There are different convention for exercising options with the two most common being:
  - **European options** can only be exercised at the expiration date.
  - **American options** can be exercised at any time between the contract origination and expiry.
- Options are written on stocks, indexes, currencies, commodities, interest rate products and on the futures contracts of these products (most commodity option contracts are options on futures).
- Options trade both over-the-counter (OTC) and on futures exchanges.
  - Similar to forward contracts, there is a large amount of counterparty credit risk on OTC options, whilst exchange traded options are margined and marked to market which minimises this risk.
- The following terminology is used for positions in options:
  - A **long position** is held by the option holder.
  - A **short position** is held by the option writer.
- There are 4 basic option positions that a market participant can take:
  1. a **long call** - buying the right to purchase an asset at a particular strike.
  2. a **long put** - buying the right to sell an asset at a particular strike.
  3. a **short call** - writing/selling the right to purchase an asset at a particular strike.
  4. a **short put** - writing/selling the right to sell an asset at a particular strike.
- The status of an option with regards to the underlying asset's spot price is denoted as **moneyness** and has the following terminology:
  - **In the money** if a call's strike is less than the underlying's spot or a put's strike is greater than the underlying's spot.
  - **Out the money** if a call's strike is greater than the underlying's spot or a put's strike is less than the underlying's spot.
  - **At the money** when the strike for either a call or put is equal to the underlying's spot.

### Basic Example: European Call

- An investor has paid a 10 USD premium for a European call with a strike price of 60 USD.
- The circumstances under which the option should be exercised:
  - If the underlying asset's spot price is greater than 60 USD, the option is likely to be exercised as it allows the buyer to purchase the asset at a cheaper price compared to the market.
- If the underlying asset's spot price is 75 USD at the option expiration, the net profit made by immediately selling the underlying asset on the market will be 5 USD ($75 - (60 + 10)$).
- If the underlying asset's spot price is 40 USD at the option expiration, the option buyer will not exercise the option and a net loss of 10 USD will be incurred.

### Assumptions

- Unless stated otherwise:
  - The options will be treated as european style.
  - The underlying assets will be a stock paying no dividends (i.e. no income).