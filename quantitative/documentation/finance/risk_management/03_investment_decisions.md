Investment Decisions - Maximizing Expected Utility

In this chapter we will deal with the mathematical foundations of doing optimal investment decisions.
This is more general than the methods presented so far. Often, the decision is quite strongly
depending on the risk involved and boils down to a decision of whether to invest at all, not invest
at all, or partially invest what is available to you. Should you invest in the same way as Bill Gates
does, just rescaling the amount of money you spend? Probably not. Individual circumstances are
very different. Optimal investment needs, and acceptable level of risks, depend very much on the
individual circumstances. This is mathematically described by the concept of utility function.

## Limitations of the mean variance portfolio analysis

The mean-variance approach to investments focuses only on two characteristics of the future portfolio
value $V_1 = w_0 R_0 + \mathbf{w}^T \mathbf{R}$, namely its mean

```math
\mathbb{E}[V_1] = w_0 R_0 + \mathbf{w}^T \boldsymbol{\mu}
```

and its variance

```math
\text{Var}(V_1) = \mathbf{w}^T \Sigma \mathbf{w}.
```

However, the mean and the variance of $V_1$ do not necessarily capture the important features of the
probability density function (pdf) underlying the RV $V_1$. This is evident in Fig. 3.1, which plots four
different pdfs, which all have the same mean and variance. This means that RVs $V_1$ characterized
by these pdfs, will all have the same outcome under the mean-variance analysis. However, for the
bimodal pdf (c) and the strongly skewed pdf (d) the mean value will not be a good representation of
the most likely outcome. The exponential distribution (b) is characterized by only two parameters,
like the Gaussian (a), but these are not the mean and the variance. Only the normal distribution (a)
is well summarized by its mean and variance. Here, the variance quantifies a range of likely deviations
from the mean, for both positive (above the mean) and negative (below the mean) deviations, and
is thus a good measure for the risk associated with the investment.
We conclude that the mean-variance approach is reasonable if $V_1$ is approximately normal dis-
tributed. For general portfolio values one can consider an approach based on so called utility functions
to value investments.

![Utility Functions](../images/utility_functions.png)

## Utility functions

Consider an investor who has the amount $V_0$ available to invest at time 0. If he invests in a portfolio
of assets (including a risk-free asset), the investor's wealth at time 1 is

```math
V_1 = w_0 R_0 + \mathbf{w}^T \mathbf{R}.
```

So far, the decision on the investment portfolio $(w_0, \mathbf{w})$ has been based on a mean-variance approach,
that is, $(w_0, \mathbf{w})$ is determined such that $\mathbb{E}[V_1]$ is maximal and $\text{Var}(V_1)$ is minimal. A more general
approach that can take into account returns that are not normal distributed relies on a function $u$,
the so-called utility function. The utility function measures the utility (subjective benefit) of the
portfolio value $V_1$ for the investor. The utility function needs to satisfy the following two generic
properties:

1.  More money always increases the utility, thus $u(x)$ is a monotonically increasing function in
    $x$.

2.  The increase in utility from additional money is less the more money you already have. If you
    are a student, to receive £1000 more from your investment increases your utility much more
    than if you are a millionaire. As a consequence, $u(x)$ is a concave function: the gain in utility
    $u(x + \Delta) - u(x)$ from an extra amount $\Delta$ decreases for larger $x$. This property characterizes
    a risk-averse investor. More precisely, we have the following definition:

**Definition 3.2.1.** (Concave function) The function $f : D \to \mathbb{R}$ (with $D \subset \mathbb{R}$) is called a concave
function if and only if for any $\lambda \in [0, 1]$ and $x, y \in D$ it holds that

```math
f(\lambda x + (1 - \lambda)y) \geq \lambda f(x) + (1 - \lambda) f(y).
```

If $f$ is twice differentiable, $f$ is concave if and only if $f''(x) \leq 0$ for all $x$. We also see that $f$ is
concave if and only if $-f$ is convex. Note that $f$ is called strictly concave if the $>$ sign holds in
Eq. (3.4) and $f''(x) < 0$ for all $x$.

    The investment decision is then based on the principle of maximal expected utility: if there

are two different possible portfolio values $V_1$ and $\tilde{V}_1$, the investor prefers $V_1$ if

```math
\mathbb{E}[u(V_1)] > \mathbb{E}[u(\tilde{V}_1)].
```

In the context of portfolio optimization problems, this means that we want to set up a portfolio with
value $V_1 = w_0 R_0 + \mathbf{w}^T \mathbf{R}$ such that $(w_0, \mathbf{w})$

```math
\text{maximize} \quad \mathbb{E}[u(V_1)]
```

Two important properties of a concave function u:

(a) Consider the function
$f(a) = \mathbb{E}[u(aW)]$,
where $W$ is an arbitrary RV. Then $f$ is a concave function in $a$.

    Proof. Choosing $a = \lambda x + (1 - \lambda)y$ yields

```math
\begin{aligned}
f(\lambda x + (1 - \lambda)y) &= \mathbb{E}[u((\lambda x + (1 - \lambda)y)W)] \\
&\geq \mathbb{E}[\lambda u(xW) + (1 - \lambda) u(yW)] \\
&= \lambda \mathbb{E}[u(xW)] + (1 - \lambda) \mathbb{E}[u(yW)] \\
&= \lambda f(x) + (1 - \lambda) f(y).
\end{aligned}
```

    The second step follows since $u$ is concave and the expectation preserves inequalities.

(b) For an arbitrary RV $W$, we have

```math
u(\mathbb{E}[W]) \geq \mathbb{E}[u(W)].
```

    This important inequality is known as "Jensen's inequality" (without proof).

### Examples of utility functions

Any function that is monotonically increasing and concave is in principle suitable as a utility function.
Which function to choose depends on your subjective risk-averseness. The most common examples
are:

• Power-law utility function $u(x) = x^\beta$ with $0 < \beta \leq 1$. In this case

```math
u''(x) = \beta(\beta - 1)x^{\beta - 2} < 0,
```

        for $x > 0$. The linear case $\beta = 1$ characterizes a risk-indifferent investor, because here the
        gain in utility $u(x + \Delta) - u(x)$ from an extra amount $\Delta$ is independent of $x$:

```math
u(x + \Delta) - u(x) = x + \Delta - x = \Delta.
```

• Logarithmic utility function $u(x) = \log(x)$. In this case

```math
u''(x) = -\frac{1}{x^2} < 0,
```

        for $x > 0$.

• The quadratic utility function

```math
u(x) = -\frac{1}{2}(\tau - x)^2, \quad x \leq \tau.
```

        is a special case of a power-law utility function. Here, $\tau$ is an upper limit, because for $x > \tau$

this utility function decreases. The expected utility of a portfolio value $V_1$ is then

```math
\begin{aligned}
\mathbb{E}[u(V_1)] &= \mathbb{E}\left[-\frac{\tau^2}{2} - \frac{V_1^2}{2} + \tau V_1\right] \\
&= \tau \mathbb{E}[V_1] - \frac{1}{2}\left(\text{Var}(V_1) + \mathbb{E}[V_1]^2\right) - \frac{\tau^2}{2}.
\end{aligned}
```

        The portfolio optimization problem is thus closely related to the mean variance approach
        discussed previously.

• Exponential utility function $u(x) = 1 - e^{-bx}$, with $b > 0$. In this case,

```math
u''(x) = -b^2 e^{-bx} < 0,
```

        for $x > 0$. The expected utility of a portfolio value $V_1$ is here

```math
\mathbb{E}[u(V_1)] = 1 - \mathbb{E}[e^{-bV_1}].
```

        Let us assume a normal distributed portfolio value with some mean value $\mu = \mathbb{E}[V_1]$ and
        variance $\sigma^2 = \text{Var}(V_1)$ such that $V_1 \sim \mathcal{N}(\mu, \sigma^2)$. The portfolio value can thus be written as

```math
V_1 = \mu + \sigma Z,
```

        where $Z \sim \mathcal{N}(0, 1)$. From the exercises we know that $\mathbb{E}[e^{aZ}] = e^{a^2/2}$, therefore we obtain the
        expected utility as follows

```math
\begin{aligned}
\mathbb{E}[u(V_1)] &= 1 - \mathbb{E}\left[e^{-(\mu + \sigma Z)b}\right] \\
&= 1 - e^{-\mu b} \mathbb{E}\left[e^{-\sigma b Z}\right] \\
&= 1 - e^{-\mu b + \sigma^2 b^2 / 2} \\
&= 1 - e^{-b(\mu - \sigma^2 b/2)} \\
&= u(\mu - \sigma^2 b/2).
\end{aligned}
```

        Since $u(x)$ is increasing in $x$, we see that $\mathbb{E}[u(V_1)]$ is maximal if $\mu - \sigma^2 b/2$ is maximal,
        i.e.,

```math
\mathbb{E}[V_1] - \frac{b}{2} \text{Var}(V_1)
```

        is maximal. We see that the principle of maximal expected utility recovers the mean variance
        approach to portfolio optimization when the utility function is given by an exponential with
        parameter b = c/V0 .

### Certainty equivalent

For every risk-averse investor there is a fixed amount of money c such that the investor is indifferent
to receiving the fixed amount c or the random amount V1 at time 1. The amount c is called the
investor's certainty equivalent of the random value $V_1$ and is determined by

```math
u(c) = \mathbb{E}[u(V_1)].
```

If the utility function is continuous, we obtain $c$ as

```math
c = u^{-1}(\mathbb{E}[u(V_1)]).
```

Jensen's inequality implies that $u(\mathbb{E}[V_1]) \geq \mathbb{E}[u(V_1)]$ for any concave function $u$, therefore

```math
u(c) = \mathbb{E}[u(V_1)] \leq u(\mathbb{E}[V_1]),
```

so that

```math
c \leq \mathbb{E}[V_1].
```

This means that for a risk-averse investor, the certainty equivalent is less or equal than the expected
amount from the risky investment.
Example. (Fire insurance) A company wants to purchase fire insurance for the coming year. For
simplicity we assume that the company's wealth in the next year is w and that the wealth will be
reduced by some fraction αw in the case of a fire, α ∈ [0, 1]. The company assumes that the
probability of a fire in the next year is given by p and that the attitude towards risk can be measured
by a power law utility function u(x) = xβ , with 0 < β ≤ 1. Determine the range of values of the
fire insurance premium f for which the company is willing to buy fire insurance.
Solution. Without fire insurance the company's wealth in the coming year is

```math
V_1 = \begin{cases} w - \alpha w = w(1 - \alpha), & \text{probability } p \\ w, & \text{probability } 1 - p \end{cases}
```

With fire insurance it is $V_1 = w - f$ for sure, since the fire insurance covers the damage due to a
possible fire. The principle of maximal expected utility allows us to decide whether to purchase fire
insurance or not for a given premium f ∗ . Namely, if u(w − f ) > E[u(V1 )] we purchase it, and if
u(w − f ) < E[u(V1 )] we do not purchase it. There is thus a particular value $f^*$ given by

```math
u(w - f^*) = \mathbb{E}[u(V_1)],
```

such that for $f < f^*$ we purchase insurance and for $f > f^*$ we don't. Therefore, the range of
values for $f$ for which the company is willing to buy fire insurance is $f < f^*$ and it only remains to
determine $f^*$. We have

```math
w - f^* = u^{-1}(\mathbb{E}[u(V_1)]) = c
```

where $c$ is the certainty equivalent and thus

```math
f^* = w - c.
```

In order to determine $c$, we first need to calculate $\mathbb{E}[u(V_1)]$:

```math
\begin{aligned}
\mathbb{E}[u(V_1)] &= u(w(1 - \alpha))p + u(w)(1 - p) \\
&= p(w(1 - \alpha))^\beta + (1 - p)w^\beta
\end{aligned}
```

The inverse function $u^{-1}$ is $u^{-1}(y) = y^{1/\beta}$ and thus

```math
c = u^{-1}(\mathbb{E}[u(V_1)]) = u^{-1}(u(w(1 - \alpha))p + u(w)(1 - p)) = w\left[p(1 - \alpha)^\beta + 1 - p\right]^{1/\beta}.
```

The value of $f^*$ is

```math
f^* = w\left(1 - \left[p(1 - \alpha)^\beta + 1 - p\right]^{1/\beta}\right).
```

## Finding optimal investments by maximizing the expected utility

For a general utility function the portfolio optimization problem for a portfolio value $V_1 = w_0 R_0 + \mathbf{w}^T \mathbf{R}$ is

```math
\begin{aligned}
\text{maximize} \quad & \mathbb{E}[u(V_1)] \\
\text{subject to} \quad & w_0 + \mathbf{w}^T \mathbf{1} \leq V_0.
\end{aligned}
```

Since $u$ is concave, property (a) above implies that $\mathbb{E}[u(w_0 R_0 + \mathbf{w}^T \mathbf{R})]$ is a concave function of
$(w_0, \mathbf{w})$. Since $-\mathbb{E}[u(w_0 R_0 + \mathbf{w}^T \mathbf{R})]$ is then convex, we can use Proposition 2.2.1 to solve this
optimization problem. In order to find the solution we thus first consider the equality constraint,
i.e., we need to solve the set of equations

```math
\frac{\partial}{\partial w_i} \left\{ -\mathbb{E}[u(w_0 R_0 + \mathbf{w}^T \mathbf{R})] + \lambda(w_0 + \mathbf{w}^T \mathbf{1} - V_0) \right\} = 0, \quad i = 0, \ldots, n
```

```math
w_0 + \mathbf{w}^T \mathbf{1} = V_0
```

This provides $n + 2$ equations for the $n + 2$ unknowns $w_0, \mathbf{w}, \lambda$. Inspection of $\lambda$ then allows you to
determine the optimal solution for the inequality constraint.
Example. Consider an investor with a utility function $u(x) = \log(x)$ and capital $V_0$. He wants
to invest in a risk-free bond with return $R_0$ and a Greek unit zero-coupon bond with price $a_0$ at
time 0 and maturity 1. Given that the probability of a default of Greece is $p$, how much money do
you invest in each of the two bonds? Determine the optimal amount to invest for a soft budget
constraint.
Solution. We need to solve the portfolio optimization problem with $u(x) = \log(x)$ and $V_1 = w_0 R_0 + w_1 R_1$, where the return of the risky bond is $R_1 = 0$ with probability $p$ and $R_1 = 1/a_0$ with
probability $1 - p$. We calculate the expected utility as

```math
\mathbb{E}[u(V_1)] = \mathbb{E}[u(w_0 R_0 + w_1 R_1)] = (1 - p) \log(w_0 R_0 + w_1 / a_0) + p \log(w_0 R_0)
```

In order to find the optimal solution we need to include the budget constraint as a strict constraint
with parameter $\lambda$ and set the derivatives to zero

```math
\frac{\partial}{\partial w_k} \left\{ -(1 - p) \log(w_0 R_0 + w_1 / a_0) - p \log(w_0 R_0) + \lambda(w_0 + w_1 - V_0) \right\} = 0, \quad k = 0, 1
```

This leads to the system of equations

```math
\begin{aligned}
-\frac{1 - p}{a_0} \cdot \frac{1}{w_0 R_0 + w_1 / a_0} + \lambda &= 0 \\
-\frac{(1 - p) R_0}{w_0 R_0 + w_1 / a_0} - \frac{p}{w_0} + \lambda &= 0.
\end{aligned}
```

Eliminating $\lambda$ yields

```math
\begin{aligned}
\frac{1 - p}{a_0} \cdot \frac{1}{w_0 R_0 + w_1 / a_0} &= \frac{(1 - p) R_0}{w_0 R_0 + w_1 / a_0} + \frac{p}{w_0} \\
\Leftrightarrow \quad \frac{1 - p}{a_0} w_0 &= (1 - p) R_0 w_0 + p(w_0 R_0 + w_1 / a_0) \\
\Leftrightarrow \quad \frac{1 - p}{a_0} w_0 &= R_0 w_0 + p w_1 / a_0 \\
\Leftrightarrow \quad (1 - p) w_0 - R_0 a_0 w_0 &= p w_1 \\
\Leftrightarrow \quad \left( \frac{1 - R_0 a_0}{p} - 1 \right) w_0 &= w_1.
\end{aligned}
```

In addition, we have the budget constraint $w_0 + w_1 = V_0$, so that

```math
w_0 = \frac{V_0 p}{1 - R_0 a_0}
```

```math
w_1 = V_0 \left( 1 - \frac{p}{1 - R_0 a_0} \right).
```

This is the solution for a strict budget constraint. For a soft constraint we need to consider the
parameter $\lambda$, which is obtained explicitly by substituting the solutions for $w_0, w_1$ into Eq. (3.28).
First we obtain

```math
\begin{aligned}
w_0 R_0 + \frac{w_1}{a_0} &= p \cdot \frac{V_0 R_0}{1 - R_0 a_0} + \frac{V_0}{a_0} \left( 1 - \frac{p}{1 - R_0 a_0} \right) \\
&= \frac{V_0}{a_0} + p \left( \frac{V_0 R_0}{1 - R_0 a_0} - \frac{V_0 / a_0}{1 - R_0 a_0} \right) \\
&= \frac{V_0}{a_0} + \frac{p V_0}{a_0} \left( \frac{R_0 a_0}{1 - R_0 a_0} - \frac{1}{1 - R_0 a_0} \right) \\
&= \frac{V_0}{a_0}(1 - p).
\end{aligned}
```

Eq. (3.28) thus yields

```math
\lambda = \frac{1 - p}{a_0} \cdot \frac{1}{w_0 R_0 + w_1 / a_0} = \frac{1}{V_0} > 0.
```

Since $\lambda > 0$ the solution for an exact budget constraint is always optimal, as is expected in the
presence of a risk-free investment. Note that the solution can lead to $w_1 < 0$ for certain parameter
values. This means that we are borrowing money from the risky bond. In practice this is not possible.
Interestingly, the optimal solution requires that as $R_0 \to 1/a_0$, i.e., the return of the risk-free bond
approaches that of the risky one, the investor should invest more and more money into the risk-free
bond by shortselling the risky one. The reason is clear: the risky bond has a non-zero probability of
default in which case you don't have to purchase back the bond, thus making shortselling more and
more advantageous.

Example. (Horse race) Consider a horse race with $n$ horses. You can place bets on different horses
simultaneously, but only one horse can win. The odds for a win of horse $i$ are quoted as $1/q_i$, where
$q_i$ is the price of a bet with payoff 1 in the case of a win and zero otherwise. Since one horse wins
for sure, we will have the payoff 1 for sure if we place simultaneous bets $q_1, \ldots, q_n$. Therefore no
arbitrage requires $\sum_{i=1}^{n} q_i = 1$ (a fair bookmaker). Usually $\sum_{i=1}^{n} q_i > 1$, so that the bookmaker
makes a profit. If you estimate the probability of the $i$th horse winning as $p_i$, how should you place
your bets for a given utility function?

Solution. The portfolio value is $V_1 = \mathbf{w}^T \mathbf{R}$ and the optimization problem is

```math
\begin{aligned}
\text{maximize} \quad & \mathbb{E}[u(V_1)] \\
\text{subject to} \quad & \mathbf{w}^T \mathbf{1} \leq V_0.
\end{aligned}
```

For the horse race the returns $R_i$ are given as

```math
R_i = \begin{cases} 1/q_i, & \text{probability } p_i \\ 0, & \text{probability } 1 - p_i \end{cases}
```

and thus $V_1 = \sum_{j=1}^{n} w_j R_j = w_i / q_i$ if horse $i$ wins. Therefore

```math
\mathbb{E}[u(V_1)] = \sum_{j=1}^{n} u\!\left( \frac{w_j}{q_j} \right) p_j.
```

Solving the optimization problem requires us to consider first the exact budget constraint and set
the partial derivatives of $-\mathbb{E}[u(V_1)] + \lambda(\mathbf{w}^T \mathbf{1} - V_0)$ with respect to the $w_i$ to zero. We obtain

```math
\frac{\partial}{\partial w_i} \left\{ -\mathbb{E}[u(V_1)] + \lambda(\mathbf{w}^T \mathbf{1} - V_0) \right\} = \frac{\partial}{\partial w_i} \left\{ -\sum_{j=1}^{n} u\!\left( \frac{w_j}{q_j} \right) p_j + \lambda \left( \sum_{j=1}^{n} w_j - V_0 \right) \right\} = -u'\!\left( \frac{w_i}{q_i} \right) \frac{p_i}{q_i} + \lambda
```

for $i = 1, \ldots, n$. Let us consider a logarithmic utility function $u(x) = \log(\tau + x)$, which requires
$\tau + x > 0$. Since $u'(x) = 1/(\tau + x)$ we have

```math
u'\!\left( \frac{w_i}{q_i} \right) \frac{p_i}{q_i} = \frac{1}{\tau + w_i / q_i} \cdot \frac{p_i}{q_i} = \frac{p_i}{w_i + \tau q_i} = \lambda,
```

which leads to the solutions

```math
w_i = \frac{p_i}{\lambda} - \tau q_i.
```

In turn, $\lambda$ is determined by substituting the $w_i$ into the budget constraint equation

```math
\sum_{j=1}^{n} w_j = \sum_{j=1}^{n} \frac{p_j}{\lambda} - \tau \sum_{j=1}^{n} q_j = \frac{1}{\lambda} - \tau \sum_{j=1}^{n} q_j = V_0,
```

so that

```math
\lambda = \frac{1}{V_0 + \tau \sum_{j=1}^{n} q_j} > 0.
```

This means the solution for the exact constraint is always optimal. Substituting $\lambda$ yields

```math
w_i = p_i \left( V_0 + \tau \sum_{j=1}^{n} q_j \right) - \tau q_i.
```

This means you bet more money on horse $i$ if the probability of winning is high (large $p_i$) or the
price of the bet is lower than the other bets ($q_i < q_j$).

Example. (Optimum investment problem) Suppose your capital is $x$. You can invest a fraction $\alpha x$
into a risky scheme, $0 \leq \alpha \leq 1$. We may either get $k\alpha x$ out of this investment, or loose $\alpha x$. That
is to say, $V_1$ is either $x + k\alpha x$ with probability $p$, or $x - \alpha x$ with probability $1 - p$. What is the
optimum fraction $\alpha$ that I should invest?

Solution. Maximize $\mathbb{E}[u(V_1)]$ as a function of $\alpha$.

```math
\mathbb{E}[u(V_1)] = p \, u(x + k\alpha x) + (1 - p) \, u(x - \alpha x).
```

The answer will depend on the chosen utility function. To find the maximum, simply differentiate
with respect to $\alpha$.

---

# Chapter 4: Stochastic Calculus

## The standard definition of an integral

Let us recall the standard definition of the integral $\int_a^b f(x)\,dx$, where $f : [a, b] \to \mathbb{R}$ is a real valued
function on $[a, b]$. To define the integral we need the following construction.

1.  Choose any $n - 1$ (interior) points from $[a, b]$ such that

```math
a = x_0 < x_1 < \ldots < x_{n-1} < x_n = b.
```

2.  Consider the integral sum $\sum_{i=0}^{n-1} f(\xi_i)\Delta x_i$, where $\Delta x_i = x_{i+1} - x_i$ and $\xi_i \in [x_i, x_{i+1}]$ (and is
    arbitrary otherwise).

3.  Set $\delta = \max_{0 \leq i \leq n-1} \Delta x_i$.

4.  Finally, the integral of the function $f(x)$ over $[a, b]$ is, by definition, the limit of the integral
    sum (if this limit exists):

```math
\int_a^b f(x)\,dx \overset{\text{def}}{=} \lim_{\delta \to 0} \sum_{i=0}^{n-1} f(\xi_i)\Delta x_i
```

**Theorem 4.1.1.** If $f(x)$ is a continuous function on $[a, b]$, then the limit $\lim_{\delta \to 0} \sum_{i=0}^{n-1} f(\xi_i)\Delta x_i$
exists (and does not depend on the choice of $x_i$, $\xi_i$, $0 \leq i \leq n$).

## Stochastic integrals (the Ito integrals)

Before we define the stochastic integral (also called the Ito integral) we have to recall several
properties of normal random variables and of the Wiener process which will play a very important
role in the study of these integrals.

1.  If $Z_1, Z_2, \ldots, Z_n$ are independent normal random variables, $Z_i \sim \mathcal{N}(\mu_i, \sigma_i^2)$, then

```math
\sum_{i=1}^{n} Z_i \sim \mathcal{N}\!\left( \sum_{i=1}^{n} \mu_i,\; \sum_{i=1}^{n} \sigma_i^2 \right).
```

2.  As usual, we denote by $W(t) \equiv W_t$ the standard Wiener process. By the definition of the
    Wiener process the following properties hold:
    1.  $W(0) = 0$

    2.  $W(t + s) - W(t) \sim \mathcal{N}(0, s)$ if $s > 0$.
    3.  Let $t_0 = 0 < t_1 < t_2 < \cdots < t_{n-1} < t_n = t$ be any points from the interval $[0, t]$. Set

```math
\Delta W_i = W(t_{i+1}) - W(t_i),\quad i = 0, 1, \ldots, n-1 \quad \text{and} \quad \Delta t_i = t_{i+1} - t_i.
```

Then $\Delta W_i$, $i = 0, 1, \ldots, n-1$ are independent normal random variables, $\Delta W_i \sim \mathcal{N}(0, \Delta t_i)$.

Our goal is to define

1.  $\int_0^t f(s)\,dW_s$, where $f(s)$ is a "usual" function (not random). This is a relatively simple case
    of a stochastic integral.

2.  $\int_0^t f(W_s)\,dW_s$ - the stochastic integral of a function of a Wiener process which is a somewhat
    more complicated case.

### Stochastic integral $\int_0^t f(s)\,dW_s$

**Definition 4.2.1.** Let $t_0 = 0 < t_1 < t_2 < \cdots < t_n = t$ be a sequence of points in $[0, t]$ and define
$\delta = \max_i \Delta t_i$. Then

```math
\int_0^t f(s)\,dW_s = \lim_{\delta \to 0} \sum_{i=0}^{n-1} f(t_i)\Delta W_i
```

if this limit exists.

**Theorem 4.2.2.** If $f(x)$ is differentiable and $f'(x)$ is a continuous function then the limit
exists.

    Let us consider several simple examples.

**Example 4.2.3.** $f(x) = c$ (constant), then

```math
\int_0^t c\,dW_s = \lim_{\max_i \Delta t_i \to 0} \sum_{i=0}^{n-1} c\,\Delta W_i = c \lim_{\max_i \Delta t_i \to 0} \sum_{i=0}^{n-1} \Delta W_i
```

where as above $\Delta W_i = W(t_{i+1}) - W(t_i)$. Since

```math
\sum_{i=0}^{n-1} \Delta W_i = (W(t_1) - W(t_0)) + (W(t_2) - W(t_1)) + \cdots + (W(t_n) - W(t_{n-1})) = W(t_n) - W(t_0) = W(t)
```

we see that $\lim_{\max_i \Delta t_i \to 0} \sum_{i=0}^{n-1} \Delta W_i = \sum_{i=0}^{n-1} \Delta W_i = W(t)$ and therefore

```math
\int_0^t c\,dW_s = c\,W(t).
```

**Remark 4.2.4.** Always remember the identity

```math
\sum_{i=0}^{n-1} (b_{i+1} - b_i) = (b_1 - b_0) + (b_2 - b_1) + \cdots + (b_n - b_{n-1}) = b_n - b_0.
```

We use it in the above example with $b_i = W(t_i)$.

**Example 4.2.5.**

```math
f(x) = \begin{cases} 1, & 0 \leq x < 1.5, \\ -1, & 1.5 \leq x \leq 2. \end{cases}
```

Then

```math
\int_0^2 f(s)\,dW_s = \int_0^{1.5} f(s)\,dW_s + \int_{1.5}^2 f(s)\,dW_s = \int_0^{1.5} dW_s - \int_{1.5}^2 dW_s = W(1.5) - (W(2) - W(1.5)) = 2W(1.5) - W(2)
```

We use $\int_a^b dW_s = W(b) - W(a)$.

**Question:** What is the distribution of this integral? Denote $Y \equiv W(1.5) - (W(2) - W(1.5))$?

**Answer:** Since $W(1.5) \sim \mathcal{N}(0, 1.5)$, $W(2) - W(1.5) \sim \mathcal{N}(0, 0.5)$ and these random variables
are independent, their difference $Y \sim \mathcal{N}(0, 2)$. (This is a particular case of (4.1). Explain this
statement.)

**Exercise 4.2.6.**

```math
f(x) = \begin{cases} 1, & 0 \leq x < 1, \\ 2, & 1 \leq x < 1.5, \\ -1.5, & 1.5 \leq x \leq 3. \end{cases}
```

What is the distribution of $\int_0^3 f(s)\,dW_s$?

### The Distribution of the Stochastic Integral $\int_0^t f(s)\,dW_s$

The integral $\int_0^t f(s)\,dW_s$ is a random variable because it is defined as a limit of a sum of random
variables.
Question What is the distribution of this random variable?
It is remarkable that this question has a simple answer. Namely, our next theorem states that
this random variable has a normal distribution and, moreover, it is relatively easy to compute the
parameters of this distribution. We shall see later that this fact plays a very important role in
constructing solutions to some it turns out questions arising in financial mathematics.
**Theorem 4.2.7.**

```math
\int_0^t f(s)\,dW_s \sim \mathcal{N}\!\left(0,\; \int_0^t (f(s))^2\,ds\right).
```

_Proof._ By the definition of a limit,

```math
\int_0^t f(s)\,dW_s \approx \sum_{i=0}^{n-1} f(t_i)\Delta W_i
```

Since $\Delta W_i$ are independent random variables and $\Delta W_i = W(t_{i+1}) - W(t_i) \sim \mathcal{N}(0, \Delta t_i)$ the random
variables $f(t_i)\Delta W_i$ also are independent and $f(t_i)\Delta W_i \sim \mathcal{N}(0, f(t_i)^2 \Delta t_i)$.
(Note that the last statement makes use of the fact that $f(t_i)$ are not random variables!)
Next, due to property (4.1) we conclude that

```math
\sum_{i=0}^{n-1} f(t_i)\Delta W_i \sim \mathcal{N}\!\left(0,\; \sum_{i=0}^{n-1} f(t_i)^2 \Delta t_i\right).
```

But, by Theorem 4.1.1,

```math
\lim_{\max_i \Delta t_i \to 0} \sum_{i=0}^{n-1} f(t_i)^2 \Delta t_i = \int_0^t f(s)^2\,ds
```

which finishes the proof.

**Exercise 4.2.8.** Find the distributions of the random variables defined in the examples of the previous
section.

### Stochastic Integrals of Functions of the Wiener Process: $\int_0^t f(W_s)\,dW_s$ and $\int_0^t f(s, W_s)\,dW_s$

As before, let $0 = t_0 < t_1 < \cdots < t_{n-1} < t_n = t$ and $\delta = \max_{0 \leq i \leq n-1}(t_{i+1} - t_i)$.

**Definition 4.2.9.** Let $f : \mathbb{R} \to \mathbb{R}$ be a function. If the limit $\lim_{\delta \to 0} \sum_{i=0}^{n-1} f(W(t_i))\Delta W_i$ exists,
then we say that

```math
\int_a^b f(W_t)\,dW_t = \lim_{\delta \to 0} \sum_{i=0}^{n-1} f(W(t_i))\Delta W_i.
```

Similarly, we define $\int_a^b f(t, W_t)\,dW_t$ by

```math
\int_a^b f(t, W_t)\,dW_t = \lim_{\delta \to 0} \sum_{i=0}^{n-1} f(t_i, W(t_i))\Delta W_i,
```

if the limit in (4.5) exists.

**Theorem 4.2.10.** Suppose that the function $f : \mathbb{R} \to \mathbb{R}$ is bounded and continuous. Then the limit
in (4.4) exists.

**Remark 4.2.11.** The existence of integrals (4.4) and (4.5) can be proved under much milder
conditions. However, in this course, we don't discuss them.

The just defined integral is of course again a random variable. But unlike in Theorem 4.2.7, it
may be very difficult to find the distribution of this random variable.
We finish this section by stating two properties of these stochastic integrals.

**Theorem 4.2.12.**

```math
\mathbb{E}\!\left[\int_a^b f(W_t)\,dW_t\right] = 0 \quad \text{and} \quad \mathbb{E}\!\left[\int_a^b f(t, W_t)\,dW_t\right] = 0
```

```math
\operatorname{Var}\!\left(\int_a^b f(W_t)\,dW_t\right) = \int_a^b \mathbb{E}[f(W_t)^2]\,dt \quad \text{and} \quad \operatorname{Var}\!\left(\int_a^b f(t, W_t)\,dW_t\right) = \int_a^b \mathbb{E}[f(t, W_t)^2]\,dt.
```

    Explanation
    First, let us introduce notations which will make our calculation less cumbersome. We set

Wi ≡ W (ti ) , fi ≡ f (Wi ) , ∆Wi ≡ W (ti+1 ) − W (ti ).
Since Wi and ∆Wi are independent, also the random variables fi = f (W (ti )) and ∆Wi are
independent. Hence

                       E(fi ∆Wi ) = E(fi ) × E(∆Wi ) = 0 because E(∆Wi ) = 0.

It is now obvious that
n−1 n−1
!
X X
E fi ∆Wi = E (fi ∆Wi ) = 0
i=0 i=0
R P  
 b n−1
and (4.6) follows because E a f (Wt )dWt = limδ→0 E i=0 f (W (ti ))∆Wi .
To explain (4.7), note that if i < j then

           Cov(fi ∆Wi , fj ∆Wj ) = E[fi ∆Wi × fj ∆Wj ] = E[fi ∆Wi fj ] × E(∆Wj ) = 0

where the expectation factorizes because ∆Wj is independent of the other three random variables.
We thus have that
n−1
! n−1
X X
Var f (Wi )∆Wi = Var(fi ∆Wi )
i=0 i=0
n−1
X n−1
X
= E(fi2 ∆Wi2 ) = E(fi2 ) × E(∆Wi2 )
i=0 i=0
n−1
X
= E(fi2 ) × ∆ti
i=0
Rb 2
The last sum converges,
as δ → 0, P a E[(f (Wt ) ]dt and
to this implies (4.7) because
Rb n−1
Var a f (Wt )dWt = limδ→0 Var i=0 f (W (ti ))∆Wi .

**Remark 4.2.13.** 1. In the above computation, we use E[∆Wi2 ] = ti+1 − ti = ∆ti . 2. We use the following fact which you are supposed to know from second year probability
courses: if X1 , ..., Xn are such that Cov(Xi , Xj ) = 0 when i ̸= j then
n n
!
X X
Var Xi = Var(Xi ).
i=1 i=1

## The 'usual' differential of a function

Suppose $F(x)$ is a function $F : \mathbb{R} \to \mathbb{R}$ and $F'(x)$ is continuous.

**Definition 4.3.1.**

```math
dF(x) = F'(x)\,dx \qquad (\text{here } dx \text{ is "small"}).
```

Explanation: $dF(x)$ is the linear part of the increment $\Delta F(x) = F(x + \Delta x) - F(x)$. By the Taylor formula,

```math
F(x + dx) = F(x) + F'(x)\,dx + \frac{1}{2}F''(\theta)\,dx^2,
```

where $\theta$ is an (unknown) point in $(x, x + dx)$ if $dx > 0$ and $\theta \in (x + dx, x)$ if $dx < 0$.
The important fact is that the difference between $\Delta F(x) = F(x + dx) - F(x)$ and $dF(x) = F'(x)\,dx$ is much smaller than $dx$ (when $dx$ is a small number). More precisely,

```math
\frac{\Delta F(x) - dF(x)}{dx} \to 0 \quad \text{as } dx \to 0.
```

Indeed, it follows from (4.12) that $\Delta F(x) - dF(x) = F(x + dx) - F(x) - F'(x)\,dx = \tfrac{1}{2}F''(\theta)\,dx^2$ and hence

```math
\frac{\Delta F(x) - dF(x)}{dx} = \frac{1}{2}F''(\theta)\,dx \to 0 \quad \text{as } dx \to 0.
```

**Example 4.3.2.** $F(x) = \sqrt{x}$. Then $F(1) = 1$, $F'(x) = \tfrac{1}{2}x^{-1/2}$, $F'(1) = \tfrac{1}{2}$.

```math
\Delta F(1) = F(1 + dx) - F(1) \simeq F'(1)\,dx.
```

Since $F(x + dx) - F(x) \simeq dF(x)$, we have

```math
F(1 + 0.05) = F(1) + dF(1), \qquad (\text{with } dx = 0.05).
```

That is

```math
\sqrt{1 + 0.05} \simeq 1 + dF(1) = 1 + \frac{0.05}{2} = 1.025.
```

Remark: $\Delta x = dx$. Indeed, in this case $F(x) = x$, $F'(x) = 1$ and $\Delta F(x) = \Delta x = x + dx - x = dx$.

## The stochastic case

Question: What is $dF(W_t)$? Here $F : \mathbb{R} \to \mathbb{R}$ and $W_t$ is the standard Wiener process.

### Ito's formula for $F(W_t)$

Note that if $g(x)$ is a differentiable function, then

```math
dF(g(x)) = F'(g(x))\,g'(x)\,dx
```

However

```math
dF(W(t)) \neq F'(W(t))\,\frac{dW(t)}{dt}\,dt,
```

since the derivative $\frac{dW(t)}{dt}$ does not exist.

Next, (4.13) can be rewritten as

```math
dF(g(x)) = F'(g(x))\,dg(x), \qquad \text{since } dg(x) = g'(x)\,dx.
```

Can we state that $dF(W(t)) = F'(W(t))\,dW(t)$?

The answer is NO! The correct answer is given by Ito's lemma.

**Lemma 4.4.1.** (Ito's lemma) Let $F(x)$ be a function $F : \mathbb{R} \to \mathbb{R}$ which has two derivatives $F'(x)$, $F''(x)$ and $F''(x)$ is continuous. Then

```math
dF(W_t) = F'(W_t)\,dW_t + \frac{1}{2}F''(W_t)\,dt.
```

**Remark 4.4.2.** By definition, $dW_t \equiv \Delta W_t \equiv W(t + dt) - W(t)$.

Explanation: The main explanation of the Ito formula is due to the following theorem.

**Theorem 4.4.3.** Suppose that $F(x)$ has two continuous and bounded derivatives: $F'(x)$, $F''(x)$. Then

```math
F(W(b)) - F(W(a)) = \int_a^b F'(W_s)\,dW_s + \frac{1}{2}\int_a^b F''(W_s)\,ds.
```

(Note: we shall not prove this theorem but you are supposed know this statement.)

Let us now compare (4.16) with the following relation which you have discussed in the Calculus courses. Namely, you know of course that

```math
F(b) - F(a) = \int_a^b F'(x)\,dx.
```

Moreover, if a function $g(x)$, $g : \mathbb{R} \mapsto \mathbb{R}$, has a continuous derivative $g'(x)$ then

```math
F(g(b)) - F(g(a)) = \int_a^b F'(g(x))\,g'(x)\,dx = \int_a^b F'(g(x))\,dg(x) \qquad (\text{since } dg(x) = g'(x)\,dx).
```

However, (4.16) tells us that

```math
F(W(b)) - F(W(a)) \neq \int_a^b F'(W_t)\,dW_t.
```

(And this happens because $W'(t)$ does not exist!)

### One useful corollary of the Ito formula

**Corollary 4.4.4.** Equation (4.16) can be rearranged as follows:

```math
\int_a^b F'(W_s)\,dW_s = F(W(b)) - F(W(a)) - \frac{1}{2}\int_a^b F''(W_s)\,ds.
```

**Example 4.4.5.** $\int_a^b dW_s = W_b - W_a$. Here $F(x) = x$, $F(W_t) = W_t$, $F'(W_t) = 1$. So

```math
\int_a^b F'(W_s)\,dW_s = \int_a^b dW_s = W_b - W_a.
```

This is a particular case of (4.17).

**Example 4.4.6.** $F(x) = x^2$. We have $F'(x) = 2x$, $F''(x) = 2$ and so (4.17) now reads

```math
\int_a^b 2W_s\,dW_s = W_b^2 - W_a^2 - \frac{1}{2}\int_a^b 2\,ds = W_b^2 - W_a^2 - (b - a).
```

In particular,

```math
\int_0^t W_s\,dW_s = \frac{1}{2}W_t^2 - \frac{1}{2}t.
```

**IMPORTANT CONCLUSION**

We know that, by definition,

```math
\int_0^t f(W_s)\,dW_s = \lim_{\max_i \Delta t_i \to 0} \sum_{i=0}^{n-1} f(W_i)\,\Delta W_i.
```

To compute this stochastic integral in terms of the ordinary integral one can do the following:

1. Find $F(x)$ such that $F'(x) = f(x)$.
2. Then $\int_0^t f(W_s)\,dW_s = F(W_t) - F(0) - \frac{1}{2}\int_0^t f'(W_s)\,ds$.

This is what we did in the examples considered above.

**Exercise 4.4.7.** Compute the following stochastic integrals:

(a) $\int_0^t W_s^3\,dW_s$

(b) $\int_0^t e^{W_s}\,dW_s$

### One more explanation of Ito's formula

The material of this subsection is not examinable. It is here for those who want to know more. By Taylor's formula,

```math
F(x + dx) - F(x) = F'(x)\,dx + \frac{1}{2}F''(x)\,dx^2 + \frac{1}{3!}F^{(3)}(\theta)\,dx^3
```

As usual, $\theta$ is not known but this does not matter since we suppose that $F^{(3)}(x) = F'''(x)$ is bounded: $|F^{(3)}(x)| < \text{Constant}$. We can use (4.18) (taking into account that $W(t + dt) = W(t) + dW(t)$) to obtain

```math
F(W_t + dW_t) - F(W_t) = F'(W_t)\,dW_t + \frac{1}{2}F''(W_t)\,dW_t^2 + \frac{1}{3!}F^{(3)}(\theta)\,(dW_t)^3.
```

Note that $\mathbb{E}(dW_t^2) = \mathbb{E}((W_{t+dt} - W_t)^2) = dt$ (by the definition of the Wiener process). Note also that $\mathbb{E}(|dW_t|^3) = c\,(dt)^{3/2}$, where $c$ is a constant.

So Ito's lemma (see Lemma 4.4.1) does the following: it tells us that we can replace $dW_t^2$ in (4.19) by $dt$ and we can drop $(dW_t)^3$ since the expectation of $|dW_t|^3$ is much smaller than $dt$.
**Exercise 4.4.8.** Compute $\mathbb{E}(|dW_t|^3)$. Thus show that $c = 2\sqrt{\tfrac{2}{\pi}}$.

Hint: $\mathbb{E}(|dW_t|^3) = \int_{-\infty}^{\infty} |x|^3 f_{dW_t}(x)\,dx$. It is convenient to write $h$ for $dt$ (that is $h = dt$) and $W(t+h) - W(t)$ for $dW_t$. So

```math
f_{W(t+h)-W(t)}(x) = \frac{1}{\sqrt{2\pi h}}\,e^{-\frac{x^2}{2h}}.
```

Setting $y = \frac{x}{\sqrt{h}}$ (change of variable), we obtain

```math
\int_0^{\infty} x^3 \frac{1}{\sqrt{2\pi h}}\,e^{-\frac{x^2}{2h}}\,dx = \frac{1}{\sqrt{2\pi}}\,h^{3/2}\int_0^{\infty} y^3\,e^{-y^2/2}\,dy = h^{3/2}\,\frac{1}{\sqrt{2\pi}}\int_0^{\infty} y^3\,e^{-y^2/2}\,dy = \sqrt{\frac{2}{\pi}}\,h^{3/2}
```

Thus $\mathbb{E}(|dW_t|^3) = 2\int_0^{\infty} x^3 f_{dW_t}(x)\,dx = 2\sqrt{\tfrac{2}{\pi}}\,(dt)^{3/2}$. So $c = 2\sqrt{\tfrac{2}{\pi}}$.

### Ito's formula for $F(t, W_t)$

Let $F(t, x)$ be a function of $t$ and $x$, $F : \mathbb{R}^2 \to \mathbb{R}$.

**Lemma 4.4.9.** (Ito's formula for $F(t, W_t)$)

```math
dF(t, W_t) = \left(\frac{\partial F(t, W_t)}{\partial t} + \frac{1}{2}\frac{\partial^2 F(t, W_t)}{\partial W_t^2}\right)dt + \frac{\partial F(t, W_t)}{\partial W_t}\,dW_t
```

**Remarks 4.4.10.**

1. Here and throughout the rest of the course, we assume that all the derivatives we need exist, are continuous functions, and have all the properties we may want them to have.

2. Even though the notations we use in (4.20) should be easy to understand, here is an additional explanation of their meaning:

```math
\frac{\partial F(t, W_t)}{\partial W_t} = \left.\frac{\partial F(t, x)}{\partial x}\right|_{x=W_t}, \qquad \frac{\partial^2 F(t, W_t)}{\partial W_t^2} = \left.\frac{\partial^2 F(t, x)}{\partial x^2}\right|_{x=W_t}.
```

**Example 4.4.11.** $F(t, x) = t^2 + x^2$. We have $\frac{\partial F}{\partial t} = 2t$, $\frac{\partial F}{\partial x} = 2x$, $\frac{\partial^2 F}{\partial x^2} = 2$. So

```math
dF(t, W_t) = (2t + 1)\,dt + 2W_t\,dW_t.
```

### The chain rule

Suppose that $Y_t$ is a stochastic process and that

```math
dY_t = a(t, Y_t)\,dt + \sigma(t, Y_t)\,dW_t,
```

where $a$ and $\sigma$ are "good" functions. Then

```math
dF(t, Y_t) = \left(\frac{\partial F}{\partial t} + \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial Y_t^2} + a\frac{\partial F}{\partial Y_t}\right)dt + \sigma\frac{\partial F}{\partial Y_t}\,dW_t.
```

Here

```math
\frac{\partial F}{\partial t} \equiv \frac{\partial F(t, Y_t)}{\partial t}, \qquad \frac{\partial F}{\partial Y_t} \equiv \frac{\partial F(t, Y_t)}{\partial Y_t}, \qquad \frac{\partial^2 F}{\partial Y_t^2} \equiv \frac{\partial^2 F(t, Y_t)}{\partial Y_t^2}.
```

Note that Ito's formula for $F(t, W_t)$ is a particular case of the Chain rule:

```math
dF(t, W_t) = \left(\frac{\partial F}{\partial t} + \frac{1}{2}\frac{\partial^2 F}{\partial W_t^2}\right)dt + \frac{\partial F}{\partial W_t}\,dW_t.
```

### How to remember (4.22) and similar formulae?

1.  Know Taylor's formula up to order 2:

```math
dF(t, x) = \frac{\partial F}{\partial t}\,dt + \frac{\partial F}{\partial x}\,dx + \frac{1}{2}\frac{\partial^2 F}{\partial x^2}\,dx^2 + \frac{\partial^2 F}{\partial x\,\partial t}\,dx\,dt + \frac{1}{2}\frac{\partial^2 F}{\partial t^2}\,dt^2.
```

    Here $\frac{\partial F}{\partial t} \equiv \frac{\partial F(t,x)}{\partial t}$, $\frac{\partial F}{\partial x} \equiv \frac{\partial F(t,x)}{\partial x}$, ...

2.  Use the following formal rules when you replace $x$ by $W_t$ or $Y_t$:

    (a) $dW_t^2 = dt$;

    (b) $dt\,dW_t = 0$, $dt^2 = 0$.

**Example 4.4.12.** Replace $x$ in (4.23) by $W_t$. Then

```math
dF(t, W_t) = \frac{\partial F}{\partial t}\,dt + \frac{\partial F}{\partial W_t}\,dW_t + \frac{1}{2}\frac{\partial^2 F}{\partial W_t^2}\,dt + 0 + 0 = \left(\frac{\partial F(t, W_t)}{\partial t} + \frac{1}{2}\frac{\partial^2 F(t, W_t)}{\partial W_t^2}\right)dt + \frac{\partial F(t, W_t)}{\partial W_t}\,dW_t
```

which is Ito's lemma for $F(t, W_t)$.

**Example 4.4.13.** Replace $x$ in (4.23) by $Y_t$. Note that, according to the second rule

```math
(dY_t)^2 = a^2\,dt^2 + 2a\sigma\,dt\,dW_t + \sigma^2\,dW_t^2 = \sigma^2\,dt.
```

Here we use equation (4.21). So

```math
\begin{aligned}
dF(t, Y_t) &= \frac{\partial F}{\partial t}\,dt + \frac{\partial F}{\partial Y_t}\,dY_t + \frac{1}{2}\frac{\partial^2 F}{\partial Y_t^2}\,dY_t^2 + 0 + 0 \\
&= \frac{\partial F}{\partial t}\,dt + \frac{\partial F}{\partial Y_t}(a\,dt + \sigma\,dW_t) + \frac{1}{2}\frac{\partial^2 F}{\partial Y_t^2}\,\sigma^2\,dt
\end{aligned}
```

Hence the chain rule:

```math
dF(t, Y_t) = \left(\frac{\partial F}{\partial t} + \frac{\partial F}{\partial Y_t}\,a + \frac{1}{2}\frac{\partial^2 F}{\partial Y_t^2}\,\sigma^2\right)dt + \sigma\frac{\partial F}{\partial Y_t}\,dW_t.
```

**Exercise 4.4.14.** Compute $dF(t, g(W_t))$.

Remark: The (4.24) above contains two zeros. This is because

```math
dt\,dY_t = dt \cdot (a\,dt + \sigma\,dW_t) = 0 \quad \text{and} \quad dt^2 = 0
```

So

```math
\frac{\partial^2 F(t, Y_t)}{\partial t\,\partial Y_t}\,dt\,dY_t = 0 \quad \text{and} \quad \frac{\partial^2 F(t, Y_t)}{\partial t^2}\,dt^2 = 0
```

## Stochastic differential equations

**Definition 4.5.1.** A stochastic differential equation (SDE) is the equation of the form

```math
dY_t = a(t, Y_t) \, dt + \sigma(t, Y_t) \, dW_t,
```

where $a(t, Y_t)$, $\sigma(t, Y_t)$ are given (random) functions and $Y_t = Y(t)$ is an unknown random process.
Remark We have seen (4.25) before: equation (4.21).

**Definition 4.5.2.** We say that $Y(t)$ is a solution to (4.25) with initial value $Y(0)$, if for $t \geq 0$

```math
Y(t) = Y(0) + \int_0^t a(s, Y_s) \, ds + \int_0^t \sigma(s, Y_s) \, dW_s.
```

Terminological remarks:

- $Y(t)$ solving (4.25) is said to be a diffusion process.
- $a(t, Y_t)$ is called the drift and $\sigma(t, Y_t)$ is the volatility of the diffusion process.
- Note that (4.26) is obtained from (4.25) by integrating both parts of (4.25). If $\sigma \equiv 0$, then it becomes $dY_t = a(t, Y_t) \, dt$ and is equivalent to $Y_t' = a(t, Y_t)$ — the ordinary differential equation (but still, $Y(t)$ is a random process if $a$ is a random process).

### Simple examples of SDEs

**Example 4.5.3.** The following relation is the simplest example of a SDE

```math
dY_t = dW_t, \quad Y(0) = 0.
```

Then $Y_t = Y(0) + \int_0^t dW_s = W_t - W_0 = W_t$. Thus $Y_t$ in this case is the Wiener process.

**Example 4.5.4.**

```math
dY_t = \mu \, dt + \sigma \, dW_t, \quad Y(0) = 1,
```

where $\mu$ and $\sigma$ are constants. Then

```math
Y(t) = Y(0) + \int_0^t \mu \, ds + \int_0^t \sigma \, dW_s
```

and we obtain

```math
Y(t) = 1 + \mu t + \sigma W_t,
```

which is the Brownian motion starting from 1.

**Exercise 4.5.5.** $dY_t = e^{-t} \, dt + 2t \, dW_t$. State the distribution of $Y_t$ if $Y(0) = -1$.

**Exercise 4.5.6.** $dY_t = e^{-t} \, dt + 2t \, dW_t$. Find $d(Y_t^2)$.

## Important examples of stochastic differential equations

### The stochastic differential equation for the price of a share

Let $S(t)$ be a random process describing the price of a share. How does the difference between $S(t)$
and $S(t + dt)$ behave?
A simple model for $dS(t) = S(t + dt) - S(t)$ is

```math
dS(t) = S(t) \cdot a \, dt + S(t) \cdot \xi(dt),
```

where $a$ is a parameter (usually $a > 0$) and $\xi(dt)$ is a random "noise". The term $S(t) \cdot a \, dt$
pushes the price up, while $\xi(dt)$ may be $\geq 0$ or $< 0$. We choose $\xi(dt) = \sigma \, dW_t$, where $W_t$ is the
standard Wiener process and $\sigma$ is a constant (which may be negative). Then we obtain the following
stochastic differential equation (SDE):

```math
dS(t) = a S(t) \, dt + \sigma S(t) \, dW_t
```

Assuming that $S(0) = S_0$ is given, how do we solve this SDE?

The first solution to

**Theorem 4.6.1.** The solution to (4.28) is given by

```math
S_t = S_0 \exp\!\left[\left(a - \frac{\sigma^2}{2}\right)t + \sigma W_t\right].
```

_Proof._ Rewrite (4.28) as follows:

```math
\frac{dS_t}{S_t} = a \, dt + \sigma \, dW_t \quad \text{with } S(0) = S_0
```

Note that the left hand side of (7.3) resembles the differential $d \ln S(t)$ (but in fact it is not equal
to this differential as will be seen below). So, let us compute $d \ln S(t)$ using the chain rule version
of Ito's lemma.
Recall that the differential of a function $F(S_t)$ (which is good enough, say has two continuous
derivatives) can be computed as follows:

```math
dF(S_t) = F'(S_t) \, dS_t + \frac{1}{2} F''(S_t) \, (dS_t)^2.
```

In our case $F(x) = \ln x$ and so $F'(x) = \frac{1}{x}$, $F''(x) = -\frac{1}{x^2}$ and $(dS_t)^2 = \sigma^2 S_t^2 \, dt$.
Hence

```math
\begin{aligned}
d \ln(S_t) &= \frac{1}{S_t}(a S_t \, dt + \sigma S_t \, dW_t) - \frac{1}{2} \cdot \frac{1}{S_t^2} \cdot \sigma^2 S_t^2 \, dt \\
&= \left(a - \frac{\sigma^2}{2}\right) dt + \sigma \, dW_t.
\end{aligned}
```

Remark. We now see that indeed $d \ln(S_t) \neq a \, dt + \sigma \, dW_t$.
Integrating both parts of the last display formula, we obtain

```math
\int_0^t d \ln(S_u) = \int_0^t \left[\left(a - \frac{\sigma^2}{2}\right) du + \sigma \, dW_u\right] = \left(a - \frac{\sigma^2}{2}\right)t + \sigma W_t
```

and hence

```math
\ln(S_t) - \ln(S_0) = \left(a - \frac{\sigma^2}{2}\right)t + \sigma W_t
```

or, equivalently,

```math
\frac{S_t}{S_0} = e^{\left(a - \frac{\sigma^2}{2}\right)t + \sigma W_t} \quad \text{and} \quad S_t = S_0 \exp\!\left[\left(a - \frac{\sigma^2}{2}\right)t + \sigma W_t\right].
```

A random variable distributed as $e^X$, where $X \sim \mathcal{N}(\mu, \sigma^2)$ is said to have $\text{LogNormal}(\mu, \sigma^2)$
distribution. Thus, $S_t \sim \text{LogNormal}\!\left((a - \sigma^2/2)t, \, \sigma^2 t\right)$. The process $S_t$ is said to be Geometric
Brownian Motion with drift parameter $a$ and volatility parameter $\sigma$. We often denote the drift
parameter by $\mu$ instead of $a$.

![Wiener Process and Geometric Brownian Motion](../images/wiener_gbm.png)

The second solution to
This approach to solving (4.28) is slightly more difficult than the first one. It can be viewed as a
useful exercise illustrating one more way in which the Ito formula can be used.
Plan: the main steps of the second solution.

1.  Suppose that $S(t)$ can be found in the form $S(t) = f(t, W_t)$, where $f(t, x)$ is a function of
    two variables, $t$ and $x$.

2.  Use Ito's lemma and substitute $S(t)$ in (4.28) by $f(t, W_t)$ and $dS(t)$ by $df(t, W_t)$.

3.  Then see whether you can find $f(t, x)$.

**Theorem 4.6.2.** $f(t, x) = S_0 e^{\mu t + \sigma x}$, where $\mu = a - \frac{\sigma^2}{2}$ and $S_0 = S(0)$.

_Proof._ Step 1. By Ito's lemma,

```math
df(t, W_t) = \left[\frac{\partial f(t, W_t)}{\partial t} + \frac{1}{2} \frac{\partial^2 f(t, W_t)}{\partial W_t^2}\right] dt + \frac{\partial f(t, W_t)}{\partial W_t} \, dW_t
```

Substituting the left side of (4.28) by (4.30) we get

```math
\left[\frac{\partial f}{\partial t} + \frac{1}{2} \frac{\partial^2 f}{\partial W_t^2}\right] dt + \frac{\partial f}{\partial W_t} \, dW_t = a f \, dt + \sigma f \, dW_t,
```

where we write $f$ for $f(t, W_t)$. Equating the coefficients in front of $dW_t$ in both sides of (4.31), we
get

```math
\frac{\partial f(t, W_t)}{\partial W_t} = \sigma f(t, W_t)
```

Rewrite (4.32) as

```math
f_x'(t, x) = \sigma f(t, x)
```

We use here the notation $f_x' = \frac{\partial f}{\partial x}$. Fix $t$, then (4.33) is the simplest linear equation (known to you
from the course Differential Equations). It has the general solution of the form

```math
f(t, x) = c(t) e^{\sigma x}.
```

Remark: you can check this by substituting this expression into (4.33). Do it!
Note that $c(t)$ in (4.34) is an unknown function of $t$. It remains to find it.
Step 2. To find $c(t)$, we shall use another relation which follows from (4.31). Namely, we equate
the coefficients in front of $dt$ on both sides of (4.31) and get

```math
f_t'(t, x) + \frac{1}{2} f_{xx}''(t, x) = a f(t, x).
```

Next, it follows from (4.34) that

```math
f_t'(t, x) = c'(t) e^{\sigma x}
```

```math
f_{xx}''(t, x) = \sigma^2 c(t) e^{\sigma x}
```

Substituting (4.36) and (4.37) into (4.35) we get

```math
c'(t) e^{\sigma x} + \frac{1}{2} \sigma^2 c(t) e^{\sigma x} = a \, c(t) e^{\sigma x}
```

and so

```math
c'(t) = \left(a - \frac{\sigma^2}{2}\right) c(t)
```

which is the same type of equation as before. Hence $c(t) = c_0 e^{\left(a - \frac{\sigma^2}{2}\right)t}$, where $c_0 = c(0)$. Finally,

```math
f(t, x) = c_0 e^{\mu t + \sigma x}, \quad \text{where } \mu = a - \frac{\sigma^2}{2}.
```

We have thus proved that $S(t)$ can be found in the form $S(t) = f(t, W_t)$, namely:

```math
S(t) = f(t, W_t) = c_0 e^{\mu t + \sigma W_t}.
```

Since $S(0) = c_0$, we get $c_0 = S_0$ and finally

```math
S(t) = S_0 e^{\mu t + \sigma W_t}.
```

**Remarks 4.6.3.** 1. We use the following fact: if $y'(x) = \alpha y(x)$ then $y(x) = c e^{\alpha x}$, where $c$ is a constant.

2. If $c$ in (4.40) depends on, say, $t$ (as in (4.34)) then this means that we are, for some reason,
   considering a "family of solutions" with $t$ being the parameter of the family.
3. (4.39) and (4.40) were used to solve (4.33) and (4.38). They will be used also in the next
   example.

### The Ornstein-Uhlenbeck process (OUP)

**Definition 4.6.4.** We say that $r(t)$ is the OUP if

```math
dr = -a(r - \mu)\,dt + \sigma\,dW_t
```

where $a$, $\mu$, $\sigma$ are the parameters of the model.
In our applications, the parameters $a$, $\mu$, and $\sigma$ will be positive: $a > 0$, $\mu > 0$, $\sigma > 0$. However,
the solution that we discuss below is valid for arbitrary values of these parameters.
Before solving (4.41), let us consider the case when $\sigma = 0$. We then have $dr = -a(r - \mu)\,dt$,
and since $dr = r'\,dt$ we obtain the following ordinary differential equation:

```math
r' = -a(r - \mu).
```

Then $(r - \mu)' = -a(r - \mu)$, (as $(r - \mu)' = r' - \mu' = r'$) and hence

```math
r - \mu = ce^{-at}, \quad \text{or} \quad r(t) = \mu + ce^{-at}.
```

It is useful to note that if $a > 0$ then $e^{-at} \to 0$ as $t \to \infty$ and hence $r(t) \to \mu$. Note also that
$r(t) = \mu$ is a solution to (4.42). (See the sketch of the graph of $r(t)$ in the hand-written version of
these Notes.)
If $a > 0$ then the solution $r(t) = \mu$ is the so called stable solution.

**Theorem 4.6.5.** Suppose that $r(t)$ is a random process which satisfies the equation

```math
dr = -a(r - \mu)\,dt + \sigma\,dW_t.
```

Then

```math
r(t) = \mu + (r(0) - \mu)e^{-at} + \sigma e^{-at} \int_0^t e^{as}\,dW_s.
```

_Proof._ We shall be looking for a function $u(t)$ such that

```math
r(t) - \mu = u(t)e^{-at}
```

Then $u(t) = e^{at}(r(t) - \mu)$. By Ito's lemma, we compute

```math
\begin{aligned}
du(t) &= ae^{at}(r - \mu)\,dt + e^{at}\,dr \\
      &= ae^{at}(r - \mu)\,dt + e^{at}(-a(r - \mu)\,dt + \sigma\,dW_t) \\
      &= \sigma e^{at}\,dW_t
\end{aligned}
```

Hence $\int_0^t du(s) = \sigma \int_0^t e^{as}\,dW_s$, or equivalently,

```math
u(t) - u(0) = \sigma \int_0^t e^{as}\,dW_s
```

It follows from (4.43) that $r(0) - \mu = u(0)$. So (4.44) can be rewritten as

```math
u(t) = u(0) + \sigma \int_0^t e^{as}\,dW_s = r(0) - \mu + \sigma \int_0^t e^{as}\,dW_s
```

and we obtain (again due to (4.43)) that

```math
\begin{aligned}
r(t) &= \mu + e^{-at}\!\left(r(0) - \mu + \sigma \int_0^t e^{as}\,dW_s\right) \\
     &= r(0)e^{-at} + \mu(1 - e^{-at}) + \sigma e^{-at} \int_0^t e^{as}\,dW_s \\
     &= (r(0) - \mu)e^{-at} + \mu + \sigma e^{-at} \int_0^t e^{as}\,dW_s
\end{aligned}
```

Some comments

1. The most important step in the proof of this theorem is the "guess" (4.43). There is a good
   reason for this guess but we shall not discuss it here. However, you are required to know and
   be able to reproduce the above proof.

2. To compute $du(t)$, we use the chain rule. In fact we derive it. Namely, if $dr = -a(r - \mu)\,dt + \sigma\,dW_t$ and $u = f(t, r)$, then

   ```math
   du = f_t'\,dt + f_r'\,dr + \frac{1}{2}f_{rr}''\,(dr)^2.
   ```

   In our case $u(t) = f(t, r) = e^{at}(r - \mu)$ and therefore

   ```math
   f_t' = \frac{\partial}{\partial t}\!\left(e^{at}(r - \mu)\right) = ae^{at}(r - \mu),
   ```

   ```math
   f_r' = \frac{\partial}{\partial r}\!\left(e^{at}(r - \mu)\right) = e^{at},
   ```

   ```math
   f_{rr}'' = 0.
   ```

   This explains the second step.

   Remark. We use the notation $f_t' = \frac{\partial f}{\partial t}$, $f_r' = \frac{\partial f}{\partial r}$, and $f_{rr}'' = \frac{\partial^2 f}{\partial r^2}$.
