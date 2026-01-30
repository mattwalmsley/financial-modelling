# Arbitrage

- [Arbitrage](#arbitrage)
  - [Conceptual Introduction](#conceptual-introduction)
  - [Formal Definition](#formal-definition)
  - [Applying the Concept of Arbitrage](#applying-the-concept-of-arbitrage)
  - [Arbitrage Examples](#arbitrage-examples)
    - [Example 1: Stocks](#example-1-stocks)
    - [Example 2: Bonds](#example-2-bonds)
  - [The Law of One Price](#the-law-of-one-price)
    - [Law of One Price Example 1: Stocks](#law-of-one-price-example-1-stocks)
    - [Law of One Price Example 2: Bonds](#law-of-one-price-example-2-bonds)
  - [Arbitrage and Discounted Cash Flow Analysis](#arbitrage-and-discounted-cash-flow-analysis)
    - [Discounted Cash Flow Analysis Example 1](#discounted-cash-flow-analysis-example-1)
    - [Discounted Cash Flow Analysis Example 2](#discounted-cash-flow-analysis-example-2)

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
| ---------- | :-----: | :------: |
| $P_{A}(1)$ | 20 USD  |  30 USD  |
| $P_{B}(1)$ | 15 USD  |  35 USD  |
| $P_{C}(1)$ | 50 USD  | 100 USD  |

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

- Take a bond with a face value of 10,000 USD which is trading at par (i.e. the current market price is 10,000 USD).
- This bond matures in 3 years and pays an annual coupon of 6%.
- The current annually compounded risk-free interest rates for 1, 2, and 3 year terms are:
  - $r(1) = 0.75\%$
  - $r(2) = 1.5\%$
  - $r(3) = 2\%$
- Given the bond pays a 600 USD coupon in years 1 and 2, and 10,600 USD (par value + coupon) in year 3, the bond pricing formula can be applied for annually compounded interest rates to find the present fair value of the bond as follows:

```math
\begin{aligned}
PV &= \sum_{i=1}^{N} \frac{c_i}{(1 + r(t_i))^{t_i}} \\
&= \frac{600}{1 + 0.0075} + \frac{600}{(1 + 0.015)^{2}} + \frac{10600}{(1 + 0.02)^{3}} \\
&= 595.53 + 582.40 + 9988.62 \\
&= \boxed{11,166.55 \text{ USD}}
\end{aligned} \\
```

- Given the bond's current market price (10,000 USD) is lower than the present fair value (11,166.55 USD), there is a potential arbitrage opportunity present that can be constructed as follows:
  - At year 0, borrow 595.53 USD with a 1 year term, 582.40 USD with a 2 year term and 9,988.62 USD with a 3 year term, the debt owed on each of these amounts will be exactly matched by the coupon payments from the bond respectively.
    - This is equivalent to selling 3 zero-coupon bonds with the original bond's coupon payments as the par values for the 3 zero-coupon bonds.
  - Having borrowed 11,166.55 USD, the original bond can be purchased for 10,000 USD (current market price).
  - This leave 1,166.55 USD left over as cash which can be invested at the risk-free annually compounded interest rate for 3 years ($r(3) = 2\%$).
  - At this point, the portfolio has 3 components:
    - The 10,000 USD face value bond
    - The 3 loans
    - A cash holding of 1,166.55 USD which is invested at the risk-free rate for 3 years
  - The cost to enter this portfolio is 0 and it will yield a positive and certain profit.
  - As each of the 3 loans is due, the debt due will equal the bond's coupon payment at that time.
  - After 3 years, the debt from taking out the 3 loans is cleared. The cash investment of 1,166.55 USD which was invested at the risk-free annually compounded interest rate of 2% can be realized as follows:
$$1166.55 \times (1 + 0.02)^{3} = \boxed{1,237.95 \space USD}$$
- This arbitrage opportunity yields a profit of 1,237.95 USD with zero risk of losing money.

## The Law of One Price

- If the probability of the prices of two assets, A and B, being equal at some time $T > 1$ is certain ($Prob(P_{A}(T) = P_{B}(T)) = 1$), then the prices at $T = 0$ must be the same or an arbitrage is present.
  - This can be justified financially/logically as follows:
    - Suppose that $P_{A}(0) \not = P_{B}(0)$ and that the prices are not random - they are known and deterministic prices at time $T = 0$ (i.e. we know the current prices).
    - Either $P_{A}(0) > P_{B}(0)$ or $P_{A}(0) < P_{B}(0)$.
    - Using the scenario where $P_{A}(0) > P_{B}(0)$, an arbitrage portfolio can be constructed by taking a short position in asset A and a long position in asset B.
    - The cash is received by entering into this portfolio is equal to $P_{A}(0) - P_{B}(0)$.
    - At time $T$, the cash is valued at $(P_{A}(0) - P_{B}(0))e^{rT}$ where $r$ is the risk-free rate.
    - As s $P_{A}(T) = P_{B}(T)$, the cash received for exiting the long position in asset B can be used to purchase asset A and exit the short position.
    - The riskless profit here is equal to $(P_{A}(0) - P_{B}(0))e^{rT}$.

### Law of One Price Example 1: Stocks

- Using the same three stocks from the earlier example for arbitrage, construct a portfolio with 1 share of A and 2 shares of B. This can be referred to as asset 1 and at time $t$ the value $V_{1}(t)$ is:
$$V_{1}(t) = P_{A}(t) + 2 P_{B}(t)$$
- Similarly, asset 2 will be one share of stock C:
$$V_{2}(t) = P_{C}(t)$$
- Assuming as per the earlier example, that there are only two states in the world at time $t = 1$, the following is true:
$$Prob(V_{1}(1) = V_{2}(2)) = 1$$
- The value of the two assets at time $t = 0$ must be equal or there is an arbitrage. In this example there is an arbitrage:
$$V_{1}(0) = 65 \space USD$$
$$V_{2}(0) = 80 \space USD$$
$$\therefore V_{1}(0) < V_{2}(0)$$

### Law of One Price Example 2: Bonds

- Using the bond from the earlier example which paid 3 coupons of 600 USD as well as the final payment of the face value of 10,000 USD, construct an arbitrage portfolio of 3 zero-coupon bonds.
  - The bond can be modelled as a series of 3 cash flows:
    - 600 USD in year 1
    - 600 USD in year 2
    - 10,600 USD in year 3
  - The arbitrage portfolio will consist of the follow zero-coupon bonds:
    - $Z_{1}$ with a face value of 600 USD and a 1 year maturity
    - $Z_{2}$ with a face value of 600 USD and a 2 year maturity
    - $Z_{3}$ with a face value of 10,600 USD and a 3 year maturity
- The portfolio of the zero-coupon bonds will have the same cash flow as the original bond and so the *Law of One Price* dictates that the value of the portfolio must equal the price of the bond at any time $t$ (up until the 3 year maturity).
- Using the same risk free rates as the earlier example: $r(1) = 0.75\%$, $r(2) = 1.5\%$, and $r(3) = 2\%$:
$$Z_{1}(0) = \frac{600}{1 + 0.0075} = 595.53 \space USD$$
$$Z_{2}(0) = \frac{600}{(1 + 0.015)^{2}} = 582.40 \space USD$$
$$Z_{3}(0) = \frac{10600}{(1 + 0.02)^{3}} = 9988.62 \space USD$$
- The value of the portfolio $V(t)$ is:
$$V(t) = Z_{1}(t) + Z_{2}(t) + Z_{3}(t)$$
- As stated, at time $t = 0$, the value of the bond $B(0)$ must equal the value of the portfolio $V(0)$. The arbitrage can be shown as follows:
$$V(0) = 11,166.55 \space USD$$
$$B(0) = 10,000 \space USD$$
$$\therefore V(0) > B(0)$$

## Arbitrage and Discounted Cash Flow Analysis

- Arbitrage is what justifies the concepts of the *time value of money* and *present value*.
- The formula: $PV = e^{-rt}X$ where $r$ is the risk-free rate, must hold true for a present value $PV$ of any value/price $X$ otherwise there is an arbitrage, as demonstrated by the *Law of One Price*.
- Both of the following examples are special cases of arbitrage pricing.

### Discounted Cash Flow Analysis Example 1

- Take a prevailing interest rate of 6% on a 3 year term and a contract paying 10,000 in 3 years time (i.e a zero-coupon bond with a 10,000 USD face value).
- Discount a 10,000 USD payment in 3 years time using the prevailing interest rate:

```math
\begin{aligned}
PV &= e^{-rt}X \\
&= e^{-0.06 \times 3} \times 10000 \\
&= \boxed{8,353 \text{ USD}}
\end{aligned}
```

- If the contract is currently trading at 9,000 USD the contract is **overpriced** and a short position should be assumed to take advantage of the arbitrage.
  - The contract can be sold for 9,000 USD and the cash received then invested at the risk-free rate (6\%):
  - This leads to a investment worth $e^{0.06 \times 3} \times 9000 = 10,775 \space USD$.
  - A riskless profit of 775 USD is realized upon exiting the short position on the contract.
- If the contract is currently trading at 7,000 USD the contract is **underpriced** and a long position should be assumed to take advantage of this arbitrage.
  - 7,000 USD should be borrowed at the 3 year term risk-free rate to buy the contract.
  - This leads to a debt worth $e^{0.06 \times 3} \times 7000 = 8,381 \space USD$
  - Upon the contract expiry, 10,000 USD will be received and a riskless profit of 1,619 USD ($10,000 - 8381$) will be realized once the debt is paid back.

### Discounted Cash Flow Analysis Example 2

- Take the context for discounted cash flow analysis where a security makes $N$ payments $c_{1}, c_{2},..,c_{N}$ at times $t_{1}, t_{2},..,t_{N}$, and model each payment $c_{n}$ as a zero-coupon bond maturing at time $t_{i}$ with a face value of $c_{i}$.
- A portfolio that consists of all $N$ zero-coupon bonds replicates the cash flow.
- Using the *Law of One Price*, the value of this portfolio must equal the value of the cash flow.
- The value of the portfolio at time $t$ is:
$$V(t) = \sum_{i=1}^{N}Z_{i}(t)$$
- The face value of the $i^{th}$ zero-coupon bond (and the cash payment $c_{i}$) at time $t_{i}$ is:
$$Z_{i}(t_{i}) = c_{i}$$
- The value at time $t = 0$ of $c_{i}$ can be written in terms of the discount factor:
$$Z_{i}(0) = d(t_{i})c_{i}$$
- Let $P(t)$ be the value of the cash flow, where $PV = P(0)$. Using the *Law of One Price*:
$$P(0) = V(0)$$
$$P(0) = \sum_{i=1}^{N}Z_{i}(0) \equiv  \sum_{i=1}^{N}d(t_{i})c_{i}$$
- This reproduces the formula for discounted cash flow analysis using arbitrage justification.
