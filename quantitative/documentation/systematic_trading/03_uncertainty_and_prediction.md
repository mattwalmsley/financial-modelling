# Uncertainty & Prediction

- [Uncertainty \& Prediction](#uncertainty--prediction)
  - [Understanding Uncertainty in Trading](#understanding-uncertainty-in-trading)
    - [Types of Uncertainty](#types-of-uncertainty)
      - [The World Changes](#the-world-changes)
      - [The Wrong Model](#the-wrong-model)
      - [Parameter Uncertainty](#parameter-uncertainty)
    - [Prediction from Past Data](#prediction-from-past-data)
      - [Conditional vs Unconditional Forecasts](#conditional-vs-unconditional-forecasts)
      - [Underlying Instrument Returns vs Trading Strategy Returns](#underlying-instrument-returns-vs-trading-strategy-returns)
  - [Predicting Means](#predicting-means)
    - [Parameter Uncertainty of Mean Estimates](#parameter-uncertainty-of-mean-estimates)
      - [T-Statistics and Breakeven Horizon](#t-statistics-and-breakeven-horizon)
    - [Empirical Examples of Mean Estimates](#empirical-examples-of-mean-estimates)
    - [Mean Estimates at Different Frequencies](#mean-estimates-at-different-frequencies)
    - [How Well Do Mean Estimates Predict the Future?](#how-well-do-mean-estimates-predict-the-future)
    - [Is It Worth Updating Forecasts More Frequently?](#is-it-worth-updating-forecasts-more-frequently)
    - [Is It Worth Pooling Data When Making Forecasts?](#is-it-worth-pooling-data-when-making-forecasts)

## Understanding Uncertainty in Trading

Understanding uncertainty, and coping with it, is key to investing and trading. The future returns of asset prices are difficult to forecast with certainty, and the best that can be done is to try and shift the probabilities slightly in one's favour.

This is doubly true for systematic traders, since they build trading strategies based on tests of past performance. In designing those strategies it's vital to have a well calibrated sense of how much uncertainty there is in asset returns, and to what degree.

Once strategies have been designed it is necessary to decide whether they are worth using, and how to allocate capital to them. To do this their historic performance needs to be evaluated, both in absolute terms, and also relative to other strategies. Again it's important to understand how meaningful these performance statistics are, and how useful they might be in predicting the future.

**Two scenarios where predictions are made about future performance:**

1. **Very simple systematic strategies** where past data is used to make conditional forecasts of future asset price returns
2. **When evaluating the performance of trading strategies**, where past data is used to make unconditional past forecasts of trading strategy returns. This is used to decide which trading strategy to use (fitting) and in what proportion capital should be allocated to different strategies (allocation).

### Types of Uncertainty

Any kind of analysis of uncertainty involves creating a statistical model for returns. Implicit in the model is a forecast for future returns. A trivial model would be:

> FTSE 100 stocks will rise by 5% a year

This model is trivial because it has no uncertainty. A better model would include some forecast of the amount of variation expected:

> There is a 95% chance that FTSE 100 stocks will have a return in the range -10% to +20%, with an expected return of 5% a year.

Given certain assumptions this can be restated as a statistical model:

> Annual returns of the FTSE 100 stock index will be drawn from a Gaussian normal distribution with a mean of 5% and a standard deviation of 15%. If the risk free interest rate is assumed to be 1% then the expected Sharpe Ratio will be 4% / 15% = 0.267

**Important features of this model:**

- It assumes a particular statistical distribution: Gaussian normal
- It has a set of parameters: for Gaussian normal two parameters are needed, the mean and standard deviation
- It describes what has happened in the past, and it also gives a range of forecasts for the future
- For the moment this is a univariate distribution – it only describes the behaviour of a single asset. Later joint distributions will be considered which jointly model the prices of multiple assets

Some of the market's uncertainty is now captured inside the model. However unless the model is perfect there will still be some unmodelled, residual uncertainty. In particular:

1. **The world could change:** a model which described the past correctly may not be any good for forecasting the future.
2. **The model might be wrong.** Gaussian normal distributions are poor models to use for most financial return data. For example equity prices tend to have negative skew and higher kurtosis than in the Gaussian model.
3. **Parameter estimate accuracy is unknown:** there is parameter uncertainty.

#### The World Changes

Not much can be done about the world changing – as quantitative traders must assume the past is a guide to the future. This doesn't mean sophisticated models cannot be used which account for multiple types of future, or update their parameters according to what has happened recently.

#### The Wrong Model

Choosing an appropriate model is a trade off. Whilst more complex models will fit past data better they also have some disadvantages:

- Beyond a certain point adding more parameters makes it less likely that a model will accurately forecast the future.
- Estimates of higher moment parameters like kurtosis and skew can be heavily influenced by one or two outliers, giving larger parameter uncertainty.
- It can give a false sense of security if one thinks that the statistical model is complex enough to explain the world entirely.
- With a simple model like the Gaussian two parameter model an intuitive grasp of many of its features can be obtained. It's probably better to use a simple model whose weaknesses are well understood than to use a complex model whose shortcomings are less well understood.

In this course only Gaussian distributions will be used, but the focus will also be on the implications of non Gaussian returns, in particular the presence of strongly negative or positive skew.

#### Parameter Uncertainty

Of the three problems listed much more time will be spent thinking about parameter uncertainty: which is the sampling error of the parameters being estimated. Parameters with high estimation uncertainty also tend to be difficult to forecast. If parameter uncertainty is understood there will be a better idea of how good forecasts of the future are likely to be.

### Prediction from Past Data

Firstly very simple systematic strategies may use unconditional estimates for asset returns and assume these are likely to repeat in the future (more complex strategies will use other information, like carry or momentum to decide what position to take).

But prediction is also important when considering the allocation of capital to trading strategies, because traders need to analyse the returns made by their trading strategies. An example of this would be deciding how good the carry strategy was on different futures, such as the S&P 500 or the Eurodollar contracts.

To make predictions the parameter uncertainty of past data first needs to be understood. It is then possible to look at how well historic estimates predict future values.

#### Conditional vs Unconditional Forecasts

When making statistical inferences from data, there are two approaches:

**Unconditional:**

- All available data is taken and statistical inferences are made from it
- No partitioning or filtering of the data based on additional information
- Example: Calculate the average return of all US 10 year bond futures data

**Conditional:**

- The data is partitioned according to some additional condition $x$ and inferences are made conditional on $x$
- Example: The dataset could be split into instruments with high carry and low carry, and the level of carry's effect on average returns can be examined
- **This is what most trading strategies do, except the very simplest**

#### Underlying Instrument Returns vs Trading Strategy Returns

It's important to distinguish between two types of returns:

**Underlying instrument returns:**

- The returns of the things being actually traded
- Example: US 10 year bond futures, S&P 500 futures, EUR/USD currency pair

**Trading strategy returns:**

- The returns of strategies trading a given instrument (or instruments) with a given set of parameters
- Example: A momentum trading strategy with a lookback of 14 days, that trades US 10 year bond futures
- Example: A carry strategy with specific position sizing rules, trading multiple currency pairs

The distinction is crucial because:

- Underlying instrument returns are what is observed in the market
- Trading strategy returns depend on both the underlying returns AND the rules applied
- Both types of returns need to be analyzed, but for different purposes

> **Note:** Conditional forecasts for the returns of trading strategies are not considered here. Systematic traders do not normally vary their allocations according to exogenous information. Instead, allocations are kept fixed using unconditional information, and any conditioning variable is incorporated inside the model itself. For example there is evidence that the carry risk premium is higher when the interest rate spread (or equivalent in futures) is higher, as long as it is not too high. One option would be to condition the expected returns for the carry model depending on the interest rate (or futures) spread. But a far simpler option is to incorporate the interest rate (or futures) spread inside the trading strategy.

## Predicting Means

### Parameter Uncertainty of Mean Estimates

From the central limit theorem it is known that the distribution of the mean estimate is Gaussian normal. The variance of the distribution of the mean estimate is:

$$\omega = \frac{\sigma^2}{N}$$

Where $N$ is the number of samples, and $\sigma$ is the estimate of the standard deviation.

**Example:** Over 100 weeks a trading strategy has an average return of 1% a week with a standard deviation of 5% a week. The variance $\omega$ of the mean estimate is $5^2 / 100 = 0.25\%$. The standard deviation of the mean estimate is the square root $\sqrt{\omega} = \sqrt{0.25\%} = 0.5\%$.

Strictly speaking the distribution of the mean estimate is a t-distribution, however in this course it is assumed that a Gaussian normal distribution can be used to find confidence intervals (the t-distribution converges on the Gaussian normal for large numbers of data points, implying large numbers of degrees of freedom).

Since the distribution is normal there is a 95% chance that the mean estimate lies within +/- 1.96 standard deviations of the mean. So there is a 95% chance that the mean estimate lies within the range $1\% \pm (0.5\% \times 1.96)$, i.e. between 0.02% and 1.98%.

This is a very wide range: generally not much certainty is obtained about mean estimates.

#### T-Statistics and Breakeven Horizon

To determine if the returns from this strategy are likely to be positive a one sided t-test would be used. For a sample size of 100 to achieve a p-value of 5% (only a 5% chance that the true value of the mean was negative) the appropriate t-statistic is around 1.67.

The t-statistic is the mean divided by the standard deviation of the mean estimate:

$$T = \frac{\mu}{\sqrt{\omega}} = \frac{\mu}{\sqrt{\sigma^2/N}} = \frac{\mu\sqrt{N}}{\sigma}$$

In the simple example being used the t-statistic is $1\% \times \sqrt{100} / 5\% = 2.0$

A useful rule of thumb is to calculate the **'breakeven' horizon**: the number of time periods to reach a t-stat of 2, where there can be roughly 97% confidence that the mean was positive can be calculated as follows:

$$2 = \frac{\mu\sqrt{N}}{\sigma}$$

$$\sqrt{N} = \frac{2\sigma}{\mu}$$

$$N = 4\left(\frac{\sigma}{\mu}\right)^2$$

This is a rough approximation since the critical value for the T-statistic will itself depend on the value of $N$. In an exam you'd be instructed how you should deal with this; usually you'll be given the critical value to find the breakeven with.

If the risk free interest rate is ignored when calculating the Sharpe Ratio, SR, then this gives $4 / SR^2$. In the simple example being considered here the Sharpe Ratio is $1\% / 5\% = 0.2$ that gives a breakeven of $4 / (0.2^2) = 100$ weeks, as expected.

### Empirical Examples of Mean Estimates

Consider the daily percentage returns of the US 10 year bond futures contract for the following 9,008 observations:

- The average is 0.0187% per business day; with a standard deviation of 0.423% per day

If compounding effects are ignored then to find the annual equivalent of a daily return just multiply by the number of days in a year. Assuming there are 256 business days in a year $0.0187\% \times 256 = 4.8\%$ a year.

> **Note on compounding:** Compounding effects are ignored throughout this course because it makes calculations easier and gives more intuitive results.
>
> **Note on business days:** 256 is used throughout this course because it is $16^2$ which is a very useful result. Other figures like 252 and 261 may be seen used elsewhere (261 is the number of weekdays in a 365 day year that has exactly 52 weekends; there are roughly 9 additional public holidays). In practice the number of days that a market opens varies depending on the country and year.

If returns are independently distributed over time then **time scale standard deviation** can be used. For example if the annual standard deviation of returns is 10%, then the weekly standard deviation will be 10% divided by the square root of the number of weeks in a year (which is around 52.2), i.e. $10\% / \sqrt{52.2} = 10\% / 7.22 = 1.38\%$.

> **Note:** Examples of series which would break these assumptions are those with significant auto correlation of returns, or prices that keep reverting towards long run averages or which exhibit strong trends.

If time scaling can be used then 0.432% works out to 6.78% a year. The daily Sharpe Ratio then is $0.019\% / 0.423\% = 0.044$, the variance of the mean estimate is $\omega = 0.423^2 / 9008 = 0.000001992\%$. The standard deviation of the mean estimate is the square root $\sqrt{\omega} = 0.00446\%$. There is a 95% chance that the mean estimate lies within the range $0.019\% \pm (0.00446\% \times 1.96)$, i.e. between 0.0099% and 0.0274%, or in more meaningful annual returns between 2.54% and 7.02%.

**This incredibly wide range is typical of real financial assets** which do not usually have high Sharpe Ratios (the annual Sharpe Ratio here is $4.78\% / 6.78\% = 0.70$), and even with plenty of data (9,008 business days is around 36 years) the confidence intervals remain very wide.

**How do the confidence intervals vary over time?**

The y axis shows the return in annualised units, so 0.1 is 10% a year. The red and blue lines show the extreme ends of the 95% confidence intervals. Notice how the interval narrows as more data is obtained, from a range of 35% to a range of around 4.5%. Also notice how the confidence interval narrows more slowly over time, as it's converging at roughly the square root of time (ignoring the effect that changing estimates of standard deviation have).

### Mean Estimates at Different Frequencies

Data is often obtained, particularly for external funds, at relatively low frequencies: monthly or annual. What if data was available weekly, daily, hourly or even second by second?

In fact under certain assumptions **the frequency at which data is obtained makes almost no difference**. Remember if returns are independently distributed over time then time scaling of standard deviation can be used.

**Example:** Suppose a fund has returned 5% annually over 16 years, with a 10% standard deviation of returns. The variance of the mean estimate $\omega$ is $10^2 / 16 = 6.25\%$, and the standard deviation will be $\sqrt{6.25\%} = 2.5\%$. The mean estimate is $5\% / 2.5\% = 2.0$ standard deviations away from zero.

Trivially the weekly average return would have been $5\% / 52.2 = 0.958\%$. Assuming time scaling can be used the standard deviation of weekly returns will be 1.38%, as already calculated. There are $52.2 \times 16 = 835.2$ weeks of data. The variance of the mean estimate is $1.38^2 / 835.2 = 0.00228\%$, and the standard deviation of the mean estimate is the square root of that, 0.04775%. The mean estimate is $0.0958\% / 0.0477\% = 2.0$ standard deviations away from zero: exactly the same result as before.

|                                                     | Years |  Weeks   |
| :-------------------------------------------------- | :---: | :------: |
| Average return $\mu$                                |  5%   | 0.0958%  |
| Standard deviation of returns $\sigma$              |  10%  |  1.38%   |
| Variance of mean estimate $\omega$                  | 6.25% | 0.00228% |
| Standard deviation of mean estimate $\sqrt{\omega}$ | 2.5%  | 0.04775% |
| Significance of mean estimate $\mu / \sqrt{\omega}$ |  2.0  |   2.0    |

Although the T-statistic is unchanged the critical value for the t-statistic will be lower with more frequent data should be kept in mind. In this simple example starting with 15 degrees of freedom with annual data, which for a 2.5% one sided test has $T_{critical} = 2.131$ (so the test for significance would be failed in this example). Using monthly data would give $(12 \times 10) - 1 = 119$ degrees of freedom, $T_{critical} = 1.98$ (resulting in a bare pass). Going to weekly or daily data doesn't improve things much as $T_{critical}$ asymptotes to 1.96 as the number of degrees of freedom increases.

If volatility scaling doesn't apply (because returns aren't independent) then having more frequent data will be more important, as otherwise the standard deviation estimate for lower frequency data will be biased, which means that the standard deviation of the mean estimate $\sqrt{\omega}$ will also be affected.

### How Well Do Mean Estimates Predict the Future?

Consider the following exercise:

1. Annually, estimate the mean from past data. Calculate a 95% confidence interval for that estimate.
2. Calculate the actual mean during the following year
3. Compare this to the confidence interval

For the US 10 year bond future analysed earlier the following results are obtained:

**Even though the confidence interval for the mean is very wide, the realised annual mean is still outside it roughly half the time. Historic mean estimates do a poor job of predicting future average returns.**

### Is It Worth Updating Forecasts More Frequently?

Theoretically all available data should always be used to make forecasts, since the formula above indicates that the parameter uncertainty will be lower the more history there is. However this ignores the problem of non stationarity that exists in the real world. In practice financial assets seem to go through periods of change; for example the relatively poor returns of equities in the 2008-9 stock market crash, and the subsequent outperformance.

So an important question is whether less data should be used and forecasts updated more frequently, or is it better to update more slowly using more data.

Referring back to the plot of the US 10 year earlier it's obvious that using a shorter lookback would be of no help here. The green line of actual returns varies considerably from year to year, so using the previous year would be of no help in predicting the next year.

This can be shown graphically with a scatter plot of the previous year's return (x axis) against the subsequent year's return (y axis):

There is clearly no clear relationship; if anything the relationship is negative. If ex-post is regressed on ex-ante annual returns a slope of -0.29 is obtained. However the p-value of the regression is 0.25, indicating a 25% probability these results are just chance. This is a lot higher than the normal value of 0.05 required for significance. The $R^2$ is just 0.04; this model is no better than random noise.

The picture is no better for monthly returns:

There is a very slight tendency for high monthly returns to predict higher monthly returns, and vice versa. The slope here is positive and the p-value is lower, 0.14, although not significant; the $R^2$ is still a lousy 0.05.

Different forecasting windows (say between a month and a year, or less than a month) have similarly poor performance.

**In fact this type of forecasting will only work for relatively fast trading strategies which have a very high Sharpe Ratio.** Such strategies performance is expected to quickly degrade over time as other market participants discover it, so it's worth updating your forecast of their performance on a regular basis.

### Is It Worth Pooling Data When Making Forecasts?

Using more history isn't the only way to get more data, data can also be pooled from multiple assets. For example with the variance of the estimate $\sqrt{\omega} = \sqrt{\sigma^2/N}$ the variance of the estimate can be halved either by using twice as much history, or by using data from two different assets.

Of course this would only make sense if there was reason to believe that the means from different assets ought to be the same. This usually doesn't make sense for underlying assets, although it might make sense for trading strategies.
