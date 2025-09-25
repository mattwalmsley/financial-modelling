# Statistics

- [Statistics](#statistics)
  - [Financial Data](#financial-data)
    - [Financial Statistics Concepts](#financial-statistics-concepts)
      - [Stationary](#stationary)
      - [Marginal Distribution](#marginal-distribution)
      - [Ergodic Theorem](#ergodic-theorem)
    - [Returns](#returns)
      - [Gross Rate of Return](#gross-rate-of-return)
      - [Example 1: Calculating Returns from Values](#example-1-calculating-returns-from-values)
      - [Example 1: Calculating Weekly Returns from Daily Returns](#example-1-calculating-weekly-returns-from-daily-returns)
      - [Continuously Compounded Returns](#continuously-compounded-returns)

## Financial Data

- The main use case for statistics in finance concern how assets will change in value over time, and more specifically what the future value of an asset is likely to be.
  - Given future asset values are unknown, probability and statistics are used to create reasonable models and forecasts.
- Fundamentally, financial entities are looking to profit from changes in asset values whilst minimising the risk of loss.
- **Time series** is the main form of financial data, with a time-dependent variable $V$ representing an asset's value at a time $t$.
$$V(t_{1}), V(t_{2}), \dots,V(t_{n-1}), V(t_{n})$$
- The unit of time can vary from milliseconds to years, but should be consistent when working with a time series dataset.
- For the purpose of financial analysis, **asset returns** are more useful than outright asset values/prices.
- **Gross rate of return** $r(t)$ represents the *percentage change* between two prices at times $t$ and $t-1$, and is calculated by $r(t) = \frac{P(t) - P(t-1)}{P(t-1)}$.
  - In other words, the gross rate of return is a measure of the *relative return* as a fraction of the value at $t-1$ realized on the asset from $t-1$ to $t$.
- Many financial time series, in particular returns, can be assumed to be stationary.

### Financial Statistics Concepts

#### Stationary

- A stationary process has constant statistical properties, such as mean, variance, and autocorrelation, over time.
  - The value for $V(T)$ does not depend on $T$.
- For instance, if returns $r(t)$ are stationary, it implies that the average return and the variability of returns do not change over different periods.
- Stationarity is crucial for making reliable forecasts and in applying many statistical models that assume constant underlying distributions.
- A common technique to achieve stationarity is to transform the raw price series into a series of returns.

#### Marginal Distribution

- The marginal distribution of a subset of a collection of random variables is the probability distribution of that subset, ignoring the influence of the other variables.
  - In finance, this often refers to the distribution of returns for a single asset over time.
- Mathematically, for a joint probability distribution $P(X, Y)$ of two random variables $X$ and $Y$ representing the returns of two assets, the marginal distribution of $X$ is obtained by summing (or integrating, if dealing with continuous variables) the joint distribution over all possible values of $Y$:
  - Discrete variables: $P_{X}(x) = \sum_{y}P(X=x,Y=y)$
  - Discrete variables: $P_{X}(x) = \int_{-\infty}^{\infty}P(X=x,Y=y)dy$

- When handling the returns of multiple assets, the marginal distribution of a single asset's returns gives the probability of different return levels for that asset, without considering the returns of the other assets.
- Understanding the marginal distribution helps in assessing the risk and expected performance of individual assets.
  -For example, knowing the marginal distribution of returns $r(t)$ for a particular stock allows an investor to evaluate the likelihood of various return outcomes based on historical data.

#### Ergodic Theorem

- In a financial context, the ergodic theorem asserts that, over a long period, the time averages of a stochastic process (like asset returns) will converge to the ensemble averages (expected values).
  - This means that the long-term average return of an asset can be considered representative of its expected return.
- The ergodic property is essential for justifying the use of historical data to make inferences about future returns.
  - Financial analysts use past performance to estimate long-term trends and make probabilistic forecasts, assuming that the future will resemble the past over a sufficiently long horizon.

### Returns

- A return is a measure of an investor's profit/loss from an investment in a particular asset, given as a fraction (or percentage) of the initial investment.
  - Returns are independent of currency and price level, so are a useful measure when comparing the performance of multiple assets.
  - Prices are dependent on a wide variety of factors that are irrelevant when evaluating the profitability of an asset.
    - For example, a stock split wil affect the share price of an asset but have no impact on the returns.
- Let $P(t)$ represent a price time series for an asset at a time $t$.
  - Assume that the unit of time for $t$ is days.
- To define the return on an asset, the *return horizon* must be specified - this is the time period over which the return will be realized.
- For sake of ease, an investment horizon of 1 period, i.e. 1 day, will be used to initially define return measures.

#### Gross Rate of Return

- As mentioned previously, the gross rate of return on an asset is defined by:
$$\text{Net Return} = \frac{P(t)-P(t-1)}{P(t-1)}$$
- This is the ratio of the change in price of an asset over the return horizon to the price at the start.
  - The profit or loss (PnL) is represented by $P(t)-P(t-1)$ so the gross rate of return is therefore the PnL represented as a fraction/percentage of the value of the investment at the previous time period, $t-1$.

#### Example 1: Calculating Returns from Values

- A price time series is given in the table below.

|   Time    | Value, P(t) |   Daily Gross Rate of Return    |
| ----------|:-----------:|:------------------------------: |
| **t = 1** |     124     |                 -               |
| **t = 2** |     131     | $\frac{131-124}{124} = 5.65\%$  |
| **t = 3** |     128     | $\frac{128-131}{131} = -2.29\%$ |
| **t = 4** |     134     | $\frac{134-128}{128} = 4.69\%$  |
| **t = 5** |     132     | $\frac{132-134}{134} = -1.49\%$ |
| **t = 6** |     135     | $\frac{135-132}{132} = 2.27\%$  |

- The weekly gross rate of return can be calculated as follows:

$$
\begin{aligned}
\text{Gross rate of return} &= \frac{P(t=6)-P(t=1)}{P(t=1)} \\\\
&= \frac{135-124}{124} \\\\
&= 8.87\%
\end{aligned}
$$

#### Example 1: Calculating Weekly Returns from Daily Returns

- The daily gross rates of return are given in the table below for a one week period.

|    Day  | Return |
| --------|:------:|
| **Mon** |  0.7%  |
| **Tue** |  -0.2% |
| **Wed** |  1.2%  |
| **Thu** |  0.8%  |
| **Fri** |  -0.7% |

- The weekly gross rate of return can be calculated by tracking the value of 1 USD

|    Day  | Multiplier |                   Value                 |
| --------|:----------:|:---------------------------------------:|
| **Mon** |   1.007    |                $1(1.007)$               |
| **Tue** |   0.998    |            $1(1.007)(0.998)$            |
| **Wed** |   1.012    |        $1(1.007)(0.998)(1.012)$         |
| **Thu** |   1.008    |     $1(1.007)(0.998)(1.012)(1.008)$     |
| **Fri** |   0.993    |  $1(1.007)(0.998)(1.012)(1.008)(0.993)$ |

- The gross rate of return for week can be calculated by $\frac{1(1.007)(0.998)(1.012)(1.008)(0.993) - 1}{1} = (1.007)(0.998)(1.012)(1.008)(0.993) - 1 = 0.0180 = 1.80\%$
- The sum of the daily rates of return is therefore equal to the weekly rate of return:
$$r_{k}(t) = r(t-k+1) + r(t-k+2) +\dots+ r(t)$$

#### Continuously Compounded Returns

- A one-period continuously compounded return, $r(t)$, is calculated as follows:
$$P(t) = e^{r(t)}P(t-1)$$
$$r(t) = \log \left(\frac{P(t)}{P(t-1)} \right)$$
- Continuously compounded returns are also referred to as *logarithmic returns*.

