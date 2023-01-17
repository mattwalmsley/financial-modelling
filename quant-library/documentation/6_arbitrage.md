# Arbitrage

- [Arbitrage](#arbitrage)
  - [Conceptual Introduction](#conceptual-introduction)
  - [Formal Definition](#formal-definition)
  - [Applying the Concept of Arbitrage](#applying-the-concept-of-arbitrage)

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