# Introduction

- [Introduction](#introduction)
  - [Cash Products](#cash-products)
  - [Derivatives](#derivatives)
  - [Value](#value)
  - [Risk](#risk)
  - [Modelling Portfolios](#modelling-portfolios)

## Cash Products

- Examples include:

  - Stocks
  - Bonds
  - Currencies
  - Commodities

## Derivatives

- Assets linked to (or **derived** from) another asset - known as the underlying asset (or just underlying).
- The structure and value of the derivative asset is defined by its relationship to the underlying.
- Examples include
  - Forwards (OTC) and futures (exchange)
    - Set a price that two parties will transact an asset for at a set future date. -
  - Swaps
    - Linked to interest rates, allows a floating interest rate to be switched to a fixed rate.
  - Options
    - Similar to forwards, but gives one party the option (not the obligation) to transact.

## Value

- There are two notions of financial value:
  - **Price** - determined on markets.
  - **Fair value** - corresponds to "correct value".
- The following concepts should be considered:
  - Time value of money
  - Discounted cash flow analysis
  - Arbitrage - relative valuation method and is used for determining the relationship between the value of a derivative and its underlying.

## Risk

- Chance or possibility of suffering financial loss, e.g. losing money on an investment.
- Derivatives can server as risk management tools.

## Modelling Portfolios

- A portfolio is a collection of assets and can be considered as a individual/unit asset.
- The value of the portfolio is the sum of the values of each of the component assets.
  - Each asset will have a natural base valuation unit - i.e. for stocks this would be 1 share, and for FX this would be one unit of the currency (1 EUR or 1 USD).
  - The portfolio values will be expressed in terms of the number of base units for each asset (the *allocation*) multiplied by the respective value of the base units.
- The spot price (cash value) at time $t$ of the base unit for the $i^{th}$asset in the portfolio can be denoted by $S_{i}(t)$.
  - The allocation of the $i^{th}$ asset can be denoted as $\alpha_{i}$.
  - If asset 1 is IBM and there are 100 shares of IBM in a portfolio, then $\alpha_{1}$ is 100.
  - If asset 2 is Japanese Yen (JPY) and there are 100,000 JPY in a portfolio, then $\alpha_{2}$ is 100,000.
  - The value of a portfolio at time $t$ is therefore:
$$V(t) = \sum_{i=1}^{N}\alpha_{i}S_{i}(t)$$
