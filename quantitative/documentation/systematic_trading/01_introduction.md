# Introduction to Systematic Trading

- [Introduction to Systematic Trading](#introduction-to-systematic-trading)
  - [What is systematic trading?](#what-is-systematic-trading)
  - [Why trade systematically?](#why-trade-systematically)
  - [Strategy Classifications](#strategy-classifications)
  - [Core Strategy Examples](#core-strategy-examples)
  - [Common Mistakes \& Failures](#common-mistakes--failures)
  - [Strategy Development Workflow](#strategy-development-workflow)
  - [Mechanics of Carry](#mechanics-of-carry)
    - [FX Carry](#fx-carry)
    - [Futures Carry (Ageing \& Rolldown)](#futures-carry-ageing--rolldown)

## What is systematic trading?

Making financial decisions using a **preset system of rules**, as opposed to human discretion. With three broad categories:

1. **Discretionary trading**
2. **Systematic trading without automation**
3. **Automated systematic trading**

In practice, most systematic trading is automated, but the key distinction is the use of a **predetermined set of rules** to make trading decisions, which can be executed by either humans or computers.

Some fund manager will use systematic strategies to aid decision making or risk management, but still have a discretionary overlay (e.g., adjusting position sizes based on macro views). This is often called "systematic with discretion" or "quantamental" trading.

## Why trade systematically?

**Computer Advantages:**

- **Speed:** Millisecond execution vs. human reaction time (~0.25s).
- **Breadth:** Analysis of thousands of assets simultaneously.
- **Consistency:** Lack of emotion/bias, adherence to plan, and repeatability.
- **Backtesting:** Ability to evaluate historical performance objectively.
- **Cost & Risk:** Lower compensation costs, no 'key-person' risk, and easy replication.

**Human Advantages (where humans still win):**

- **Complex/Novel Info:** Reading annual reports/footnotes.
- **Non-quantifiable Info:** Subjective judgement on management skill/character.
- **Adaptation:** Dealing with "Black Swan" events or environments without historical precedent.

## Strategy Classifications

- **Asset Class:** Equities, Bonds, Futures, FX, Commodities.
- **Exposure:** Neutral, Long/Short, Long Biased.
- **Direction:** Directional vs. Relative Value (Stat Arb).
- **Speed:** HFT, Strategic Asset Allocation, etc.

## Core Strategy Examples

| Strategy                        | Focus                                                  | Characteristics                                                                                      |
| :------------------------------ | :----------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| **Equity Market Neutral (EMN)** | Stock selection via factors (Value, Quality, Momentum) | Market neutral, high diversification, 3-5x leverage, automated execution, negatively-skewed returns. |
| **Carry**                       | Interest rate differentials                            | Borrow low-rate, lend high-rate (usually FX). Negative skew risk if currency depreciates.            |
| **Momentum**                    | Trend following                                        | Directional bets on futures/equities. Positive skew returns. Works best at weeks/months horizons.    |

## Common Mistakes & Failures

1. **Overconfidence:** Underestimating uncertainty in past data. Past returns are noisy; distinguish between skill and noise.
2. **Overfitting (Howie Hubler / Morgan Stanley):** Hubler lost $8.5bn by tuning hedge ratios (8:1) to a historical period whee house prices only rose. The "safe" side of the trade collapsed when the environment changed.
3. **Overbetting (Long Term Capital Management):** Using 25:1 to 300:1 leverage on low-risk/low-return strategies. Wiped out by the 1998 Russian default.
4. **Overtrading (Knight Capital):** Lost $440m in 45 minutes due to a buggy automated system that couldn't be shut down quickly.

## Strategy Development Workflow

1. **Predict:** Develop models for future returns.
2. **Fit:** Apply to past data (avoiding overfitting).
3. **Evaluate:** Measure performance.
4. **Allocate:** Determine position size, leverage, and portfolio optimization.
5. **Risk Management:** Monitor exposure.
6. **Trading Cost:** Balance trade frequency against costs.

## Mechanics of Carry

Carry is the return earned if prices remain unchanged.

### FX Carry

- **Mechanism:** Borrow in a low-interest currency (e.g., JPY), lend/deposit in a high-interest currency (e.g., USD).
- **Return:** Primarily the interest rate differential.
- **Approximation:** Return $\approx \text{Rate}_{\text{High}} - \text{Rate}_{\text{Low}}$.
- **Risk:** Currency appreciation of the funding currency (the one you borrowed) can wipe out interest gains.
- **Breakeven:** The exchange rate move required to offset the interest gain (e.g., if the differential is 3%, a 3% currency move hits breakeven).

### Futures Carry (Ageing & Rolldown)

- **Term Structure:** Relationship between futures prices and time to delivery.
- **Convergence:** On expiry, a futures price must equal the **Spot Price**.
- **Carry Capture:**
  - If the future is above spot (**Contango**): Short the future to capture the price decline as it "ages" toward spot.
  - If the future is below spot (**Backwardation**): Long the future.
- **Rolldown:** A contract's price moves toward the price of a younger contract as it approaches maturity, even if the overall curve doesn't move.
