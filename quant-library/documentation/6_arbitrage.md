# Arbitrage

- [Arbitrage](#arbitrage)
  - [Conceptual Introduction](#conceptual-introduction)
  - [Formal Definition](#formal-definition)
  - [Applying the Concept of Arbitrage](#applying-the-concept-of-arbitrage)
  - [Arbitrage Examples](#arbitrage-examples)
    - [Example 1: Stocks](#example-1-stocks)
    - [Example 2: Bonds](#example-2-bonds)

## Conceptual Introduction

- On a conceptual level, arbitrage is the ability to take a *riskless profit* - i.e. an investment opportunity with a positive chance of making money and **zero** chance of losing money.
- A simple example of arbitrage is between FX rates in 3 currencies - A, B and C:
  - 1000 units of currency A is changed into 1200 units of currency B.
  - 1200 units of currency B is changed in 800 units of currency C.
  - 800 units of currency C is changed into 1050 units of currency A.
  - Assuming no transaction fees, the profit from exploiting this arbitrage is 50 units of currency A.
  - This process can be repeated indefinitely until the FX rates between the 3 currencies are adjusted to remove this arbitrage.
- Market forces generally correct any arbitrages as they occur - supply and demand will restore equilibrium to the assets' prices.
- An arbitrage will appear if a derivative and its underlying asset have two difference prices.

## Formal Definition

- The mathematical definition of an arbitrage is a portfolio with value $V(t)$ satisfying the following conditions:
  - At time $t = 0$ the value of the portfolio will be less than or equal to zero: $V(0) \leq 0$.
    - In other words, The portfolio can be bought without the buyer spending any money.
  - At some time $T > 0$ there is zero probability that the value of the portfolio will be negative: $Prob(V(T) < 0) = 0$ and there is greater than zero probability that the portfolio has a value greater than zero: $Prob(V(T) > 0) > 0$.
    - In other words, at a time $T$, there is **no** chance of losing money and there is a positive chance of losing money - the opportunity to make a riskless profit.
- A portfolio will be presented that can be entered without cost ($V(0) = 0$) and will yield a certain and positive profit at some time $t > 0$.

## Applying the Concept of Arbitrage

- The **basic principle** is that arbitrage cannot exist - economic equilibrium will always be found.
- If assumptions are made which imply that a portfolio with arbitrage exists, these assumptions are invalid.
- Following this idea, assume 2 assets do not have the same price. Then show that this assumption allows the construction of a portfolio with arbitrage. Finally, conclude that the assets must have the same price as the assumption that the prices of the two assets were different was wrong.

## Arbitrage Examples

### Example 1: Stocks

- Take three stocks, A, B, and C with prices at time $t$ being $P_{A}(t)$, $P_{B}(t)$, and $P_{C}(t)$ respectively.
- At time $t = 0$, let the prices, in USD be:
  - $P_{A}(0) = 25$
  - $P_{B}(0) = 20$
  - $P_{C}(0) = 80$
- Assume that time is discrete and that nothing will change until $t =1$ (one-period model).
- At time $t = 1$, assume that there are only 2 states of the world: State I and State II.
- In each state, the price of the stocks can only take one value:

|            | State I | State II |
|------------|:-------:|:--------:|
| $P_{A}(1)$ |  20 USD |  30 USD  |
| $P_{B}(1)$ |  15 USD |  35 USD  |
| $P_{C}(1)$ |  50 USD | 100 USD  |

- Notice that in both states, the following holds true: $P_{A}(1) + 2P_{B}(1) = P_{C}(1)$.
  - However, this does not hold at time $t = 0$ where $25 + 2 \times 20 = 65$ which is less than the price of stock C (80 USD).
  - This indicates that stock C is overpriced at time $t = 0$.
  - A mispriced asset is a red flag that an arbitrage opportunity may exist.
- To construct an arbitrage when there is a relative mispricing between two assets (i.e. one asset is more expensive than the other):
  - Take a short position on the more expensive asset.
  - Take a long position on the cheaper asset.
- The expensive asset in this example is 1 share of stock C.
- The cheap asset in this example is a portfolio containing 1 share of stock A and 2 shares of stock B.
- An arbitrage portfolio can be constructed by taking long positions on 1 share of stock A and 2 shares of stock B, whilst taking a short position on 1 share of stock C.
  - In other words, at time $t = 0$, enter an arbitrage portfolio consisting of:
    - 1 share of stock A
    - 2 shares of stock B
    - a short position in 1 share of stock C
  - The total cost of entering into the long position is 65 USD: $P_{A}(0) + 2P_{B}(0) \equiv 25 + 2 \times 20$.
  - Upon entering into a short position of 1 share of stock C, a cash value of 80 USD will be received immediately (effectively borrowing and then selling 1 share).
  - After entering into both the long and short positions, there will be a remaining cash value of 15 USD (the 80 USD received less the 65 USD spent) which can be invested at the risk-free interest rate.
- The arbitrage portfolio is held until $t = 1$, at which time the following can occur:
  - The shares in stock A and stock B are sold for the price of 1 share of stock C.
  - 1 share of stock C is then bought and the short position in stock C is then closed (i.e. the bought share of stock C is given to the lender).
- The 15 USD made at $t = 0$ becomes the realized profit.
  - This profit is a riskless profit with nothing spent to enter into the arbitrage portfolio.
  - There was never a possibility of losing money, with a probability of 1 (i.e. all the states in the world) of earning the 15 USD profit.

### Example 2: Bonds

