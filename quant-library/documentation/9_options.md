# Options

## Introduction

- Options are contracts between two counterparties that gives one counterparty *the right but not the obligation* to buy/sell a particular asset to/from the other counterparty at a price agreed to upon entering the contract.
  - An option to **buy** is called a **call**.
  - An option to **sell** is called a **put**.
  - The counterparty with the option is the **buyer** or **holder** and they will **exercise** the option upon deciding to buy or sell at the agreed price.
  - The counterparty which must accept the decision of the buyer is the **seller** or **writer** of the option.
- Option contracts will have a predefined **specification** that states the **underlying** asset, the **quantity** of that asset, the **type** (call/put), the **strike** price, and the **expiration** date of the contract.
  - The **strike price** is the price at which the underlying asset will be bought or sold should the option be exercised.
- The **option premium** is the price paid by the buyer of an option contract to the writer/seller, compensating the writer for the risks involved with issuing the associated rights.
  - Without an option premium, there would be an arbitrage opportunity as option buyers have no downside risk other than the price paid to enter into the option contract.
- There are different convention for exercising options with the two most common being:
  - **European options** can only be exercised at the expiration date.
  - **American options** can be exercised at any time between the contract origination and expiry.
- Options are written on stocks, indexes, currencies, commodities, interest rate products and on the futures contracts of these products (most commodity option contracts are options on futures).
- Options trade both over-the-counter (OTC) and on futures exchanges.
  - Similar to forward contracts, there is a large amount of counterparty credit risk on OTC options, whilst exchange traded options are margined and marked to market which minimises this risk.
- The following terminology is used for positions in options:
  - A **long position** is held by the option holder.
  - A **short position** is held by the option writer.
- There are 4 basic option positions that a market participant can take:
  1. a **long call** - buying the right to purchase an asset at a particular strike.
  2. a **long put** - buying the right to sell an asset at a particular strike.
  3. a **short call** - writing/selling the right to purchase an asset at a particular strike.
  4. a **short put** - writing/selling the right to sell an asset at a particular strike.
- The status of an option with regards to the underlying asset's spot price is denoted as **moneyness** and has the following terminology:
  - **In the money** if a call's strike is less than the underlying's spot or a put's strike is greater than the underlying's spot.
  - **Out the money** if a call's strike is greater than the underlying's spot or a put's strike is less than the underlying's spot.
  - **At the money** when the strike for either a call or put is equal to the underlying's spot.

### Basic Example: European Call

- An investor has paid a 10 USD premium for a European call with a strike price of 60 USD.
- The circumstances under which the option should be exercised:
  - If the underlying asset's spot price is greater than 60 USD, the option is likely to be exercised as it allows the buyer to purchase the asset at a cheaper price compared to the market.
- If the underlying asset's spot price is 75 USD at the option expiration, the net profit made by immediately selling the underlying asset on the market will be 5 USD ($75 - (60 + 10)$).
- If the underlying asset's spot price is 40 USD at the option expiration, the option buyer will not exercise the option and a net loss of 10 USD will be incurred.

### Assumptions

- Unless stated otherwise:
  - The options will be treated as european style.
  - The underlying assets will be a stock paying no dividends (i.e. no income).

## Option Payoffs

- The option payoff is central to valuing the option and uses the same principals as the [payoffs for derivatives contracts](./7_forwards_futures_swaps.md#payoffs) where the payoffs are equal to the revenue paid to a particular counterparty (either the long or short position).
- For European options which have a single expiration date, the option payoff will be equal to the option value at the time of the payoff (option expiration).
- The notation used for option pricing will extend the notation used so far:
  - $S(t)$ will be the price of the underlying asset at time $t$.
  - $K$ is the strike price.
  - $T$ is the expiration date.
  - The premium, when taking a long position in the call ($C$) or put ($P$), is denoted by any of the following:
    - $C(S(t))$ or $P(S(t))$ - dependent on the price of the underlying asset.
    - $C(S(t), t)$ or $P(S(t), t)$  - as above and also dependent on time $t$.
    - $C(S(t),t;K,T)$ or $P(S(t),t;K,T)$  - as above and also dependent on the strike $K$ and expiration date $T$.

### Long Call Payoff

- If an investor holds a long position in a European call option, then at the expiration date $T$, the investor has the right to buy the underlying asset at the strike price $K$.
- It only makes sense for the investor to exercise the option if the strike $K$ is less than the spot price of the underlying asset at the expiration date $S(T)$
- Assuming $S(T) > K$, the payoff from immediately selling the underlying asset at the expiration date is $S(T) - K$.
- If $S(T) \leq K$ then the option will not be exercised and the payoff will be 0.
- The long call payoff can be written as follows:

```math
\begin{aligned}
C(S(T), T) &=
\begin{cases}
S(T) - K &S(T) > K \\
0 &S(T) \leq K
\end{cases} \\\\
&=\text{max}\{0,S(T)-K\}
\end{aligned}
```

  ![Long Call Profit](images/long-call.png "Long Call Profit")

### Short Call Payoff

- The short call payoff is the negative of the [long call payoff](#long-call-payoff):
$$-C(S(T),T) = - \text{max}\{0,S(T)-K\}$$

  ![Short Call Profit](images/short-call.png "Short Call Profit")

### Long Put Payoff

- A long position in a European put provides the right to sell the underlying for the strike price $K$ at contract expiration $T$.
- Assuming $S(T) < K$, the payoff from buying the underlying asset at the spot rate and selling to the short position for $K$ at the expiration date is $K - S(T)$.
- If $S(T) \geq K$ then the option will not be exercised and the payoff will be 0.
- The long put payoff can be written as follows:

```math
\begin{aligned}
P(S(T), T) &=
\begin{cases}
K - S(T) &S(T) < K \\
0 &S(T) \geq K
\end{cases} \\\\
&=\text{max}\{0,K-S(T)\}
\end{aligned}
```

  ![Long Put Profit](images/long-put.png "Long Put Profit")

### Short Put Payoff

- The short put payoff is the negative of the [long put payoff](#long-put-payoff):
$$-P(S(T),T) = - \text{max}\{0,K-S(T)\}$$

  ![Short Put Profit](images/short-put.png "Short Put Profit")

## Arbitrage Bounds on Option Prices

- From the Law of One Price, the following equalities apply to option prices:
  - Call prices:
    - Less than or equal to the underlying price: $C(t) \leq S(t)$
    - Greater than or equal to the long forward position: $C(t) \geq S(t) - e^{-r(T-t)}K$
  - Put prices:
    - Less than or equal to the discounted strike price: $P(t) \leq e^{-r(T-t)}K$
    - Greater than or equal to the short forward position: $P(t) \geq e^{-r(T-t)}K - S(t)$

### Arbitrage Inequality Example 1: Call Price Less Than Underlying Price

- To demonstrate that $C(t) \leq S(t)$ due to arbitrage principles, start by assuming that the opposite is true: $C(t) >S(t)$ at time $t$.
- The following arbitrage portfolio can be constructed:
  - Sell/write a call on a stock collecting cash for the price of the call $C(t)$.
  - Purchase the underlying stock, paying $S(t)$.
- This results in a cash of holding of $C(t) - S(t) > 0$ due to the (incorrect) earlier assumption.
  - This cash sum is invested at the risk free rate $r$.
- At the expiration of the call, the portfolio consists of:
  - A short position on the call.
  - A long position on the underlying stock.
  - A cash holding now worth $e^{-r(T-t)}(C(t) - S(t))$.
- If, at the expiration, the call is out of the money ($S(T) \leq K$) then the option will **not** be exercised and will expire worthless.
  - This results in a portfolio worth $e^{-r(T-t)}(C(t) - S(t)) + S(T) > 0$
- Alternatively, if the call is in the money ($S(T) > K$) at expiration, the option will be exercised and the long position in the underlying stock will be sold for the strike price $K$.
  - This results in a portfolio worth $K + e^{-r(T-t)}(C(t) - S(t)) > 0$
- In both these scenarios, a profit has been retained that is *risk-free* and therefore, if $C(t) > S(t)$, there will be an arbitrage opportunity.

### Arbitrage Inequality Example 2: Call Price Greater Than Long Forward Position

- Similar to example 1, assume that $C(t) \geq S(t) e-^{-r(T-t)}K$ is not true and that if $C(t) < S(t) -e^{-r(T-t)}K$ is true at time $t$, there will be to an arbitrage opportunity present.
- Rewrite this inequality as $C(t) + e^{-r(T-t)}K < S(t)$ for ease and construct the following arbitrage portfolio:
  - A short position on the underlying stock, receiving $S(t)$ in cash.
  - A long position on the call, paying $C(t)$.
  - Given the inequality, there will be a remaining cash sum equal to $S(t) - C(t)$ which can be invested at the risk-free rate $r$.
- Now rewrite the inequality as follows:

```math
\begin{aligned}
C(t) + e^{-r(T-t)}K &< S(t) \\
e^{r(T-t)}C(t) + K &< e^{r(T-t)}S(t) \\
K &< e^{r(T-t)}(S(t) - C(t)) \\
\end{aligned}
```

- The inequality now shows that the value of the remaining cash sum $S(t) - C(t)$ at time $T$, having been invested at the risk-free rate $r$, is greater than the strike price $K$.
- At the expiration of the call option $T$, the arbitrage portfolio contains the following:
  - The long call position.
  - The short position on the stock.
  - The cash investment with value $e^{r(T-t)}(S(t) - C(t))$.
- If, at the expiration, the call is out of the money ($S(T) \leq K$), which can be written as $S(T) < e^{r(T-t)}(S(t) - C(t))$ using the rearranged inequality, then the option will **not** be exercised and the underlying stock will be bought for $S(T)$ to close the short position in the underlying stock.
  - This results in a portfolio worth $e^{r(T-t)}(S(t) - C(t)) - S(T) > 0$
- Alternatively, if the call is in the money ($S(T) > K$) at expiration, the call option will be exercised by paying the strike price $K$ and using the underlying stock received to close the short position in the underlying stock.
  - This results in a portfolio worth $e^{r(T-t)}(S(t) - C(t)) - K > 0$
- In both these scenarios, a profit has been retained that is *risk-free* and therefore, if $C(t) < S(t) -e^{-r(T-t)}K$, there will be an arbitrage opportunity.

### Extending Option Bounds

- The value of an option will never be negative as options will become worthless when the underlying asset moves out of the money.
  - The largest possible loss for a long position on an option is the price paid to buy the option (the premium).
  - An option with a negative premium would present an immediate arbitrage opportunity.
- The following bounds can therefore also be added for option prices:
  - $C(S(t),t) \geq 0$
  - $P(S(t),t) \geq 0$
- This leads to a combined lower bound for options:
  - $C(S(t),t) \geq \text{max}\{0,S(t) - e^{-r(T-t)}K\}$
  - $P(S(t),t) \geq \text{max}\{0,e^{-r(T-t)}K - S(t)\}$

### Application of Option Bounds Example

- A 1-year call on a stock is currently trading at 65 USD.
- The strike price for this call is 45 USD and the risk-free rate is assumed to be 3%.
- If the call premium is currently 75 USD, there would be an arbitrage opportunity which could be exploited as follows:
  - Check the bounds for call prices to confirm the arbitrage opportunity:
    - Less than or equal to the underlying price: $C(t) \leq S(t)$
    - Greater than or equal to the long forward position: $C(t) \geq S(t) - e^{-r(T-t)}K$
    - Since the underlying stock price $S(t)$ is currently 65 USD which is less than the current 75 USD call price $C(t)$, there is an arbitrage opportunity present: $75 > 65$ so $C(t) > S(t)$
  - The call price is too expensive compared to the stock price, so a short position should be taken in the call option.
  - The cash received from selling the call option can be used to buy the stock, leaving a remaining cash sum of $C(t) - S(t) = 75 - 65 = 10 \text{ USD}$.
  - The remaining cash sum can be invested at the risk-free rate (3%) so after 1 year this remaining cash sum is equal to $e^{r(1)}(C(t) - S(t)) = e^{0.03(1)}(C(t) - S(t)) = 10.30 \text{ USD}$
  - If after 1 year, at the contract expiration, the strike price of the call is less than the spot price of the underlying stock, the call option will be exercised and the long position on the underlying asset will be exchanged for the value of the strike price.
    - This will give a risk-free profit of $K + e^{r(1)}(C(t) - S(t)) = 45 + 10.30 = 55.30 \text{ USD}$
  - If after 1 year, the value of the underlying stock is less than the strike price, the option will not be exercised.
    - This will give a risk-free profit of $S(T) + e^{r(1)}(C(t) - S(t)) = S(T) + 10.30$
  - A minimum of 10.30 USD will be received from exploiting this arbitrage opportunity - a risk-free profit.

### Arbitrage Bounds on American Style Options

- The bounds on american options are calculated for an underlying stock that does not pay dividends.
- The lower bounds for American options are the same as European Options as American style options have more 'optionality' than European style (i.e. American style has the option to be redeemed before the expiry).

#### Intrinsic Value

- The **intrinsic value** of an option is the value that can be recovered from exercising the option at some point in the life of the option.
  - European style options do not have an intrinsic value as they can only be exercised at expiry.
  - For American option holders, the decision to exercise the option will be based on whether the intrinsic value is more or less than the market value of the option.
- Similar to the [long call pay-off](#long-call-payoff) of a European style option, the intrinsic value of a call option is the payoff of the call at time $t$ where $t < T$:

$$C(S(t), t) =\text{max}\{0,S(t)-K\}$$

#### Bounds for American Calls

- An American style call will never be less than a European style call (assuming the same strike and expiry) because of the increased optionality that American options have.
- Denote $C_{A}(S(t), t)$ as the price of an American call, continue to denote a European call as $C(S(t), t)$ at time $t$.
- The lower bound for an American call is therefore:

```math
\begin{aligned}
C_{A}(S(t),t) &\geq C(S(t),t) \\
&\geq \text{max}\{0,S(t) - e^{-r(T-t)}K\} \\\\
\text{With } r > 0 \Longrightarrow \text{max}\{0,S(t) - e^{-r(T-t)}K\} &> \text{max}\{0,S(t)-K\} \\\\
\therefore C_{A}(S(t),t) &> \text{max}\{0,S(t)-K\} \\
&\equiv \text{call's intrinsic value}
\end{aligned}
```

- The market value of an American style call is always more than the intrinsic value.
  - This is because the intrinsic value is the amount that will be the realized from exercising the option early.

    ![American Long Call Profit](images/american-long-call.png "American Long Call Profit")
  - Therefore American options will never be exercised early as their market value (purple line) is greater than their intrinsic value (red and green) - selling the option on the market will return more than exercising the option.
- For an American call on a non-dividend paying stock, the early exercise functionality is essentially worthless as shown so an American option will be worth the same as a European style option.

#### Bounds for American Puts

- An American put can be exercised at any point during the life of the contract, the same as an American call.
- Since exercising a put option will always recover its intrinsic value, the value of an American put can never be less than this intrinsic value.
- Similarly, exercising a put option can never recover more than the strike price due to arbitrage opportunities.
- Therefore the price of an AMerican put $P_{A}(S(t), t)$ will satisfy the following conditions:
$$\text{max}\{0, K - S(t)\} \leq P_{A}(S(t), t) \leq K$$
- Unlike American calls, there are cases where exercising an American put early can be optimal.
  - This cannot be demonstrated using only arbitrage conditions and so a model for the underlying asset is required.

## Put-Call Parity

- Put-call parity is a fundamental concept in options pricing that establishes a relationship between the prices of European call and put options with the same strike price $K$ and expiration date $T$.
- A long call and a short put position is equal to the long forward position:

$$C(t) - P(t) = S(t) - e^{-r(T-t)}K$$

- This relationship can be shown diagrammatically as follows:

    ![Put-Call Parity](images/put-call-parity.png "Put-Call Parity")

### Deriving the Put Call Parity Using Arbitrage principles

- The put-call parity relationship follows from the Law of One Price, and be derived using arbitrage principles.
- First assume that $C(t) - P(t) > S(t) - e^{-r(T-t)}K$
  - This inequality can be rewritten as $C(t) + e^{-r(T-t)}K > P(t) + S(t)$
  - A portfolio can be constructed as follows:
    - A short position on the call $C(t)$
    - A debt of $e^{-r(T-t)}K$
  - By taking these positions, $C(t) + e^{-r(T-t)}K$ will be received in cash.
  - Respecting the inequality, the following positions may also be taken, leaving a small amount of cash:
    - A long position on the put $P(t)$
    - A long position on the stock $S(t)$
    - The remaining cash is now equal to $C(t) + e^{-r(T-t)}K - P(t) - S(t) > 0$ and can be invested at the risk-free rate $r$.
  - At the expiration date $T$, the debt with original value $e^{-r(T-t)}K$ will have a value of $K$.
  - If $S(T) \leq K$, the call $C(T)$ will expire worthless and the put $P(T)$ will be exercised so a cash value of $K$ will be received in exchange for the long position in the underlying stock $S(T)$.
    - This cash received with value $K$ can be used to close the debt of the same value.
  - If $S(T) > K$, the call $C(T)$ will be exercised so the long position in the stock can be sold for $S(T) > K$ and the cash received will be used to close the debt position.
    - The put $P(T)$ will expire worthless.
  - In either case the positions are all closed and a risk-free profit of $e^{r(T-t)} \left(C(t) + e^{-r(T-t)}K - P(t) - S(t) \right) > 0$ is retained.
- Now assume that $C(t) - P(t) < S(t) - e^{-r(T-t)}K$
  - This inequality can be rewritten as $C(t) + e^{-r(T-t)}K < P(t) + S(t)$
  - A portfolio can be constructed as follows:
    - A short position on the put $P(t)$
    - A short position on the stock $S(t)$
  - By taking these positions, $P(t) + S(t)$ will be received in cash.
  - Respecting the inequality, the following position may also be taken, leaving a small amount of cash:
    - A long position on the call $C(t)$
    - The remaining cash $P(t) + S(t) - C(t) > e^{-r(T-t)}K$ can be invested at the risk free rate $r$
  - The inequality can be rewritten as $K < e^{r(T-t)} (P(t) + S(t) - C(t))$
  - At the expiration date $T$, the cash investment will have a value of $e^{r(T-t)} (P(t) + S(t) - C(t)) > K$.
  - If $S(T) \leq K$, the call $C(T)$ will expire worthless and the put $P(T)$ will be exercised so the underlying stock $S(T)$ will be bought for $K$ using the cash investment to close the short position in the put.
    - The short position in the underlying stock can now also be closed.
  - If $S(T) > K$, the call $C(T)$ will be exercised so the short position in the stock can be closed for $K$ using the cash investment.
    - The put $P(T)$ will expire worthless.
  - In either case the positions are all closed and a risk-free profit of $e^{r(T-t)} (P(t) + S(t) - C(t)) - K > 0$ is retained.
- If either of these inequalities are true, an arbitrage portfolio can be constructed leading to the conclusion that $C(t) - P(t) = S(t) - e^{-r(T-t)}K$ must be true.

## The Binomial Model

- Although mathematical simple, the binomial model is a powerful tool for pricing options and other derivatives.
- From the binomial model, the [Black-Scholes Option Pricing Model](#the-black-scholes-option-pricing-model) can be derived.

### One-Step Binomial Model

- In the one-step binomial model, there are only two states/times: $t=0$ at the start and $t=1$.
- Consider a stock with price $S_{0}$ at time $0$ and $S_{t}$ at time $t$ for $t=0,1$.
  - $S_{t}$ is the convention used to denote $S(t)$ in the binomial model - i.e. the price level $S$ is still a function of time $t$.
- At time $t=1$, assume the stock can only take two different values, denoted by $S_{1}(+)$ and $S_{1}(-)$ where $S_{1}(-) < S_{1}(+)$.
  - This assumption is relaxed in later steps.
- $S_{1}$ is a random variable with the probabilities of $S_{1}(+)$ and $S_{1}(-)$ as follows:
  - $\text{Prob}(S_{1}=S_{1}(+)) = p$
  - $\text{Prob}(S_{1}=S_{1}(-)) = q$
  - Given there are only two outcomes: $p + q = 1$
- A derivative asset $D$ is also considered which has the aforementioned stock as the underlying asset and a contract expiry at time $t=1$.
- The values that $D$ can take at time $t=1$, i.e. the payoff of the derivative, are determined by the value of the underlying stock.
  - $D_{1} = D_{1}(+)$ when $S_{1} = S_{1}(+)$
  - $D_{1} = D_{1}(-)$ when $S_{1} = S_{1}(-)$
- $D_{0}$ is the fair value of the derivative at time $t=0$ and must be determined using arbitrage principles.
  - To apply the arbitrage principles, assumed that a risk-free investment with interest rate $r$ can be introduced.
  - Also assume that the interest rate $r$ has the same implicit unit of time and compounding period that the time unit for the binomial model has.
  - Therefore a cash sum with value $K$ invested at the risk-free rate $r$ at time $t=0$ will be worth $K(1+r)$ at time $t=1$, regardless of the value of $S_{1}$

![One-Step Binomial Model](images/one-step-binomial-model.png "One-Step Binomial Model")

#### Example: One-Step Binomial Model

- A stock has an initial value ($t=0$) of 50 and at time $t=1$ the value of the stock has the following probabilities:
  - A value of 65 is $p > 0$
  - A value of 40 is $1-p > 0$
- A call option with strike price 55, expiring at time $t=1$ will have the following payoff values:
  - $D_{1}(+) = \text{max}\{0,65-55\} = 10$
  - $D_{1}(-) = \text{max}\{0,40-55\} = 0$
- Assuming a risk-free interest rate $r$ of 8%, the fair value of the call at time $t=0$ (i.e the premium, denoted as $D_{0}$) can be calculated using arbitrage principles as follows.
  - An arbitrage portfolio can be constructed by purchasing a portion of the underlying stock and a short position on the call.
  - Let $\Delta$ denote the allocation of the stock and $D_{t}$ the value of the call at time $t$.
  - The value of the portfolio at time $t$ is therefore: $V_{t} = \Delta S_{t} - D_{t}$
  - $\Delta$ can be calculated so that at time $t=1$, the value of the portfolio will be the same in both states: $D_{1}(+)$ and $D_{1}(-)$
    - Leading to: $\Delta S_{1}(+) - D_{1}(+) = \Delta S_{1}(-) - D_{1}(-)$
    - This can be rearranged and solved for delta: $\Delta  =  \frac{D_{1}(+)- D_{1}(-)}{S_{1}(+) - S_{1}(-)} = \frac{10 - 0}{65-40}=0.4$
  - A portfolio consisting of 0.4 shares of the stock and a short position in a call option has the same value in both states at time $t=1$.
  - The value can be calculated in either state and will be equal to $V_{t} = \Delta S_{t} - D_{t} = 0.4(65) - 10 = 16$.
  - Therefore $\text{Prob}(V_{1} = 16) = 1$ and the portfolio has the same payoff as an investment at the risk-free rate which has a final value of 16.
  - Discounting the value of $V_{1}$ from $t=1$ to $t=0$ gives $V_{0}$, the value of the portfolio at $t=0$.
    - Therefore: $V_{1} = V_{0}(1 + r) \Longrightarrow V_{0} = \frac{V_{1}}{1 + r} = \frac{16}{1+0.08} = 14.81$
    - At $t=0$, the following is true: $V_{0} = \Delta S_{0} - D_{0}$.
    - Rearranging to solve for $D_{0}$ gives: $D_{0}= \Delta S_{0} - V_{0} = 0.4(50) - 14.81 = 5.19$
  - The fair value of the call premium at time $t=0$ is 5.19, as calculated by arbitrage principles.
  - This technique of applying principles is a simple example of *delta hedging* the option with the underlying asset to create a 'riskless' portfolio.

#### The General Case for the One-Step Binomial Model

##### One-Step Binomial Model Assumptions Recap

- Recapping the arbitrage pricing technique in the [previous example](#example-1-one-step-binomial-model) which assumes the following:
  - The underlying stock price $S_{t}$ has an initial value $S_{0}$ at $t=0$ and has the following probability of taking values $S_{1}(+)$ and $S_{1}(+)$ at time $t=1$:
    - $\text{Prob}(S_{1}=S_{1}(+)) = p$
    - $\text{Prob}(S_{1}=S_{1}(-)) = q$
  - The probabilities have the following relationships:
    - $q=1-p$
    - $0 < p,q$
  - The risk-free interest rate $r$ is such that a cash investment at time $t=0$ with value $K$ will be worth $K(1+r)$ at time $t=1$.
- The following notation to relate $S_{0}$ with $S_{1}(+)$ and $S_{1}(+)$ can be added for completeness:
  - $S_{1}(+) = uS_{0}$
  - $S_{1}(-) = dS_{0}$
  - $0 < d < u$
  - Conceptually, $d < 1 < u$ can also be assumed as generally $S_{1}(-) < S_{0} < S_{1}(+)$
  - $u$ and $d$ are the *gross returns* in the $+$ and $-$ states respectively.
- Arbitrage principles require that $d < 1+r < u$ as the return on the stock cannot be more or less than the return on the risk-free interest rate $r$.
  - If $1+r \leq d$ a risk-free profit could be obtained by borrowing cash at the risk-free rate and purchasing the underlying stock.
  - Similarly, if $u \leq 1+r$, a risk-free profit could be obtained by taking a short position in the underlying stock and investing the proceeds at the risk-free rate.
- As with the [previous example](#example-1-one-step-binomial-model), assume that the derivative with value $D_{t}$ at time $t$ has the stock as the underlying asset, an initial value $D_{0}$, and the following states:
  - $D_{1} = D_{1}(+)$ when $S_{1} = uS_{0}$
  - $D_{1} = D_{1}(-)$ when $S_{1} = dS_{0}$
- The values denoted as $D_{1}(+)$ and $D_{1}(-)$ constitute the payoff of the derivative and are assumed to be known values.

##### One-Step Binomial Model General Case Derivation

- The fair price for $D_{0}$, the initial value at time $t=0$ of the derivative, can be determined using arbitrage principles for the general case as follows:
- Create an arbitrage portfolio with $\Delta$ positions in the underlying stock and a short position in the derivative.
- Choose a value for $\Delta$ that creates a riskless portfolio - where the value of the portfolio at time $t=1$ in both the $+$ and $-$ cases is the same.
- Denote the value function of the arbitrage portfolio as $V_{t} = \Delta S_{t} - D_{t}$ and then solve the following equation to find $\Delta$:

```math
\begin{aligned}
\Delta uS_{0} - D_{1}(+) &= \Delta dS_{0} - D_{1}(-) \\\\
\therefore \Delta &= \frac{D_{1}(+) - D_{1}(-)}{(u-d)S_{0}}
\end{aligned}
```

```math
\begin{aligned}
\Longrightarrow V_{1} &= \Delta S_{1} - D_{1} \\\\
&= \frac{D_{1}(+) - D_{1}(-)}{(u-d)S_{0}}S_{1} - D_{1}
\end{aligned}
```

- This holds true in both the $+$ and $-$ states due to the derivation for $\Delta$ and can therefore be calculated using either state. Hence, for the $+$ state:

```math
\begin{aligned}
\Longrightarrow &S_{1} = uS_{0} \\
\Longrightarrow &D_{1} = D_{1}(+) \\\\
V_{1} &= \frac{D_{1}(+) - D_{1}(-)}{(u-d)S_{0}}uS_{0} - D_{1}(+) \\\\
&= \frac{D_{1}(+) - D_{1}(-)}{(u-d)}u - D_{1}(+) \\\\
&= \frac{(D_{1}(+) - D_{1}(-))u - (u-d)D_{1}(+)}{u-d} \\\\
&= \frac{uD_{1}(+) - uD_{1}(-) - uD_{1}(+) + dD_{1}(+)}{u-d} \\\\
V_{1} &= \boxed{\frac{dD_{1}(+) - uD_{1}(-)}{u-d}}
\end{aligned}
```

- The value of $V_{1}$ is a constant value with probability 1 by arbitrage principles and at time $t=0$, discounting can be applied to find the initial value of the portfolio $V_{0}$:

```math
\begin{aligned}
V_{0} &= \frac{dD_{1}(+) - uD_{1}(-)}{(1+r)(u-d)} \\\\
V_{0} &= \Delta S_{0} - D_{0} \\\\
\Longrightarrow \Delta S_{0} - D_{0} &= \frac{dD_{1}(+) - uD_{1}(-)}{(1+r)(u-d)} \\\\
D_{0} &= \Delta S_{0} - \frac{dD_{1}(+) - uD_{1}(-)}{(1+r)(u-d)} \\\\
\Longrightarrow \Delta &= \frac{D_{1}(+) - D_{1}(-)}{(u-d)S_{0}} \\\\
\therefore D_{0} &= \frac{D_{1}(+) - D_{1}(-)}{(u-d)S_{0}}S_{0} - \frac{dD_{1}(+) - uD_{1}(-)}{(1+r)(u-d)} \\\\
&= \frac{(1+r)(D_{1}(+) - D_{1}(-))}{(1+r)(u-d)} - \frac{dD_{1}(+) - uD_{1}(-)}{(1+r)(u-d)} \\\\
&= \frac{(1+r)(D_{1}(+) - D_{1}(-)) - dD_{1}(+) + uD_{1}(-)}{(1+r)(u-d)} \\\\
&= \frac{(1+r-d)D_{1}(+) + (u-1-r)D_{1}(-)}{(1+r)(u-d)} \\\\
&= \frac{(1+r-d)D_{1}(+)}{(1+r)(u-d)} + \frac{(u-1-r)D_{1}(-)}{(1+r)(u-d)} \\\\
&= \frac{(1+r-d)}{(u-d)} \underbrace{\frac{D_{1}(+)}{(1+r)}}_{\text{Discounted value of } D_{1}(+)} + \frac{(u-1-r)}{(u-d)} \underbrace{\frac{D_{1}(-)}{(1+r)}}_{\text{Discounted value of } D_{1}(-)} \\\\
\end{aligned}
```

- The above formula displays the fair price of the derivative at time $t=0$ as a linear combination of the discounted values it takes at expiry.

#### One-Step Risk Neutral Pricing

- Recalling the following equation as the fair price of a derivative at time $t=0$:
$$D_{0} = \frac{(1+r-d)}{(u-d)} \frac{D_{1}(+)}{(1+r)} + \frac{(u-1-r)}{(u-d)} \frac{D_{1}(-)}{(1+r)}$$
- Denote $\tilde{p}$ and $\tilde{q}$ as follows:
$$\tilde{p} = \frac{(1+r-d)}{(u-d)}$$
$$\tilde{q} = \frac{(u-1-r)}{(u-d)}$$
- By definition, $\tilde{p} + \tilde{q} = 1$, as shown below:

```math
\begin{aligned}
\tilde{p} + \tilde{q} &\equiv \frac{(1+r-d)}{(u-d)} + \frac{(u-1-r)}{(u-d)} \\\\
&\equiv \frac{(1+r-d) + (u-1-r)}{(u-d)} \\\\
&\equiv \frac{-d + u}{(u-d)} \\\\
&\equiv 1
\end{aligned}
```

- $D_{0}$, the fair price of the derivative at time $t=0$, is a weighted average of the possible values discounted from expiry when $t=1$ to the initial time $t=0$.
$$D_{0} = \tilde{p} \frac{D_{1}(+)}{(1+r)} + \tilde{q} \frac{D_{1}(-)}{(1+r)}$$
- The probability $\tilde{P} = (\tilde{p},\tilde{q})$ defines a probability distribution on the 2 point set $\{+,-\}$ with the definition for $D_{0}$ as the expected value on this distribution of $D_{1}$ after discounting.
  - $\tilde{P}$ is the **risk neutral distribution** on this 2 point set $\{+,-\}$.
- The expected value for $D_{0}$ can be denoted as follow:
$$D_{0} = E^{\tilde{P}} \left[\frac{D_{1}}{1+r} \right]$$
- In other words, for the one-step binomial model in the absence of arbitrage, the price of a derivative asset on an underlying stock is the expected value, in the risk neutral distribution, of the derivative asset at time $t=1$ discounted to time $t=0$.
  - Any derivative can be priced for time $t=0$ using the discounted risk neutral expected price at time $t=1$.
- For any derivative with value $W(t)$ the price at $t=0$ can be calculated by $W_{0} = E^{\tilde{P}} \left[\frac{W_{1}}{1+r} \right]$.
  - Given that $W(0)$ and $1+r$ are deterministic, both terms can be moved in/out of the expectation which leads to:

```math
\begin{aligned}
1+r &= E^{\tilde{P}} \left[\frac{W(1)}{W(0)} \right] \\\\
&= E^{\tilde{P}}[\text{Gross Return of } W]
\end{aligned}
```

- This concept is also true for the underlying asset, the stock in this case:

```math
\begin{aligned}
1+r &= E^{\tilde{P}} \left[\frac{S(1)}{S(0)} \right] \\\\
&= E^{\tilde{P}}[\text{Gross Return of } S]
\end{aligned}
```

- The risk neutral distribution is such that the expected return for any asset is the same as the expected return for a riskless asset, regardless of the risk level of the asset.
  - The risk neutral distribution is the distribution for asset prices if all investors in the economy were indifferent to risk levels.
  - However, in a real economy, asset prices are not distributed by a risk neutral distribution as investors expect better returns from riskier investments and generally accept lower returns for lower risk.
  - The risk neutral distribution is therefore just a mathematical convenience for calculating arbitrage prices.
  - Real world probabilities are irrelevant for calculating arbitrage based prices.

##### Example: One-Step Risk Neutral Pricing

- Using the same case as the [one-step binomial model example](#example-one-step-binomial-model), which has the following values:
  - A stock has an initial value ($t=0$) of 50 and at time $t=1$ the value of the stock has the following probabilities:
    - A value of 65 is $p > 0$
    - A value of 40 is $1-p > 0$
  - A call option with strike price 55, expiring at time $t=1$ will have the following payoff values:
    - $D_{1}(+) = \text{max}\{0,65-55\} = 10$
    - $D_{1}(-) = \text{max}\{0,40-55\} = 0$
  - The risk-free interest rate $r$ is 8%.
- $D_0$ can be determined using the risk neutral distribution as follows:

```math
\begin{aligned}
\tilde{p} &= \frac{(1+r-d)}{(u-d)} \\\\
\tilde{q} &= \frac{(u-1-r)}{(u-d)} \\\\
&\Longrightarrow u = \frac{S_{1}(+)}{S_{0}} = \frac{65}{50} = 1.3 \\\\
&\Longrightarrow d = \frac{S_{1}(-)}{S_{0}} = \frac{40}{50} = 0.8 \\\\
\therefore \tilde{p} &=\frac{1+0.08-0.8}{1.3-0.8} = 0.56 \\\\
\therefore \tilde{q} &= \frac{1.3-1-0.08}{1.3-0.08} = 0.44 \\\\\\
D_{0} &= \left[\frac{D_{1}}{1+r} \right] \\\\
&= \tilde{p} \frac{D_{1}(+)}{(1+r)} + \tilde{q} \frac{D_{1}(-)}{(1+r)} \\\\
&= 0.56 \frac{10}{1+0.08} + 0.44 \frac{0}{1+0.08} \\\\
&= 5.19
\end{aligned}
```

### Two-Step Binomial Model

- The [one-step binomial model](#one-step-binomial-model) is extended by considering three times: $t=0$, $t=1$ and $t=2$
- A stock price $S_{t}$, will be defined as follows:
  - $S_{0}$ is the initial value and is known at $t=0$.
  - At $t=1$, the stock price is a random variable $S_{1}$ with two possible values: $S_{1}(+)$ and $S_{1}(-)$.
  - At $t=2$, the stock price is a random variable $S_{2}$ with three possible values: $S_{2}(++)$, $S_{2}(+-)$ and $S_{2}(--)$.
- The relationship between the stock prices at the $t=2$ is assumed to be $S_{2}(--) < S_{2}(+-) < S_{2}(++)$.
- Similar to the one-step model, values $d$ and $u$ exist such that:
  - $S_{1}(+) = uS_{0}$
  - $S_{1}(-) = dS_{0}$
  - $S_{2}(++) = uS_{1}(+) = u^{2}S_{0}$
  - $S_{2}(+-) = dS_{1}(+) = uS_{1}(-) = udS_{0}$
  - $S_{2}(--) = dS_{1}(-) = d^{2}S_{0}$
- Also assume that there is a risk-free interest rate $r$ such that an initial investment $K$ at time $t=0$ will have a value $K(1+r)$ at time $t=1$ and a value of $K(1+r)^{2}$ at $t=2$.
- A derivative asset, with the stock as the underlying asset and expiration $t=2$, will have a value $D_{t}$ at time $t$.
  - The value $D_{2}$ is the payoff of the derivative, but the earlier values $D_{1}$ and $D_{0}$ will be determined through arbitrage principles.

![Two-Step Binomial Model](images/two-step-binomial-model.png "Two-Step Binomial Model")

- To calculate the arbitrage value of $D_{1}(+)$, the values for $D_{2}(++)$ and $D_{2}(+-)$ are discounted and then the risk neutral expectation is taken.
- Similarly, $D_{1}(-)$ is the risk neutral expectation of the discounted values of $D_{2}(+-)$ and $D_{2}(--)$.
- Finally $D_{0}$ can be calculated by taking the risk neutral expectation of the discounted values of $D_{1}(+)$ and $D_{1}(-)$.
- Due to the relationship between the stock prices values as the descendants of these values in the binomial model (i.e. the same values for $u$ and $d$ are used in both steps), the risk neutral probability are the same fo each step.

#### Asset Price Distribution in the Two-Step Binomial Model

- The risk neutral probability distribution for the asset price $S_{2}$ at time $t=2$ in the two-step binomial model can be calculated.
- The arbitrage price of any derivative asset contingent on this asset will be expressed as a risk neutral expectation.
- The terms $\tilde{p}$ and $\tilde{q}$ represent the risk neutral probabilities, similar to the [one-step binomial model risk neutral pricing](#one-step-risk-neutral-pricing), and can be expressed as follows where $r$ is the risk-free rate:
$$\tilde{p} = \frac{(1+r-d)}{(u-d)}$$
$$\tilde{q} = \frac{(u-1-r)}{(u-d)}$$
- The risk neutral expectations for $D_{1}(+)$ and $D_{1}(-)$ can therefore be expressed in terms of the potential values of $D_{2}$ as follows:
$$D_{1}(+) = \tilde{p} \frac{D_{2}(++)}{1+r} + \tilde{q} \frac{D_{2}(+-)}{1+r}$$
$$D_{1}(-) = \tilde{p} \frac{D_{2}(+-)}{1+r} + \tilde{q} \frac{D_{2}(--)}{1+r}$$
- The risk neutral expectation for $D_{0}$ is then expressed in terms of the potential values of $D_{2}$ as follows:

```math
\begin{aligned}
D_{0} &= \tilde{p} \frac{D_{1}(+)}{1+r} + \tilde{q} \frac{D_{1}(-)}{1+r} \\\\
&= \frac{\tilde{p}}{1+r} \left(\tilde{p} \frac{D_{2}(++)}{1+r} + \tilde{q} \frac{D_{2}(+-)}{1+r} \right) + \frac{\tilde{q}}{1+r} \left( \tilde{p} \frac{D_{2}(+-)}{1+r} + \tilde{q} \frac{D_{2}(--)}{1+r} \right) \\\\
&= \tilde{p}^{2} \frac{D_{2}(++)}{(1+r)^{2}} + \tilde{p}\tilde{q} \frac{D_{2}(+-)}{(1+r)^{2}} + \tilde{p}\tilde{q} \frac{D_{2}(+-)}{(1+r)^{2}} + \tilde{q}^{2} \frac{D_{2}(--)}{(1+r)^{2}} \\\\
&= \tilde{p}^{2} \frac{D_{2}(++)}{(1+r)^{2}} + 2\tilde{p}\tilde{q} \frac{D_{2}(+-)}{(1+r)^{2}} + \tilde{q}^{2} \frac{D_{2}(--)}{(1+r)^{2}}
\end{aligned}
```

- This represents the [binomial distribution from the random walk](./8_stochastic-processes.md#the-binomial-distribution) with binomial probabilities $\text{bin}(k;2,\tilde{p})$ which can be substituted in as follows:
$$D_{0} = \text{bin}(2;2,\tilde{p}) \frac{D_{2}(++)}{(1+r)^{2}} + \text{bin}(1;2,\tilde{p}) \frac{D_{2}(+-)}{(1+r)^{2}} + \text{bin}(0;2,\tilde{p}) \frac{D_{2}(--)}{(1+r)^{2}}$$
- The derivative price $D_{0}$ in the two-step binomial model is the binomial expectation of the discounted payoff values:
$$D_{0} = E^{\text{bin}(;2,\tilde{p})} \left[ \frac{D_{2}}{(1+r)^{2}} \right]$$

#### Example: Two-Step Binomial Model

- A stock with price $S_{t}$ has a derivative asset with price $D_{t}$ and expiration at time $t=2$.
- The possible payoffs for the derivative asset are:
  - $D_{2}(++)=-15$
  - $D_{2}(+-)=10$
  - $D_{2}(--)=25$
- The risk-free investment rate $r$ is assumed to be 6%.
- A two-step binomial model with $u=1.2$ and $d=0.9$ can be used to calculate $D_{0}$, the fair price of the derivative asset at time $t=0$, by applying arbitrage principles to find the risk neutral expectations.
- The risk neutral probabilities are given by:

```math
\begin{aligned}
\tilde{p} &= \frac{(1+r-d)}{(u-d)} \\\\
&= \frac{1+0.06-0.9}{1.2-0.9} \\\\
&= 0.5333 \\\\\\
\tilde{q} &= \frac{(u-1-r)}{(u-d)} \\\\
&= \frac{1.2-1-0.06}{1.2-0.9} \\\\
&= 0.4667
\end{aligned}
```

- The risk neutral expectations and arbitrage prices for the derivate asset at time $t=1$ can now be calculated as follows:

```math
\begin{aligned}
D_{1}(+) &= \tilde{p} \frac{D_{2}(++)}{1+r} + \tilde{q} \frac{D_{2}(+-)}{1+r} \\\\
&= 0.5333 \left( \frac{-15}{1+0.06} \right) + 0.4667 \left( \frac{10}{1+0.06} \right) \\\\
&= -3.145 \\\\\\
D_{1}(-) &= \tilde{p} \frac{D_{2}(+-)}{1+r} + \tilde{q} \frac{D_{2}(--)}{1+r} \\\\
&= 0.5333 \left( \frac{10}{1+0.06} \right) + 0.4667 \left( \frac{25}{1+0.06} \right) \\\\
&= 16.038
\end{aligned}
```

- Finally, the risk neutral expectation and arbitrage price for the derivative asset at time $t=0$ can be calculated as follows:

```math
\begin{aligned}
D_{0} &= \tilde{p} \frac{D_{1}(+)}{1+r} + \tilde{q} \frac{D_{1}(-)}{1+r} \\\\
&= 0.5333 \left( \frac{-3.145}{1+0.06} \right) + 0.4667 \left( \frac{16.038}{1+0.06} \right) \\\\
&= 5.478
\end{aligned}
```

- The fair price of the derivative asset at time $t=0$ is 5.478.
- Alternatively, the risk neutral expectation formula can be used:

```math
\begin{aligned}
D_{0} &= E^{\text{bin}(;2,\tilde{p})} \left[ \frac{D_{2}}{(1+r)^{2}} \right] \\\\
&= \tilde{p}^{2} \frac{D_{2}(++)}{(1+r)^{2}} + 2\tilde{p}\tilde{q} \frac{D_{2}(+-)}{(1+r)^{2}} + \tilde{q}^{2} \frac{D_{2}(--)}{(1+r)^{2}} \\\\
&= (0.5333)^{2} \frac{-15}{1.06^{2}} + 2(0.5333)(0.4667) \frac{10}{1.06^{2}} + (0.4667)^{2} \frac{25}{1.06^{2}} \\\\
&= 5.478
\end{aligned}
```

### The Full Binomial Model

- The full binomial expands the [two-step binomial model](#two-step-binomial-model) for an arbitrary number of steps $n$ > 0.
- By extending to three steps, the general case can be derived.
- At time $t=3$, there will be four potential values for $S_{3}$:
  - $S_{3}(+++) = u^{3}S_{0}$
  - $S_{3}(++-) = u^{2}dS_{0}$
  - $S_{3}(+--) = u^{2}dS_{0}$
  - $S_{3}(---) = d^{3}S_{0}$

![Full Binomial Model](images/full-binomial-model.png "Full Binomial Model")

## The Black-Scholes Option Pricing Model