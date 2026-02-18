Credit Risk and Credit Derivatives

Credit risk is the risk that a person or an organisation will fail to make a payment they have promised.
There are several kinds of models addressing the problem of how to estimate credit risk.
In this course, we consider two types of models.

• The structural models are the models which link default events (see the definitions below)
with the structure of a corporate entity's equity and debt. The Merton model is the simplest
example of a structural model and the only one that will be discussed in this course.

• The reduced-form models are statistical models which use observed market statistics along
with the data on the default-free market to model the movement of the credit rating of the
bonds issued by the corporate entity over time. The main output of such a model is the
distribution of the time of default.
They are called "reduced-form" because they ignore specific data concerning the company
which issues the bond. Instead, they use credit ratings issued by credit rating agencies such
as Standard and Poor's and Moody's.
In turn, when setting there ratings, the credit rating agencies would use detailed data specific
to the corporate entity issuing the bond.

## Terminology: credit events and recovery rates

The aim of this section is to recall/introduce some terminology which will be used below.
A bond (or a fixed income security) is a debt instrument created to raise capital. More precisely:

**Definition 7.1.1.** A bond is a loan agreement between a bond issuer and an investor in which the
bond issuer is obligated to pay a specified amount of money at specified future dates.

**Definition 7.1.2.** A default-free bond is the one which repays interest and the principal with
absolute certainty.

    Government bonds may be viewed as an example of default-free bonds but corporate bonds may

default. Default may mean that the payment

1. is rescheduled,
2. is reduced,
3. is continued but at reduced rate,
4. is completely wiped out.

**Definition 7.1.3.** A credit event is an event that will trigger the default of a bond.

    Examples of credit events are:

1. Failure to pay either the capital or a coupon.
2. Bankruptcy.
3. Rating downgrade of the bond (we shall say more about the ratings later).

**Definition 7.1.4.** Recovery rate is the fraction of the default amount that can be recovered trough
bankruptcy proceedings or some other form of settlement.

## The Merton model

The Merton model is an example of a model describing the structure of the value (total capital) of
a corporate entity.
We denote by $F(t)$ the value of a corporate entity at time $t$. $F(t)$ consists of two parts:

```math
F(t) = E(t) + B(t),
```

where $E(t)$ is the corporate entity's equity and $B(t)$ is its debt.

**Remarks 7.2.1.** 1. A corporate entity is an organization (e.g. enterprise, institution, firm, gov-
ernment agency, etc) that is recognized as having privileges and obligations, such as having
the ability to enter into contracts, to sue, and to be sued. 2. In the above context, the value of a corporate entity is the same as the total capital of the
corporate entity. 3. Equity or shareholders' equity is the part of the total capital of a business which belongs to
the business (while debt doesn't).

### Definition of the Merton model

**Definition 7.2.2.** The Merton model describes the behaviour of the capital of a corporate entity.
It assumes that:

1.  At time $t = 0$, the capital $F(0)$ of the corporate entity consists of equity $E(0)$ and debt $B(0)$
    (that is $F(0) = E(0) + B(0)$). The equity $E(0)$ is owned by the shareholders and its debt
    $B(0)$ is the cost of the zero coupon bonds sold by the corporate entity.
2.  The corporate entity promises to pay to bondholders the amount $L$ at future time $T$.

**Remark 7.2.3.** The amount that a corporate entity (CE) promises to pay to a bondholder is called
the nominal value of the bond. Usually, there are many bondholders and each of them buys a
certain number of bonds issued by the CE. The amount $L$ mentioned in Definition (7.2.2) is the
total nominal value (of all bonds sold by the CE). The meaning of the expression nominal value is
always clear from the context.
If $F(T) \geq L$, that is at time $T$ the total value of the corporate entity is grater than (or equal
to) its debt $L$ to the bondholders, then the bondholders receive $L$ and the shareholders receive
$F(T) - L$.
But if $F(T) < L$ then the corporate entity defaults, the bondholders receive $F(T)$ and the
shareholders receive nothing.
So, the payoff to these two categories of investors will be:

Shareholders:

```math
R_{sh}(T) = \max[F(T) - L, 0] = (F(T) - L)^+
```

Bondholders:

```math
R_{bh}(T) = \min[F(T), L] = F(T) - (F(T) - L)^+
```

![Merton Model](../images/merton_model.png)

**Exercise 7.2.4.** Prove that for any real numbers $x, y$ the following is true:

```math
\min[x, y] = y - (y - x)^+ = x - (x - y)^+.
```

**Remark 7.2.5.** The inequality $L > B(0)$ has to be satisfied because if it were otherwise then buying
such a bond would have been a meaningless investment for the bondholder.

**Exercise 7.2.6.** Suppose that the interest rate compounded continuously is $r$. Prove that then the
following stronger inequality holds: $B(0) \leq e^{-rT} L$.
Hint. Note that $R_{bh}(T) \leq L$ and use the fact that $B(0) = e^{-rT} \tilde{E}(R_{bh}(T))$.

### Merton's observation: model-independent facts

Merton made a simple but important observation:
The payoff function $R_{sh}(T) = \max[F(T) - L, 0] = (F(T) - L)^+$ is exactly the payoff function
for a European call option $\text{Call}(L, T)$ on the underlying capital $F(t)$ of the corporate entity. This
means that the shareholders of the corporate entity are treated as having a European call option
$\text{Call}(L, T)$. This implies the following statement.

**Lemma 7.2.7.** Suppose that the interest rate compounded continuously is $r$. Then

```math
E(0) = e^{-rT} \tilde{E}(F(T) - L)^+,
```

where $\tilde{E}$ is the expectation with respect to the risk-neutral probability.

_Proof._ By the general theorem, the price $C$ of a derivative maturing at time $T$ and having a payoff
function $R(T)$ is given by $C = e^{-rT} \tilde{E}(R(T))$. In our case, shares are treated as $\text{Call}(L, T)$ European
options with the payoff function (7.1). Hence their price is

```math
C = e^{-rT} \tilde{E}(F(T) - L)^+.
```

On the other hand, according to the definition of the model, the cost of the shares is $E(0)$. So,
$C = E(0)$ and this implies (7.3).

**Remark 7.2.8.** The derivation of equation (7.3) does not rely on any specific properties of the
process $F(t)$. This means that this relation is model-independent.

### Merton's observation and the Black-Scholes formula

All the statements made in the previous section are independent of any special properties of the
process $F(t)$. Here, we shall prove a theorem which makes use of Merton's observation in the context
of the Black-Scholes formula. This theorem states an equation which establishes the dependence
between the price of the bond $B(0)$ and the equity value $E(0)$.

**Theorem 7.2.9.** Suppose that the total value $F(t)$ of the corporate entity evolves according to
the geometric Brownian motion, $F(t) = F(0)e^{\mu t + \sigma W(t)}$, and that the interest rate compounded
continuously is $r$. Then

```math
E(0) = (E(0) + B(0))\Phi(\omega) - Le^{-rT}\Phi(\omega - \sigma\sqrt{T}),
```

where

```math
\omega = \frac{\log \frac{E(0)+B(0)}{L} + rT}{\sigma\sqrt{T}} + \frac{1}{2}\sigma\sqrt{T}.
```

_Proof._ Recall that within the framework of the Black-Scholes model the price $C$ of a European call
option $\text{Call}(K, T)$ (that is with the strike price $K$ and expiration time $T$) is given by

```math
C = e^{-rT} \tilde{E}(F(T) - K)^+ = S\Phi(\omega) - Ke^{-rT}\Phi(\omega - \sigma\sqrt{T}),
```

where

```math
\Phi(x) := \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-t^2/2} \, dt \quad \text{and} \quad \omega = \frac{\log \frac{S}{K} + rT}{\sigma\sqrt{T}} + \frac{1}{2}\sigma\sqrt{T}.
```

In our case $S = F(0) = E(0) + B(0)$, $K = L$, and, as has been explained above, $C = E(0)$.
Replacing $S$, $K$, and $C$ in (7.5) by these values we obtain (7.4).

**Corollary 7.2.10.** If we know $E(0)$ (which may often be the case) then there is just one unknown
variable in (7.4), namely $B(0)$. We can solve (7.4) numerically and thus compute $B(0)$.
Similarly, if $B(0)$ is known then $E(0)$ can be computed as solution to (7.4).
Finally, if $F(0)$ is known then we compute $E(0)$ using (7.4) and find $B(0) = F(0) - E(0)$.

**Corollary 7.2.11.** If we know $F(0)$ then we can find the probability of default:

```math
P(\text{default}) = P(F(T) < L).
```

## Credit derivatives

Credit derivatives emerged in the early 1990s, and represent a fairly new asset class compared with
more traditional derivatives. The size of the credit derivatives market in 2018 exceeded USD 4
Trillion. Types of credit derivatives include: credit options, credit swaps, credit default swaps, asset
backed securities and credit linked notes.
Basics about Credit Derivatives:

• Underlying assets are credit assets, such as debt or fixed income securities.

• Used to transfer the credit risk of such securities without trading the underlying asset itself.

• Popular with financial institutions, MNEs and other market participants, credit derivatives are
used to reduce credit risk, diversify portfolios and hedge against changing market rates or
conditions.

Credit Ratings

• There are several credit rating agencies that rate corporate bonds, for example, Standard &
Poor's, Moody's, and Fitch.

• Standard & Poor's ratings are AAA, AA, A, BBB, BB, B

• Moody's ratings are Aaa, Aa, A, Baa, Ba, B

Particular credit derivatives are credit options:

• Similar to options for other markets, except that their payoffs are linked with changes in credit
conditions (for instance, credit options on a corporate bond are linked with changes in credit
ratings).

• These derivatives can also be linked with changes in credit spreads (for example, the strike
price might be a pre specified spread between AAA and BBB rated corporate bonds).

Example of a credit option:

• Company Y wants to issue $8 Million in corporate bonds in three months time, expecting they
will be rated AAA.

• Currently, AAA rated debt securities are trading in the market at 20 basis points (bps) above
Treasury bills.

• Company Y could buy a credit option with the spread as the underlying and a strike price of
20 bps.

• If this pre specified credit spread of 20 bps increases in three months time, the bonds will have
to be issued by Company Y at a higher interest rate

• However, Company Y's additional cost will be offset by the credit option payoff.

Credit Default Swaps (CDS)

• The CDS buyer pays a premium to the CDS seller for protection against default by the reference
entity (i.e. the debt issuer/borrower).

• If there is a credit event (e.g., the reference entity defaults on a pre specified number of
payments), the CDS buyer receives compensation from the CDS seller.

• For instance, the CDS buyer could sell his debt at a pre-agreed price to the CDS seller. The
contract could also be financially settled.

Figure 7.1 illustrates an interest rate swap.

                                Credit Default Swap
                                       Premium - paid for the lifetime of the
                                           contract or until credit event


                                    CDS                                   CDS
                                   Buyer                                 Seller

                                           Payoff in the case that the
                                            reference entity defaults

Benefits of CDS

• Credit risks can be traded in the same manner as market risks.

• A CDS can be used to transfer credit risks to a third party

• This instrument allows credit risks to be diversified.

## Two-state intensity-based model for credit ratings

A two-state model for credit rating is the simplest example of the so called reduced-form model (see
Introduction). An intensity-base model is a particular type of continuous time reduced-form model
which is defined as follows.

**Definition 7.4.1.** A two-state model assumes that:

1.  At each time t, a corporate entity can be in one of two states:

    (a) N =not previously defaulted;
    (b) D =defaulted.

    Denote by X(t) the state of the corporate at time t, that is either X(t) = N or X(t) = D.

2.  There is a function λ(t) ≥ 0 called the hazard rate such that for ∆t > 0 the following
    relations hold:

```math
P(X(t + \Delta t) = N \mid X(t) = N) = 1 - \lambda(t)\Delta t + o(\Delta t)
```

and

```math
P(X(t + \Delta t) = D \mid X(t) = N) = \lambda(t)\Delta t + o(\Delta t)
```

where $o(\Delta t)$ is the so called "o small of $\Delta t$": $\lim_{\Delta t \to 0} \frac{o(\Delta t)}{\Delta t} = 0$.
$\lambda(t)$ is called the transition intensity from $N$ to $D$.

3. Let $\tau$ be the time of default. If the corporate defaults then the bond payments are reduced
    by a deterministic factor:

```math
\text{payment} = \begin{cases} 1 & \text{if } \tau > T \text{ (no default by time } T\text{)}, \\ \delta & \text{if } \tau \leq T \text{ (default takes place by time } T\text{)}. \end{cases}
```

    where $0 \leq \delta < 1$, $T$ is the maturity time of the bond.

4.  The interest rate compounded continuously is r (and does not depend on t).

### Probability of default and the distribution of the time of default

The default of a bond takes place if $\tau \leq T$ and so the probability of default is

```math
P(\text{default}) = P(\tau \leq T)
```

Recall that the cumulative distribution function of the time of default $\tau$ is defined by $F_\tau(t) = P(\tau \leq t)$. We shall prove the following theorem.

**Theorem 7.4.2.** For $t \geq 0$

```math
F_\tau(t) = 1 - e^{-\int_0^t \lambda(s)\,ds}
```

_Proof._ Define $p(t) = P(\tau > t)$. Obviously $F_\tau(t) = 1 - p(t)$ and hence, in order to prove Theorem 7.4.2 it suffices to prove the following equivalent statement:

```math
p(t) = e^{-\int_0^t \lambda(s)\,ds}
```

In turn, (7.8) will be deduced from the following lemma.

**Lemma 7.4.3.**

```math
p'(t) = -\lambda(t)p(t)
```

_Proof._ Note that for $\Delta t > 0$

```math
p(t + \Delta t) = P(\tau > t + \Delta t) \overset{(*)}{=} P(\tau > t + \Delta t \text{ and } \tau > t) \overset{(**)}{=} P(\tau > t)P(\tau > t + \Delta t \mid \tau > t)
```

We use here two facts which you know from the Introduction to Probability course:
(a) $(*)$ follows from $P(A) = P(A \cap B)$ if $A \subset B$
(b) $(**)$ follows from $P(A \cap B) = P(B)P(A \mid B)$ for any two events $A$ and $B$.
Here $A = \{\tau > t + \Delta t\}$, $B = \{\tau > t\}$.
It follows that

```math
\begin{aligned}
p(t + \Delta t) &= p(t)P(\tau > t + \Delta t \mid \tau > t) \\
&= p(t)P(X(t + \Delta t) = N \mid X(t) = N) = p(t)(1 - \lambda(t)\Delta t + o(\Delta t)),
\end{aligned}
```

where we use the equality of events $\{\tau > t\} = \{X(t) = N\}$ and the definition of the model. We
thus have proved that

```math
p(t + \Delta t) = p(t)(1 - \lambda(t)\Delta t + o(\Delta t)) = p(t) - \lambda(t)p(t)\Delta t + o(\Delta t)
```

Rearranging this equality we obtain

```math
\frac{p(t + \Delta t) - p(t)}{\Delta t} = -\lambda(t)p(t) + \frac{o(\Delta t)}{\Delta t}
```

Taking the limit of both parts of the last equation as $\Delta t \to 0$ we obtain

```math
p'(t) = \lim_{\Delta t \to 0} \frac{p(t + \Delta t) - p(t)}{\Delta t} = -\lambda(t)p(t) + \lim_{\Delta t \to 0} \frac{o(\Delta t)}{\Delta t}
```

or $p'(t) = -\lambda(t)p(t)$. Lemma is proved.
It remains to establish (7.8). To this end, rewrite (7.9) as

```math
\frac{p'(t)}{p(t)} = -\lambda(t) \quad \text{or, equivalently} \quad (\ln(p(t)))' = -\lambda(t)
```

Integrating the last relation gives

```math
\int_0^t (\ln(p(s)))' \,ds = -\int_0^t \lambda(s)\,ds \quad \text{and hence} \quad \ln(p(t)) - \ln(p(0)) = -\int_0^t \lambda(s)\,ds
```

It follows that $\frac{p(t)}{p(0)} = \exp\left(-\int_0^t \lambda(s)\,ds\right)$ and so

```math
p(t) = p(0)e^{-\int_0^t \lambda(s)\,ds}
```

Note that $p(0) = 1$ because the time of default is always strictly positive (no corporate can start its
existence by defaulting). This proves (7.8). Also the theorem is now proved.

**Corollary 7.4.4.** The probability of default is given by

```math
P(\text{default}) = P(\tau \leq T) = 1 - e^{-\int_0^T \lambda(s)\,ds}
```

**Remarks 7.4.5.** 1. We computed $F_\tau(t)$ for $t \geq 0$. It is obvious that $F_\tau(t) = 0$ if $t < 0$.
(Nevertheless, explain this statement.) 2. If $\lambda > 0$ does not depend on $t$ then $F_\tau(t) = 1 - e^{-\lambda t}$ and the probability density function of
$\tau$ is

```math
f_\tau(t) = F'(t) = \lambda e^{-\lambda t} \quad \text{if } t \geq 0 \quad (\text{and } f_\tau(t) = 0 \text{ if } t < 0).
```

We thus see that $\tau$ is an exponential random variable, $\tau \sim \text{Exp}(\lambda)$, if $\lambda > 0$ does not depend
on $t$. 3. The probability that default will eventually happen is 1 if and only if $\int_0^\infty \lambda(s)\,ds = \infty$. Exercise.
Prove this statement.

### Bonds in the framework of the two-state model

Let $B(t, T)$ be the (risk neutral) price at time $t$, $0 \leq t \leq T$, of the bond with the payoff function $R(T)$

```math
R(T) = \begin{cases} 1 & \text{if } \tau > T \text{ (no default by time } T\text{)}, \\ \delta & \text{if } \tau \leq T \text{ (default takes place by time } T\text{)}. \end{cases}
```

The question is: how do we compute $B(t, T)$?
By the general rule (Theorem 5.6, Notes 3), $B(t, T) = e^{-rT}\tilde{E}(R(T))$. Here, as usual, $\tilde{E}$ is the
expectation over the risk-neutral probability. To proceed, we need the following statement which we
shall use without proof.
Statement. There exists the risk-neutral intensity $\tilde{\lambda}(t)$ which can be used to compute prices of
derivatives related to the two-state model.
Suppose that $\tilde{\lambda}(t)$ is known to us and that the risk-neutral probabilities can be computed in the
same way as the real life probabilities discussed above: the only difference is that $\lambda(t)$ should be
replaced by $\tilde{\lambda}(t)$.

**Example 7.4.6.** The real-life probability of default is given by (7.10). Hence, the risk-neutral
probability of this event is

```math
\tilde{P}(\tau \leq T) = 1 - e^{-\int_0^T \tilde{\lambda}(s)\,ds}
```

Similarly,

```math
\tilde{P}(\tau > T) = e^{-\int_0^T \tilde{\lambda}(s)\,ds}
```

It is now easy to compute $B(0, T)$ in terms of $\tilde{\lambda}(s)$. Namely, $R(T)$ is a random variable taking
values 1 and $\delta$. Hence

```math
\tilde{E}(R(T)) = 1 \times \tilde{P}(R(T) = 1) + \delta \times \tilde{P}(R(T) = \delta)
```

Since $\tilde{P}(R(T) = 1) = \tilde{P}(\tau > T)$ and $\tilde{P}(R(T) = \delta) = \tilde{P}(\tau \leq T)$ we obtain (using (7.11) and (7.12)):

```math
\tilde{E}(R(T)) = \tilde{P}(\tau > T) + \delta\,\tilde{P}(\tau \leq T) = e^{-\int_0^T \tilde{\lambda}(s)\,ds} + \delta\left(1 - e^{-\int_0^T \tilde{\lambda}(s)\,ds}\right) = (1 - \delta)e^{-\int_0^T \tilde{\lambda}(s)\,ds} + \delta
```

Finally,

```math
B(0, T) = e^{-rT}\left[(1 - \delta)e^{-\int_0^T \tilde{\lambda}(s)\,ds} + \delta\right]
```

How can we compute $B(t, T)$ when $0 < t \leq T$, conditional on no default before time $t$?

**Exercise 7.4.7.** Prove that

```math
B(t, T) = e^{-r(T-t)}\left[(1 - \delta)e^{-\int_t^T \tilde{\lambda}(s)\,ds} + \delta\right]
```

Hint. You can view the whole process as starting at time $t$ rather than 0 and take into account that
in this case the duration of the process is $T - t$.

## The Jarrow-Lando-Turnbull (JLT) model

The JLT model is an example of a more realistic reduced-form model which describes the behaviour
of the ratings of bonds.
Ratings of bonds are provided by well-established rating agencies, such as Standard & Poor's
(S&P) and Moody's. E.g., the Standard&Poor's ratings are
AAA, AA, A, BBB, BB, B, CCC, D,
where AAA is the best value of the rating, AA is the next one, ... , and D means default.
Example In 2014 one of the Barclays' bonds was rated BBB by the Standard&Poor's.

**Remark 7.5.1.** The above list of possible values of a rating is just an example which is suffi-
cient for our purposes. In reality, S&P provide also more finely tuned values of a rating such as
AAA+, AAA−, etc.

### Definition of the JLT model

Suppose that the rating of a bond can take n different values: 1, 2, ..., n−1, n, where 1 corresponds
to the best rating, 2 correspond the next one, ..., n corresponds to D (default).
In the above example n = 8 with rating 1 corresponding to AAA, 2 corresponding to AA, ..., 7
corresponding to CCC, and 8 corresponding to D.
Denote by X(t) the rating of the bond at time t ≥ 0. So, X(t) takes one of the values from
the range $1, 2, \ldots, n$. As time progresses, the rating may change, say from $X(s) = i$ to $X(t) = j$
(where $t \geq s$). Let $p_{ij}(s, t)$ be the conditional probability of the event that the rating of the bond
at time $t$ will be $j$ given that at time $s$, $s \leq t$, it is $i$:

```math
p_{ij}(s, t) = P(X(t) = j \mid X(s) = i), \quad \text{where } 1 \leq i, j \leq n;\; s \leq t
```

**Definition 7.5.2.** The JLT model assumes that for $\Delta t \geq 0$

```math
p_{ij}(t, t + \Delta t) = \lambda_{ij}(t)\Delta t + o(\Delta t) \quad \text{if } i \neq j
```

```math
p_{ii}(t, t + \Delta t) = 1 - \lambda_{ii}(t)\Delta t + o(\Delta t)
```

where $\lambda_{ij}(t) \geq 0$ are the transition intensities satisfying

```math
\lambda_{ii}(t) = \sum_{\substack{1 \leq j \leq n \\ j \neq i}} \lambda_{ij}(t)
```

The following very important fact is proved in the theory of Markov chains.
Statement. If $\lambda_{ij}(t)$ are known then $p_{ij}(s, t)$ can be computed.

**Remarks 7.5.3.** Here are several concluding remarks.

1.  The JLT model is used for solving problems similar to the ones discussed in the previous section
    (e.g., computing the probabilities of default and the related bond prices).

2.  Those who are familiar with the theory of random processes may have noticed that the JLT
    model is a particular example of a continuous time Markov chain.

3.  It is obvious that $\sum_{j=1}^{n} p_{ij}(s, t) = 1$ (but do explain this statement!). This equality implies
    that (7.13) is satisfied.
    Exercise. Prove this fact.

4.  By the definition of default, $p_{n,n}(s, t) = 1$ (and hence $p_{n,j}(s, t) = 0$ for $j \neq n$). In terms of
    the theory of Markov chains, $n$ is the so called absorbing state: if at some (random) moment
    $\tau$ the process $X$ reaches $n$, $X(\tau) = n$, then it remains in this state for ever.

5.  A more advanced theory of credit risk deals also with intensities $\lambda_{ij}(t)$ which are themselves
    random processes.

## Copula models

With respect to credit risk, copulas are useful for modelling random vectors of dependent risk factors.
We begin by covering general principles of copula models and then focus on the Gaussian copula
model.
Default correlation is the likelihood of two firms defaulting at approximately the same point in
time. Reasons for this:

• External events can similarly affect firms within the same industry or geographic region; thus,
financial hardship can hit such firms all at once.

• Economic conditions, particularly periods of recessions can result in an increase in default
rates, and credit contagion to be more prevalent.

Given default correlation, we can't completely rid ourselves of credit risk through diversification. In
previous lectures, we've already covered two types of default correlation models: Intensity based (or
reduced form) models and structural models.
The Gaussian copula model is similar in structure to Merton's model. This model addresses
default correlation by:

• Assuming all firms will eventually default

• Trying to measure, for two or more firms, the correlation between their probability distributions
of default times.

We first define the following for the model framework:

• T1 = time to default of firm 1

• T2 = time to default of firm 2.

Note that we are turning to the Gaussian copula model because the probability distribution of a
firm's default time is not normal.
Next, we transform our default times and into normally distributed variables $X_1$ and $X_2$ as
follows:

```math
X = \Phi^{-1}[Q_1(T_1)], \quad Y = \Phi^{-1}[Q_2(T_2)]
```

where $Q_1$ and $Q_2$ are the cumulative probability distributions for $T_1$ and $T_2$ and $\Phi^{-1}$ is the inverse
of the cumulative normal distribution ($u = \Phi^{-1}(v)$ when $v = \Phi(u)$). The random variables are each
standard normal. We further suppose that they are jointly bivariate normal distributed. This means
their joint p.d.f. is

```math
f_{X,Y}(x, y) = \frac{1}{2\pi\sqrt{1 - \rho^2}} \exp\left(-\frac{1}{2(1 - \rho^2)}\left(x^2 - 2\rho xy + y^2\right)\right)
```

where $\rho$ is the correlation $\rho = \text{Corr}(X, Y)$. Thus, only one parameter $\rho$, the copula correlation,
needs to be specified. The Gaussian copula model is also very convenient since it can be extended to
the case of several firms, using the multivariate normal distribution instead of the bivariate normal
distribution.
Generally, we use a one-factor Gaussian copula model. This allows us to avoid defining a different
correlation between and for each pair of firms. We assume that

```math
X_i = a_i F + \sqrt{1 - a_i^2}\,Z_i
```

where $F$ is a common factor affecting defaults for all companies and $Z_i$ is a factor affecting only
company $i$. The $F$ and $Z_i$ all have standard normal distributions. The $a_i$ are parameters, $-1 \leq a_i \leq 1$. The correlation between $X_i$ and $X_j$ is $a_i a_j$.
Now, define $Q_i(t)$ as the probability that firm will default by time $t$. According to our model, a
default event occurs by time $t$ when $T \leq t$, i.e.

```math
\Phi(X_i) \leq Q_i(t)
```

or

```math
X_i \leq \Phi^{-1}(Q_i(t))
```

This condition is equivalent to

```math
a_i F + \sqrt{1 - a_i^2}\,Z_i \leq \Phi^{-1}(Q_i(t))
```

or

```math
Z_i \leq \frac{\Phi^{-1}(Q_i(t)) - a_i F}{\sqrt{1 - a_i^2}}
```

Hence, the probability of default (conditional on the value of $F$) is

```math
Q_i(t \mid F) = \Phi\left(\frac{\Phi^{-1}(Q_i(t)) - a_i F}{\sqrt{1 - a_i^2}}\right)
```

Finally, let's consider a specific scenario of the one-factor Gaussian copula model. Suppose that

default probability distributions $Q_i$ for all $i$ are equivalent: $Q_i(t) = Q(t)$. For all firm pairs
suppose that $a_i = \sqrt{\rho}$ for all $i$, where $\rho$ is the common correlation. The last equation turns into

```math
Q(t \mid F) = \Phi\left(\frac{\Phi^{-1}(Q(t)) - \sqrt{\rho}\,F}{\sqrt{1 - \rho}}\right)
```

---

# Chapter 8: Credit Risk Management and Valuation Adjustment

## Review of general concepts

We've seen that credit risk applies to many different financial transactions, for example, when
purchasing a bond, entering into a loan, or selling CDS protection. Credit loss risk is typically
affected by three related quantities, as we have seen in credit risk models covered in previous
lectures:

• Exposure at default

• Probability of default

• Loss (or recovery) given default

All three quantities are used by Basel in the determination of capital requirements for portfolios with
credit risk.
Exposure at default, the first of our three quantities, reflects the fact that credit risk exposure
for many securities is dependent upon the precise time of default. In the case of purchasing a bond
or making a loan, for example, our exposure primarily consists of the principal amount, with added
uncertainty regarding potential losses from coupon or interest payments. The use of credit lines
poses another source of exposure.
In the case of OTC derivatives, exposure to counterparty risk is more problematic to measure:
There is a random variable involved, representing unknown default time of counterparty. A derivative
value evolves up to the point of counterparty default time. An example is interest rate swaps.
The use of collateral also affects the level of credit risk exposure. Collateral reduces exposure
and helps to mitigate losses.
Probability of default, our second measure, provides an estimate of default occurring by a
specified time horizon. This quantity is related to the obligor's credit quality or credit worthiness.
When concerned with securities in which loss depends on the exact default time, such as OTC
derivatives subject to counterparty credit risk, the entire distribution of possible default times is
taken into account, rather than simply the default probability by a fixed time horizon.
Loss given default is used to explain the percentage of the credit risk exposure that is actually
lost when a default event occurs. Similarly, it can describe the recovery in the case of default, in
which case it quantifies the proportion of the exposure that can be recovered (for example, through
the process of debt restructuring and asset sales).

     An example of loss (or recovery) given default is a bond issuer going into administration. In

this scenario, bondholders will be partly compensated for losses (of principal and coupon payments)
from the sale of the company's assets.
Another common example is when the holder of a residential mortgage defaults. In this case,
proceeds from the sale of the property (the collateral asset) by the bank will make up for some of
the lost principal and interest.
Exposure at default, probability of default and loss (recovery) given default are dependent quan-
tities. Hence, when modelling, it's important to recognise that it is not realistic to model them as
independent random variables. For instance, consider a period of financial distress:
• Probability of defaults will generally increase, while firm asset values decline.
• Subsequently, recoveries will also be expected to be low.
• Hence, there will be a positive dependence between the probability of default and loss given
default.

## Credit risk management

There are several ways to mitigate credit risk, including the following:
• Netting
• Collateralization
• Downgrade trigger
• Hedging
Netting consists of the offsetting of contracts that have positive and negative values in the
event of a counterparty default. It is also used in determining collateral requirements. This method
is one way that financial institutions (i.e. banks) attempt to reduce their credit risk in bilaterally
cleared transactions.
Collateral agreements are another important means of reducing credit risk: Collateral can be
in the form of cash (which earns interest) or marketable securities (property and other real assets,
for example). In the case of derivatives transactions, the party which does not default is entitled to
keep any collateral put up by the defaulting party.
Downgrade trigger is another risk mitigation method: This represents a contractual clause
stating that if the credit rating of the counterparty declines below a specified level, (for example,
below Bbb), the financial institution has the option of closing out all outstanding derivatives trans-
actions at market value. A downgrade trigger provides protection against small changes in credit
ratings, but not large ones (for instance, falling from Aaa to default).
Hedging credit risk through derivatives has already been covered.

## CVA and DVA

Derivative valuations typically assume that neither party will default. A separate calculation is
usually done for the consideration of credit risk. The credit value adjustment (CVA) accounts for
this counterparty credit risk and makes appropriate adjustment to the derivative's market value. A
bank, for instance, will estimate the present value of the expected cost it might face in the case of
a default event by the counterparty.
Let's consider the example of a bank and counterparty that have entered into a bilaterally cleared
derivatives portfolio.

• Netting will most likely apply here, meaning that in the case of default all outstanding deriva-
tives will be considered as a single derivative.
• If the counterparty party fails to fulfil the terms of agreement (for example, by failing to post
collateral, making payments or declaring bankruptcy), the bank can declare a default event.
• The default event will result in the closing out of any outstanding transactions in the derivatives
portfolio.
Following from the previous example, we could have two scenarios at the time of a default event:
• The value of the derivatives portfolio is positive for the bank and negative for the counterparty,
in which case the bank will face a loss because the full value of the portfolio can't be recovered.
• Conversely, if the value of the portfolio is negative for the bank but positive for the counterparty,
the bank will not incur a loss.
Suppose that the life of the longest outstanding derivatives transaction between the bank and
the counterparty is T years. In order to calculate CVA, the bank in our example would break up
the next T years (T representing the derivative with the longest transaction time between the two
parties involved) into intervals. The following would then be computed for each of these intervals:
• qi = The probability of an early termination because of a default event during interval .
• vi = The present value of expected loss of the portfolio because of a default event at the
midpoint of interval .
We then compute CVA as follows:

```math
\text{CVA} = \sum_{i=1}^{N} q_i v_i
```

where $N$ is the number of intervals. Note that the computation of the parameters involved, especially
for the determination of vi , can be fairly complex.
The previous CVA example only took into account the possibility of default by the counterparty.
But what about the possibility of the bank defaulting? This leads us to the concept of debit value
adjustment (DVA). DVA is calculated as the present value of the expected gain due to the bank
itself defaulting. The computation is comparable to our CVA formula: In the calculation for DVA,
we have:
• qi∗ = The probability of the bank defaulting during interval.
• vi∗ = The present value of the gain to the bank (meaning a loss to the counterparty) if the
bank itself defaults at the midpoint of interval .
If both CVA and DVA values are considered, the derivative portfolio's value to the bank becomes:

```math
f_{\text{nd}} - \text{CVA} + \text{DVA}
```

where $f_{\text{nd}}$ is the no-default value of the derivatives portfolio to the bank.
We now turn to CVA and DVA in derivatives transactions. A credit spread is the excess of
the interest rate on a loan over the risk-free interest rate. Our first step in valuing a transaction
is to estimate credit spreads for the counterparty. We do this for several different maturities. Next
we estimate the counterparty's credit spread, s(ti ), for maturity ti , using interpolation. Recall the
definition of hazard rate $\lambda(t)$ in Definition 7.4.1. The average hazard rate in the interval $[0, T]$ is

```math
\tilde{\lambda}(T) = \frac{1}{T} \int_0^T \lambda(t) \, dt
```

Suppose that the bond yield spread for a T -year bond is s(T ) per annum. This means that the
average loss rate on the bond between time 0 and time T should be approximately s(T ) per annum.
Another expression for the average loss rate is $\tilde{\lambda}(T)(1 - R)$, where $R$ is the estimated recovery rate.
This means that it is approximately true that

```math
\tilde{\lambda}(T)(1 - R) = s(T)
```

or

```math
\tilde{\lambda}(T) = \frac{s(T)}{1 - R}
```

For an estimate of the average hazard rate for the counterparty between times 0 and ti , we therefore
use:

```math
\frac{s(t_i)}{1 - R}
```

where $R$ is the expected recovery rate in the case of default by the counterparty. The probability of
no-default by of the counterparty by time $t_i$ is then

```math
\exp\left(-\frac{s(t_i) \, t_i}{1 - R}\right)
```

The previous expression signifies that:

```math
q_i = \exp\left(-\frac{s(t_{i-1}) \, t_{i-1}}{1 - R}\right) - \exp\left(-\frac{s(t_i) \, t_i}{1 - R}\right)
```

This equation represents the probability of default by the counterparty during interval i . In a similar
manner, we can also compute the probability qi∗ from the credit spreads of the bank.
The calculation of variables vi and vi∗ is computationally more intensive, requiring the use, for
example, of Monte Carlo simulation. Using Monte Carlo simulation, no-default values between times
0 and T of outstanding derivatives transactions in the portfolio are determined by simulating market
variables. The bank's exposure to the counterparty at the midpoint of each interval is computed
in each Monte Carlo simulation trial. The resulting exposure is equivalent to max(V, 0), with V
representing the bank's total transaction value: If V is negative, there is no exposure to the bank;
if V is positive, then the bank's exposure is equivalent to this total transaction value. Following
our Monte Carlo simulations, vi becomes the present value of the average exposure across all trials,
multiplied by 1 − R. In a similar manner, we compute vi∗ .

---