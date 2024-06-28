# Statistics

- [Statistics](#statistics)
  - [Financial Data](#financial-data)
    - [Key Concepts](#key-concepts)
      - [Stationary](#stationary)
      - [Marginal Distribution](#marginal-distribution)
      - [Ergodic Theorem](#ergodic-theorem)
    - [Returns](#returns)
      - [Gross Returns](#gross-returns)
      - [Net Returns](#net-returns)
      - [Example: Calculating Returns on a Financial Time Series](#example-calculating-returns-on-a-financial-time-series)

## Financial Data

- The main use case for statistics in finance concern how assets will change in value over time, and more specifically what the future value of an asset is likely to be.
  - Given future asset values are unknown, probability and statistics are used to create reasonable models and forecasts.
- Fundamentally, financial entities are looking to profit from changes in asset values whilst minimising the risk of loss.
- **Time series** is the main form of financial data, with a time-dependent variable $V$ representing an asset's value at a time $t$.
$$V(t_{1}), V(t_{2}), ...,V(t_{n-1}), V(t_{n})$$
- The unit of time can vary from milliseconds to years, but should be consistent when working with a time series dataset.
- For the purpose of financial analysis, **asset returns** are more useful than outright asset values/prices.
- **Net return** $r(t)$ represents the *percentage change* between two prices at times $t$ and $t-1$, and is calculated by $r(t) = \frac{P(t) - P(t-1)}{P(t-1)}$.
  - In other words, the net return is a measure of the *relative return* as a fraction of the value at $t-1$ realized on the asset from $t-1$ to $t$.
- Many financial time series, in particular returns, can be assumed to be stationary.

### Key Concepts

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

#### Gross Returns

- The gross return on an asset is defined by:
$$\text{Gross Return} = \frac{P(t)}{P(t-1)}$$
- This is the ratio of the price of an asset at the end of the return horizon to the price at the start.

#### Net Returns

- As mentioned previously, the net return on an asset is defined by:
$$\text{Net Return} = \frac{P(t)-P(t-1)}{P(t-1)}$$
- This is the ratio of the change in price of an asset over the return horizon to the price at the start.
  - The profit or loss (PnL) is represented by $P(t)-P(t-1)$ so the net return is therefore the PnL represented as a fraction/percentage of the value of the investment at the previous time period, $t-1$.
- The net return can be rearranged to be expressed as:
$$\text{Net Return} = \frac{P(t)}{P(t-1)} -1$$

#### Example: Calculating Returns on a Financial Time Series