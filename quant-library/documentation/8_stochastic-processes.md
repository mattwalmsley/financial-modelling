# Stochastic Processes

- [Stochastic Processes](#stochastic-processes)
  - [Introduction](#introduction)
  - [Formal Definition](#formal-definition)

## Introduction

- The pricing formulas for [forwards, futures and swaps](./7_forwards_futures_swaps.md) were derived by only using arbitrage principals.
  - These instruments are known as being **linear** - i.e. the [payoff](./7_forwards_futures_swaps.md#payoffs) has a linear correlation to the price of the underlying asset.
- [Options](./9_options.md), on the other hand, are known as **non-linear** as the price of the underlying asset does not have a linear correlation to the option payoff.
  - A model for the behaviour of the underlying asset that uses **stochastic processes** is therefore needed to price options.
- In simple terms, stochastic processes try to model 'random changes over time'. Other ways to describe stochastic processes include:
  - A random evolution
  - A random function
  - A collection of random paths
- Applying stochastic processes to finance can be done by denoting $S(t)$ as the price of an asset at time $t$ where $t \geq 0$. Whilst $S(0)$ is known, $S(t)$ will evolve over time and take a random/uncertain path such that $S(t)$ will be a collection of random values.
![Stochastic Processes](images/stochastic-processes.png "Stochastic Processes")
- For times where $t \geq 0$, the value $S(t)$ is said to be a stochastic process.

## Formal Definition

> A **stochastic process** is a family of random variables $X(t)$ indexed by a parameter $t$ that can be interpreted as time.

- Stochastic processes can be categorised as being **discrete-time** stochastic processes where the process evolves at specific/discrete times ($X_{1}$ at $t_{1}$, $X_{2}$ at $t_{2}$, etc.) and as **continuous-time** stochastic processes where the process continuously evolves over time where $t \geq 0$.
  
> The **sample paths** of a stochastic process are the actual realized paths that could be followed by the process.

- In other words, a stochastic process could be regarded as being a probability distribution on the set of all sample paths.