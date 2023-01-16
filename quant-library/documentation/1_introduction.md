# Introduction

- [Introduction](#introduction)
  - [Cash Products](#cash-products)
  - [Derivatives](#derivatives)
  - [Value](#value)
  - [Risk](#risk)
  - [Modelling Portfolios](#modelling-portfolios)
  - [Foreign Currencies (FX)](#foreign-currencies-fx)
  - [Long versus Short Positions](#long-versus-short-positions)

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
- The holding of $K$ units in a foreign currency, $Ke^{r_{f}t}$, can be interpreted as a time dependent allocation of the foreign currency.
  - The interest rate $r_{f}$ represents the continuously compounded return earn by the foreign currency.
  - Returns on the foreign currency can therefore be modelled in a similar way to [dividends](4_equities.md#dividends) on stocks and [convenience yields](5_commodities.md#convenience-yield) on commodities.

## Long versus Short Positions

- Having a **long position** in an asset will cause the portfolio value to *increase* as the asset value increases.
- Having a **short position** in an asset will cause the portfolio value to *decrease* as the asset value increases.
- The simplest way to take a long position in the cash markets is to buy the asset.
  - This can be very expensive as assets will need to be bought outright.
- Taking a short position in the cash markets is not possible on all assets but some do accommodate for this
  - **Stocks** can be shorted on most exchanging using the following mechanism:
    1. Investor A borrows the desired number of shares from investor B who owns the stock.
    2. Investor A then sells the stock on the market for the current market value.
    3. Investor A will then need to compensate investor B for any of the dividends paid by the stock during this time.
    4. Investor A is obligated to give the shares back to investor B at a set point in the future and will need to buy the shares at a future market price. 
    5. A lower market price in the future will make a profit for investor A (assuming the drop in the stocks value is greater than the dividend payments). The risk-free rate and transaction related costs (broker fee, capital gains tax, etc.) should also be considered.
  - **Foreign currencies** can be shorted by borrowing money in the desired currency with the aim of paying back the amount with less of the domestic currency.
  - **Bonds** can be shorted using *reverse repurchase agreements* as well as other investment vehicles.
  - **Commodities** can be shorted by using *exchange traded funds* (ETFs).
- Sometimes it is hard to take long and short positions directly in the cash market (e.g. commodities), so investors will use **derivatives** to take positions on assets.
