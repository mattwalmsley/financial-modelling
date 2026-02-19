# Investment Decisions - Maximizing Expected Utility

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
