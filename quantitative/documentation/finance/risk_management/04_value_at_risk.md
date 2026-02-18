# Value at Risk

The value at risk (VaR) at level $p \in (0, 1)$ of a portfolio with value $X$ at time 1 is

```math
\text{VaR}_p(X) = \min\{m : \Pr(mR_0 + X < 0) \leq p\}
```

In other words, VaRp (X) is the smallest amount of money that, if invested in a risk free asset and
added to the portfolio, ensures that the probability of a negative portfolio value is smaller than p.
Typical values of p are 5%, 1%, 0.5%. Usually one considers X = V1 − V0 R0 , i.e., the initial capital
is included as a liability including the accumulated risk free interest.
It is useful to consider an alternative representation as follows. Using basic manipulations we
obtain

```math
\begin{aligned}
\{m : \Pr(mR_0 + X < 0) \leq p\} &= \{m : \Pr(-X/R_0 > m) \leq p\} \\
&= \{m : 1 - \Pr(-X/R_0 \leq m) \leq p\} \\
&= \{m : \Pr(-X/R_0 \leq m) \geq 1 - p\} \\
&= \{m : \Pr(L \leq m) \geq 1 - p\},
\end{aligned}
```

where we set $L = -X/R_0 = V_0 - V_1/R_0$, which is the discounted loss. We thus obtain the
representation of $\text{VaR}_p(X)$:

```math
\text{VaR}_p(X) = \min\{m : \Pr(L \leq m) \geq 1 - p\}
```

In words, VaRp (X) is the smallest amount of money that, if invested in a risk-free asset at time
zero, can cover the loss at time 1 with a probability > 1 − p.
The cumulative distribution function (CDF) of $L$ is

```math
F_L(m) = \int_{-\infty}^{m} f_L(x) \, dx = \Pr(L \leq m)
```

Since $F_L$ is an increasing function, we see that the minimum used in the definition of VaRp (X)
indeed exists.
Let us now introduce the inverse $F_L^{-1}$ of the CDF $F_L$. The inverse can be defined in general as

```math
F_L^{-1}(y) = \min\{m : F_L(m) \geq y\}
```

Therefore, we see that $\text{VaR}_p(X)$ is just

```math
\text{VaR}_p(X) = F_L^{-1}(1 - p)
```

We know that $F_L$ is strictly increasing. If $F_L$ is also continuous, we can determine $F_L^{-1}$ and thus
$\text{VaR}_p$ by a direct inversion. See Fig. 9.1 for an illustration of VaRp (X) in terms of the CDFs FX/R0
and FL . In statistics, the inverse of a CDF is also called quantile function.
defined as an average over VaRp (X) and thus corresponds to the indicated area divided by p.

![Value at Risk and Expected Shortfall](../images/var_es.png)

**Proposition 9.0.1.** VaRp has the properties translation invariance, monotonicity, and positive ho-
mogeneity.

_Proof._ Consider $\lambda X + aR_0$ to show translation invariance and positive homogeneity:

```math
\begin{aligned}
\text{VaR}_p(\lambda X + aR_0) &= \min\{m : \Pr(mR_0 + \lambda X + aR_0 < 0) \leq p\} \\
&= \min\left\{m : \Pr\left(\frac{m+a}{\lambda} R_0 + X < 0\right) \leq p\right\} \\
&= \min\left\{m : F_L\left(\frac{m+a}{\lambda}\right) \geq 1 - p\right\}
\end{aligned}
```

using the same steps as above. Setting $k = (m + a)/\lambda$ we obtain thus

```math
\begin{aligned}
\text{VaR}_p(\lambda X + aR_0) &= \lambda \min\{k : F_L(k) \geq 1 - p\} - a \\
&= \lambda \text{VaR}_p(X) - a,
\end{aligned}
```

where $m = \lambda k - a$. Therefore, translation invariance follows by setting λ = 1 and positive homo-
geneity by setting a = 0.
Monotonicity: $L_1 \leq L_2$ implies $F_{L_2}(m) \leq F_{L_1}(m)$. Therefore

```math
\begin{aligned}
F_{L_2}^{-1}(1 - p) &= \min\{m : F_{L_2}(m) \geq 1 - p\} \\
&\geq \min\{m : F_{L_1}(m) \geq 1 - p\} \\
&= F_{L_1}^{-1}(1 - p)
\end{aligned}
```

If $X_2 \leq X_1$ then $L_2 \geq L_1$ so that

```math
\text{VaR}_p(X_2) = F_{L_2}^{-1}(1 - p) \geq F_{L_1}^{-1}(1 - p) = \text{VaR}_p(X_1)
```

In order to explicitly calculate $\text{VaR}_p$ we need the following proposition.

**Proposition 9.0.2.** If g : R → R is increasing and continuous, then for any random variable Z it
holds that

```math
F_{-g(Z)}^{-1}(1 - p) = -F_{g(Z)}^{-1}(p)
```

and

```math
F_{g(Z)}^{-1}(p) = g(F_Z^{-1}(p))
```

_Proof._ We have

```math
\begin{aligned}
F_{-g(Z)}(x) &= \Pr(-g(Z) \leq x) \\
&= \Pr(g(Z) \geq -x) \\
&= 1 - \Pr(g(Z) \leq -x) \\
&= 1 - F_{g(Z)}(-x)
\end{aligned}
```

Therefore, solving $F_{-g(Z)}(x) = 1 - p$ for $x$ is equivalent to solving $1 - F_{g(Z)}(-x) = 1 - p$ for $x$,
which implies

```math
x = F_{-g(Z)}^{-1}(1 - p) = -F_{g(Z)}^{-1}(p)
```

and Eq. (9.7) follows. In order to show Eq. (9.8) we start with

```math
\begin{aligned}
F_{g(Z)}(x) &= \Pr(g(Z) \leq x) \\
&= \Pr(Z \leq g^{-1}(x)) \\
&= F_Z(g^{-1}(x))
\end{aligned}
```

Therefore, solving $F_{g(Z)}(x) = p$ for $x$ is equivalent to solving $F_Z(g^{-1}(x)) = p$ for $x$, which implies

```math
x = F_{g(Z)}^{-1}(p) = g(F_Z^{-1}(p))
```

and Eq. (9.8) follows.

Example. Consider a portfolio that consists of a single share with price S0 today and price S1 at
the time 1 in the future. Assume zero interest rates (R0 = 1). What is VaRp (X) at time 1 under
the assumption that St follows geometric Brownian motion, i.e., log SS01 ∼ N (µ, σ 2 )?

Solution. The portfolio value considered is: $X = V_1 - V_0 R_0 = S_1 - S_0$ and the loss is

```math
\begin{aligned}
L = -X/R_0 &= S_0 - S_1 \\
&= S_0 - S_0 e^{\log S_1/S_0} \\
&= S_0\left(1 - e^{\mu + \sigma Z}\right) \\
&= -g(Z),
\end{aligned}
```

where $Z \sim N(0, 1)$ and $g(x) = -S_0(1 - e^{\mu + \sigma x})$ is continuous and strictly increasing. We can
therefore apply Proposition 4.1.2 to obtain for $\text{VaR}_p(X)$:

```math
\begin{aligned}
\text{VaR}_p(X) &= F_L^{-1}(1 - p) \\
&= F_{-g(Z)}^{-1}(1 - p) \\
&= -F_{g(Z)}^{-1}(p) \\
&= -g(F_Z^{-1}(p)) \\
&= S_0\left(1 - e^{\mu + \sigma \Phi^{-1}(p)}\right)
\end{aligned}
```

where $\Phi^{-1}$ is the inverse of the standard cumulative distribution function.

## Expected shortfall

VaRp gives the loss that will not be exceeded with a certain confidence. For example, if VaRp of
a portfolio is £3000 for p = 1%, it means that there is only a 1% chance that the loss will exceed
£3000. However, VaRp does not provide any information on how bad the loss can actually be. Let's
assume that the above example applies for an investment horizon of 1 day and a trader is instructed
to construct a portfolio such that VaR0.01 < £3000. This means that, even if the trader satisfies
the risk requirement, there might be 1 or 2 trading days per year, where the loss could, e.g., be
£3,000,000, with catastrophic consequences for the company.
An alternative risk measure that takes into account the amount of the possible loss is expected
shortfall (ES). ES is defined as an average of $\text{VaR}_p$ up to a certain $p$-level:

```math
\text{ES}_p(X) = \frac{1}{p} \int_0^p \text{VaR}_y(X) \, dy
```

Using Eq. (9.5), we can also write

```math
\text{ES}_p(X) = \frac{1}{p} \int_0^p F_L^{-1}(1 - y) \, dy = \frac{1}{p} \int_{1-p}^{1} F_L^{-1}(z) \, dz
```

after a variable transformation $z = 1 - y$ in the integral. As before, we have the discounted loss
L = −X/R0 . We see that ES takes into account the left tail of the CDF of the portfolio value X.
In this way catastrophic loss events with very small p are considered. In other words, ES provides a
measure of how much the loss can be expected to be, if a catastrophic event happens. In Fig. 9.1(c),
ESp (X) corresponds to the indicated area divided by p.
