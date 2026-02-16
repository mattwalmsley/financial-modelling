# Portfolio Optimisation

- [Portfolio Optimisation](#portfolio-optimisation)
  - [Markowitz Optimisation](#markowitz-optimisation)
  - [Two Main Problems](#two-main-problems)
  - [The Problem of Robustness](#the-problem-of-robustness)
  - [Effect of Parameter Uncertainty on Portfolio Weights](#effect-of-parameter-uncertainty-on-portfolio-weights)
  - [Solutions to Robustness and Uncertainty](#solutions-to-robustness-and-uncertainty)

## Markowitz Optimisation

The classical approach to portfolio construction uses methods developed by Markowitz in the 1950s. Given a vector of portfolio weights $\mathbf{w}$, expected returns $\mathbf{r}$, correlation matrix $\rho$, and vector of standard deviations $\boldsymbol{\sigma}$, an optimal set of weights is calculated to maximise excess portfolio return subject to a constraint on portfolio standard deviation (or investor risk preference). The set of weights that suit different risk preferences forms the **efficient frontier**.

If leverage is freely available, the **Sharpe Ratio** can be maximised, yielding a single solution.

**Formally:**

- Expected excess portfolio return: $\mathbf{r}^T\mathbf{w} - r_f$
- Portfolio Sharpe Ratio: $\frac{\mathbf{r}^T\mathbf{w} - r_f}{\sigma_p}$
- Expected portfolio standard deviation: $\sigma_p = \sqrt{\mathbf{w}^T \Sigma \mathbf{w}}$
- Where $\Sigma = \text{diag}(\boldsymbol{\sigma})\, \rho\, \text{diag}(\boldsymbol{\sigma})$ is the covariance matrix

## Two Main Problems

1. **Robustness:** Very small differences in inputs can lead to wildly different results. Extreme portfolios (entire value in one asset) are common, particularly with highly correlated assets.
2. **Input uncertainty:** The inputs are not known with high accuracy. Standard deviations and (to a lesser extent) correlations can be forecasted reasonably well, but predicting expected returns or Sharpe Ratios is extremely difficult.

## The Problem of Robustness

The behaviour of the Markowitz optimiser under various conditions:

**Equal inputs → Equal weights:**

- If correlations, means, and standard deviations are all equal, the optimiser produces equal portfolio weights, regardless of the correlation level

**Unequal correlations:**

- More diversifying assets (lower correlation with others) receive higher weight

**Unequal risk:**

- Riskier assets receive lower weight

**High correlations with small differences:**

- Even a small difference in standard deviation can result in **zero** weights for one asset
- A small difference in means can produce **extreme** portfolios (all weight in one asset)

**Low correlations:**

- Quite large differences in inputs do not affect weights as dramatically

## Effect of Parameter Uncertainty on Portfolio Weights

**Empirical example:** Three assets — US S&P 500 equity index, US 5 year bond futures, and US 10 year bond futures. Given the presence of a highly correlated pair (the two bond markets), the optimiser produces extreme weights, with a relatively small advantage in Sharpe Ratio for the 5 year bond resulting in it taking all the weight.

**Sensitivity to Sharpe Ratio estimates:**

- S&P 500 SR has a wide distribution of possible estimates
- As SR increases, S&P 500 weight rises at the expense of US 5 year
- 90% distributional range for S&P 500 SR: (−0.18, 0.5) → weight range: (9.8%, 17%)
- Bond SR plots show a dramatic "flip" in weights at a critical point — the correct weight is either ~0% or ~85%

**Sensitivity to standard deviation estimates:**

Standard deviations are better behaved (known with more certainty and smaller effect on weights):

- 90% range for S&P 500 $\sigma$: (0.152, 0.180) → weight range: (14.2%, 14.9%)
- 90% range for US 10Y $\sigma$: (0.053, 0.059) → weight remains at 0%
- 90% range for US 5Y $\sigma$: (0.034, 0.039) → weight range: (85.3%, 85.7%)

**Sensitivity to correlation estimates:**

Although correlation distributions are wider than standard deviations, the effect on weights is moderate:

- 90% range for S&P 500/US 10Y correlation: (−0.32, −0.19) → S&P 500 weight ≈ 14.5%
- 90% range for S&P 500/US 5Y correlation: (−0.34, −0.22) → S&P 500 weight: (12.8%, 16.0%)
- 90% range for US 5Y/US 10Y correlation: (0.95, 0.96) → US 5Y weight ≈ 85.5%

## Solutions to Robustness and Uncertainty

| Solution                                                        | Disadvantage                                                                                |
| :-------------------------------------------------------------- | :------------------------------------------------------------------------------------------ |
| **Applying constraints** to the optimisation                    | Can lead to implicit fitting through constraints; makes optimisation less robust            |
| **Overriding estimated inputs** (e.g. equalising Sharpe Ratios) | Does not address the non-overridden inputs; may discard useful information                  |
| **Bayesian methods** (adjusting inputs for uncertainty)         | Prior distributions and shrinkage factors may be arbitrary; handles constraints poorly      |
| **Bootstrapping** (repeating optimisation, taking average)      | Computationally intensive; results not always intuitive; handles constraints poorly         |
| **Inverse volatility weighting**                                | Ignores correlations and Sharpe Ratio estimation; must be combined with other methods       |
| **Clustering**                                                  | Clusters not always obvious; must be combined with other methods                            |
| **Heuristic methods**                                           | Difficult to backtest; not always theoretically optimal; complex portfolios are challenging |
| **Partial correlations**                                        | Relatively new and unproven; does not solve the Sharpe Ratio estimation problem             |
| **Higher moments / alternative utility functions**              | More complex to implement; does not fix the fundamental uncertainty problem                 |
