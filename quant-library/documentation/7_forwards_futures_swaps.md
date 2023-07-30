# Forwards, Futures, and Swaps

- [Forwards, Futures, and Swaps](#forwards-futures-and-swaps)
  - [Introduction](#introduction)
    - [Derivative Products](#derivative-products)
    - [Derivative Markets](#derivative-markets)
    - [Assumptions](#assumptions)
  - [Forwards](#forwards)
    - [Settlement](#settlement)
    - [Payoffs](#payoffs)
    - [Pricing Contracts on an Underlying Asset with No Income](#pricing-contracts-on-an-underlying-asset-with-no-income)
    - [Cash and Carry Arbitrage](#cash-and-carry-arbitrage)
      - [Zero Coupon Bond Example](#zero-coupon-bond-example)
      - [Stock (No Dividends) Example](#stock-no-dividends-example)
      - [Asset Paying a Known Income Example](#asset-paying-a-known-income-example)
    - [Pricing Forward Contracts](#pricing-forward-contracts)
      - [Underlying Asset with Known Income](#underlying-asset-with-known-income)
      - [Underlying Asset with Known Yield](#underlying-asset-with-known-yield)
      - [Underlying Asset with Dividends](#underlying-asset-with-dividends)
    - [FX Forwards](#fx-forwards)
      - [Pricing FX Forwards](#pricing-fx-forwards)
      - [Interest Rate Parity Relationship](#interest-rate-parity-relationship)

## Introduction

- Derivatives are financial products or assets whose structure and value is derived from another asset.
- The base asset is called the **underlying asset** (generally referred to as the underlying).
- The derivative is linked to the underlying through revenues paid to the holder of the derivative product - these revenues are known as **payoffs**.
  - The payoffs of a derivative are generally determined by the price of the underlying asset at a set point during the derivative contract's life - often the expiration date of the contract.
  - Arbitrage is the main tool for linking the derivative's value to its underlying.
- The price of the underlying asset is referred to as the **cash price** or **spot price** to distinguish it from the price of its derivatives.
- The underlying asset is traded on the **cash market**, assuming it is a cash product (not always the case).
- The profit and loss is the change in the value of an investment or financial position(s) and is usually shortened to **P&L**.

### Derivative Products

- **Forwards**/**futures**: contracts that lock in a price that two parties will exchange an asset for at a set future date.
- **Options**: contracts that give one party the right, but not the obligation, to exchange an asset.
- **Swaps**: contracts that allow two parties to exchange cash flows or liabilities from two different financial instruments. Interest rate swaps are the most common, facilitating a swap between a floating interest rate and a fixed one.

### Derivative Markets

- Markets can be divided into **over the counter (OTC)** or on organised **exchanges**.
- OTC markets consist of deals between two counterparties that make private deals within financial regulations (little price transparency).
- Exchanges, such as the Chicago Mercantile Exchange (CME), allow for more standardised products and regulated trading which are visible to all market participants (price transparency).
- Generally, exchange-traded products are much more liquid than OTC products and have a less exposure to **counterparty credit risk** (risk of one counterparty failing to meet their obligations).
  - The exchange acts as a counterparty to every deal made with its clients and are subject to strict regulations.
  - With OTC deals, there is always a major concern than one counterparty will default.
- OTC markets allow for more customisable deals to be made between broker-dealers and clients, or between broker-dealers themselves.
- Following the 2008 financial crisis, there has been a push to move OTC products onto exchanges.

### Assumptions

- Transactions costs are zero.
- Unlimited investing and borrowing at the risk-free rate.
- No restrictions on short selling assets.

## Forwards

- A forward contract is an agreement between a buyer and seller where the seller agrees to sell an asset to the buyer at a set point in the future at a price agreed upon entering into the contract.
- By definition, forward contracts are traded on OTC markets and are often highly customised.
- Generally, one of the counterparties is a financial institution or dealer, whilst the other counterparty is an end user of another dealer.
- Forwards are usually used to hedge against changes in price.
- Terminology:
  - **Long position**: position of the buyer
  - **Short position**: position of the seller
  - **Expiration date or expiry**: agreed date on which the transaction will take place
  - **Forward price**: the agreed transaction price
- The **underlying asset** will be the asset that is traded at the forward contract's expiration date.
- The forward contract is priced such that the value is 0 at the time of entering into the contract.

### Settlement

- At the expiration date, forward contracts can be **settled by delivery** or by **cash settlement**.
- Settlement by delivery involves the seller exchange the underlying asset for the contract price with the buyer.
- In a cash settled deals, the party with the negative cash position at the expiry compensates the other party with cash.
- Due to the customised nature of the deals, forward contracts are illiquid securities and are usually held until expiry.

### Payoffs

- The revenue a particular counterparty earns from a derivative contract is referred to as the **payoff**.
- With forward contracts, neither the long position nor the short position receive any payment from the contract until the expiry date.
  - Therefore at expiration, the values of the long and short positions in a forward contract are equal to the long and short payoffs respectively.
- The payoff for a long position in a forward contract can be modelled as follows:
  - Using the following notation:
    - $S(t)$ as the price of the underlying asset at time $t$.
    - $K_{\tau}$ as the forward price for expiry $\tau$.
    - $T$ as the expiration (expiry date).
    - $V(t)$ as the value of the long position at time $t$.
  - At expiration of the contract, the underlying is transferred to the long position from the short position - the long position receives an asset (cash flow) with value $S(T)$.
  - The long position must pay the short position the forward price $K_{\tau}$ to receive the asset - this should be deducted from the value received in order to calculate the long position's payoff.
$$V(T) = S(T) - K_{\tau}$$
- Similarly, the short position's payoff is:
$$-V(T) = K_{\tau} - S(T)$$
- Graphically, this can be represented as follows:

    ![Forward Payoff](images/forward-payoff.png "Forward Payoff")

### Pricing Contracts on an Underlying Asset with No Income

- The value of the **long position**, $V(T) = S(T) - K_{\tau}$, can be calculated by using the Law of One Price and constructing a portfolio which models the payoff at time $t = T$.
  - $S(T)$ can be modelled by holding the underlying asset in the portfolio.
  - $-K_{T}$ can be modelled as a cash payment (debt) discounted at time $t = 0$. This discounted (absolute) value is calculated by $e^{-rT}K_{T}$.
  - The future value of this debt at time $t$ can then be calculated by $e^{rt}\left(e^{-rT}K_{T}\right)$.
  - The value of this portfolio at time $t$ is modelled as follows:
$$V(t) = S(t) - e^{rt}\left(e^{-rT}K_{T}\right)$$
$$\boxed{V(t) = S(t) - e^{-r(T-t)}K_{T}}$$
- This model can be validated by showing that at time $t = T$, the value of the portfolio is equal to $S(T) - K_{T}$:
$$V(T) = S(T) - e^{-r(T-T)}K_{T}$$
$$V(T) = S(T) - e^{0}K_{T}$$
$$V(T) = S(T) - K_{T}$$
- Using the Law of One Price, the value of the forward contract $V(t)$ at any time $t < T$ must be equal to the value of the portfolio.
- Similarly, the payoff of the **short position** can be modelled as:
$$\boxed{-V(t) = e^{-r(T-t)}K_{T} - S(t)}$$
- The forward price $K_{T}$ is set such that the value of the forward contract at $t = 0$ will be zero: $V(0) = 0$ and can be calculated as follows:
$$V(0) = S(0) - e^{-r(T-0)}K_{T} = 0$$
$$\Longrightarrow S(0) - e^{-rT}K_{T} = 0$$
$$\therefore S(0) = e^{-rT}K_{T}$$
$$\boxed{K_{T} = e^{rT}S(0)}$$

### Cash and Carry Arbitrage

- Forward prices may be deduced from two arbitrage strategies: the cash and carry arbitrage, and the reverse cash and carry arbitrage.
- Recall the forward price, $K_{T} = e^{rT}S(0)$, where $S(t)$ is the underlying spot price, $r$ is the risk-free rate and $T$ is the expiration date of the forward contract.
- If $K_{T} > e^{rT}S(0)$, a **cash and carry arbitrage** can be constructed and therefore this inequality will never be present. The portfolio can be constructed as follows:
  - Take a short position in the forward contract.
  - Borrow $S(0)$ in cash at the risk-free rate and purchase the underlying with the proceeds.
  - The portfolio has three components:
    1. the short forward position
    2. the underlying asset
    3. a debt of $S(0)e^{rt}$ at time $t$
  - This portfolio is held until time $T$, at which point the short forward position (1) is exited by transferring the underlying asset (2) to the long forward position (counterparty) for the  contract price $K_{T}$.
  - The debt of $S(0)e^{rT}$ (3) can be repaid, leaving a **profit** of $K_{T} - e^{rT}S(0)$.
- Similarly $K_{T} < e^{rT}S(0)$ will lead to a **reverse cash and carry arbitrage** by constructing the following portfolio:
  - Take a long position in the forward contract.
  - Take a short position in the underlying and invest the proceeds $S(0)$ at the risk-free rate.
  - The portfolio has three components:
    1. the long forward position
    2. the short position in the underlying asset
    3. a cash holding of $S(0)e^{rt}$ at time $t$
  - This portfolio is held until time $T$, at which point the forward contract price $K_{T}$ is paid to exit the long forward position (1). This then delivers the underlying asset which is used to exit the short position in the underlying asset (2).
  - The cash holding of $S(0)e^{rT}$ (3) is left, leaving a **profit** of $e^{rT}S(0) - K_{T}$.
- The **cost of carry** in the cash and carry portfolio was only the risk-free rate $r$; however, there will generally be other financing charges and costs associated with storage, transportation and holding. Additionally any income from holding the underlying asset such as dividends or convenience yields should be considered.
- For the reverse cash and carry arbitrage, the **cost of carry** is reversed due to the short position in the underlying asset so any charges are received as income.

#### Zero Coupon Bond Example

- Take a forward contract on zero-coupon bond maturing in 1 year and a risk-free interest rate of 3.5%.
- If the bond currently has a market price of 925 USD, the forward price for a 6 month forward contract on this bond can be calculated as follows:
  - Assume the risk-free rate, $r = 0.035$, is continuously compounded.
  - The value of the underlying $S$ at $t = 0$ is $925 \text{ USD}$
  - The forward contract expiration $T$ is $0.5$
  - Taking the formula for the forward price a $K = e^{rT}S(0)$, the price of a 6 month forward contract on this bond is calculated as $e^{0.035 \times 2} \times 925 \Longrightarrow 941.33 \text{ USD}$
- If one bond dealer offers a forward price of 950 USD, a riskless profit can be obtained as follows:
  - Borrow 925 USD and buy the underlying bond.
  - Enter into a short position in the forward contract with forward price 950 USD.
  - This creates a portfolio with the following components:
    1. the short forward position
    2. the bond
    3. a debt valued at $e^{0.035t}(925)$ at time $t$.
  - This portfolio is held for 6 months, by which time the debt is worth 941.33 USD (this is also the fair forward price we calculated).
  - The short position in the forward contract can be exited by selling the bond for 950 USD.
  - This leaves a profit of $950 - 941.33 = 8.67 \text{ USD}$
- If another bond dealer offers a forward price of 935 USD, a riskless profit can be obtained as follows:
  - Enter into a short position in the underlying bond and receive 925 USD in cash to invest at the risk-free rate.
  - Enter into a long position in the forward contract with forward price 935 USD.
  - This creates a portfolio with the following components:
    1. the long forward position
    2. the short position in the underlying bond
    3. a cash investment valued at $e^{0.035t}(925)$ at time $t$.
  - This portfolio is held for 6 months, by which time the cash investment is worth 941.33 USD.
  - This cash investment can be used to exit the forward contract and buy the bond for the price of 935 USD.
  - The short position in the underlying bond can fulfilled using the purchased bond.
  - This leaves a profit of $941.33 - 935 = 6.33 \text{ USD}$

#### Stock (No Dividends) Example

- Take a stock which does not pay dividends and is currently trading for 150 USD.
- The price of a forward contract in 9 months time, assuming a risk-free interest rate of 4%, can be calculated as follows:
  - Using the formula $K = e^{rT}S(0)$ where $r$ is the risk free interest rate ($4\%$), $T$ is the length of the contract ($0.75$), and $S(0)$ is the current price of the stock ($150 \text{ USD}$), the forward price is $K = e^{0.04 \times 0.75} \times 150 = 154.57 \text{ USD}$.
- The value of the forward contract in 3 months $V(0.25)$, given the value of the stock in 3 months $S(0.25)$ is $130 \text{ USD}$, can be calculated as follows:
  - $V(0.25) = S(0.25) - e^{-r(T-0.25)}K \Longrightarrow V(0.25) = 130 - e^{-0.04(0.75 - 0.25)}(154.57) = -21.51 \text{ USD}$
  - The negative value indicates that a long position in this forward contract would lose money.
- The value of the forward contract in 3 months $V(0.25)$, given the value of the stock in 3 months $S(0.25)$ is $170 \text{ USD}$, can be calculated as follows:
  - $V(0.25) = S(0.25) - e^{-r(T-0.25)}K \Longrightarrow V(0.25) = 170 - e^{-0.04(0.75 - 0.25)}(154.57) = 18.49 \text{ USD}$
  - The positive value indicates that a long position in this forward contract would make money.
- Remember, a long position in a forward contract locks in a price to buy an asset.
  - If the value of the underlying asset goes down, the forward contract loses money as the asset is could be bought at a cheaper price on the market.
  - If the value of the underlying asset goes up, the forward contract makes money as the asset is being bought at a cheaper price than the current mark price.

#### Asset Paying a Known Income Example

- Let $I$ be the present value, at the inception of the contract ($t = 0$), of the known income paid by the asset during the life of the forward contract.
  - **N.B. generally $I(t)$ denotes the present value at time $t$ of the income provide by an asset between $t$ and $T$.**
- Considering arbitrage, the forward price can be calculated as:
$$\boxed{K_{T} = (S(0) - I)e^{rT}}$$
- This relationship can be proven using the *cash and carry arbitrage* as well as the *reverse cash and carry arbitrage*.
- First consider the case where $K_{T} > (S(0) - I)e^{rT}$ and construct an arbitrage portfolio as follows:
  - Take a short position in the forward contract.
  - Borrow S(0) in cash at the risk-free rate and purchase the underlying asset.
  - This gives a portfolio of:
    1. the short forward position
    2. the underlying asset
    3. the debt valued at $S(0)e^{rt}$ at time $t$.
  - This portfolio is held until time $T$, accruing the income paid by the asset, and will consist of the following:
    1. the short forward position
    2. the underlying asset
    3. the debt valued at $S(0)e^{rT}$
    4. the accrued income valued at $Ie^{rT}$
  - The short forward position can be exited by exchanging the underlying asset for $K_{T}$ in cash.
  - By rewriting the initial case as $K_{T} + Ie^{rT} > S(0)e^{rT}$ and calculating the total cash holding at time $T$ to be $K_{T} + Ie^{rT}$, it can be shown that an arbitrage profit will be retained once the debt of $S(0)e^rT$ is repaid.
- Now consider the case where $K_{T} < (S(0) - I)e^{rT}$ and construct an arbitrage portfolio as follows:
  - Take a long position in the forward contract.
  - Take a short position in the underlying asset in return for $S(0)$ in cash which is invested at the risk-free rate.
  - This gives a portfolio of:
    1. the long forward position
    2. the short position in the underlying asset
    3. the cash holding valued at $S(0)e^{rt}$ at time $t$.
  - This portfolio is held until time $T$
  - By rewriting the initial case as $K_{T} + Ie^{rT} < S(0)e^{rT}$ and calculating that the value of the cash holding at time $T$ to be $S(0)e^{rT}$, it can be shown that the there will be sufficient cash funds to:
    1. pay the forward contract price $K_{T}$ in return for the underlying asset which can be used to exit the short position.
    2. pay the future value of the accrued income calculated as $Ie{rT}$ to the owner of the underlying asset.
  - This inequality leads to an arbitrage profit equal to $S(0)e^{rT} - \left(K_{T} + Ie^{rT}\right)$.

### Pricing Forward Contracts

#### Underlying Asset with Known Income

- Extending the notation for the value of a forward contract (long position) to: $V(t;K,T)$ where $K$ is the forward price and $T$ is the expiration date.
  - The fair forward price for a forward contract, as per the prevailing market conditions at time $t$, can be denoted as $K_{T}(t)$.
  - In previous examples $K_{T}(t=0)$ was used, denoted as just $K_{T}$.
  - This means that $V(t;K_{T}(t),T) = 0$ by definition given the value of the forward contract at the time of initiation will be 0.
- It has been shown that a forward contract on an underlying asset that pays no income is valued as: $K_{T}(t) = e^{r(T-t)}S(t)$ and for an asset paying known income with a present value $I$ between $t$ and $T$, the forward contract is valued as $K_{T}(t) = (S(t)-I(t))e^{r(T-t)}$.
- The general notation for the value of a forward contract at time $t$ is:
$$V(t;K_,T) = (K_{T}(t) - K)e^{-r(T-t)}$$
- This formula can be proven using arbitrage as follows:
  - At time $t$, enter into 2 forward positions:
    1. a long position in a forward contract expiring at time $T$ with contract price $K$.
    2. a short position on a forward contract also expiring at time $T$ and with contract price $K_{T}(t)$.
  - At a time $\tau$ where $t \leq \tau \leq T$, the value of the two forward positions is calculated as $V(\tau;K,T) - V(\tau;K_{T}(t),T)$.
  - At time $T$ when both forward contracts expire, the value of the contracts will be $V(T;K,T) - V(T;K_{T}(t),T) \equiv S(T) - K - (S(T) - K{T}(t)) \equiv K_{T}(t) - K$.
  - If the value of the forward contracts at time $T$ is equal to $K_{T} - K$ then, by the law of one price, the value at time $t$ will be equal to the discounted value of this cash value: $(K_{T}(t) - K)e^{-r(T-t)}$.
  - This leads to $V(t;K,T) - V(t;K_{T}(t),T) = (K_{T}(t) - K)e^{-r(T-t)}$ and given $V(t;K_{T}(t),T) = 0$ by definition, this can be simplified to $V(t;K,T) = (K_{T}(t) - K)e^{-r(T-t)}$ as above.
- Using the forward price for an asset paying a known income $K_{T}(t) = (S(t)-I(t))e^{r(T-t)}$ and substituting in $(K_{T}(t) - K)e^{-r(T-t)}$ leads to:
$$V(t) = \left((S(t) - I(t))e^{r(T-t)} - K\right)e^{-r(T-t)}$$
$$\boxed{ V(t) = S(t) - I(t) - Ke^{-r(T-t)}}$$

#### Underlying Asset with Known Yield

- For an underlying with price $S(t)$ and a dividend yield $y$, where all dividends are reinvested and an initial allocation $e^{-yT}$, the value of a position at time $t$ can be calculated as $e^{-yT}e^{yt}S(t) \equiv e^{-y(T-t)}S(t)$ as shown in the [dividend yields](./4_equities.md#dividends) section.
  - At time $t = T$ the position will therefore have a value of $S(T)$ and at time $t = 0$ the value (initial investment) will be equal to $e^{-yT}S(0)$.
- The forward contract price on this underlying asset can be derived using the replicating portfolio method as follows:
  - A long position in the forward contract will have a payoff $S(T) - K_{T}$.
    - $S(T)$ can be represented by an allocation of $e^{-yT}$ in the underlying asset given the value of this position at time $T$ will be equal to $S(T)$.
    - $K_{T}$ can be replicated by a debt of $e^{-rT}K_{T}$, borrowed at the risk-free rate $r$.
  - At time $t = 0$, the portfolio will consist of:
    1. an allocation of $e^{-yT}$ in the underlying asset
    2. a debt of $e^{-rT}K_{T}$
  - At time $t$ the allocation of the underlying asset will be worth $e^{-y(T-t)}S(t)$ and the debt will be worth $-e^{rT}e^{-rT}K_{T} \equiv -e^{-r(T-t)}K_{T}$.
  - The value of the portfolio at time $t$ is therefore calculated as $\boxed{V(t) = e^{-y(T-t)}S(t) - e^{-r(T-t)}K_{T}}$.
    - This portfolio replicates the forward payoff because at time $t = T$, the portfolio will be $V(T) = S(T) - K_{T}$ and by the Law of One Price, $V(T)$ is the value of the contract at any time $t \leq T$.
  - At time $t = 0$, the value of the portfolio is calculated as $V(T) = e^{-y(T)}S(0) - e^{-r(T)}K_{T}$ and given the value of the forward contract at time $t = 0$ must equal 0, we can calculate the forward price $K_{T}$ as follows:
$$V(0) = 0$$
$$e^{-y(T)}S(0) - e^{-r(T)}K_{T} = 0$$
$$e^{-y(T)}S(0) = e^{-r(T)}K_{T}$$
$$e^{-y(T)+r(T)}S(0) = K_{T}$$
$$\boxed{K_{T} = e^{(r-y)T}S(0)}$$

- The cost of carry is represented by $r - y$ which is the finance charge net the income paid by the asset.
- If the underlying asset was a commodity, the yield $y$ could be represented by $y = c - s$ where $c$ is the convenience yield and $s$ is the rate of storage cost. Hence the cost of carry would be $r + s - c$ and the forward price would be calculated as $K_{T} = e^{(r+s-c)T}S(0)$
- This formula could also have been demonstrated using the cash and carry arbitrage.

#### Underlying Asset with Dividends

- Take a stock that is currently trading for 247 USD and pays dividends of 5 USD in 2 months, 5 months and 8 months time.
- The price of a forward contract in 9 months time, assuming a risk-free interest rate of 1.5%, can be calculated as follows:
  - Calculate the present value at time $t = 0$ of the stream of dividend payments: $I(0) = e^{-0.015(\frac{2}{12})}(5) + e^{-0.015(\frac{5}{12})}(5) + e^{-0.015(\frac{8}{12})}(5)$ which equals $14.91 \text{ USD}$.
  - The price of the forward contract is then calculated using $K_{T} = (S(0) - I)e^{rT} \Longrightarrow K = (247 - 14.91)e^{(0.015)(075)} = 234.72 \text{ USD}$
- The value of a position at time $t$ is calculated by $V(t) = S(t) - I(t) - Ke^{-r(T-t)}$ where $I(t)$ is the present value of the remaining dividend payments between time $t$ and the end of the contract at time $t = T$.
- A short position in 3 months, when the underlying share price is 220 USD, is calculated by negating the value of the position as follows:
  - $-V(t) = Ke^{-r(T-t)} - S(t) + I(t)$ where $I(0.25) = e^{-0.015(\frac{2}{12})}(5) + e^{-0.015(\frac{5}{12})}(5)$ as the dividends will be paid 2 months and 5 months after this point in time.
  - The present value of the remaining dividends is therefore $I(0.25) = 9.96 \text{ USD}$ which leads to the value of the short position in 3 months: $-V(0.25) = (234.72)e^{-0.015(0.75-0.25)} - 220 + 9.96 = 22.93 \text{ USD}$

### FX Forwards

- Foreign Exchange forward contracts will lock in a particular exchange rate between two currencies at the contract expiration date.
- The notation used for foreign currencies is explained [here](1_introduction.md#foreign-currencies-fx) and uses $r_{f}$ for the foreign currency risk-free rate and $r_{d}$ or just $r$ for the domestic risk-free rate.
- It is also assumed that any holding of foreign currency is invested at $r_{f}$ and so foreign currency holding can be modelled to be assets that pay a known yield $y = r_{f}$.

#### Pricing FX Forwards

- Let S(t) be the spot exchange rate at time $t$, so that $S(t)$ is the price in the domestic currency for 1 unit of the foreign currency.
- $K_{T}$ is the forward price (or exchange rate) for a contract that expires at time $t = T$.
- Using the formula derived for [pricing a forward contract fo an asset with known yield](#underlying-asset-with-known-yield), the FX forward rate for a contract expiring at time $T$ is given by:

$$\boxed{K_{T} = e^{(r_{d}-r_{f})T}S(0)}$$

#### Interest Rate Parity Relationship

- The theory for pricing FX forwards in known independently in foreign currency economics as the interest rate parity relationship and can be derived using the cash and carry arbitrage.
- Take a situation where a forward rate $K_{T}$ is being offered such that $K_{T} > e^{(r_{d}-r_{f})T}S(0)$.
- This inequality can be rewritten as $Ke^{r_{f}T}\frac{1}{S(0)} > e^{r_{d}T}$.
- Multiplying through by a notional amount of 1000 USD to give:
  $$\underbrace{K}_{\text{conversion of foreign currency back to domestic at forward rate}} \times \underbrace{e^{r_{f}T}}_{\text{investing foreign currency holding at foreign risk-free rate}} \times \underbrace{\frac{1000}{S(0)}}_{\text{conversion of 1000 USD to foreign currency at } t = 0} > \underbrace{1000e^{r_{d}T}}_{\text{value at time } T \text{ of a 1000 USD debt borrowed at time } t = 0}$$
- In other words, this inequality implies that that the seller of this FX forwards contract can make a riskless profit by:
  1. borrowing 1000 USD at the domestic risk-free rate
  2. converting this cash to a foreign currency
  3. investing the converted cash at the foreign risk-free rate
  4. converting the foreign cash back to domestic cash at the expiry, using the contracted rate $K_{T}$
- Similarly, if $K_{T} < e^{(r_{d}-r_{f})T}S(0)$ then an arbitrage profit can be constructed by:
  1. borrowing 1000 units of the foreign currency at the foreign risk-free rate
  2. converting this cash to the domestic currency
  3. investing the converted cash at the domestic risk-free rate
  4. converting the domestic cash back to foreign cash at the expiry, using the contracted rate $K_{T}$
- These inequalities cannot be present so $K_{T} = e^{(r_{d}-r_{f})T}S(0)$.