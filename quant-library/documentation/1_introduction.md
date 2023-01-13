# Introduction

- [Introduction](#introduction)
  - [Cash Products](#cash-products)
  - [Derivatives](#derivatives)
  - [Value](#value)
  - [Risk](#risk)
  - [Modelling Portfolios](#modelling-portfolios)
  - [Foreign Currencies (FX)](#foreign-currencies-fx)

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
- Any cash held in a portfolio is assumed to be invested at the risk-free rate.
  - Let $r$ be the continuously compounded risk-free interest rate.
  - A lump sum of cash $X$ can be represented in a portfolio's value expression by $Xe^{rt}$, assuming it was brought into the portfolio at time $t=0$.
- Similarly, any debt in the portfolio can be represented as a negative cash allocation.
  - A debt of $X$, taken on at time $t = 0$ at the risk-free interest rate $r$, would be represented by $-Xe^{rt}$.
  - The value of a portfolio containing $n$ assets with values $S_{i}(t)$ for $i = 1 ... n$ and a debt of value of $Xe^{rt}$ would be:
$$V(t) = \sum_{i=1}^{N}S_{i}(t) - Xe^{rt}$$
- The portfolio could have a negative value if $Xe^{rt} > \sum_{i=1}^{N}S_{i}(t)$ at some time $t$.
  - The owner of a portfolio with a negative value would need to pay any potential buyers of the portfolio.

## Foreign Currencies (FX)

- The (spot) price of one unit of foreign currency, priced in the domestic currency, can be denoted as $S(t)$.
- A holding of $\alpha$ units of a foreign currency at time $t = 0$ would be represented in a portfolio's value by the term $\alpha S(0)$.
- Any foreign currency in a portfolio is assumed to be invested at the respective currency's risk-free rate, denoted by $r_{f}$.
  - Similarly, the domestic currency's risk-free rate is denoted by $r_{d}$.
- A holding of $N$ units of domestic currency is represented by $Ne^{r_{d}t}$.
- A holding of $K$ units of foreign currency is represented by $Ke^{r_{f}t}$.
  - This can be represented in the domestic currency by $Ke^{r_{f}t}S(t)$.
