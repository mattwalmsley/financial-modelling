# Systematic Trading

- [Systematic Trading](#systematic-trading)
  - [Introduction](#introduction)
    - [What is systematic trading?](#what-is-systematic-trading)
    - [Why trade systematically?](#why-trade-systematically)
    - [Strategy Classifications](#strategy-classifications)
    - [Core Strategy Examples](#core-strategy-examples)
    - [Common Mistakes \& Failures](#common-mistakes--failures)
    - [Strategy Development Workflow](#strategy-development-workflow)
  - [Mechanics of Carry](#mechanics-of-carry)
    - [1. FX Carry](#1-fx-carry)
    - [2. Futures Carry (Ageing \& Rolldown)](#2-futures-carry-ageing--rolldown)
  - [Statistical Foundations](#statistical-foundations)
    - [Return Distributions (The Four Moments)](#return-distributions-the-four-moments)
    - [The Sharpe Ratio](#the-sharpe-ratio)
  - [Sources of Alpha: Why Systematic Trading Works](#sources-of-alpha-why-systematic-trading-works)
    - [1. Efficient Market Hypothesis (EMH) View](#1-efficient-market-hypothesis-emh-view)
      - [CAPM (Single Factor Model)](#capm-single-factor-model)
      - [APT (Arbitrage Pricing Theory)](#apt-arbitrage-pricing-theory)
      - [Carhart 4-Factor Model (Specific APT Implementation)](#carhart-4-factor-model-specific-apt-implementation)
    - [2. Behavioural Finance View (Prospect Theory)](#2-behavioural-finance-view-prospect-theory)
    - [3. Pragmatic Participant View](#3-pragmatic-participant-view)
  - [Systematic Ways to Extract Returns](#systematic-ways-to-extract-returns)
  - [Strategy Dimensions](#strategy-dimensions)

## Introduction

### What is systematic trading?

Making financial decisions using a **preset system of rules**, as opposed to human discretion.

**Three types of trading:**

1. **Discretionary trading**
2. **Systematic trading without automation**
3. **Automated systematic trading**

### Why trade systematically?

**Computer Advantages:**

- **Speed:** Millisecond execution vs. human reaction time (~0.25s).
- **Breadth:** Analysis of thousands of assets simultaneously.
- **Consistency:** Lack of emotion/bias, adherence to plan, and repeatability.
- **Backtesting:** Ability to evaluate historical performance objectively.
- **Cost & Risk:** Lower compensation costs, no 'key-person' risk, and easy replication.

**Human Advantages (where we still win):**

- **Complex/Novel Info:** Reading annual reports/footnotes.
- **Non-quantifiable Info:** Subjective judgement on management skill/character.
- **Adaptation:** Dealing with "Black Swan" events or environments without historical precedent.

### Strategy Classifications

- **Asset Class:** Equities, Bonds, Futures, FX, Commodities.
- **Exposure:** Neutral, Long/Short, Long Biased.
- **Direction:** Directional vs. Relative Value (Stat Arb).
- **Speed:** HFT, Strategic Asset Allocation, etc.

### Core Strategy Examples

| Strategy                        | Focus                                                  | Characteristics                                                                                   |
| :------------------------------ | :----------------------------------------------------- | :------------------------------------------------------------------------------------------------ |
| **Equity Market Neutral (EMN)** | Stock selection via factors (Value, Quality, Momentum) | Market neutral, high diversification, 3-5x leverage, automated execution.                         |
| **Carry**                       | Interest rate differentials                            | Borrow low-rate, lend high-rate (usually FX). Negative skew risk if currency depreciates.         |
| **Momentum**                    | Trend following                                        | Directional bets on futures/equities. Positive skew returns. Works best at weeks/months horizons. |

### Common Mistakes & Failures

1. **Overconfidence:** Underestimating uncertainty in past data. Past returns are noisy; distinguish between skill and noise.
2. **Overfitting (Howie Hubler / Morgan Stanley):** Hubler lost $8.5bn by tuning hedge ratios (8:1) to a historical period whee house prices only rose. The "safe" side of the trade collapsed when the environment changed.
3. **Overbetting (Long Term Capital Management):** Using 25:1 to 300:1 leverage on low-risk/low-return strategies. Wiped out by the 1998 Russian default.
4. **Overtrading (Knight Capital):** Lost $440m in 45 minutes due to a buggy automated system that couldn't be shut down quickly.

### Strategy Development Workflow

1. **Predict:** Develop models for future returns.
2. **Fit:** Apply to past data (avoiding overfitting).
3. **Evaluate:** Measure performance.
4. **Allocate:** Determine position size, leverage, and portfolio optimization.
5. **Risk Management:** Monitor exposure.
6. **Trading Cost:** Balance trade frequency against costs.

## Mechanics of Carry

Carry is the return earned if prices remain unchanged.

### 1. FX Carry

- **Mechanism:** Borrow in a low-interest currency (e.g., JPY), lend/deposit in a high-interest currency (e.g., USD).
- **Return:** Primarily the interest rate differential.
- **Approximation:** Return $\approx \text{Rate}_{\text{High}} - \text{Rate}_{\text{Low}}$.
- **Risk:** Currency appreciation of the funding currency (the one you borrowed) can wipe out interest gains.
- **Breakeven:** The exchange rate move required to offset the interest gain (e.g., if the differential is 3%, a 3% currency move hits breakeven).

### 2. Futures Carry (Ageing & Rolldown)

- **Term Structure:** Relationship between futures prices and time to delivery.
- **Convergence:** On expiry, a futures price must equal the **Spot Price**.
- **Carry Capture:**
  - If the future is above spot (**Contango**): Short the future to capture the price decline as it "ages" toward spot.
  - If the future is below spot (**Backwardation**): Long the future.
- **Rolldown:** A contract's price moves toward the price of a younger contract as it approaches maturity, even if the overall curve doesn't move.

## Statistical Foundations

### Return Distributions (The Four Moments)

1. **Mean ($\mu$):** Expected return.
2. **Variance ($\sigma^2$):** Measure of dispersion/risk.
3. **Skew ($\gamma$):** Asymmetry of returns.
   - **Negative Skew:** Frequent small gains, rare "catastrophic" losses (e.g., Carry, Stock Markets).
   - **Positive Skew:** Frequent small losses, rare large gains (e.g., Momentum/Trend Following).
4. **Kurtosis:** "Fat tails" or frequency of extreme events. High kurtosis means more extreme outliers than a Gaussian distribution.

### The Sharpe Ratio

$$\text{Sharpe Ratio} = \frac{\mu - r_f}{\sigma}$$

- Standardized measure of excess return per unit of volatility.
- **Limitation:** Doesn't account for skew. A high Sharpe ratio can mask "hidden blow-up risk" (Negative Skew/Peso Problem).
- The risk-free rate ($r_f$) is often approximated as zero for short-term trading strategies.

## Sources of Alpha: Why Systematic Trading Works

### 1. Efficient Market Hypothesis (EMH) View

**Core Premise:** Above-average returns only come from accepting above-average risks. No "free lunches."

> EMH is widely criticized but remains a foundational concept in finance.

#### CAPM (Single Factor Model)

Returns are compensation for **market risk only** (Beta):

$$\mathbb{E}[R_i] = \alpha_i + R_f + \beta_i(\mathbb{E}[R_m] - R_f)$$

Where:

- $\beta_i = \rho_{i,m} \frac{\sigma_i}{\sigma_m}$ (correlation × relative volatility)
- $\alpha_i = 0$ under pure EMH (no excess return beyond what market risk explains)
- Assets with high $\beta_i$ are either risky ($\sigma_i$ high) or correlated with market ($\rho_{i,m}$ high)

**Limitation:** Assumes investors can leverage the market portfolio at $R_f$. In reality, leverage constraints mean CAPM doesn't fully explain returns.

#### APT (Arbitrage Pricing Theory)

General multi-factor framework: Returns are rewards for exposure to **multiple risk factors** that rational investors dislike.

$$\mathbb{E}[R_i] = \alpha_i + \sum_{j=1}^{K} \beta_{i,j} \mathbb{E}[R_j]$$

Where $R_j$ are factor returns (e.g., Market, Size, Value, Momentum, Carry). Under APT, $\alpha_i = 0$ if markets are efficient.

#### Carhart 4-Factor Model (Specific APT Implementation)

*Note: All returns below are excess returns (i.e., $R_f$ terms removed for clarity).*

$$\mathbb{E}[R_i] = \alpha_i + \beta_{i,m}\mathbb{E}[R_m] + \beta_{i,s}\mathbb{E}[R_{SMB}] + \beta_{i,v}\mathbb{E}[R_{HML}] + \beta_{i,u}\mathbb{E}[R_{WML}]$$

**Factors:**

- $R_m$: **Market** (equity risk premium)
- $R_{SMB}$: **Size** (Small Minus Big) — Long small-cap, short large-cap
- $R_{HML}$: **Value** (High Minus Low book-to-market) — Long cheap stocks, short expensive
- $R_{WML}$: **Momentum** (Winners Minus Losers, "Up-Down") — Long recent winners, short recent losers

### 2. Behavioural Finance View (Prospect Theory)

- Anomalies exist due to deep-rooted human cognitive biases:
  - **Lottery Hook:** Investors overpay for positive skew (small chance of huge gain).
  - **Risk Attitudes:** People are risk-averse regarding gains (locking in profits too early) and risk-seeking regarding losses (holding losing positions too long). This fuels **momentum**.
  - **Overestimation:** Rare events are often overestimated in price (e.g., expensive insurance/options).

### 3. Pragmatic Participant View

- **Irrational/Structural Flows:** Money is made from participants trading for non-profit reasons:
  - **Central Banks:** Manipulating currency levels (e.g., BoJ keeping JPY low for exports).
  - **Ignorant/Institutional Rebalancing:** Large funds trading on fixed schedules.
  - **Government Needs:** Predictable bond issuance (e.g., US Treasury auctions).
- **Micro-Inefficiencies:** Small mispricings that require technology and speed to capture (HFT, Stat Arb).

## Systematic Ways to Extract Returns

| Method                  | Source of Return                                                            |
| :---------------------- | :-------------------------------------------------------------------------- |
| **Market Beta**         | Reward for equity/bond market volatility.                                   |
| **Alternative Factors** | Value, Size, Quality, Momentum, Carry.                                      |
| **Short Volatility**    | Reward for providing "insurance" (selling options). Strongly negative skew. |
| **Liquidity Provision** | Market making; capturing the bid-ask spread.                                |
| **Arbitrage**           | Spotting mispricings between related assets (relative value).               |
| **Anomaly Timing**      | Exploiting calendar effects (e.g., January effect).                         |

## Strategy Dimensions

- **Asset Class:** From Equities to Crypto/Timber.
- **Speed:** HFT (milliseconds) to Asset Allocation (decades).
- **Activeness:** Indexing (Passive) $\rightarrow$ Smart Beta $\rightarrow$ Alternative Beta $\rightarrow$ Active Alpha.
- **Leverage:** Essential for low-risk strategies (Relative Value, Market Neutral).
