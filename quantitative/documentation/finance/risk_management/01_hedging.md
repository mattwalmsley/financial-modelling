# Hedging

- [Hedging](#hedging)
  - [Risk Management for Liabilities](#risk-management-for-liabilities)
  - [Hedging Scenarios](#hedging-scenarios)
  - [Immunisation of Cash Flows](#immunisation-of-cash-flows)
    - [Duration and Convexity](#duration-and-convexity)
    - [Surplus](#surplus)
    - [Redington's Immunisation Conditions](#redingtons-immunisation-conditions)
    - [The Convexity Inequality](#the-convexity-inequality)
  - [Quadratic Hedging](#quadratic-hedging)
  - [Portfolio Formulation](#portfolio-formulation)
  - [Single Financial Instrument (n = 1)](#single-financial-instrument-n--1)
  - [Delta Hedging](#delta-hedging)
    - [Delta Hedging Example with Geometric Brownian Motion](#delta-hedging-example-with-geometric-brownian-motion)
  - [General Solution (Any value of $n$)](#general-solution-any-value-of-n)
    - [Background: Convexity](#background-convexity)
    - [Problem Setup](#problem-setup)
    - [Deriving the Variance of Hedging Error](#deriving-the-variance-of-hedging-error)
    - [The Covariance Matrix](#the-covariance-matrix)
    - [Variance Formula in Matrix Form](#variance-formula-in-matrix-form)
    - [Properties of Covariance Matrices](#properties-of-covariance-matrices)
    - [Finding the Optimal Portfolio](#finding-the-optimal-portfolio)
    - [Solution in Matrix Form](#solution-in-matrix-form)
    - [Minimum Variance Achieved](#minimum-variance-achieved)
  - [Notation Summary](#notation-summary)
  - [The Complete Optimal Hedging Portfolio](#the-complete-optimal-hedging-portfolio)
    - [Properties of the Optimal Hedging Portfolio](#properties-of-the-optimal-hedging-portfolio)
    - [Worst Case: Uncorrelated Assets](#worst-case-uncorrelated-assets)
    - [The Role of Correlations in Risk Reduction](#the-role-of-correlations-in-risk-reduction)

> **Overview**: This chapter addresses the fundamental question every financial institution faces: _how do you protect yourself against future obligations you cannot perfectly predict?_ Whether you are a pension fund manager who must pay retirees in 30 years, an insurance company facing uncertain claims, or a derivatives desk hedging complex payoffs, the mathematical framework is the same. Three increasingly sophisticated approaches are developed — immunisation (for interest rate risk), quadratic hedging (for general market risk), and delta hedging (for derivative pricing) — each building on the insight that **correlations between assets and liabilities are the key to risk reduction**.

## Risk Management for Liabilities

- The holder of some given liabilities does not want to speculate on a favourable or unfavourable market movement but wants to minimise risk.
- For liabilities $L$ at a future time $T$, regarded as random variables (e.g., derivative instruments, insurance claims), the goal is to purchase a portfolio $A$ at time $T$ that matches the value of the liabilities.
- In other words, this portfolio **hedges** the liabilities.

## Hedging Scenarios

1. **Immunisation**: Liabilities and assets are specified cash flows depending on variable interest rates. Uncertainty arises from fluctuating interest rates.
2. **Quadratic Hedging**: Liabilities and assets are random variables due to market fluctuations (stocks, futures, etc.). The goal is to set $\mathbb{E}[A - L] = 0$ and minimise $\text{Var}(A - L)$, thus minimising $\mathbb{E}[(A - L)^2]$. The quantity $A - L$ measures the risk of the hedging error.

## Immunisation of Cash Flows

An institution holds assets with present value $V_A$ to meet liabilities with present value $V_L$. Both are sensitive to interest rate $r$ (annualised) changes.
For a cash flow $\{C_1, \dots, C_n\}$ of payments made at the end of each year over $n$ years, the present value is:

$$
V(r) = \sum_{i=1}^n C_i \beta(r)^i, \quad \beta(r) = \frac{1}{1+r}
$$

where $\beta(r)$ is the discounting factor.

The relative change in $V(r)$ following a small change $\epsilon$ in the interest rate $r$ is denoted as $\Delta V$:

$$
\Delta V = \frac{V(r + \epsilon) - V(r)}{V(r)}
$$

For a general function $f(x)$ with derivatives denoted as primes $f'(x)$ and $f''(x)$, the Taylor expansion around a point $x_0$ is:

$$
f'(x) = \frac{df}{dx}, \quad f''(x) = \frac{d^2f}{dx^2}
$$

$$
f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{1}{2}f''(x_0)(x - x_0)^2 + \dots
$$

for small deviations $x - x_0$. Setting $x = r + \epsilon$ and $x_0 = r$, and then using the Taylor expansion of $V(r + \epsilon)$, this gives:

$$
V(r + \epsilon) = V(r) + V'(r)\epsilon + \frac{1}{2}V''(r)\epsilon^2 + \dots
$$

Ignoring higher-order terms, the (approximate) relative change in present value is:

$$
\Delta V = \frac{1}{V(r)} \left(V'(r)\epsilon + \frac{1}{2}V''(r)\epsilon^2 \right) =-\nu(r)\epsilon + \frac{1}{2}c(r)\epsilon^2
$$

### Duration and Convexity

- **Effective Duration** $\nu(r)$:

  $$
  \begin{aligned}
  \nu(r) & = -\frac{1}{V(r)} V'(r) \\\\
  &= -\frac{1}{V(r)} \sum_{i=1}^n C_i i \beta(r)^{i-1} \beta'(r) \\\\
  &= \frac{1}{V(r)} \sum_{i=1}^n C_i i \beta(r)^{i+1}
  \end{aligned}
  $$

  since $\beta'(r) = -\beta(r)^2$

- **Convexity** $c(r)$:

  $$
  \begin{aligned}
  c(r) & = \frac{1}{V(r)} V''(r) \\\\
  & = \frac{1}{V(r)} \frac{d}{dr} \left(-\sum_{i=1}^{n}{C_i i \beta (r)^{i+1}}\right) \\\\
  & = \frac{1}{V(r)} \sum_{i=1}^n C_i i (i+1) \beta(r)^{i+2}
  \end{aligned}
  $$

### Surplus

The institution is immunised against small changes in the interest rate r if:

1. The present values of assets and liabilities are equal: $V_A(r) = V_L(r)$. The institution can ensure this from the onset since $r$ is known at time 0.
2. A small change in the interest rate by $\plusmn\epsilon$ will change the value of the assets to be greater or equal to that of the value of the liabilities, i.e. $V_A(r + \epsilon) - V_L(r + \epsilon) \geq 0$

The surplus is defined as:

$$
S(r) = V_A(r) - V_L(r)
$$

Taylor's theorem yields for small $\epsilon$ up to quadratic order:

$$
S(r + \epsilon) \approx S(r) + S'(r)\epsilon + \frac{1}{2}S''(r)\epsilon^2 + \dots
$$

For immunisation, the requirement is $S(r + \epsilon) \geq 0$ for small $\epsilon$. This leads to the conditions on the derivatives of $S(r)$ at $r$.

- For the first term, it is necessary that $S(r) = 0$ or $V_A(r) = V_L(r)$.
- For the second term, it is necessary that $S'(r) = 0$ or $V_A'(r) = V_L'(r)$.

$$
V_A'(r) = V_l'(r) \iff - \frac{1}{V_A(r)} V_A'(r) = - \frac{1}{V_L(r)} V_L'(r) \iff \nu_A(r) = \nu_L(r)
$$

- **The durations of assets and liabilities must be equal.**
- For the third term, it is necessary that $S''(r) \geq 0$ or $V_A''(r) \geq V_L''(r)$.

$$
V_A''(r) \geq V_L''(r) \iff \frac{1}{V_A(r)} V_A''(r) \geq \frac{1}{V_L(r)} V_L''(r) \iff c_A(r) \geq c_L(r)
$$

- **The convexity of assets must be at least that of liabilities.**

### Redington's Immunisation Conditions

Named after Frank M. Redington (1906-1984), an institution is immunised against small changes in interest rates if the surplus $S(r) = V_A(r) - V_L(r)$ satisfies $S(r+\epsilon) \geq 0$. This leads to three conditions:

1. **Present Value Equality**: $V_A(r) = V_L(r)$
2. **Duration Matching**: $\nu_A(r) = \nu_L(r)$ (Implies $S'(r) = 0$)
3. **Convexity Condition**: $c_A(r) \geq c_L(r)$ (Implies $S''(r) \geq 0$)

### The Convexity Inequality

A function $f: K \to \mathbb{R}$ defined on a convex set $K$ is **convex** if for any $\lambda \in [0, 1]$ and $x_1, x_2 \in K$:

$$
f(\lambda x_1 + (1 - \lambda) x_2) \leq \lambda f(x_1) + (1 - \lambda) f(x_2)
$$

- The **left-hand side** represents a **point on the curve** at the weighted average of $x_1$ and $x_2$.
- The **right-hand side** represents a **point on the chord** (straight line) connecting $f(x_1)$ and $f(x_2)$.
- For a convex function, the chord always lies **above** the curve.

**Special Case ($\lambda = \frac{1}{2}$)**: When $\lambda = \frac{1}{2}$, the convex combination simplifies to the midpoint:

$$
\frac{x_1}{2} + \frac{x_2}{2} = \frac{x_1 + x_2}{2}
$$

$$
f\left(\frac{x_1 + x_2}{2}\right) \leq \frac{f(x_1) + f(x_2)}{2}
$$

This states that the function value at the midpoint $\frac{x_1 + x_2}{2}$ is less than or equal to the average of the function values at $x_1$ and $x_2$.

![Convex Function](../images/convex_function.png "Convex Function: The Chord Lies Above the Curve")

- The **blue curve** represents the convex function $f(x) = x^2 + 2$
- The **red dashed chord** connects the two points $(x_1, f(x_1))$ and $(x_2, f(x_2))$
- The **purple triangle** marks the point on the curve: $f(\lambda x_1 + (1-\lambda)x_2)$
- The **red square** marks the point on the chord: $\lambda f(x_1) + (1-\lambda)f(x_2)$
- The **green shaded region** shows where the chord lies above the curve (the convexity gap)
- The **dotted vertical line** illustrates the inequality: the point on the curve is always below the point on the chord

**Relevance to Immunisation**: The present value function $V(r)$ is convex in the interest rate $r$ (due to the positive convexity $c(r) > 0$). This convexity ensures that the surplus $S(r) = V_A(r) - V_L(r)$ has a local minimum that is also a global minimum when Redington's conditions are satisfied.

## Quadratic Hedging

- Aim to choose a portfolio $A$ to hedge a liability $L$ at time $T$ such that $E[A - L] = 0$ and $\text{Var}(A - L)$ is minimised.
- If the variance is small, the spread around the expected value is small and thus the probability to be far away from the expected value is small.
- If the variance is large, the hedging error can deviate significantly from zero, potentially lead to catastrophic consequences.
- The key is determining the optimal portfolio $A$ to minimise the hedging error variance.

## Portfolio Formulation

Let $\mathbf{Z} = \begin{pmatrix} Z_1 \\ \vdots \\ Z_n \end{pmatrix}$ be the values of assets at time $T$.

Different combination of these assert (or derivative instruments based on these assets) can be purchased.

The portfolio value at time $T$ is denoted as $f(\mathbf{Z})$ with linear combinations of financial instruments $\mathbf{Z}$:

$$
f(\mathbf{Z}) = h_0 + \sum_{i=1}^n h_i Z_i = h_0 + \mathbf{h}^{\intercal} \mathbf{Z}
$$

where the vector $\mathbf{h} = \begin{pmatrix} h_1 \\ \vdots \\ h_n \end{pmatrix}$ represent the number of units held in each asset.

The entries $h_i$ are in principle integers denoting the amount of units of the $i$th financial instrument in the portfolio; however, in order to simplify the mathematics, $h_i$ is allowed to be a real number.

Expressions of type $a_1 b_1 + a_2 b_2 + \dots + a_n b_n$ can be written as the dot product of two vectors $\mathbf{a}^{\intercal} \mathbf{b}$.

$$
\mathbf{a} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix}, \quad \mathbf{b} = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}
$$

$$
\mathbf{a}^{\intercal}  = \begin{pmatrix} a_1 & a_2 & \dots & a_n \end{pmatrix}, \quad \mathbf{b}^{\intercal} = \begin{pmatrix} b_1 & b_2 & \dots & b_n \end{pmatrix}
$$

$$
a_1 b_1 + a_2 b_2 + \dots + a_n b_n = \sum_{i=1}^{n}{a_ib_i} = \mathbf{a}^{\intercal} \mathbf{b} = \begin{pmatrix} a_1 & a_2 & \dots & a_n \end{pmatrix} \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}
$$

> Note that bold letters denote vectors in this documentation, other texts may use alternative notation such as an arrow above the letter (e.g., $\vec{a}$) or a tilde (e.g., $\tilde{a}$).

To satisfy the quadratic hedging objective, the task is to choose $h_0$ and $\mathbf{h}$ such that the constants $h_0, h_1, \ldots, h_n$:

- Satisfy $\mathbb{E}[h_0 + \sum_{i=1}^n{h_i Z_i - L}] = 0$
- Minimise $\text{Var}(h_0 + \mathbf{h}^{\intercal}\mathbf{Z} - L)$

The set $(h_0, \mathbf{h})$ specifies the portfolio of financial instruments to use for hedging and $h_0$ is the amount invested in a risk-free asset, e.g. a bank account or government bond.

The positions $h_1, h_2, \ldots, h_n$ are associated with the random variables $Z_1, Z_2, \ldots, Z_n$ representing the values of the risky assets/instruments.

Formally, the solution of minimising the variance $\text{Var}(h_0 + \mathbf{h}^{\intercal}\mathbf{Z} - L)$ is a standard linear regression of $L$ onto the regressors $Z_1, Z_2, \ldots, Z_n$.

The solution is obtained by first considering the simpler case of $n=1$.

## Single Financial Instrument (n = 1)

For a single financial instrument $n=1$, $\mathbf{Z}=Z$ and the optimal hedging portfolio has the value $A = h_0 + hZ$:.

$(h_0, h)$ are chosen such that $\mathbb{E}[A - L] = 0$ and $\text{Var}(A - L)$ is minimised.

$$
\begin{aligned}
\text{Var}(A - L) = \text{Var}(h_0 + hZ - L) &= \text{Var}(h_0 + hZ) + Var(L) - 2\text{Cov}(hZ, L) \\
&= \text{Var}(hZ) + \text{Var}(L) - 2\text{Cov}(hZ, L) \\
&=h^2 \text{Var}(Z) + \text{Var}(L) - 2h\text{Cov}(Z, L)
\end{aligned}
$$

Where the following properties are used:

- $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y) - 2\text{Cov}(X, Y)$
- $\text{Var}(X + c) = \text{Var}(X)$ for any constant $c$
- $\text{Var}(aX) = a^2 \text{Var}(X)$ for any constant $a$
- $\text{Cov}(aX, Y) = a \text{Cov}(X, Y)$ for any constant $a$

Since the variance $\text{Var}(A - L)$ is a quadratic function of $h$ and the factor $h^2$ is positive, the variance is a convex function of $h$ and has a unique minimum. This minimum is found by setting the derivative with respect to $h$ to zero:

$$
\boxed{h^* = \frac{\text{Cov}(Z, L)}{\text{Var}(Z)}}
$$

Using $E[A - L] = 0$ to determine $h_0$:

$$
E[A - L] = E[h_0 + hZ - L] = h_0 + hE[Z] - E[L] = 0
$$

From the condition $\mathbb{E}[A^* - L]=0$, the optimal risk-free position is therefore:

$$
\boxed{h_0^* = E[L] - h^* E[Z]}
$$

Using quadratic hedging portfolio, given by $(h_0^*, h^*)$, to calculate the variance of the hedging error $A^* - L$ for the optimal portfolio value $A^* = h_0^* + h^* Z$:

$$
\begin{aligned}
\text{Var}(A^* - L) &= \text{Var}(A*) + \text{Var}(L) - 2\text{Cov}(A^*, L) \\\\
&= \text{Var} \left(\frac{\text{Cov}(L, Z)}{\text{Var}(Z)} Z \right) + \text{Var}(L) - 2 \text{Cov} \left( \frac{\text{Cov}(L,Z)}{\text{Var}(Z)}Z,L \right) \\\\
&= \frac{\text{Cov}(L,Z)^2}{\text{Var}(Z)^2} \text{Var}(Z) + \text{Var}(L) - 2 \frac{\text{Cov}(L,Z)}{\text{Var}(Z)} \text{Cov}(Z,L) \\\\
&= \text{Var}(L) - \frac{\text{Cov}(L,Z)^2}{\text{Var}(Z)}
\end{aligned}
$$

Hence, the variance of the hedging error can be written in terms of the correlation coefficient $\text{Corr}(L, Z) = \frac{\text{Cov}(L, Z)}{\sqrt{\text{Var}(L)}\sqrt{\text{Var}(Z)}}$:

$$
\boxed{\text{Var}(A^* - L) = \text{Var}(L) \left( 1 - \text{Corr}(L, Z)^2 \right)}
$$

The hedging portfolio reduces the risk associated with the liability $L$, measured by its variance $\text{Var}(L)$, without hedging. The worst case scenario is when $\text{Cov}(L,Z) = 0$ when the hedging instrument $Z$ is uncorrelated with the liability $L$. In this case, quadratic hedging does not provide any improvement on the intrinsic risk of the liability since $h^*_0 = E[L]$ and $h^* = 0$ so the variance of the hedging error is $\text{Var}(A^* - L) = \text{Var}(L)$.

> Simply put, hedging exploits correlations to reduce risk. If $\text{Cov}(L, Z) = 0$, no risk reduction is achieved: $\text{Var}(A^* - L) = \text{Var}(L)$.

## Delta Hedging

Using the following assumptions:

- That the price of a financial contract is given by a function $f$ of the price of an underlying asset $S_t$ at time $t$
- The function $f$ is assumed to be known at time $0$ and differentiable

The aim is to hedge the liability $L = f(S_t)$ by taking a position $h$ in the underlying asset and position $h_0$ in a risk-free investment, e.g. a unit zero-coupon bond maturing at time $t$.

Taking the optimal quadratic hedge for $n=1$:

$$
h^* = \frac{\text{Cov}(S_t, f(S_t))}{\text{Var}(S_t)}, \quad h_0^* = E[f(S_t)] - h^* E[S_t]
$$

The Taylor expansion of $f(S_t)$ around the expected value $\bar{S}_t = E[S_t]$ provides an approximation for the optimal hedge.

$$
L = f(S_t) \approx f(\bar{S}_t) + f'(\bar{S}_t)(S_t - \bar{S}_t)
$$

The optimal hedge is therefore:

$$
\begin{aligned}
h^* & = \frac{\text{Cov}(S_t, f(\bar{S}_t) + f'(\bar{S}_t)(S_t - \bar{S}_t))}{\text{Var}(S_t)} \\\\
& = \frac{f'(\bar{S}_t) \text{Cov}(S_t, S_t - \bar{S}_t)}{\text{Var}(S_t)} \\\\
& = \frac{f'(\bar{S}_t) \text{Var}(S_t)}{\text{Var}(S_t)} \\\\
& = f'(\bar{S_t})
\end{aligned}
$$

and

$$
\begin{aligned}
h_0^* & = E[f(S_t) + f'(\bar{S}_t)(S_t - \bar{S}_t)] - f'(\bar{S}_t)S_t \\\\
& = f(\bar{S}_t) - f'(\bar{S}_t) \bar{S}_t
\end{aligned}
$$

The hedging error is therefore:

$$
\begin{aligned}
h^*_0 + h^*St - f(S_t) &= f(\bar{S}_t) - f'(\bar{S}_t) \bar{S}_t + f'(\bar{S}_t) S_t - f(S_t) \\\\
&= f(\bar{S}_t) + f'(\bar{S}_t)(S_t - \bar{S}_t) - f(S_t)
\end{aligned}
$$

This is just the error made by approximating $f(S_t)$ by its linear Taylor expansion around $\bar{S}_t$.

If $t$ is small, $\bar{S}_t \approx S_0$, and the delta hedge can be obtained:

$$
h^* = f'(S_0), \quad h_0^* = f(S_0) - f'(S_0)S_0
$$

The approximation of the optimal hedge does not need any knowledge of an underlying pdf of the asset price $S_t$. However, the approximation is only valid for small times $t$ so that is can only be used reasonably with frequent re-adjustments of the hedge (dynamic hedging). This usually leads to high transaction costs in practice.

### Delta Hedging Example with Geometric Brownian Motion

Assume a contract with payoff $g(S_T)$ at time $T$ depending on the price of an underlying asset $S_T$. The price of the contract at time $0$ is given by the risk-neutral valuation formula:

$$
\pi_0 = e^{-r_{0,T}T} \mathbb{E}^{\mathbb{Q}}[g(S_T)]
$$

Assuming risk-neutral Geometric Brownian Motion (GBM) for $S_t$:

$$
S_T = S_0 e^{\mu_0 T + \sigma_0 \sqrt{T} W}
$$

$$
W \sim N(0,1), \quad \mu = r_{0,T} - \frac{1}{2}\sigma_0^2
$$

Therefore,

$$
S_T = S_0 e^{(r_{0,T} - \frac{1}{2}\sigma_0^2)T + \sigma_0\sqrt{T}W}
$$

The contract price at $t=0$ is:

$$
\pi_0 = e^{-r_{0,T}T} \int_{-\infty}^{\infty} g\left(S_0 e^{(r_{0,T} - \frac{1}{2}\sigma_0^2)T + \sigma_0\sqrt{T}w}\right) \frac{1}{\sqrt{2\pi}} e^{-w^2/2} dw
$$

At time $t$ the price of the contract is:

$$
\begin{aligned}
\pi_t & = e^{-r_{t,T}(T-t)} \mathbb{E}^{\mathbb{Q}}[g(S_T) | S_t] \\\\
& = e^{-r_{t,T}(T-t)} \int_{-\infty}^{\infty} g\left(S_t e^{(r_{t,T} - \frac{1}{2}\sigma_t^2)(T-t) + \sigma_t\sqrt{T-t}w}\right) \frac{1}{\sqrt{2\pi}} e^{-w^2/2} dw
\end{aligned}
$$

Therefore, the assumption underlying the delta hedge is:

$$
\pi_t \approx f(S_t)
$$

where $f$ is a function known at time $0$ and holds oly approximately if $t$ is close to $0$. Assuming, this the following approximations hold:

$$
r_{t,T} \approx r_{0,T}, \quad \sigma_t \approx \sigma_0
$$

The underlying assumptions of the delta hedge are typically only valid for small times $t$ so that frequent re-adjustments of the hedge are required in practice.

If the payoff function $g(x)$ is given by $g(x) = \max(x - K, 0)$ for a European call option with strike $K$:

$$
\pi_0 = C_{\text{BS}}(S_0, K, r_{0,T}, \sigma_0, T)
$$

where $C_{\text{BS}}$ is the Black-Scholes formula for a European call option.

The Black-Scholes Greek (Delta) $\Delta = \frac{\partial C_{\text{BS}}}{\partial S_0} = h^*$ denotes the shares needed. The risk-free investment is $h_0^* = C_{\text{BS}} - \Delta S_0$.

## General Solution (Any value of $n$)

For the general case, assume that there is a large number $n$ of risk assets $\mathbf{Z} = (Z_1, Z_2, \ldots, Z_n)^{\intercal}$ available for hedging the liability $L$.

In the single case $n=1$, the calculation for the minimum of $\text{Var}(A - L)$ was straightforward since it was a quadratic function of a single variable $h$ which had a unique minimum.

For higher dimensions, the convexity of the variance in $\mathbf{h}$ still holds, but the calculation of the minimum is more involved as follows.

### Background: Convexity

- The set $\mathbb{C} \subset \mathbb{R}^n$ is called a **convex set** if for any $\lambda \in [0, 1]$ and any $\mathbf{x}, \mathbf{y} \in \mathbb{C}$, the convex combination $\lambda \mathbf{x} + (1 - \lambda)\mathbf{y} \in \mathbb{C}$ holds true.

- The function $f: \mathbb{C} \to \mathbb{R}$ is called **convex** if for any $\lambda \in [0, 1]$ and any $\mathbf{x}, \mathbf{y} \in \mathbb{C}$, the inequality

$$
f(\lambda \mathbf{x} + (1 - \lambda)\mathbf{y}) \leq \lambda f(\mathbf{x}) + (1 - \lambda) f(\mathbf{y})
$$

holds true.

- Both set and function are **strictly convex** if $<$ holds instead of $\leq$.

**Key insight**: Since variance is a strictly convex function of $\mathbf{h}$, any local minimum is also a global minimum, which guarantees the uniqueness of the optimal hedging portfolio.

### Problem Setup

The **optimal quadratic hedging portfolio** is determined by the conditions:

1. $\mathbb{E}[A - L] = 0$ (matching expected values)
2. $\text{Var}(A - L)$ is minimised

Let $(h_0^*, \mathbf{h}^*)$ denote the optimal portfolio with value $A^* = h_0^* + \mathbf{h}^{*T} \mathbf{Z}$, where:

- $h_0^*$ is the position in the risk-free asset (cash)
- $\mathbf{h}^* = (h_1^*, h_2^*, \ldots, h_n^*)^{\intercal}$ are the positions in the $n$ risky assets
- $\mathbf{Z} = (Z_1, Z_2, \ldots, Z_n)^{\intercal}$ are the values of the risky assets

### Deriving the Variance of Hedging Error

The first step is to minimize $\text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L)$ with respect to $\mathbf{h}$. Since $\text{Var}(h_0 + \mathbf{h}^{\intercal} \mathbf{Z} - L) = \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L)$ (adding a constant doesn't affect variance), the variance of the hedging error is:

$$
\text{Var}(A-L) = \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) = \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z}) + \text{Var}(L) - 2\text{Cov}(\mathbf{h}^{\intercal} \mathbf{Z}, L)
$$

**Expanding the covariance term:**

The last term can be rewritten using $\mathbf{h}^{\intercal} \mathbf{Z} = \sum_{i=1}^n h_i Z_i$ as:

$$
\begin{aligned}
\text{Cov}(\mathbf{h}^{\intercal} \mathbf{Z}, L) & = \text{Cov}\left(\sum_{i=1}^n h_i Z_i, L\right) \\
& = \mathbb{E}\left[\sum_{i=1}^n h_i Z_i \cdot L \right] - \mathbb{E}\left[\sum_{i=1}^n h_i Z_i\right] \mathbb{E}[L] \\
& = \sum_{i=1}^n h_i \left( \mathbb{E}[Z_i L] - \mathbb{E}[Z_i] \mathbb{E}[L] \right) \\
& = \sum_{i=1}^n h_i \text{Cov}(Z_i, L) \\
& = \mathbf{h}^{\intercal} \mathbf{\Sigma}_{L, \mathbf{Z}}
\end{aligned}
$$

**Note**: Here $\mathbf{\Sigma}_{L, \mathbf{Z}}$ is a **column vector** (dimension $n \times 1$) containing the covariances of $L$ with each asset:

$$
\mathbf{\Sigma}_{L, \mathbf{Z}} = \begin{pmatrix} \text{Cov}(L, Z_1) \\ \text{Cov}(L, Z_2) \\ \vdots \\ \text{Cov}(L, Z_n) \end{pmatrix}
$$

This vector indicates how strongly the liability $L$ co-moves with each hedging instrument.

### The Covariance Matrix

Using the result $\text{Var}(\mathbf{h}^{\intercal} \mathbf{Z}) = \mathbf{h}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{h}$, where $\Sigma_{\mathbf{Z}}$ is the **covariance matrix** (dimension $n \times n$) of $\mathbf{Z}$ containing the covariances among all pairs of financial instruments:

$$
\Sigma_{\mathbf{Z}} = \begin{pmatrix}
\text{Var}(Z_1) & \text{Cov}(Z_1, Z_2) & \dots & \text{Cov}(Z_1, Z_n) \\
\text{Cov}(Z_2, Z_1) & \text{Var}(Z_2) & \dots & \text{Cov}(Z_2, Z_n) \\
\vdots & \vdots & \ddots & \vdots \\
\text{Cov}(Z_n, Z_1) & \text{Cov}(Z_n, Z_2) & \dots & \text{Var}(Z_n)
\end{pmatrix}
$$

**Note**: The diagonal elements are variances (i.e., $\text{Cov}(Z_i, Z_i) = \text{Var}(Z_i)$), while off-diagonal elements are covariances between different assets.

This matrix captures the entire correlation structure among the hedging instruments—essential information for portfolio construction.

### Variance Formula in Matrix Form

The variance of the hedging error can now be written compactly as:

$$
\boxed{\text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) = \mathbf{h}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{h} + \text{Var}(L) - 2 \mathbf{h}^{\intercal} \mathbf{\Sigma}_{L, \mathbf{Z}}}
$$

**Breaking down the terms**:

- $\mathbf{h}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{h}$ = variance of the hedging portfolio (quadratic form)
- $\text{Var}(L)$ = variance of the liability (constant)
- $2 \mathbf{h}^{\intercal} \mathbf{\Sigma}_{L, \mathbf{Z}}$ = twice the covariance between portfolio and liability

Writing out the indices explicitly:

$$
\text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) = \sum_{i=1}^n \sum_{j=1}^n h_i h_j \text{Cov}(Z_i, Z_j) + \text{Var}(L) - 2 \sum_{i=1}^n h_i \text{Cov}(L, Z_i)
$$

### Properties of Covariance Matrices

The covariance matrix $\Sigma_{\mathbf{Z}}$ is an important quantity which quantifies the correlations among the financial instruments used for hedging. Any covariance matrix has the following properties:

**1. Symmetry**:

$$
(\Sigma_{\mathbf{Z}})_{ij} = \text{Cov}(Z_i, Z_j) = \text{Cov}(Z_j, Z_i) = (\Sigma_{\mathbf{Z}})_{ji} \quad \text{for all } i, j
$$

This follows from the definition of covariance.

**2. Positive Semi-definite**:
For any vector $\mathbf{x} \in \mathbb{R}^n$,

$$
\mathbf{x}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{x} \geq 0
$$

This means the quadratic form is always non-negative, which is crucial for the existence of a minimum.

**Proof of positive semi-definiteness**:

Define $\bar{Z}_i = \mathbb{E}[Z_i]$ and $\bar{\mathbf{Z}}$ as the vector containing the elements $\bar{Z}_i$.
The covariance can be written as $\text{Cov}(Z_i, Z_j) = \mathbb{E}[(Z_i - \bar{Z}_i)(Z_j - \bar{Z}_j)]$.

Thus,

$$
\begin{aligned}
\mathbf{x}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{x} & = \sum_{i=1}^n \sum_{j=1}^n x_i x_j \text{Cov}(Z_i, Z_j) \\
& = \sum_{i=1}^n \sum_{j=1}^n x_i x_j \mathbb{E}[(Z_i - \bar{Z}_i)(Z_j - \bar{Z}_j)] \\
& = \mathbb{E}\left[ \sum_{i=1}^n \sum_{j=1}^n x_i x_j (Z_i - \bar{Z}_i)(Z_j - \bar{Z}_j) \right] \\
& = \mathbb{E}\left[ \sum_{i=1}^n x_i (Z_i - \bar{Z}_i) \sum_{j=1}^n x_j (Z_j - \bar{Z}_j) \right] \\
& = \mathbb{E}\left[ \left( \mathbf{x}^{\intercal} (\mathbf{Z} - \bar{\mathbf{Z}}) \right) \left( \mathbf{x}^{\intercal} (\mathbf{Z} - \bar{\mathbf{Z}}) \right) \right] \\
& = \mathbb{E}\left[ \left( \mathbf{x}^{\intercal} (\mathbf{Z} - \bar{\mathbf{Z}}) \right)^2 \right]
\end{aligned}
$$

The scalar product $\mathbf{x}^{\intercal} (\mathbf{Z} - \bar{\mathbf{Z}})$ is a random variable, so its square is non-negative. Defining $Y = \mathbf{x}^{\intercal} (\mathbf{Z} - \bar{\mathbf{Z}})$, it follows that $\mathbf{x}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{x} = \mathbb{E}[Y^2] \geq 0$.

Furthermore, $\mathbb{E}[Y^2] = \text{Var}(Y) + (\mathbb{E}[Y])^2 \geq 0$ since $\mathbb{E}[Y] = 0$.

**Important**: If the assets are linearly independent (no redundant assets), then $\Sigma_{\mathbf{Z}}$ is **positive definite** (not just semi-definite), meaning $\mathbf{x}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{x} > 0$ for all $\mathbf{x} \neq \mathbf{0}$, which ensures $\Sigma_{\mathbf{Z}}$ is invertible.

### Finding the Optimal Portfolio

The global minimum of $\text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L)$ is now determined with respect to $h_1, h_2, \ldots, h_n$ by taking the partial derivatives and setting them equal to zero.

For the $m$-th variable $h_m$ (where $m = 1, 2, \ldots, n$):

$$
\begin{aligned}
\frac{\partial}{\partial h_m} \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) & = \frac{\partial}{\partial h_m} \left( \mathbf{h}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{h} + \text{Var}(L) - 2 \mathbf{h}^{\intercal} \mathbf{\Sigma}_{L, \mathbf{Z}} \right) \\
& = \frac{\partial}{\partial h_m} \left( \sum_{i=1}^n \sum_{j=1}^n h_i h_j \text{Cov}(Z_i, Z_j) - 2 \sum_{i=1}^n h_i \text{Cov}(L, Z_i) \right) \\
& = 2 \sum_{j=1}^n h_j \text{Cov}(Z_m, Z_j) - 2 \text{Cov}(L, Z_m) \\
& = 0
\end{aligned}
$$

**Why the factor of 2?** The quadratic term $\mathbf{h}^{\intercal} \Sigma_{\mathbf{Z}} \mathbf{h}$ is differentiated using the identity:

$$
\frac{\partial}{\partial \mathbf{h}} (\mathbf{h}^{\intercal} A \mathbf{h}) = (A + A^{\intercal})\mathbf{h}
$$

Since $\Sigma_{\mathbf{Z}}$ is symmetric ($\Sigma_{\mathbf{Z}} = \Sigma_{\mathbf{Z}}^{\intercal}$), this gives $2\Sigma_{\mathbf{Z}}\mathbf{h}$.

This calculation can be verified explicitly for $n=2$:

$$
\begin{aligned}
\frac{\partial}{\partial h_1} \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) & = \frac{\partial}{\partial h_1} \bigg( h_1^2 \text{Cov}(Z_1, Z_1) + h_1 h_2 \text{Cov}(Z_1, Z_2) \\
& \quad + h_2 h_1 \text{Cov}(Z_2, Z_1) + h_2^2 \text{Cov}(Z_2, Z_2) \\
& \quad + \text{Var}(L) - 2 h_1 \text{Cov}(L, Z_1) - 2 h_2 \text{Cov}(L, Z_2) \bigg) \\
& = 2 h_1 \text{Cov}(Z_1, Z_1) + h_2 \text{Cov}(Z_1, Z_2) + h_2 \text{Cov}(Z_2, Z_1) - 2 \text{Cov}(L, Z_1) \\
& = 2 h_1 \text{Cov}(Z_1, Z_1) + 2 h_2 \text{Cov}(Z_1, Z_2) - 2 \text{Cov}(L, Z_1)
\end{aligned}
$$

where $\text{Cov}(Z_1, Z_2) = \text{Cov}(Z_2, Z_1)$ follows by symmetry.

### Solution in Matrix Form

Setting all partial derivatives to zero, this yields the system of equations:

$$
\begin{aligned}
\frac{\partial}{\partial h_1} \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) &= 0 \\
& \vdots \\
\frac{\partial}{\partial h_n} \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) &= 0
\end{aligned}
$$

In vector-matrix notation, this system can be written compactly as:

$$
2\Sigma_{\mathbf{Z}} \mathbf{h} - 2\mathbf{\Sigma}_{L, \mathbf{Z}} = \mathbf{0}
$$

or equivalently:

$$
\Sigma_{\mathbf{Z}} \mathbf{h} = \mathbf{\Sigma}_{L, \mathbf{Z}}
$$

This is a **system of $n$ linear equations in $n$ unknowns**. Multiplying both sides from the left by the inverse of the covariance matrix $\Sigma_{\mathbf{Z}}^{-1}$ (which exists if $\Sigma_{\mathbf{Z}}$ is positive definite), the optimal vector $\mathbf{h}^*$ is given by:

$$
\boxed{\mathbf{h}^* = \Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}}
$$

**Interpretation**:

- The optimal hedge weights $\mathbf{h}^*$ depend on two factors:
  1. The **inverse covariance matrix** $\Sigma_{\mathbf{Z}}^{-1}$: accounts for correlations among hedging instruments
  2. The **covariance vector** $\mathbf{\Sigma}_{L, \mathbf{Z}}$: measures how each instrument relates to the liability

- If assets were uncorrelated ($\Sigma_{\mathbf{Z}}$ diagonal), then each $h_i^* = \frac{\text{Cov}(L, Z_i)}{\text{Var}(Z_i)}$, which is the simple regression coefficient.

- With correlations, $\Sigma_{\mathbf{Z}}^{-1}$ adjusts for redundancy and overlap among hedging instruments.

Once $\mathbf{h}^*$ is determined, $h_0^*$ is set to satisfy the first condition $\mathbb{E}[A - L] = 0$:

$$
h_0^* = \mathbb{E}[L] - \mathbf{h}^{*T} \mathbb{E}[\mathbf{Z}]
$$

This ensures the expected hedging error is zero.

### Minimum Variance Achieved

Substituting $\mathbf{h}^*$ back into the variance formula, the **minimum variance** is:

$$
\text{Var}(A^* - L) = \text{Var}(L) - \mathbf{\Sigma}_{L, \mathbf{Z}}^{\intercal} \Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}
$$

The second term represents the variance reduction achieved through hedging. Perfect hedging (zero variance) occurs when $L$ lies in the span of $\mathbf{Z}$.

## Notation Summary

> **Important Distinction**:
>
> - $\mathbf{\Sigma}_{L, \mathbf{Z}}$ (bold) denotes the **covariance vector** (dimension $n \times 1$) containing the covariances of $L$ with each of the financial instruments $Z_1, \ldots, Z_n$.
> - $\Sigma_{\mathbf{Z}}$ (non-bold) denotes the **covariance matrix** (dimension $n \times n$) containing the covariances among all pairs of financial instruments.

**Dimensions check**:

- $\Sigma_{\mathbf{Z}}$: $n \times n$ matrix
- $\mathbf{\Sigma}_{L, \mathbf{Z}}$: $n \times 1$ vector
- $\mathbf{h}^*$: $n \times 1$ vector
- $\Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}$: $(n \times n)(n \times 1) = n \times 1$ ✓

## The Complete Optimal Hedging Portfolio

The formula $\mathbf{h}^* = \Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}$ gives the solutions for the optimal quadratic hedging positions $h_1^*, h_2^*, \ldots, h_n^*$ in the risky assets.

In the presence of a risk-free asset, the solution for $\mathbf{h}^*$ is the same since $\text{Var}(h_0 + \mathbf{h}^{\intercal} \mathbf{Z} - L) = \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L)$. The contribution $h_0$ allows fixing the expected hedging error at zero: $\mathbb{E}[h_0^* + \mathbf{h}^{*T} \mathbf{Z} - L] = 0$.

Solving this condition for $h_0^*$ yields:

$$
h_0^* = \mathbb{E}[L] - \mathbf{h}^{*T} \mathbb{E}[\mathbf{Z}]
$$

Note that $\mathbb{E}[\mathbf{Z}]$ is the column vector containing the entries $\mathbb{E}[Z_i]$:

$$
\mathbb{E}[\mathbf{Z}] = \begin{pmatrix} \mathbb{E}[Z_1] \\ \mathbb{E}[Z_2] \\ \vdots \\ \mathbb{E}[Z_n] \end{pmatrix}
$$

### Properties of the Optimal Hedging Portfolio

The optimal hedging portfolio with positions $(h_0^*, \mathbf{h}^*)$ giving portfolio value $A^* = h_0^* + \mathbf{h}^{*T} \mathbf{Z}$ has the following properties:

**1. Zero expected hedging error:**

$$
\mathbb{E}[A^* - L] = 0
$$

**2. Minimum variance:**

$$
\text{Var}(A^* - L) = \text{Var}(L) - \mathbf{\Sigma}_{L, \mathbf{Z}}^{\intercal} \Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}
$$

The second term $\mathbf{\Sigma}_{L, \mathbf{Z}}^{\intercal} \Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}$ represents the **variance reduction** achieved through optimal hedging. This is always non-negative (since $\Sigma_{\mathbf{Z}}$ is positive semi-definite), so the hedged variance is never worse than the unhedged variance.

**3. Orthogonality condition:**

It can also be shown that

$$
\text{Cov}(A^* - L, Z_k) = 0 \quad \text{for all } k = 1, 2, \ldots, n
$$

This means the **hedging error is uncorrelated with all hedging instruments**. This is the multivariate analogue of the orthogonality principle in regression—the residual is orthogonal to all regressors.

**Proof sketch**: The first-order conditions from $\nabla_{\mathbf{h}} \text{Var}(\mathbf{h}^{\intercal} \mathbf{Z} - L) = \mathbf{0}$ at $\mathbf{h}^*$ imply:

$$
\Sigma_{\mathbf{Z}} \mathbf{h}^* = \mathbf{\Sigma}_{L, \mathbf{Z}}
$$

This means $\text{Cov}(\mathbf{h}^{*T} \mathbf{Z}, Z_k) = \text{Cov}(L, Z_k)$ for all $k$, which gives:

$$
\text{Cov}(\mathbf{h}^{*T} \mathbf{Z} - L, Z_k) = \text{Cov}(\mathbf{h}^{*T} \mathbf{Z}, Z_k) - \text{Cov}(L, Z_k) = 0
$$

### Worst Case: Uncorrelated Assets

Similar to the case $n = 1$, the worst possible situation is when the hedging instruments are all uncorrelated with the liability. If

$$
\text{Cov}(L, Z_k) = 0 \quad \text{for all } k
$$

then quadratic hedging does not provide any improvement on the intrinsic risk of the liability, since:

$$
h_0^* = \mathbb{E}[L], \quad \mathbf{h}^* = \mathbf{0}
$$

and the variance of the hedging error is just:

$$
\text{Var}(A^* - L) = \text{Var}(L)
$$

**Economic interpretation**: If $\mathbf{\Sigma}_{L, \mathbf{Z}} = \mathbf{0}$ (the liability is uncorrelated with all available hedging instruments), then the optimal strategy is to hold no risky assets ($\mathbf{h}^* = \mathbf{0}$) and invest everything in the risk-free asset ($h_0^* = \mathbb{E}[L]$) to match the expected liability. No variance reduction is possible.

### The Role of Correlations in Risk Reduction

Comparing the unhedged variance $\text{Var}(L)$ with the optimally hedged variance:

$$
\text{Var}(A^* - L) = \text{Var}(L) - \mathbf{\Sigma}_{L, \mathbf{Z}}^{\intercal} \Sigma_{\mathbf{Z}}^{-1} \mathbf{\Sigma}_{L, \mathbf{Z}}
$$

highlights that **quadratic hedging exploits the correlations** between the liability and the underlying securities in order to reduce the effective risk (variance) of the liability.

These correlations are captured by:

- The **covariance matrix** $\Sigma_{\mathbf{Z}}$: describes how the hedging instruments co-move with each other
- The **covariance vector** $\mathbf{\Sigma}_{L, \mathbf{Z}}$: describes how each instrument co-moves with the liability

The stronger the correlations (larger entries in $\mathbf{\Sigma}_{L, \mathbf{Z}}$), and the less correlated the instruments are with each other (more diagonal $\Sigma_{\mathbf{Z}}$), the greater the variance reduction achieved.

**Perfect hedging** occurs when $L$ can be perfectly replicated as a linear combination of $\mathbf{Z}$, i.e., when $L = c_0 + \mathbf{c}^{\intercal} \mathbf{Z}$ for some constants. In this case, $\mathbf{h}^* = \mathbf{c}$ and the minimum variance is zero.
$$
