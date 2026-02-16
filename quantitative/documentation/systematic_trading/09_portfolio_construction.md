# Portfolio Construction

- [Portfolio Construction](#portfolio-construction)
  - [Why Create Portfolios?](#why-create-portfolios)
  - [Fama-French Style Long-Short Equity Portfolios](#fama-french-style-long-short-equity-portfolios)
  - [Characteristics of Fama-French Style Portfolios](#characteristics-of-fama-french-style-portfolios)
  - [Inverse Volatility Portfolios with Variable Risk and Forecast](#inverse-volatility-portfolios-with-variable-risk-and-forecast)
  - [Setting a Fixed Risk Target](#setting-a-fixed-risk-target)
  - [Controlling Net Exposure](#controlling-net-exposure)
  - [Long-Only Portfolios](#long-only-portfolios)
  - [Controlling Leverage and Margin](#controlling-leverage-and-margin)
  - [A Warning About Relative Value Strategies](#a-warning-about-relative-value-strategies)

## Why Create Portfolios?

From the position sizing section:

- Trading rules can be created for a single instrument (e.g. VIX or Crude oil futures) that calculate a forecast-implied Sharpe Ratio
- The optimal position to hold can be determined

However, the vast majority of systematic traders trade more than one instrument and may use multiple trading rules per instrument. Diversifying across different sources of return is generally acknowledged as excellent practice. Certain relative value strategies also inherently involve multiple instruments.

**Running example:** An equity market-neutral strategy with three instruments: Facebook, Google, and Citigroup. Current forecast-implied Sharpe Ratios: 1.0, −1.5, and 0.5 respectively. Standard deviations: 25%, 20%, and 12%. Market $\beta$: 0.9, 0.7, and 0.4. Correlations: Facebook/Google = 0.90, Facebook/Citi = 0.60, Google/Citi = 0.65.

## Fama-French Style Long-Short Equity Portfolios

The most famous constructed portfolios in academic literature are those from the Fama and French papers, which identified factors predicting US stock prices (later extended to other countries and factors).

> **Reference:** Fama, E. and French, K. — portfolio data available at the [Dartmouth data library](http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

**Construction method:**

1. Sort all stocks by factor value (e.g. book-to-price ratio)
2. Group the ranked stocks into quartiles, quintiles, or deciles
3. Place equally weighted **long** positions in the top group and equally weighted **short** positions in the bottom group

> **Reference:** The idea of portfolio sorts predates Fama and French. See Basu, S. (1977) "Investment Performance of Common Stocks in Relation to their Price Earnings Ratios: A Test of the Efficient Market Hypothesis" _Journal of Finance_ 32.

**Contrast with portfolio optimisation:**

- Estimate correlations and volatilities for every stock
- Use factor values to imply expected mean returns
- Optimise the portfolio — but this approach will probably produce extreme weights (since US equity correlations tend to be high)

**Applied to the running example:**

1. Sort by forecast-implied Sharpe Ratio: Facebook (1.0), Citi (0.5), Google (−1.5)
2. Group into terciles (one asset per group)
3. Long Facebook (\$500,000), short Google (\$500,000), no position in Citigroup

## Characteristics of Fama-French Style Portfolios

Using portfolio weights $w_1 = 1$ (Facebook), $w_2 = -1$ (Google), $w_3 = 0$ (Citigroup):

**1. Cash neutrality:**

$$\text{Net cash exposure} = \sum_i w_i = 1 + (-1) + 0 = 0$$

**2. Short selling required** — which may not always be possible.

**3. Fixed leverage factor:**

$$\text{Leverage factor} = \sum_i |w_i| = 2.0$$

This is fixed regardless of forecast confidence, and may not be appropriate.

**4. Not necessarily market-neutral:**

$$\text{Net Beta exposure} = \sum_i \beta_i w_i = 0.9 \times 1 + 0.7 \times (-1) + 0.4 \times 0 = 0.2$$

> If leverage is increased proportionally, Beta exposure scales proportionally (unless it is zero).

**5. Portfolio risk:**

$$\sigma_p = \sqrt{w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2w_1 w_2 \sigma_1 \sigma_2 \rho}$$

$$= \sqrt{1^2 \times 0.25^2 + (-1)^2 \times 0.20^2 + 2 \times 1 \times (-1) \times 0.25 \times 0.20 \times 0.90} = 11.18\%$$

This risk appears low given the double leverage, due to the high correlation (0.90) between the two assets. With zero correlation, the standard deviation would be 32.0%.

**6. Concentrated and potentially undiversified.** No position in Citigroup. Even in original Fama-French portfolios, long and short components often have different sector exposures.

**7. Does not account for forecast strength.** Positions would be identical if all forecast-implied Sharpe Ratios were halved.

**8. Discards aggregate signal information.** Cash neutrality ignores any signal about overall market direction. The forecasts suggest being net long banks and net short tech, but the actual position is neutral in both.

## Inverse Volatility Portfolios with Variable Risk and Forecast

An alternative construction method addresses many of the above problems. It is appropriate when:

- Leverage is freely available and margin is not a constraint
- Short positions are straightforward
- No constraints on cash, $\beta$, or net volatility exposure are required
- Portfolio risk is allowed to vary with forecast strength

The position calculation from the previous section is:

$$\text{Raw position} = \frac{\text{Trading capital} \times \text{Risk target}}{\text{Risk of instrument} \times \text{Value of instrument}}$$

Adjusted for forecast conviction:

$$\text{Position} = \text{Raw position} \times \frac{\text{Current implied forecast SR}}{\text{Average implied forecast SR}}$$

Expressed as a portfolio weight (position × value / capital):

$$w_i = \frac{\text{Current implied SR}_i \times \text{Risk target}}{\sigma_i \times \text{Average implied SR}_i}$$

Assuming an average implied forecast SR of 1.0 and a risk target of 12%:

| Instrument | Calculation                            | Weight |
| :--------- | :------------------------------------- | :----: |
| Facebook   | $1.0 \times 12\% / (25\% \times 1.0)$  | +0.48  |
| Google     | $-1.5 \times 12\% / (20\% \times 1.0)$ | −0.90  |
| Citi       | $0.5 \times 12\% / (12\% \times 1.0)$  | +0.50  |

**Capital allocation between strategies:**

A portfolio optimisation problem must be solved to allocate capital across instruments. Key differences from standard optimisation:

- Allocation is between separate trading strategies (one per instrument), not positions directly
- Weights should all be positive (a loss-making strategy would not be used)
- All strategies can be assumed to have the same expected volatility (the risk target), so the covariance matrix simplifies to the correlation matrix
- Correlation is measured between _strategy_ returns, not instrument returns

Using a simple allocation of 50% to Citigroup and 25% each to Facebook and Google:

| Instrument | Calculation         | Final Weight |
| :--------- | :------------------ | :----------: |
| Facebook   | $0.48 \times 25\%$  |    +0.12     |
| Google     | $-0.90 \times 25\%$ |    −0.225    |
| Citi       | $0.50 \times 50\%$  |    +0.25     |

**Properties of this portfolio:**

- **Net cash exposure:** $0.12 - 0.225 + 0.25 = 14.5\%$ (not cash-neutral)
- **Net Beta:** $0.9 \times 0.12 + 0.7 \times (-0.225) + 0.4 \times 0.25 = 0.0505$ (not Beta-neutral; depends on forecast strength)
- **Leverage factor:** $|0.12| + |0.225| + |0.25| = 0.595$ (varies with forecast strength)
- **Portfolio risk:** 2.68% (much lower than the 12% target — discussed below)

**Risk adjustment:** If all assets had a current implied forecast SR equal to the long-run average (1.0) and all assets were perfectly correlated ($\rho = 1.0$), then the portfolio risk would equal the 12% target. In practice, imperfect correlations and offsetting positions produce lower risk, requiring an upward adjustment to the risk target to compensate.

## Setting a Fixed Risk Target

To set a fixed risk target, the current implied risk is calculated and all positions are scaled proportionally:

$$\text{Scaling factor} = \frac{\text{Target risk}}{\text{Current implied risk}} = \frac{12\%}{2.68\%} = 4.48$$

**Advantages:** No correction factor needed for long-term risk.

**Disadvantages:** The same amount of risk is taken even as opportunities diminish, violating Kelly optimality. For example, if the half-Kelly optimal risk target is 15% but current forecasts imply only 10%, insisting on 15% exceeds the Kelly optimum.

## Controlling Net Exposure

Many funds have mandates limiting net exposure (cash or Beta), which can be zero (market-neutral) or capped.

**Method:**

1. Calculate the net exposure implied by current positions
2. Compare to the limit
3. Proportionally reduce positions on the "wrong" side

**Example:** If 5% net cash exposure is desired, but current exposure is 14.5%:

- Long exposure: 37%, which must reduce to 27.5% — a reduction of 25.7%
- Multiply all long positions by 0.743

> This affects portfolio risk and other exposure measures. Multiple simultaneous constraints should be approached with caution.

## Long-Only Portfolios

If short positions cannot be held, an offsetting factor is added to forecasts to eliminate negative values. For the running example, add 1.5 to all forecasts:

- Facebook: $1.0 + 1.5 = 2.5$
- Citi: $0.5 + 1.5 = 2.0$
- Google: $-1.5 + 1.5 = 0.0$

This adjustment generally **increases** portfolio risk.

## Controlling Leverage and Margin

If leverage or margin requirements are constraining, all positions are reduced pro rata:

**Example** (constraining leverage from 0.595 to 0.5):

$$\text{Adjustment factor} = \frac{0.5}{0.595} = 0.840$$

| Instrument | Original Weight | Adjusted Weight |
| :--------- | :-------------: | :-------------: |
| Facebook   |      +0.12      |     +0.101      |
| Google     |     −0.225      |     −0.189      |
| Citi       |      +0.25      |     +0.210      |

This adjustment always reduces risk. For long-only strategies with leverage constraints, apply the long-only adjustment first, then the leverage adjustment.

## A Warning About Relative Value Strategies

Relative value strategies take long and short positions in very similar assets (high positive correlations). They are **potentially very dangerous**.

**Example — Facebook and Google relative value portfolio:**

With forecast-implied Sharpe Ratios of 1 and −1, and 50% of risk allocated to each:

- Facebook: $50\% \times 1.0 \times 12\% / (25\% \times 1.0) = 0.24$
- Google: $50\% \times (-1.0) \times 12\% / (20\% \times 1.0) = -0.30$

With correlation 0.90, portfolio risk is just 2.68%. The leverage factor is 0.54. This appears sensible.

**The danger emerges when targeting a constant high risk level.** To hit 12%, positions must be scaled by $12\% / 2.68\% = 4.47$:

- Leverage factor becomes 2.41
- If correlation falls to 0.5: risk more than doubles to 26.8%
- If correlation falls to 0: risk hits 38%
- A 50% rise in Google with no change in Facebook would lose approximately two-thirds of capital

**The crisis cycle for relative value strategies:**

1. An opportunity develops; traders begin placing the trade
2. As more traders enter, potential profit reduces, but constant risk targeting means positions are maintained
3. The trade becomes **crowded** as traders dominate the market; correlation increases
4. Apparent risk falls, leading traders to increase leverage
5. An exogenous shock causes losses
6. Traders unwind positions, causing further losses (a feedback loop)
7. Risk measures explode; risk managers force faster unwinding
8. Once all leveraged traders exit, prices stabilise. Unleveraged traders with cash reserves can then enter at attractive levels
