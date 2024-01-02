# Stochastic Processes

- [Stochastic Processes](#stochastic-processes)
  - [Introduction](#introduction)
  - [Formal Definitions](#formal-definitions)
  - [Time Series Statistics](#time-series-statistics)
  - [Fat-Tailed Distributions](#fat-tailed-distributions)
    - [Quantile-Quantile (Q-Q) Plots](#quantile-quantile-q-q-plots)
    - [Moments of a Distribution](#moments-of-a-distribution)
      - [Kurtosis](#kurtosis)
  - [Asset Return Measures](#asset-return-measures)
    - [Continuously-Compounded Returns](#continuously-compounded-returns)
    - [Asset Return Measures Example](#asset-return-measures-example)
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

## Fat-Tailed Distributions

- The density of a normal (Gaussian) distribution with mean $\mu$ and variance ${\sigma}^{2}$ is given by:
$$f(x) = \frac{1}{\sqrt{2 \pi {\sigma}^{2}}}e^{-\frac{(x- \mu)^{2}}{2 {\sigma}^{2}}}$$
- As $x \rightarrow \plusmn \infty$, the normal density (and the probability) will decay exponentially.
- **Fat-tailed** distributions are probability distributions with densities that decay to 0 slower than exponentially and typically, will decay algebraically by $\frac{1}{x^{k}}$.
  - For example, the density of the [Student T-Distribution](https://www.investopedia.com/terms/t/tdistribution.asp) with $\nu$ degrees of freedom decays by $\frac{1}{|x|^{\nu + 1}} \text{ as } x \rightarrow \plusmn \infty$.

  ![Normal Distribution vs Fat-Tailed T-Distribution](images/t-distribution.png "Normal Distribution vs Fat-Tailed T-Distribution")

- As shown, outlier values of x are much more likely with fat-tailed distributions.

### Quantile-Quantile (Q-Q) Plots

- Quantile-quantile (q-q) plots compare the quantile of one random sample to the quantile of another random sample.
- A normal q-q plot compares the quantiles of a sample against the theoretical quantiles of a normal (Gaussian) distribution.
- If a random sample $\{x_{i}\}_{i=1}^{N}$ is from a normal distribution, the its normal q-q plot will resemble a straight line.
- For a fat-tailed distribution, the q-q plot will deviate from resembling a straight line at the extreme/outlier values:

  ![Normal Distribution vs Fat-Tailed T-Distribution Q-Q Plot](images/t-distribution-q-q.png "Normal Distribution vs Fat-Tailed T-Distribution Q-Q Plot")

### Moments of a Distribution

- The idea of a distribution having [moments](https://en.wikipedia.org/wiki/Moment_(mathematics)) stem from mechanics and is used to describe the shape of a function's graph. If a function describe the mass density, the zeroth moment would be the total mass, the first moment would be the center of mass and the second momnent would be the moment of intertia.
- In statistics, distributions have the following moments:
  - **First moment** is the mean (expected value)
  - **Second moment** is the variance (spread of values around the mean) and the standard deviation in the square root of the variance
  - **Third moment** is the skewness (how symmetric/asymetric the distribution is around the mean)
  - **Fourth moment** is the kurtosis ('fatness' of the tails)

#### Kurtosis

- A high kurtosis indicates that a lot of the data is distributed in the tails, whereas a low kurtosis indicates fewer data points in the tails.
- As this is the fourth moment, kurtosis is more sensitive to extreme outliers than the second moment variance.
- The standard definition for kurtosis is a **normalized** version of the fourth moment and, for a mean $\mu$ and variance $\sigma$, is given by:
$$\text{Kurt}(X) = E \left[ \left( \frac{X - \mu}{\sigma} \right)^4 \right]$$
- For a normally distributed random variable, the kurtosis is 3 so **excessive kurtosis** is defined as $\text{Kurt}(X) - 3$ for a random variable $X$.

## Asset Return Measures

### Continuously-Compounded Returns

- The 1-period **continuously compounded return** or **log return** of an asset with price $P(t)$ at time $t$ is defined as:

```math
\begin{aligned}
r(t) &= \text{log} \left( \frac{P(t)}{P(t-1)} \right) \\\\
&= \text{log}(P(t)) - \text{log}(P(t-1))
\end{aligned}
```

- The $k$-period continuously compounded return between a time $t$ and a time $k$-periods before $t$ can therefore be defined as:

```math
\begin{aligned}
r_k(t) &= \text{log} \left( \frac{P(t)}{P(t-k)} \right) \\
&= \text{log}(P(t)) - \text{log}(P(t-k)) \\\\
\end{aligned}
```

- The period $k$ should be in the same unit of time as the value for $t$ - this is normally years of days when working with financial models.
- The continuously compounded return is the $\text{log}$ of the corresponding [gross return](./2_interest-rates.md#gross-return).
- The continuously compounded returns across a period from $t$ to $t-k$ can be written as the sum of all the intervals within the period as follows:

```math
\begin{aligned}
r_{k}(t) &= \text{log}(P(t)) - \text{log}(P(t-1)) \\
&+ \text{log}(P(t-1)) - \text{log}(P(t-2)) \\
&+ \text{log}(P(t-2)) - \text{log}(P(t-3)) \\
&+ ...  \\
&+ \text{log}(P(t-k+1)) - \text{log}(P(t-k)) \\\\

r_{k}(t) &\equiv r(t) + r(t-1) + r(t-2) + ... + r(t-k+1) \\\\
r_{k}(t) &= \sum_{i=0}^{k-1}r(t-i)
\end{aligned}
```

### Asset Return Measures Example

- The prices for a stock on 6 consecutive business days ($t=[1,6]$) are as shown in the table below:

| Time, $t$ | Price, $P(t)$|
|:---------:|:-------------:|
|     1     |      105      |
|     2     |      111      |
|     3     |      102      |
|     4     |      109      |
|     5     |      107      |
|     6     |      108      |

- The daily $\text{log}$ returns can be calculated as follows:

```math
\begin{aligned}
r(t) &= \text{log} \left( \frac{P(t)}{P(t-1)} \right) \\\\
r(2) &= \text{log} \left( \frac{P(2)}{P(1)} \right) = \text{log} \left( \frac{111}{105} \right) = \boxed{2.41 \%} \\\\
r(3) &= \text{log} \left( \frac{P(3)}{P(2)} \right) = \text{log} \left( \frac{102}{111} \right) = \boxed{-3.67 \%} \\\\
r(4) &= \text{log} \left( \frac{P(4)}{P(3)} \right) = \text{log} \left( \frac{109}{102} \right) = \boxed{2.88 \%} \\\\
r(5) &= \text{log} \left( \frac{P(5)}{P(4)} \right) = \text{log} \left( \frac{107}{109} \right) = \boxed{-0.80 \%} \\\\
r(6) &= \text{log} \left( \frac{P(6)}{P(5)} \right) = \text{log} \left( \frac{108}{107} \right) = \boxed{0.40 \%} \\\\
\end{aligned}
```

- The weekly $\text{log}$ return can be calculated as follows:

```math
\begin{aligned}
r_{k}(t) &\equiv r(t) + r(t-1) + r(t-2) + ... + r(t-k+1) \\\\
r_{f}(6) &= r(2) + r(3) + r(4) + r(5) + r(6) \\
&= 2.41 \% -3.67 \% + 2.88 \% - 0.80 \% + 0.40 \% \\
&= \boxed{1.22 \%}
\end{aligned}
```

## Brownian Motion