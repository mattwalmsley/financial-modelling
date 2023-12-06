# Stochastic Processes

- [Stochastic Processes](#stochastic-processes)
  - [Introduction](#introduction)
  - [Formal Definitions](#formal-definitions)
  - [Time Series Statistics](#time-series-statistics)
  - [Brownian Motion](#brownian-motion)

## Introduction

- The pricing formulas for [forwards, futures and swaps](./7_forwards_futures_swaps.md) were derived by only using arbitrage principals.
  - These instruments are known as being **linear** - i.e. the [payoff](./7_forwards_futures_swaps.md#payoffs) has a linear correlation to the price of the underlying asset.
- [Options](./9_options.md), on the other hand, are known as **non-linear** as the price of the underlying asset does not have a linear correlation to the option payoff.
  - A model for the behaviour of the underlying asset that uses **stochastic processes** is therefore needed to price options.
- In simple terms, stochastic processes try to model 'random changes over time'. Other ways to describe stochastic processes include:
  - A random evolution
  - A random function
  - A collection of random paths
- A **Random Walk** is a stochastic process comprised of a succession *random steps* that are determined probabilistically.
  - As an [example](https://mathworld.wolfram.com/RandomWalk1-Dimensional.html), let the result of flipping a coin determine whether a person takes a step to the left or to the right. Flipping the coin every minute for 10 minutes would take the person on a 'random walk' comprised of a succession of randomly determined steps.
  - The probability of taking one specific path is $\left(\frac{1}{2}\right)^{10} = \frac{1}{1024}$ and because every path has the same probability of being taken, the total number of possible paths is 1024.
- Applying stochastic processes to finance can be done by denoting $S(t)$ as the price of an asset at time $t$ where $t \geq 0$. Whilst $S(0)$ is known, $S(t)$ will evolve over time and take a random/uncertain path such that $S(t)$ will be a collection of random values.
  - For times where $t \geq 0$, the value $S(t)$ is said to be a stochastic process.

    ![Stochastic Processes](images/stochastic-processes.png "Stochastic Processes")

## Formal Definitions

> A **stochastic process** is a family of random variables $X(t)$ indexed by a parameter $t$ that can be interpreted as time.

- Stochastic processes can be categorised as being **discrete-time** stochastic processes where the process evolves at specific/discrete times ($X_{1}$ at $t_{1}$, $X_{2}$ at $t_{2}$, etc.) and as **continuous-time** stochastic processes where the process continuously evolves over time where $t \geq 0$.
- Continuous-time stochastic processes are defined by specifying joint probability distribution for the random variables $X(t_{1})$, $X(t_{2})$,...etc. at arbitrary times $t_{1}$, $t_{2}$,...etc.
  - [Brownian motion](#brownian-motion), the random motion of particles suspended in a medium, is denoted as $W(t)$ and the following assumptions are made:
    - For times $t_{1} < t_{2} < t_{3}$, the random variables $W(t_{2}) - W(t_{1})$ and $W(t_{3}) - W(t_{2})$ are independent.
    - For any times $t_{1} < t_{2}$ the random variables can be modelled by a normal distribution with mean 0 and variance $t_{2} - t_{1}$, i.e. in notation form: $W(t_{2}) - W(t_{1}) \sim \mathcal{N}(0, t_{2} - t_{1})$.
  
> The **sample paths** of a stochastic process are the actual realized paths that could be followed by the process.

- In other words, a stochastic process could be regarded as being a probability distribution on the set of all sample paths.

> A **Random Walk** is a discrete time stochastic process and is defined as having $j$ steps where the $j$'th step is denoted $X_{j}$.

- The steps, a succession of $X_{j}$, are independent and identically distributed such that:
$$\text{Prob}(X_{j} = +1) = \frac{1}{2}$$
$$\text{Prob}(X_{j} = -1) = \frac{1}{2}$$
- The random walk of $n$ steps is therefore defined as:
$$S_{n} = \sum_{j=1}^{n}X_{j}$$
- In financial terms, $X(j) \equiv P(t_{j})$ could be the prices of a financial asset on a business day $t_{j}$ assuming $t_{1}$, $t_{2}$,... etc. are successive business days.

## Time Series Statistics

- For a time series: $...X(t_{0}), X(t_{0}+1), X(t_{0}+2),..., X(t_{0}+k)...$ where $X(t)$ is the price of an asset observed at time $t$ and $t_{0}$, $(t_{0}+1)$, $(t_{0}+2)$,...etc. are consecutive business days.
- The joint distribution of $(X(k), X(k+1),..., X(k+j))$ is said to be **strictly stationary** if the distribution only changes with $j$ and not $k$ - i.e. with the number of successive observations and not the point in time that these observations are made.
  - In simpler terms, the joint distribution of a set of observations in the time series is the same regardless of when or where in the time series the observation is made.
- This leads to the assumption that $X(k)$ has the same distribution as $X(1)$ and that $(X(k), X(k+1))$ has the same distribution as $(X(1), X(2))$ etc.
- In practice strict stationarity is reduced to **stationarity** so that this principle holds up only to *second moments* - i.e. only as far as *variance* and *covariance* are concerned.
- The **autocovariance** function of a time series $X(t)$ is defined to be: $\gamma (k,\mathcal{l}) \equiv \text{cov}(X(k),X(\mathcal{l})) \equiv E[(X(k) - E(X(k)))(X(\mathcal{l}) - E(X(\mathcal{l})))]$ for observations made at time $k$ and $\mathcal{l}$.
- The time series is *stationary* if its autocovariance function is **translation invariant** along with the expectation $E[X(k)]= \mu$ - i.e. $\mu$ is independent of $k$.
  - **Translation invariance** defines the observation to be independent of time, such that $\gamma (k+t,\mathcal{l}+t) = \gamma (k,\mathcal{l})$.
  - $\text{cov}(X(k),X(\mathcal{l}))$ only depends on the lag $\mathcal{l}-k$.
- *Stationarity* implies the following:
  - The covariance of any two successive observations is the same, such that $\text{cov}(X(0),X(1)) = \text{cov}(X(1),X(2)) = \text{cov}(X(2),X(3))=...= \text{cov}(X(k),X(k+1))$
  - The covariance is also equal where the lag between the observations is equal, such that $\text{cov}(X(0),X(5)) = \text{cov}(X(1),X(6))$ etc.
  - The variances are also equal for all observations, such that $\text{Var}(X(0)) = \text{Var}(X(1))=...= \text{Var}(X(k))$.
- The autocovariance function for the *stationary* case can therefore be denoted as $\gamma (k) \equiv \text{cov}(X(k),X(t+k))$ as this is independent of $t$.
- Given that, for a stationary time series, the covariance between two terms in the series only depends on the lag between, the **autocorrelation** function for a stationary time series is defined as $\rho(k) = \text{corr}(X(t),X(t+k)) = \frac{\gamma(k)}{\gamma(0)}$ which is also independent of $t$.
  - $\rho(0) = 1$ for any time series.
- The **sample autocovariance** and **sample autocorrelations** function, given a realized sample of a time series: $x(1)$, $x(2)$,...,$x(t)$,...,$x(N)$ with $N$ observations, are defined as follows:
  - The sample mean for this series will be $\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x(i)$
  - The **sample autocovariance** function is $\hat{\gamma}(k) = \frac{1}{N} \sum_{i=1}^{N-k}(x(i)-\bar{x})(x(i+k)-\bar{x})$
  - The **sample autocorrelation** function is $\hat{\rho}=\frac{\hat{\gamma}(k)}{\hat{\gamma}(0)}$

## Brownian Motion