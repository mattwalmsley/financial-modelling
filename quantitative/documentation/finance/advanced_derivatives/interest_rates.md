# Interest Rates

## Stochastic Interest Models

### The Vasicek Model

In the real world markets, interest rates behave, at a local scale, in a way which resembles some
kind of a Brownian motion. In fact, this random process is a function of a Brownian motion and has
interesting and important properties which are very different from those of the Brownian motion.
The simplest model describing this behaviour is the so called Vasicek Model. Mathematically
speaking, the Vasicek Model is the Ornstein-Uhlenbeck process:

```math
dr = -a(r - \mu)\,dt + \sigma\,dW_t
```

where $a > 0$, $\mu > 0$ and we usually think of $\sigma$ as a positive number.

**Remark 5.1.1.** We have already mentioned before that it is not important whether $\sigma$ is positive
or negative. The reason for that is the if $dW_t = W_{t+dt} - W_t$, then $\sigma\,dW_t \sim \mathcal{N}(0, \sigma^2\,dt)$ and
$-\sigma\,dW_t \sim \mathcal{N}(0, \sigma^2\,dt)$ - they have the same distribution.

#### Properties of the Vasicek Model

1.  First of all, we already know the explicit solution to (5.1):

    ```math
    r(t) = (r_0 - \mu)e^{-at} + \mu + \sigma e^{-at} \int_0^t e^{as}\,dW_s.
    ```

2.  Next, Theorem 1.8 in Notes 5 states that $\int_0^t e^{as}\,dW_s \sim \mathcal{N}\!\left(0, \int_0^t e^{2as}\,ds\right)$ and so we can compute
    $\mathbb{E}(r(t))$ and $\text{Var}(r(t))$. Namely,

    ```math
    \mathbb{E}(r(t)) = (r_0 - \mu)e^{-at} + \mu.
    ```

    Since $e^{-at} \to 0$ as $t \to \infty$, we see that also
    $\mathbb{E}(r(t)) \to \mu$ as $t \to \infty$.
    Next

    ```math
    \begin{aligned}
    \text{Var}(r(t)) &= \text{Var}\!\left(\sigma e^{-at} \int_0^t e^{as}\,dW_s\right) = \sigma^2 e^{-2at} \text{Var}\!\left(\int_0^t e^{as}\,dW_s\right) \\
                     &= \sigma^2 e^{-2at} \int_0^t e^{2as}\,ds \\
                     &= \frac{\sigma^2}{2a} e^{-2at}(e^{2at} - 1)
    \end{aligned}
    ```

    Thus

    ```math
    \text{Var}(r(t)) = \frac{\sigma^2}{2a}(1 - e^{-2at})
    ```

    and

    ```math
    \text{Var}(r(t)) \to \frac{\sigma^2}{2a} \quad \text{as } t \to \infty
    ```

    Remark: (5.4) and (5.6) are due to $a > 0$.

3.  Hence

    ```math
    r(t) \sim \mathcal{N}\!\left((r_0 - \mu)e^{-at} + \mu,\; \frac{\sigma^2}{2a}(1 - e^{-2at})\right)
    ```

    and for large values of $t$, $r(t) \sim \mathcal{N}\!\left(\mu, \frac{\sigma^2}{2a}\right)$ (with good precision). This means that for large
    values of $t$, the distribution of $r(t)$ does not depend on $t$.

4.  The unfortunate property of this model is that $r(t)$ can be negative. However, the probability
    of such an event is small when $\sigma$ is small.

    Exercise 5.1.2. Assuming property 3, what is the probability that $r(t) < 0$ for large values
    of $t$? More precisely, compute $\lim_{t\to\infty} P(r(t) < 0)$.

    ANSWER.

    ```math
    \lim_{t\to\infty} P(r(t) < 0) = \Phi\!\left(\frac{-\mu\sqrt{2a}}{|\sigma|}\right) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\frac{-\mu\sqrt{2a}}{|\sigma|}} e^{-\frac{x^2}{2}}\,dx.
    ```

    Can you now see that this probability decreases to 0 as $|\sigma| \to 0$?

5.  The most important good feature of this model is the "mean reversion" property of $r(t)$:
    the value $r(t)$ will eventually return to its long-term mean $\mu$.

    ```math
    dr(t) = -a(r(t) - \mu)\,dt + \sigma\,dW_t.
    ```

    If $r(t) - \mu > 0$, then the larger the deviation of $r(t)$ from $\mu$, the stronger is the "drive"
    $-a(r(t) - \mu)\,dt$ which pushes $r(t)$ back to $\mu$. If $r(t) - \mu < 0$, then $-a(r(t) - \mu)\,dt > 0$ and
    again the interest rate $r$ is pushed back to $\mu$.

    Note that the Vasicek model can create temporarily negative interest rates (though with a low

proability if b is large). This was originally seen as a disadvantage of the model. However, it seems
negative interest rates are not unrealistic anymore as they are sometimes seen in real markets (the
current situation in the UK is close to negative interest rates). Also note that we can certainly also
calculate expectation values for other return functions, as relevant e.g. for put and call options on
bonds with a given strike price. This then leads to option pricing formulas for bond options based
on the Vasicek model (for more details, see e.g. F. Jamshidian, Journal of Finance 44, 205 (1989)).
The result differs from that obtained for Black's model, because a different stochastic process is
chosen.

![Interest Rate Models](../images/interest_rate_models.png)

### The Cox-Ingersoll-Ross model

**Definition 5.2.1.** The Cox-Ingersoll-Ross model (CIR) with parameters $a > 0$, $\mu > 0$, $\sigma > 0$ is the
one according to which the interest rate is governed by the following equation:

```math
dr(t) = -a(r(t) - \mu)\,dt + \sigma\sqrt{r(t)}\,dW_t.
```

The following important property of this model can be proved:

**Theorem 5.2.2.** If $\sigma^2 < 2a\mu$ then $r(t) > 0$ for all $t > 0$.

    This model is also mean-reversible.
    Equation (5.7) cannot be solve explicitly and we shall not prove these properties of the CIR

model. However, the method we have used to solve the equation for the OU process can be used
to prove an interesting relation for rt also in the case of the CIR model.

**Lemma 5.2.3.** If $r_t$ solves equation (5.7) with an initial condition $r_0$ then

```math
r_t = \mu + e^{-at}(r_0 - \mu) + \sigma \int_0^t e^{-a(t-s)}\sqrt{r_s}\,dW_s.
```

_Proof._ Define $U_t = e^{at}(r_t - \mu)$. Applying Ito's lemma in the form of the chain rule gives

```math
dU_t = e^{at}\sigma\sqrt{r_t}\,dW_t.
```

Integrating the above from $0$ to $t$ gives

```math
U_t = U_0 + \sigma \int_0^t e^{as}\sqrt{r_s}\,dW_s.
```

Since $U_0 = r_0 - \mu$ we get

```math
U_t = r_0 - \mu + \sigma \int_0^t e^{as}\sqrt{r_s}\,dW_s,
```

and hence

```math
r_t = \mu + e^{-at}U_t = \mu + e^{-at}(r_0 - \mu) + \sigma \int_0^t e^{-a(t-s)}\sqrt{r_s}\,dW_s.
```

We note that, unlike in the case of the Vasicek model, here the distribution of $r_t$ can't be
computed explicitly. However, relation (5.8) allows us to compute the expectation and the variance
of $r_t$.

**Lemma 5.2.4.** The expectation and the variance of $r_t$ satisfying (5.7) with initial condition $r_0$ are:

```math
\mathbb{E}(r_t) = \mu + e^{-at}(r_0 - \mu),
```

```math
\text{Var}(r_t) = \frac{\sigma^2 \mu}{2a}\!\left(1 - e^{-2at}\right) + \frac{\sigma^2(r_0 - \mu)e^{-at}}{a}\!\left(1 - e^{-at}\right).
```

_Proof._ We recall the following facts (see Notes 6 and 8): for any stochastic process $\{X_s\}_{s \geq 0}$, under
some mild conditions, one has

```math
\mathbb{E}\!\left[\int_0^t X_s\,dW_s\right] = 0, \qquad \text{Var}\!\left(\int_0^t X_s\,dW_s\right) = \int_0^t \mathbb{E}[X_s^2]\,ds.
```

Applying these results to (5.8), we get

```math
\mathbb{E}(r_t) = \mu + e^{-at}(r_0 - \mu) + \mathbb{E}\!\left[\sigma \int_0^t e^{-a(t-s)}\sqrt{r_s}\,dW_s\right] = \mu + e^{-at}(r_0 - \mu),
```

and this proves the first equality. Next,

```math
\begin{aligned}
\text{Var}(r_t) &= \sigma^2 \int_0^t \mathbb{E}\!\left[e^{-2a(t-s)} r_s\right] ds = \sigma^2 \int_0^t e^{-2a(t-s)}\!\left[\mu + e^{-as}(r_0 - \mu)\right] ds \\
               &= \frac{\sigma^2 \mu}{2a}\!\left(1 - e^{-2at}\right) + \frac{\sigma^2(r_0 - \mu)e^{-at}}{a}\!\left(1 - e^{-at}\right)
\end{aligned}
```

Note that $\lim_{t\to\infty} \mathbb{E}(r_t) = \mu$ and $\lim_{t\to\infty} \text{Var}(r_t) = \frac{\sigma^2 \mu}{2a}$.

The Cox-Ingersoll-Ross (CIR) model was developed in 1985 by John C. Cox, Jonathan E. Ingersoll
and Stephen A. Ross as an offshoot of the Vasicek Interest Rate model. It was long thought that
the inability of the model to produce negative rates when $\sigma^2 < 2a\mu$ was a big advantage of the Cox-
Ingersoll-Ross model over the Vasicek model, but in recent years —as many European central banks
have introduced negative rates—it's not so clear anymore whether this positivity is an advantage or
a disadvantage. Note that both the Vasicek and the CIR model are somewhat unrealistic as they
have only a small number of relevant parameters and there are difficulties to calibrate them properly
to reflect the real market term structure of interest rates.

### The Hull-White model

**Definition 5.3.1.** The Hull-White model is the one which assumes that the interest rate is governed
by the following equation:

```math
dr_t = -a(r_t - \mu(t))\,dt + \sigma\,dW_t,
```

where $\mu(t) > 0$ is a given function of $t$, $a > 0$, $\sigma > 0$.

In the Hull-White model, as in the Vasicek model, $r_t$ can take negative values. However, this
model is more flexible in the sense that $r_t$ now fluctuates around a function which we call $\tilde{\nu}(t)$ and
which is defined in terms of $\mu(t)$ (see the theorem below).

**Theorem 5.3.2.** The solution to (5.9) with initial value $r_0$ is given by

```math
r_t = \tilde{\nu}(t) + r_0 e^{-at} + \sigma \int_0^t e^{-a(t-s)}\,dW_s, \quad \text{where } \tilde{\nu}(t) = a\int_0^t e^{-a(t-s)}\mu(s)\,ds.
```

_Proof._ Set $U_t = e^{at}r_t$. Using Ito's lemma, we compute the differential

```math
dU_t = ae^{at}r_t\,dt + e^{at}\,dr_t.
```

Replacing $dr_t$ by the right-hand side of (5.9), we get

```math
dU_t = ae^{at}r_t\,dt + e^{at}\!\left(-a(r_t - \mu(t))\,dt + \sigma\,dW_t\right),
```

and so

```math
dU_t = ae^{at}\mu(t)\,dt + \sigma e^{at}\,dW_t.
```

Integrating both parts of the last equality from $0$ to $t$, we get

```math
U_t - U_0 = a\int_0^t e^{as}\mu(s)\,ds + \sigma \int_0^t e^{as}\,dW_s.
```

Since $U_0 = r_0$, we have:

```math
U_t = r_0 + a\int_0^t e^{as}\mu(s)\,ds + \sigma \int_0^t e^{as}\,dW_s.
```

Finally,

```math
r_t = e^{-at}U_t = r_0 e^{-at} + ae^{-at}\int_0^t e^{as}\mu(s)\,ds + \sigma e^{-at}\int_0^t e^{as}\,dW_s.
```

### Zero coupon bonds and their prices

Bonds are fixed income securities.

**Definition 5.4.**1 (Definition of a bond). A bond is a contract issued by a government or a corporate
in order to raise capital. Investors who purchase a bond are promised a stream of fixed payments
known as coupons plus the total capital invested at the bond expiry.
In this section, our aim is to compute the price of a zero coupon bond in the case when the
interest rate is modelled as random processes.
But first, let us recall an elementary fact concerned with continuously compounded interest rate
$r(t)$: if at time $t \geq 0$ £1 is deposited into a bank then the capital of this portfolio at time $T \geq t$
will be $£e^{\int_t^T r(s)\,ds}$. This fact implies the following lemma.

**Lemma 5.4.2.** Suppose that the continuously compounded interest rate is $r(t)$ and that the payoff
of a bond at time $T$ is £1. Then the price $B(t, T)$ of this bond at time $t$, $0 \leq t \leq T$, is

```math
B(t, T) = e^{-\int_t^T r(s)\,ds}.
```

_Proof._ If $B(t, T)$ is deposited in the bank at time $t$ then (as noted above) the value of this money is
at time $T$: $B(t, T)e^{\int_t^T r(s)\,ds}$. We know that $B(t, T)e^{\int_t^T r(s)\,ds} = 1$. Hence $B(t, T) = e^{-\int_t^T r(s)\,ds}$.
Equivalently, we can say that in order to accumulate £1 by time $T$, one has to deposit $£e^{-\int_t^T r(s)\,ds}$
at time $t$.

## Statement of the problem

We shall consider only zero coupon bonds which simply means that there are no coupon payments.
Our model is defined as follows.

1.  The interest rate is $r(t)$, $t \geq 0$, compounded continuously, where $r(t)$ is a random process
    satisfying the equation

```math
dr(t) = a(t, r)\,dt + \sigma(t, r)\,dW_t.
```

2.  Let $B(t, T)$ be the price at time $t$ of a zero coupon bond maturing at time $T$, $0 \leq t \leq T$. By
    definition, this means that the owner of the bond is paid £1 at time $T$ for $\text{£}B(t, T)$ invested
    at time $t$.
    The question we are going to discuss is:
    Question: Given $r(t)$, what is the risk-neutral price $B(t, T)$ of the bond?
    The answer to this question is given by the following theorem.

**Theorem 5.4.3.** If the continuously compounded interest rate is governed by a SDE (5.11) then

```math
B(t, T) = E\left[e^{-\int_t^T r(s)\,ds} \;\middle|\; r(t)\right]
```

The no-arbitrage price of B(t, T ) in the framework of the Vasicek model
According to the Vasicek model, the $r(t)$ satisfies the following SDE:

```math
dr(t) = -a(r(t) - \mu)\,dt + \sigma\,dW_t,
```

where $a > 0$, $b > 0$, $\sigma > 0$ are constants.

**Theorem 5.4.4.** Suppose that the interest rate $r(t)$ is governed by the Vasicek model with param-
eters $a > 0$, $b > 0$. Then the no-arbitrage price of the bond at time $t$ is given by

```math
B(t, T) = e^{-u(\tau) - v(\tau)\,r(t)},
```

where $r(t)$ is the interest rate at time $t$, $\tau = T - t$ and

```math
v(\tau) = \frac{1 - e^{-a\tau}}{a}, \qquad u(\tau) = (\tau - v(\tau))\left(\mu - \frac{\sigma^2}{2a^2}\right) + \frac{\sigma^2}{4a}(v(\tau))^2
```

The proof of this theorem may be given as an exercise.

The no-arbitrage price of B(t, T ) in the framework of the CIR model
According to the Cox-Ingersoll-Ross model, the $r(t)$ satisfies the following SDE:

```math
dr(t) = -a(r(t) - \mu)\,dt + \sigma\sqrt{r(t)}\,dW_t,
```

where $a > 0$, $b > 0$, $\sigma > 0$ are constants. Set

**Theorem 5.4.5.** Suppose that the interest rate $r(t)$ is governed by the CIR model with param-
eters $a > 0$, $b > 0$. Then the no-arbitrage price of the bond at time $t$ is given by

```math
B(t, T) = e^{-u(\tau) - v(\tau)\,r(t)},
```

where $r(t)$ is the interest rate at time $t$, $\tau = T - t$, $\theta := \sqrt{a^2 + 2\sigma^2}$ and

```math
v(\tau) = \frac{2(e^{\theta\tau} - 1)}{(\theta + a)(e^{\theta\tau} - 1) + 2\theta}, \qquad u(\tau) = \frac{2a\mu}{\sigma^2} \ln\frac{2\theta\, e^{(\theta + a)\tau/2}}{(\theta + a)(e^{\theta\tau} - 1) + 2\theta}.
```

## Forward Rates

We have been dealing with instantaneous interest rates. We also have interest rates induced by
bonds of different maturities.
The price at time $t$ of a zero-coupon bond with maturity $T$ will be denoted by $P(t, T)$. The
price will change over time, but as the payoff at time $T$ is 1, we must have $P(T, T) = 1$. The
curve $P(0, s)$, $0 \leq s \leq T$, will be a (generally) decreasing curve as a function of $T$, but the curve
$P(t, T)$, $0 \leq t \leq T$ will be a noisy stochastic process. Note that the end point of the first curve is
the starting point of the second curve.
Now, the fact that $P(0, s)$ is always decreasing means its shape does not contain a lot of
information. The corresponding interest rate $r = r(t, T)$ between time $t$ and $T$ should satisfy

```math
P(t, T) = e^{-r(T - t)},
```

and so we define the yield by

```math
R(t, T) = -\frac{\ln P(t, T)}{T - t}
```

Yield curves $R(0, T)$ can be increasing or decreasing functions of $T$ revealing the average return of
bonds stripped of the crude effects of maturity - the term structure of the market.

![Bond Yield Curves](../images/bond_yield_curves.png)
What is the cost of money now? If at time $t$ we borrow over the period $t$ to $t + h$, where $h$ is a
small time increment, the rate we get is the yield

```math
R(t, t + h) = -\frac{\ln P(t, t + h)}{h}.
```

As we let $h \to 0$, we get the instantaneous interest rate

```math
r_t = R(t, t) = -\frac{\partial}{\partial T} \ln P(t, t).
```

Knowledge of the short rate $r_t$ is not enough to recover the price curve $P(t, T)$.
We also consider forward contracts, which is agreeing at time $t$, to make a payment at a later
date $T_1$ and receive a unit payment at time $T_2$. We can replicate this contract, at time $t$, by buying
a $T_2$ bond and selling $k$ units of a $T_1$ bond. This will require us to make a payment of $k$ at time
$T_1$ and receiving one unit of money at time $T_2$. To give the contract nil initial value, we must set $k$
to be

```math
k = \frac{P(t, T_2)}{P(t, T_1)}.
```

The corresponding (forward) yield is then

```math
f(t, T_1, T_2) = -\frac{\ln k}{T_2 - T_1} = -\frac{\ln P(t, T_2) - \ln P(t, T_1)}{T_2 - T_1}.
```

It is the interest rate between time $T_1$ and $T_2$ that at time $0$ we expect.
Letting $T_1 = T$ and $T_2 = T + h$ and letting $h \to 0$, we get the forward rate for instantaneous
borrowing or forward rate:

```math
f(t, T) = -\frac{\partial}{\partial T} \ln P(t, T).
```

It is the instantaneous rate at time $T$ that at time $0$ we expect. The present instantaneous rate of
borrowing is $r_t = f(t, t)$.
From the forward rates, we can recover the prices $P(t, T)$ and yields $R(t, T)$ by

```math
P(t, T) = \exp\left(-\int_t^T f(t, u)\,du\right)
```

and (5.14).

## The Heath-Jarrow-Morton framework

Forward curve models address several limitations of the short rate models:
• The allow more than one risk factor (more than one Wiener process)
• They allow more choice for structuring the volatility in the interest rate model.
The Heath, Jarrow and Morton (HJM) framework was developed to model forward interest rates.
Unlike short rate models, the aim of this framework is to predict the entire forward rate curve. In
practice, this framework is used to price instruments that are interest rate sensitive, including bonds
and swaps (which we will study later). The HJM framework began in the late 1980s from the work
of David Heath, Robert Jarrow, and Andrew Morton.
We will look at the HJM model under the following assumptions:

• Single factor (one Brownian motion)

• Risk neutrality

• The return of a zero-coupon bond in a risk neutral world is r.

Hence, we can express the stochastic process of this security as follows:

```math
dP(t, T) = r(t)P(t, T)\,dt + \sigma(t, T, \Omega_t)P(t, T)\,dW(t),
```

where $\Omega_t$ represents relevant past and present interest rates and bond prices at time $t$, the volatility,
$\sigma$, of the zero-coupon bond can be a function of such interest rates and bond prices. Since the $\sigma$ of
a bond's price is zero at maturity, we can write:

```math
\sigma(t, t, \Omega_t) = 0.
```

As was noted in the previous section, the relationship between forward rates $f(t, T_1, T_2)$ and zero-coupon
bond prices $P(t, T)$ for continuously compounded interest is:

```math
f(t, T_1, T_2) = \frac{\ln P(t, T_1) - \ln P(t, T_2)}{T_2 - T_1}.
```

From our previously defined stochastic process and Itô's lemma, we have the following two
equations:

```math
d\ln P(t, T_1) = \left(r(t) - \frac{\sigma(t, T_1, \Omega_t)^2}{2}\right)dt + \sigma(t, T_1, \Omega_t)\,dW(t)
```

and

```math
d\ln P(t, T_2) = \left(r(t) - \frac{\sigma(t, T_2, \Omega_t)^2}{2}\right)dt + \sigma(t, T_2, \Omega_t)\,dW(t).
```

From (5.16), we have

```math
df(t, T_1, T_2) = \frac{\sigma(t, T_2, \Omega_t)^2 - \sigma(t, T_1, \Omega_t)^2}{2(T_2 - T_1)}\,dt + \frac{\sigma(t, T_1, \Omega_t) - \sigma(t, T_2, \Omega_t)}{T_2 - T_1}\,dW(t).
```

The forward rate f (t, T1 , T2 ) becomes the instantaneous forward rate f (t, T ) when we do the fol-
lowing:

• Make $T_1 = T$

• Make $T_2 = T + \Delta T$

• Take limits as $\Delta T \to 0$.

The coefficient of $dW(t)$ becomes $-\frac{\partial}{\partial T} \sigma(t, T, \Omega_t) = -\sigma_T(t, T, \Omega_t)$, while for $dt$ the coefficient
becomes

```math
\frac{1}{2} \frac{\partial}{\partial T} \sigma(t, T, \Omega_t)^2 = \sigma(t, T, \Omega_t)\,\sigma_T(t, T, \Omega_t),
```

from which

```math
df(t, T) = \sigma(t, T, \Omega_t)\,\sigma_T(t, T, \Omega_t)\,dt - \sigma_T(t, T, \Omega_t)\,dW(t).
```

The risk neutral processes for the instantaneous forward rates are known as soon as we define the
function $\sigma(t, T, \Omega_t)$.

We can use (5.17) to derive the main finding of the HJM model: the existence of a relationship
between the drift and standard deviation of the instantaneous forward rate $f(t, T)$. First, note that

```math
\sigma(t, T, \Omega_t) - \sigma(t, t, \Omega_t) = \int_t^T \sigma_\tau(t, \tau, \Omega_t)\,d\tau
```

Remembering (5.15), the above is really

```math
\sigma(t, T, \Omega_t) = \int_t^T \sigma_\tau(t, \tau, \Omega_t)\,d\tau
```

Next define the following for $f(t, T)$:

• $m(t, T, \Omega_t)$ is the drift

• $s(t, T, \Omega_t)$ is the volatility

so that

```math
df(t, T) = m(t, T, \Omega_t)\,dt + s(t, T, \Omega_t)\,dW(t).
```

Finally, comparing the last equation with (5.17), we see that

```math
m(t, T, \Omega_t) = -s(t, T, \Omega_t) \int_t^T s_\tau(t, \tau, \Omega_t)\,d\tau.
```

### Limitations of implementing the HJM model

- The main drawback for the general HJM is the short rate, which follows a non Markov process,
resulting in the need for Monte Carlo simulation.

- The model is expressed in terms of instantaneous forward rates, which can't be directly observed
in the market.

Undef certain assumptions the HJM model is the same as the Hull-White model.

# The Black-Scholes framework

Some of you will have got to know the Black-Scholes option pricing theory, which is treated in
more detail in MTH762U/P Continuous Time Models in Finance, running in parallel to our module.
The underlying stochastic process for a given asset (e.g. some share price) is given by geometric
Brownian motion with parameters µ and σ, as defined in Subsection 4.6.1.
The discounted share price has SDE

```math
d(e^{-rt} S_t) = -re^{-rt} S_t \, dt + e^{-rt} \, dS_t = e^{-rt} S_t (\mu - r) \, dt + e^{-rt} S_t \sigma \, dW_t
```

Thus, if $\mu = r$, then

```math
d(e^{-rt} S_t) = -re^{-rt} S_t \, dt + e^{-rt} \, dS_t = e^{-rt} S_t \sigma \, dW_t
```

and there is no drift term. The parameters of $S_t$ are $r$ and $\sigma$. This is called risk-neutral geometric
Brownian motion. By Theorem 4.6.1,

```math
S_t = S_0 \exp\left(\left(r - \frac{\sigma^2}{2}\right)t + \sigma W_t\right)
```

for risk-neutral Brownian motion.
It is a remarkable fact that derivatives on the underlying geometric Brownian motion (with
parameters µ and σ) can be priced using the risk-neutral Brownian motion.
Let's make this idea mathematically more precise:
Example. (Strategy for pricing a derivative). Assume there is a derivative with payoff function
$g(S_T)$ at time $T$, where $S_t$ is the underlying asset, whatever it is. The price of the contract at time
$t = 0$ is then given as

```math
\pi_0 = e^{-rT} \mathbb{E}[g(S_T)]
```

where $r$ is the current interest rate over the period $T$ and $S_t$ is risk-neutral geometric Brownian
motion. One can write

```math
S_T = S_0 \exp\left(\mu' T + \sigma \sqrt{T} \, W\right),
```

with $W \sim N(0, 1)$, i.e. $W$ is normally distributed with mean 0 and variance 1, and $\mu' = r - \frac{1}{2} \sigma^2$.
Therefore,

```math
\pi_0 = e^{-rT} \int_{-\infty}^{\infty} g\!\left(S_0 \, e^{rT - \frac{1}{2}\sigma^2 T + \sigma\sqrt{T}\,w}\right) \frac{1}{\sqrt{2\pi}} e^{-w^2/2} \, dw
```

At time $t$ the price of the contract is

```math
\pi_t = e^{-r(T-t)} \int_{-\infty}^{\infty} g\!\left(S_t \, e^{r(T-t) - \frac{1}{2}\sigma^2(T-t) + \sigma\sqrt{T-t}\,w}\right) \frac{1}{\sqrt{2\pi}} e^{-w^2/2} \, dw
```

and clearly this price will evolve in time. The function g, in the most general case, may depend
on all values of the stochastic process over the entire time, i.e. it is a so-called functional of the
stochastic process.

If the payoff function $g(x)$ in the above example is just given by $g(x) = \max(x - K, 0)$, that
is, the payoff of a European call option, then the above expression Eq. (6.2) yields the well-known
Black-Scholes option pricing formula:

```math
\pi_0 = C_0(S_0, K, T, r_{0,T}, \sigma_0).
```

Explicitly, by calculating the expectation for risk-neutral geomeric Brownian motion the above ex-
pression Eq. (6.2) yields the cost $C_0$ of a European call option at time 0:

```math
C_0(T, S_0, K, r, \sigma) = S_0 \Phi(d_+(T, S_0)) - K e^{-rT} \Phi(d_-(T, S_0))
```

where

```math
d_{\pm}(T, S_0) = \frac{1}{\sigma\sqrt{T}} \left[\log \frac{S_0}{K} + \left(r \pm \frac{\sigma^2}{2}\right) T\right]
```

and $\Phi(x)$ is the normal cumulative distribution function. S0 denotes the initial asset price, and σ
the volatility parameter (assumed to be constant). The interest rate r is assumed to be constant.
The price of a European put option with the same parameters is

```math
P_0(T, S_0, K, r, \sigma) = K e^{-rT} \Phi(-d_-(T, S_0)) - S_0 \Phi(-d_+(T, S_0))
```

For some interest rate derivatives (e.g. options on bonds) the Black-Scholes framework can be
developed, if the underlying is assumed to be LogNormally distributed. This idea leads to Black's
model, which is discussed after the next section. First we must discuss interest rate instruments.

## Interest rate instruments

An interest rate derivative is a financial instrument with a value that is strongly linked to the
movements of an interest rate or several interest rates. Interest rate derivatives are often used as
hedges by institutional investors, banks, companies, and individuals to protect themselves against
changes in market interest rates, but they can also be used to increase or refine the holder's risk profile
in a given portfolio or to speculate on rate moves. In the early parts of this course, we concentrated
on fluctuations as induced by share prices moving in an unpredictable way. But fluctuations in
interest rates can also have a huge effect on the value of a given portfolio, in particular if the
portfolio contains some derivatives that are highly sensitive to such moves in the interest rate.
An interest rate derivative is a financial contract whose value is based on some underlying interest
rate or interest-bearing asset. These may include interest rate futures, options, swaps, swaptions,
etc. Entities with interest rate risk can use these derivatives to hedge or minimize potential losses
that may accompany a change in interest rates. Interest rate risk also exists in an interest-bearing
asset, such as a loan or a bond, due to the possibility of a change in the asset's value resulting
from the variability of interest rates. Interest rate risk management has become very important in
practice in the finance industry, and a large variety of assorted instruments have been developed to
deal with interest rate risk.

    Interest rate derivatives can range from simple to highly complex. Among the most common

types of interest rate derivatives are interest rate futures, swaps, caps, collars, and floors.
Interest Rate Swaps
Interest-rate swaps are contracts that involve the exchange of one set of future interest payments
for another set of future interest payments.

    • One stream of interest payments is typically fixed, the other floating (could also be two streams
      of floating payments)

    • Interest payments are based on a pre-determined principle amount.

    • The duration of life of this derivative is known as the swap term or tenor.

Through this exchange of cash flows, the two parties aim to reduce uncertainty and the threat of
loss from changes in market interest rates.
The simplest type of interest rate swap is a plain vanilla swap, a contract which specifies:

    • The interest rates being exchanged

    • The notional principle amount

    • Settlement dates (when cash flows are exchanged)

    • Currency (cash flows are paid in the same currency)

    • Swap term

Figure 6.1 illustrates an interest rate swap. A swap costs nothing to enter into.

                                      Interest Rate Swap

                                                  3.5% (Fixed Rate)

                                                    Tenor: 5 years
                                         FIRM A     Principal: $10M   FIRM B
                                                        Annual
                                                      settlement

                                                   LIBOR (Floating
                                                       Rate)

At every instant $T_i$ in a prespecified set of dates $T_{\alpha+1}, \ldots, T_\beta$ within a year, the fixed leg pays out
the amount $N \tau_i K$, corresponding to a fixed interest rate $K$, a nominal value $N$ and $\tau_i = T_i - T_{i-1}$,
whereas the floating leg pays the amount $N \tau_i L(T_{i-1}, T_i)$, where $L(T_{i-1}, T_i)$ is the floating interest
rate in the time interval $(T_{i-1}, T_i)$. The letter $L$ stands for LIBOR, which is a simple interest rate.
When the fixed leg is paid and the floating leg is received the IRS is termed Payer IRS (PFS),
whereas in the other case we have a Receiver IRS (RFS). The discounted payoff at a time $t < T_\alpha$
of a PFS can be expressed as

```math
\sum_{i=\alpha+1}^{\beta} P(t, T_i) N \tau_i \bigl(L(T_{i-1}, T_i) - K\bigr)
```

where $P(t, T)$ is the value of a zero-coupon bond at time $t$ and maturity $T$.
A Forward Rate Agreement (FRA) is a swap with $\alpha + 1 = \beta$, so the only times to consider
are the current time $t$, the expiry time $T > t$, and the maturity time $S > T$.
Caps and Floors A company with a floating rate loan that does not want to swap to a fixed rate
but does want some protection can buy an interest rate cap. The cap is set at the top rate that the
borrower wishes to pay; if the market moves above that level, the owner of the cap receives periodic
payments based on the difference between the cap and the market rate. The premium, which is the
cost of the cap, is based on how high the protection level is above the then-current market.
A company receiving a stream of floating rate payments can buy a floor to protect against
declining rates. Like a cap, the price depends on the protection level and maturity. Selling, rather
than buying, the cap or floor increases rate risk.
We can look at the payoff of these instruments in two ways:

    • As a portfolio of interest rate options

    • As a portfolio of put options on zero coupon bonds

To price this derivative as a portfolio of interest rate options, we first define the following:

    • $T$ = Total life of the interest rate cap

    • $L$ = The principal amount

    • $R_K$ = The cap rate

    • $R_k$ = LIBOR rate between time $t_k$ and $t_{k+1}$, observed at $t_k$ ($1 \leq k \leq n$)

    • $t_1, t_2, \ldots, t_n$ = The reset dates

    • $t_{n+1} = T$

The payoff at $t_{k+1}$, $k = 1, 2, \ldots, n$, is

```math
L \delta_k \max(R_k - R_K, 0)
```

where $\delta_k = t_{k+1} - t_k$. This represents the payoff (at time $t_{k+1}$) from a European style call option on
the LIBOR rate (observed at time $t_k$). The cap consists of a portfolio of $n$ options called caplets.
To see interest rate caps as a portfolio of put options on zero coupon bonds, our payoff at $t_{k+1}$
becomes the following at $t_k$

```math
\frac{L \delta_k}{1 + R_k \delta_k} \max(R_k - R_K, 0)
```

This, after some algebraic rearranging, is equivalent to:

```math
\max\!\left(L - \frac{L(1 + R_K \delta_k)}{1 + R_k \delta_k},\, 0\right)
```

From the previous equation, observe that the following term represents the value of a zero coupon
bond at $t_k$ with a payoff of $L(1 + R_K \delta_k)$:

```math
\frac{L(1 + R_K \delta_k)}{1 + R_k \delta_k}
```

Therefore, we see how the expression (6.9) is a put option payoff with maturity $t_k$ on a zero-coupon
bond with maturity $t_{k+1}$ when the strike price is $L$ and the bond's face value is $L(1 + R_K \delta_k)$.

Opposite to an interest rate cap, an interest rate floor gives a payoff when the interest rate on
the underlying decreases below a given level. The payoff at $t_k$ ($1 \leq k \leq n$) of an interest rate floor
is:

```math
L \delta_k \max(R_K - R_k, 0)
```

Similar to the case of the interest rate cap, we can look at the payoff of floors in two ways:

• As a portfolio of put options on interest rates

• As a portfolio of call options on zero coupon bonds

The individual $n$ options that make up a floor are called floorlets.

## Black's model

Black's Model is an adjustment of his earlier and more famous Black-Scholes options pricing model.
It was developed in 1976. Unlike the earlier model, the revised model is useful for valuing general
options on interest rates. Black's Model has also been used in the application of capped variable
rate loans and is also applied to price a variety of other derivatives. The model is quite generally
applicable, and a kind of standard pricing model for valuing assets such as options on futures and
capped variable rate debt securities. The model was developed by Fischer Black by elaborating on
the earlier and more well-known Black-Scholes-Merton option pricing formula. Like other financial
models, it relies on several assumptions, such as a log-normal distribution of prices and zero trading
costs - some of which are more realistic than others. Black's goal in 1976 was to improve the
understanding of commodity options and their pricing. Existing models at that time, including
Black-Scholes and Merton models, had been unable to address this problem.
A forward contract contract exists between a buyer and seller agreeing to the future delivery of
a commodity or interest-bearing asset, such as a bond. They are not exchange-traded and may be
customized between counterparties. They cost nothing to enter into, but a fixed payment must be
made at the time of delivery. Let's say that the item to be delivered provides no income during the
duration of the contract. Let $K$ be the amount of the payment. Then,

```math
K = S e^{rT}
```

where $S$ is the spot price of the asset to be delivered, $T$ is the delivery time, and $r$ is the interest
rate. The reason is that the price of the contract is

```math
0 = e^{-rT} \mathbb{E}(S(T) - K) = e^{-rT} \mathbb{E}(S(T)) - e^{-rT} K = S - e^{-rT} K.
```

A futures contract is like a forward in that it exists between a buyer and seller agreeing to the

future delivery of any interest-bearing asset, such as a bond. The difference is that futures are
tradable. An example is U.S. Treasury Futures. The interest rate future allows the buyer and seller
to lock in the price of the interest-bearing asset for a future date. The futures price is related to the
spot price $S$ (current price) of the bond by

```math
F = (S - I) e^{rT}
```

where $I$ is the present value of the coupons during the life of the futures contract, $T$ is the time
until the futures contract matures, and r is the interest rate.
Blacx's model initially was used to price futures options. The key difference between this 1976
model and the Black-Scholes model is that the revised model uses forward prices to model the value

of a futures option at maturity versus the spot prices that Black-Scholes uses. The pricing formula
of the Black model is

```math
C = P(0, T) \bigl[F_0 \Phi(d_1) - K \Phi(d_2)\bigr]
```

where

```math
d_1 = \frac{\ln(F_0 / K) + \sigma^2 T / 2}{\sigma \sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}
```

Here $C$ is the price of a call option, $P(t, T)$ is the price at time $t$ of a zero-coupon bond paying the
unit amount 1 at time $T$ (or equivalently the discount factor $D(t, T)$), $F$ is the forward price of a
quantity $V$ for a contract with maturity $T$, and $V_T$ is the value of $V$ at time $T$. The quantity $\sigma$ is
the volatility of the futures price, which can often be shown to be the same as the volatility of the
underlying asset. The pay-off is given by $\max(V_T - K, 0)$, where $K$ is the strike price. Again, the
model depends on the assumption that the random variable $V_T$ is lognormally distributed, with the
variance of $\ln V_T$ equal to $\sigma \sqrt{T}$.
Options on Bonds A bond is a security that provides a known cash income. One can then
purchase call options on a given bond, at the price $C$ estimated by Black's model, for a given strike
price $K$. For a European bond option one has

```math
F_0 = \frac{B_0 - I}{P(0, T)}
```

where $B_0$ is the bond price at time zero and $I$ is the present value of the coupons that will be paid
during the life time of the option. See Subsection 5.4 for an explanation of bond pricing.
Swaptions Also called swap options, they give the buyer the option to enter into a swap in
exchange for a premium. Over the counter (OTC) contracts, hence, like interest rate swaps these
derivatives are highly customizable. Upon entering a swaption, the buyer/seller agree on the price,
maturity, notional, and stream of interest rate payments. Parties must also decide execution method,
for example, American, European or Bermudan.
Swaptions can be a payer swaption or receiver swaption:

• Payer swaption: gives holder the option of paying the fixed rate and receive floating rate
(exercised if the fixed swap price is above the strike price).

• Receiver swaption: gives holder the option of paying the floating rate and receiving the fixed
rate. (exercised if the fixed swap price is below the strike price).

    Consider a payer swaption on a swap; as described in Subsection 6.2 with payoff (6.7). The

swaption will only be used if its value is positive. Forward interest rates are the future rates of
interest implied by current zero rates for periods of time in the future. The forward rates for $T < S$
for LIBOR are given by

```math
F(t;\, T, S) := \frac{1}{\tau(T, S)} \left(\frac{P(t, T)}{P(t, S)} - 1\right)
```

It can be shown that the value at time $t$ of the payoff is

```math
\begin{aligned}
&\max\!\left(\sum_{i=\alpha+1}^{\beta} P(t, T_i) N \tau_i \bigl(F(t;\, T_{i-1}, T_i) - K\bigr),\, 0\right) \\
&= N \max\!\left(\sum_{i=\alpha+1}^{\beta} \bigl[P(t, T_{i-1}) - P(t, T_i) - K P(t, T_i) \tau_i\bigr],\, 0\right) \\
&= N \max\!\left(P(t, T_\alpha) - P(t, T_\beta) - \sum_{i=\alpha+1}^{\beta} K P(t, T_i) \tau_i,\, 0\right) \\
&= N \max\bigl(S(\alpha, \beta) - K,\, 0\bigr) \sum_{i=\alpha+1}^{\beta} P(t, T_i) \tau_i
\end{aligned}
```

where

```math
S(\alpha, \beta) = \frac{P(t, T_\alpha) - P(t, T_\beta)}{\sum_{i=\alpha+1}^{\beta} P(t, T_i) \tau_i}
```

is the forward swap rate.
The standard market model gives the value of the swaption as

```math
\bigl[S \Phi(d_1) - K \Phi(d_2)\bigr] \sum_{i=\alpha+1}^{\beta} P(t, T_i) N \tau_i
```

where $S = S(\alpha, \beta)$, $\sigma$ is the volatility of the forward swap rate, and $d_1$ and $d_2$ are given by (6.11),
(6.12), with $F_0 = S$ and $T = T_\alpha$.
Caps and Floors We can price caps and floors as a natural extension of Black's model. We
define the following:

• $F_k = F(0;\, t_k, t_{k+1})$ The forward interest rate at time 0 for the time period between $t_k$ and
$t_{k+1}$

• $\sigma_k$ = the volatility of $F_k$

• $P(0, t_{k+1})$ = the discount factor

• $\delta_k = t_{k+1} - t_k$

Recalling (6.8), the value of a caplet is

```math
L \delta_k P(0, t_{k+1}) \bigl[F_k \Phi(d_1) - R_K \Phi(d_2)\bigr]
```

where

```math
d_1 = \frac{\ln(F_k / R_K) + \sigma_k^2 t_k / 2}{\sigma_k \sqrt{t_k}}, \qquad d_2 = d_1 - \sigma_k \sqrt{t_k}
```

Observe that $\sigma_k$ is multiplied by $t_k$ since the interest rate $R_k$ is observed at $t_k$, but $P(0, t_{k+1})$
indicates that the payoff occurs at $t_{k+1}$, not $t_k$.