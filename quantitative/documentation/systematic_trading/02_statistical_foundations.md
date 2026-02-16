# Statistical Foundations & Market Theory

- [Statistical Foundations \& Market Theory](#statistical-foundations--market-theory)
  - [Return Distributions (The Four Moments)](#return-distributions-the-four-moments)
  - [The Sharpe Ratio](#the-sharpe-ratio)
  - [Efficient Market Hypothesis (EMH)](#efficient-market-hypothesis-emh)
    - [CAPM (Single Factor Model)](#capm-single-factor-model)
    - [APT (Arbitrage Pricing Theory)](#apt-arbitrage-pricing-theory)
    - [Carhart 4-Factor Model (Specific APT Implementation)](#carhart-4-factor-model-specific-apt-implementation)
    - [Criticisms of EMH](#criticisms-of-emh)
  - [Behavioural Finance (Prospect Theory)](#behavioural-finance-prospect-theory)
  - [A Pragmatic Traders View](#a-pragmatic-traders-view)
  - [Systematic Ways to Extract Returns](#systematic-ways-to-extract-returns)
    - [Other EMH Compatible Sources of Return](#other-emh-compatible-sources-of-return)
    - [Inefficient Markets](#inefficient-markets)
  - [Strategy Dimensions](#strategy-dimensions)

## Return Distributions (The Four Moments)

1. **Mean ($\mu$):** Expected return.
2. **Variance ($\sigma^2$):** Measure of dispersion/risk.
3. **Skew ($\gamma$):** Asymmetry of returns.
   - **Negative Skew:** Frequent small gains, rare "catastrophic" losses (e.g., Carry, Stock Markets).
   - **Positive Skew:** Frequent small losses, rare large gains (e.g., Momentum/Trend Following).
4. **Kurtosis:** "Fat tails" or frequency of extreme events. High kurtosis means more extreme outliers than a Gaussian distribution.

## The Sharpe Ratio

$$\text{Sharpe Ratio} = \frac{\mu - r_f}{\sigma}$$

- Standardized measure of excess return per unit of volatility.
- **Limitation:** Doesn't account for skew. A high Sharpe ratio can mask "hidden blow-up risk" (Negative Skew/Peso Problem).
- The risk-free rate ($r_f$) is often approximated as zero for short-term trading strategies.

## Efficient Market Hypothesis (EMH)

**Core Premise:** Above-average returns only come from accepting above-average risks. No "free lunches."

> EMH is widely criticized but remains a foundational concept in finance.

### CAPM (Single Factor Model)

Returns are compensation for **market risk only** (Beta):

$$\mathbb{E}[R_i] = \alpha_i + R_f + \beta_i(\mathbb{E}[R_m] - R_f)$$

Where:

- $\beta_i = \rho_{i,m} \frac{\sigma_i}{\sigma_m}$ (correlation × relative volatility)
- $\alpha_i = 0$ under pure EMH (no excess return beyond what market risk explains)
- Assets with high $\beta_i$ are either risky ($\sigma_i$ high) or correlated with market ($\rho_{i,m}$ high)

**Limitation:** Assumes investors can leverage the market portfolio at $R_f$. In reality, leverage constraints mean CAPM doesn't fully explain returns.

### APT (Arbitrage Pricing Theory)

General multi-factor framework: Returns are rewards for exposure to **multiple risk factors** that rational investors dislike.

$$\mathbb{E}[R_i] = \alpha_i + \sum_{j=1}^{K} \beta_{i,j} \mathbb{E}[R_j]$$

Where $R_j$ are factor returns (e.g., Market, Size, Value, Momentum, Carry). Under APT, $\alpha_i = 0$ if markets are efficient.

### Carhart 4-Factor Model (Specific APT Implementation)

This model forms the basis for many equity market neutral strategies. It extends CAPM by adding three additional factors to capture common sources of return:

_Note: All returns below are excess returns (i.e., $R_f$ terms removed for clarity)._

$$\mathbb{E}[R_i] = \alpha_i + \beta_{i,m}\mathbb{E}[R_m] + \beta_{i,s}\mathbb{E}[R_{SMB}] + \beta_{i,v}\mathbb{E}[R_{HML}] + \beta_{i,u}\mathbb{E}[R_{WML}]$$

**Factors:**

- $R_m$: **Market** (equity risk premium)
- $R_{SMB}$: **Size** (Small Minus Big) — Long small-cap, short large-cap
- $R_{HML}$: **Value** (High Minus Low book-to-market) — Long cheap stocks, short expensive
- $R_{WML}$: **Momentum** (Winners Minus Losers, "Up-Down") — Long recent winners, short recent losers

### Criticisms of EMH

- Why do risk factors earn a premium?
  - Small firm premia still exists even after friction & liquidity
  - Tenous attempts to explain value premium with macroeconomic factors
  - There is no rational reason why momentum should work
- How can the price of risk be explained?
  - Eg for many years the equity premium was too high
  - Price of other types of risk is even harder to explain
- The price of risk is not stable over time, and can be affected by structural changes in the market (e.g., regulation, technology).
- CAPM has poor explanatory power, especially within asset classes
  - High $\beta$ underperforms low $\beta$.
  - This persists as exploiting would require buying low $\beta$ and using leverage. Most investors can't or won't use leverage.
  - This is the 'leverage premium' or 'low volatility effect'
- Numerous anomalies have been identified
  - Calendar effects
  - Many of these may have been 'data mined'
- Behavioural finance
  - Explains anomalies in terms of "irrational" behaviour, which can be explained by well known psychological effects

## Behavioural Finance (Prospect Theory)

Low probability events are overweighted.

- Anomalies exist due to deep-rooted human cognitive biases:
  - **Lottery Hook:** Investors overpay for positive skew (small chance of huge gain).
  - **Risk Attitudes:** People are risk-averse regarding gains (locking in profits too early) and risk-seeking regarding losses (holding losing positions too long). This fuels **momentum**.
  - **Overestimation:** Rare events are often overestimated in price (e.g., expensive insurance/options).

This may also explain why high $\beta$ (or high volatility) stocks are so expensive (and low $\beta$ or low volatility assets can be expected to outperform).

Prospect theory explains both momentum and skew.

## A Pragmatic Traders View

- Explicable returns are better than inexplicable
- Systematic strategies should harvest risk premium
- Markets contain irrational investors
  - Some know they are irrational and don't care
    - Central banks
  - Some don't know they are irrational
    - Large funds doing large rebalancing trades
    - Retail day traders
- Small, temporary, mispricings do occur; but will be difficult and costly to exploit

- **Irrational/Structural Flows:** Money is made from participants trading for non-profit reasons:
  - Central Banks: Manipulating currency levels (e.g., BoJ keeping JPY low for exports).
  - Ignorant/Institutional Rebalancing: Large funds trading on fixed schedules.
  - Government Needs: Predictable bond issuance (e.g., US Treasury auctions).
- **Micro-Inefficiencies:** Small mispricings that require technology and speed to capture (HFT, Stat Arb).

## Systematic Ways to Extract Returns

- Systematic strategies require the existence of codified sources of return, that can be systematized and backtested.
- The possible sources can be divided into:
  - EMH compatible:
    - Risk factors, including CAPM
    - Other EMH compatible sources of return
  - Sources of return that imply markets are inefficient

| Method                  | Source of Return                                                            |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Market Beta**         | Reward for equity/bond market volatility.                                   |
| **Alternative Factors** | Value, Size, Quality, Momentum, Carry.                                      |
| **Short Volatility**    | Reward for providing "insurance" (selling options). Strongly negative skew. |
| **Credit Risk**         | Reward for bearing default risk.                                            |
| **Liquidity Provision** | Market making; capturing the bid-ask spread.                                |
| **Arbitrage**           | Spotting mispricings between related assets (relative value).               |
| **Anomaly Timing**      | Exploiting calendar effects (e.g., January effect).                         |

### Other EMH Compatible Sources of Return

- Betting against b (EMH compatible, not CAPM)
  - Traders get rewarded if they can use leverage, or have a high tolerance for risk
- Paying for speed
  - High frequency trading is an expensive business; logically traders should earn additional returns to compensate
- Providing liquidity
  - Market making
- Taking higher moment risk, skew and kurtosis
  - Prospect theory suggests investors prefer positive to negative skew
  - This is borne out by empirical evidence
  - Buying negative skew should yield positive returns

### Inefficient Markets

- Use factor timing
  - 'Wrong' factor valuation may only be apparent in hindsight
  - Equilibrium is difficult to measure
  - Limited number of extreme values in data history
  - Difficult to call turning points
- Exploit market anomalies
  - Beware: many of these may be data mined
- Pick off irrational counterparties
  - Either knowing (eg central banks) or ignorant (large, slow moving funds or retail traders)
  - Knowing irrational traders may change their minds
  - Ignorant irrational traders may learn from their mistakes
- Find limited pure arbitrage opportunities
  - _Example_: certain complex option strategies may provide frequent misvaluations but this requires speed, expertise and complex technology to exploit

## Strategy Dimensions

- **Asset Class:** From Equities to Crypto/Timber.
- **Speed:** HFT (milliseconds) to Asset Allocation (decades).
- **Activeness:** Indexing (Passive) $\rightarrow$ Smart Beta $\rightarrow$ Alternative Beta $\rightarrow$ Active Alpha.
- **Leverage:** Essential for low-risk strategies (Relative Value, Market Neutral).
