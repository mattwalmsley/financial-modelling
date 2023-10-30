# Forwards, Futures, and Swaps

- [Forwards, Futures, and Swaps](#forwards-futures-and-swaps)
  - [Derivatives Introduction](#derivatives-introduction)
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
      - [Example 1: Euros and US Dollars](#example-1-euros-and-us-dollars)
      - [Example 2: Australian Dollars and US Dollars](#example-2-australian-dollars-and-us-dollars)
  - [Futures](#futures)
    - [Futures Exchanges and Products](#futures-exchanges-and-products)
    - [Futures Prices](#futures-prices)
      - [Convergence of Futures Prices to Spot Prices](#convergence-of-futures-prices-to-spot-prices)
      - [Futures Prices versus Forward Contract Prices](#futures-prices-versus-forward-contract-prices)
    - [Futures Marking to Market (Settlement)](#futures-marking-to-market-settlement)
      - [Marking to Market Example](#marking-to-market-example)
      - [Margin Accounts](#margin-accounts)
      - [Futures Settlement versus Forwards Settlements](#futures-settlement-versus-forwards-settlements)
    - [Futures Hedging](#futures-hedging)
      - [Cash Market Exposure](#cash-market-exposure)
      - [Risk Management using Futures Hedging](#risk-management-using-futures-hedging)
      - [Futures Hedging Example 1: Oil Refinery](#futures-hedging-example-1-oil-refinery)
      - [Basis Risk](#basis-risk)
        - [Commodity Basis Risk](#commodity-basis-risk)
        - [Basis Risk Example](#basis-risk-example)

## Derivatives Introduction

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
  - This portfolio is held for 6 months, by which time the debt is worth 941.33 USD (this is also the fair forward price that was calculated).
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
  - At time $t = 0$, the value of the portfolio is calculated as $V(T) = e^{-y(T)}S(0) - e^{-r(T)}K_{T}$ and given the value of the forward contract at time $t = 0$ must equal 0, the forward price $K_{T}$ can be calculated as follows:
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
- In other words, this inequality implies that that the seller of this FX forward contract can make a riskless profit by:
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

#### Example 1: Euros and US Dollars

- Using a spot EUR/USD exchange rate of 1.20 USD, a domestic USD risk-free rate of 5% and a Eurozone risk-free rate of 8%, the price of a 6 month EUR/USD FX forward contract can be calculated as follows:
  - Allocating the standard notation as: $S(0) = 1.20 \text{ USD}$, $r_{d} = 5\%$, $r_{f} = 8\%$, $T = 0.5$.
  - Using $K_{T} = e^{(r_{d}-r_{f})T}S(0)$ and substituting in the values: $K_{T} = e^{(0.05-0.08)(0.5)}(1.2)$, the fair forward rate is $1.1821 \text{ USD}$.
- If a forward contract in this example had a price of 1.21 USD, an arbitrage profit could be obtained as follows:
  1. Borrow a notional amount of 1000 USD and convert into EUR at the spot rate of 1.20 USD to give 833.33 EUR.
  2. Enter a forward contract to convert EUR to USD in 6 months time at a rate of 1.21 USD.
  3. Invest the 833.33 EUR at the foreign risk-free rate of 8% for 6 months to give a cash value of $(833.33)e^{(0.08)(0.5)} = 867.34 \text{ EUR}$.
  4. The 867.34 EUR can be converted back into USD at a rate of 1.21 USD to give 1049.48 USD.
  5. After 6 months, the debt from borrowing 1000 USD will be valued at $(1000)e^{(0.05)(0.5)} = 1025.32 \text{ USD}$
  6. This leaves an arbitrage profit of $1049.48 - 1025.32 = 24.16 \text{ USD}$
- Similar, if the forward contract price was 1.15 USD then an arbitrage profit could be obtained as follows:
  1. Borrow a notional amount of 1000 EUR and convert into USD at the spot rate of 1.20 USD to give 1200 EUR.
  2. Enter a forward contract to convert USD to EUR in 6 months time at a rate of 1.15 USD.
  3. Invest the 1200 USD at the domestic risk-free rate of 5% for 6 months to give a cash value of $(1200)e^{(0.05)(0.5)} = 1230.38 \text{ USD}$.
  4. After 6 months, the debt from borrowing 1000 EUR will be valued at $(1000)e^{(0.08)(0.5)} = 1040.81 \text{ EUR}$ which can be paid off using USD, converted at the forward rate of 1.15 USD. At this exchange rate, 1196.93 USD will be needed to pay off the 1040.81 EUR debt.
  5. This leaves an arbitrage profit of $1230.38 - 1196.93 = 33.45 \text{ USD}$

#### Example 2: Australian Dollars and US Dollars

- Using a spot AUD/USD exchange rate of 0.75 USD, a domestic USD risk-free rate of 4% and an Australian risk-free rate of 6%, the price of a 2 month AUD/USD FX forward contract can be calculated as follows:
  - Allocating the standard notation as: $S(0) = 0.75 \text{ USD}$, $r_{d} = 4\%$, $r_{f} = 6\%$, $T = \frac{1}{6}$.
  - Using $K_{T} = e^{(r_{d}-r_{f})T}S(0)$ and substituting in the values: $K_{T} = e^{(0.04-0.06)(\frac{1}{6})}(0.75)$, the fair forward rate is $0.7475 \text{ USD}$.
- The value of the forward contract in 1 month time ($t=\frac{1}{12}$) when the exchange rate ($S(t)$) is 0.71 USD can be calculated by:
$$\boxed{{V(t) = e^{-r_{f}(T-t)}S(t) - e^{-r_{d}(T-t)}K_{T}}}$$
$$\text{Where } K_{T} = 0.7475$$
$$V(t) = e^{-0.06(\frac{2}{12}-\frac{1}{12})}(0.71) - e^{-0.04(\frac{2}{12}-\frac{1}{12})}(0.7475) = 0.03855 \text{ USD}$$

## Futures

- A futures contract is very similar to a forward contract in the sense that it is a contract between a buyer and a seller to sell a specific asset at a fixed time in the future at a price which is agreed when the contract is initiated.
- The differences between a futures contracts and a forward contracts is that futures contracts are traded on exchanges and forward contracts are private deals between two counterparties, traded over-the-counter (OTC).
- Futures contracts will closely track the cash price and are therefore used for a number of reasons:
  - provide exposure to the underlying asset
  - risk management purposes
  - speculation on the underlying assets
  - leverage
- Examples of futures exchanges include the Chicago Mercantile Exchange (CME) and its subsidiaries: Chicago Board of Trade (CBOT), New York Mercantile Exchange (NYMEX).

### Futures Exchanges and Products

- Exchanges are responsible for creating futures contracts and therefore dictate the exact specification (expiry dates, delivery, etc.) and underlying assets for these contracts.
- Futures Contracts are available on the following underlying assets:
  - **Agricultural commodities**: wheat, corn, live cattle, dairy, orange juice, etc.
  - **Energy commodities**: crude oil, natural gas, power, etc.
  - **Metals**: gold, nickel copper, etc.
  - **Equities**: indices, single stocks
  - **Fixed income**: US Treasury notes and bonds, interest rates
  - **Foreign Currencies**
- The underlying assets will need to adhere to certain requirements to be accepted - both qualitatively (e.g. the grade of wheat, the maturity of bonds, etc.) and quantitatively (e.g. 10,000 bushels of corn, 100,000 USD bond face value etc.)
- The **delivery month** is the month when the delivery of the underlying asset must take place and will often be used to distinguish different futures contract - e.g. 'the March corn futures contract'.
- Certain assets will also need a **delivery location** specified in the contract too.
- Some ambiguities are left in a futures contract so the seller (short position) in the contract has optionality over the time and location to deliver the underlying asset.
- Only a small fraction of futures contracts are held until expiry and most will be terminated or closed out prior to expiry by the long position holder entering into a short position on the contract - the exchange will then terminate both positions.

### Futures Prices

- Similar to forward contracts prices, futures prices are denoted by $K_{T}(t)$ and futures contracts will have 0 value when being entered into.
- The futures prices are decide by supply and demand forces on futures exchanges and therefore $K_{T}(t)$ represents the market price observed at time $t$.
- The market for the underlying asset will clearly have an effect on the futures market and, in simple terms, the futures prices are expected to represent the market's expectation for the future spot price.
  - This can be expressed in quantitative terms as $K_{T}(t) = E(S(T)|\mathcal{F}_{t})$ where $E(\cdot|\mathcal{F}_{t})$ represents an expectation conditional on the knowledge available at time $t$.
  - Arbitrage opportunities would be present if the futures price systematically underestimated or overestimated the spot price at the expiration of the futures contract.
  - For spot prices $S(t)$ and for a cost of carry $c$, futures price at time $t$ are expected to have the following relationship:
$$\boxed{K_{T}(t) \approx e^{c(T-t)}S(T)}$$
- Futures prices will also consider a risk premium that hedgers are willing to pay for protection from price risk and will agree to less favourable futures prices.
  - The futures price will be an overestimate or underestimate depending on whether the hedgers in the market are net long or short in their positions.
- The general consensus is that a futures price will be determined by a combination of both the predicted spot price at the futures expiration and the risk premium that hedgers are willing to pay.
- It should be noted that the current spot price does not usually determine the futures prices, and in some markets it is the futures prices that actually drive the current spot price.
- **The futures price may be quoted for a single unit where as the contract size will be for a specified number of units**.
  - E.g. Crude oil futures are quoted per barrel of oil but the contract size for a NYMEX oil futures is 1000 barrels. Futures positions are therefore calculated by multiplying the futures contract price by the contract size and then by the number of contracts.
- As shown, the delivery process for futures contracts is a critical process for relating the spot price to the futures price.

#### Convergence of Futures Prices to Spot Prices

- As time $t$ approaches the expiration date $T$, the futures price and spot price will come together (converge).
- During the delivery month, the futures price must equal (or be very close to) the spot price: $K_{T}(T) = S(T)$.
- This relationship can be validated using the arbitrage argument:
  - Taking the case of $K_{T}(T) > S(T)$ in the expiration/delivery month, an arbitrage profit can be realized as follow:
    1. take a short position in the futures contract, receiving $K_T(T)$
    2. purchase the underlying asset at the spot price, paying $S(T)$
    3. immediately make delivery on the futures contract and receive an arbitrage profit of $K_T(T) - S(T)$
  - For the opposite case where $K_{T}(T) < S(T)$, an arbitrage profit can be obtained in a similar way:
    1. take a long position in the futures contract, paying $K_{T}(T)$
    2. receive the underlying asset at delivery of the futures contract
    3. sell the underlying asset on the spot market, receiving $S(T)$ and obtaining an arbitrage profit of $S(T) - K_{T}(T)$

#### Futures Prices versus Forward Contract Prices

- The basic financial structure between forwards and futures is the same; however, the institutional differences between them will lead to price differences.
- Denoting a futures price as $K_{T}(t)$ and a forwards price as $F_{T}(t)$ at time $t$, there will rarely be a case where $K_{T}(t) = F_{T}(t)$ due to the following reasons:
  - the difference in price transparency between the less visible over-the-counter (OTC) forwards market and the publicly visible futures exchanges.
  - the presence of counterparty credit risk for forward contracts (futures exchange acts as counterparty for futures contracts which reduces the counterparty credit risk to almost zero).
  - futures positions will be **marked to market** or settled everyday so there will be cash flow between counterparties (by contrast, cash flow only occurs for forwards at the expiration of the contract).
- In most markets, prices for forwards and futures are closely aligned due to the potential for arbitrage opportunities if large price differences are observed.

### Futures Marking to Market (Settlement)

- The days between the start and expiration of a futures contract can be denoted by $t_{1}, t_{2},...,t_{N} \equiv T$.
- Between day 1 ($t_{1}$) and day 2 ($t_{2}$), the futures price will change from $K_{T}(t_{1})$ to $K_{T}(t_{2})$.
- Taking the case where $K_{T}(t_{2}) < K_{T}(t_{1})$:
  - The seller of the futures contract would  be in the **superior** position and the buyer of the futures contract in the **inferior** position.
  - As part of the daily settlement process at the end of day 2, the exchange would demand a cash payment from the long position holder for an amount equal to $K_{T}(t_{1}) - K_{T}(t_{2})$ and give this amount to the short position holder.
- Similarly for the case where $K_{T}(t_{2}) > K_{T}(t_{1})$:
  - The seller of the futures contract would be in the **inferior** position and the buyer of the futures contract in the **superior** position.
  - As part of the daily settlement process at the end of day 2, the exchange would demand a cash payment from the short position holder for an amount equal to $K_{T}(t_{2}) - K_{T}(t_{1})$ and give this amount to the long position holder.
- The cash flows at settlement between $t_{i}$ and $t_{i+1}$ will be calculated for the actual futures position by:
$$\text{Number of Contracts} \times \text{Contract Size} \times (K_{T}(t_{i+1})-K_{T}(t_{i}))$$

#### Marking to Market Example

- The COMEX Silver futures contract which has a contract size of 5000 ounces.
- If two long positions in the futures contract were taken, the settlement cash flows can calculated by $2 \times 5000 \times (K_{T}(t_{i+1})-K_{T}(t_{i}))$ using the following example settlement prices :
  - $K_{T}(t_{1}) = 16.20 \text{ USD/ounce}$
  - $K_{T}(t_{2}) = 16.50 \text{ USD/ounce}$
  - $K_{T}(t_{3}) = 16.15 \text{ USD/ounce}$
  - $K_{T}(t_{4}) = 16.00 \text{ USD/ounce}$
- On day $t_{2}$ the cash flow will be $2 \times 5000 \times (16.50 - 16.20)) = 3000 \text{ USD}$ so the long position will be credited by this amount (exchange will deliver a cash payment to the account).
- On day $t_{3}$ the cash flow will be $2 \times 5000 \times (16.15 - 16.50)) = -3500 \text{ USD}$ so the long position will be debited by this amount (exchange will demand a cash payment from the account).
- On day $t_{4}$ the cash flow will be $2 \times 5000 \times (16.00 - 16.15)) = -1500 \text{ USD}$ so the long position will be debited by this amount (exchange will demand a cash payment from the account).

#### Margin Accounts

- When a new futures position is opened, the investor must deposit an **initial margin** in cash in a margin **account** with the exchange.
- The margin account is used during the exchange's settlement process, depositing or withdrawing amounts as required.
- The balance of the margin account must not fall below a set level - known as the **maintenance margin**. This is smaller the the initial margin amount.
- The exchange will issue a **margin call** if the balance falls below the maintenance margin requirement.
- The main purpose of margin accounts is to ensure futures investors are able to meet the requirements for the daily settlement process - i.e. this is the exchange protecting itself against counterparty credit risk.
- Using the [marking to market example](./7_forwards_futures_swaps.md#marking-to-market-example) and assuming a initial margin requirement of 3,500 USD and a maintenance margin requirement of 3,000 USD, the flows into and out of the margin account can be shown as follows:
  - A long position in 2 contracts requires a margin deposit of $2 \times 3500 \text{ USD} = 7000 \text{ USD}$, i.e. the starting balance of the margin account.
  - On day two, 3000 USD is deposited into the account leading to a balance in the margin account of 10, 000 USD.
  - On day three, 3500 USD is withdrawn from the account leading to a balance in the margin account of 6,500 USD. This is above the maintenance margin requirement of $2 \times 3000 \text{ USD} = 6000 \text{ USD}$.
  - On day four, 1500 USD is withdrawn from the account leading to a balance in the margin account of 5,000 USD. This is now below the maintenance margin requirement and an additional 2,000 USD will be need to be deposited to reach the initial margin requirement of 7000 USD. Otherwise, the positions will be closed.

#### Futures Settlement versus Forwards Settlements

- First consider the [cash settlement](./7_forwards_futures_swaps.md#settlement) process for forward contracts.
  - The long position in a forward contract is obligated to receive/pay the forward payoff at the expiration date.
  - The [forward payoff](./7_forwards_futures_swaps.md#payoffs) amount will be equal to $S(T) - K$ and can be modelled as a cash flow where, if the payoff is negative, the long position holder must pay the short position holder.
- In the settlement process of a futures contract, the long position holder has the obligation to receive a stream of daily cash flows over the duration of the contract: $[K_{T}(t_{2}) - K_{T}(t_{1})], [K_{T}(t_{2}) - K_{T}(t_{1})], ... , [K_{T}(T) - K_{T}(t_{N-1})]$.
  - Given that futures contracts can be terminated before delivery, a futures position can be viewed as an obligation to receive/pay daily amounts up until the expiration or termination of the contracts.
- With a forward contract, no cash payments are made until the contract expiry when the transaction takes places for the contract forward price.
- The modelling methods used to derive the forward price and contract value ([cash and carry arbitrage](./7_forwards_futures_swaps.md#cash-and-carry-arbitrage) and replication arguments) are therefore not applicable to futures contracts.

### Futures Hedging

#### Cash Market Exposure

- As discussed, the futures prices are strongly linked to the spot prices of their underlying assets:
  - The futures price and spot price converge together at expiration: $K_{T}(T) = S(T)$
  - There is an approximate relationship that relates the futures price at time $t$ to the spot price: $K_{T}(t) \approx e^{c(T-t)}S(t)$ where $c$ is the cost of carry.
    - This is due to arbitrage opportunities becoming present with any large deviations from this approximation.
    - Any resulting arbitrage opportunities being taken will force the prices closer together.
- Exposure to the cash market can therefore be obtained by taking a futures position and can be proven as follows:
  - Taking an initial case where the cost of carry $c$ can assumed to be zero: $c = 0$, the futures contract price is equal to the underlying spot price: $K_{T}(t) = S(t)$.
  - Through the settlement process, the value of a long futures position will following the change in value of the underlying spot price: $K_{T}(t_{2}) - K_{T}(t_{1}) = S(t_{2}) - S(t_{1})$ per unit.
  - This change in value will be scaled up if the contract size is $C$ units and the position size is $J$ contracts: $JC(K_{T}(t_{2}) - K_{T}(t_{1})) = JC(S(t_{2}) - S(t_{1}))$.
  - For a long position of J futures contracts, the daily profit and losses will exactly match the profit and losses of holding JC units of the underlying asset.
  - A short position of J futures contracts would be exposed to reversed value changes: $JC(K_{T}(t_{1}) - K_{T}(t_{2})) = JC(S(t_{1}) - S(t_{2}))$.

#### Risk Management using Futures Hedging

- Price risk in an asset can be controlled through hedging with futures contracts due to the exposure futures contracts have to the underlying asset's cash market.
- A **long cash position** can be hedged with a **short futures position**, and similarly, a **short cash position** can be hedged with a **long futures position**.
- For a cash position containing $N$ units of an asset at a price per unit of $S(t)$, the number of futures contracts of contract size $C$ required to hedge the entire position would be $J = \frac{N}{C}$.
  - For the case that $\frac{N}{C}$ is not an integer, $J$ would be rounded up to the nearest integer.
- A futures position that fully hedges a cash position is called a **unitary hedge**.
- Denote the value of a portfolio containing the underlying assets and futures positions required for the cash position to be unitary hedged as $W(t)$.
  - For a position that is long $N$ units of the underlying asset (cash position) and short $J$ futures contracts (futures position) the portfolio value is: $W(t) = NS(t) + \text{ Short Futures Position Value}$.
  - The 1-day change in the portfolio value is therefore:  
$$\Delta W(t) = \Delta \text{Cash} + \Delta \text{Futures}$$
$$ \Delta W(t)= N \Delta S(t) - JC \Delta K_{T}(t) \text{ where } J = \frac{N}{C}$$
$$\Delta W(t) = N \Delta S(t)- N \Delta K_{T}(t)$$
$$\Delta W(t) = N(S(t_{2}) - S(t_{1}))- N(K_{T}(t_{2}) - K_{T}(t_{1})) \text{ where } K_{T}(t_{2}) - K_{T}(t_{1}) = S(t_{2}) - S(t_{1})$$
$$\Delta W(t) = N(S(t_{2}) - S(t_{1}))- N(S(t_{2}) - S(t_{1}))$$
$$ \therefore \Delta W(t) = 0$$
- As shown, any changes in the price of a underlying asset, in this idealised scenario, has no effect on the value of a unitary hedged portfolio.
  - This is known as a **perfect hedge**.

#### Futures Hedging Example 1: Oil Refinery

- In the current month, June, an oil refinery is planning for the number of barrels required for the month of October.
- The refinery expects to refine a total of 2 millions barrels of oil in October and wants to control its price risk through futures hedging.
- The current spot price for WTI is 55 USD per barrel.
- The cost of carry is assumed to be 0 so the futures price is equal to the spot price: $K_{T}(t) = S(t) = 55 \text{ USD}$.
- The contract size for the NYMEX WTI crude oil futures contract is 1000 barrels.
- Given that the refinery needs 2 million barrels (i.e. the refinery is short), the refinery will need to take a long position in $\frac{2000000}{1000} = 2000$ futures contracts to hedge the price of WTI.
- The November futures contract will be chosen as the hedging instrument as it delivers from the 1st November, ensuring complete coverage of October.
- The portfolio value is equal to the long futures position plus the short cash position (i.e. the need for the barrels of oil).
- For a spot price in October of 60 USD per barrel, the change in the value of the position is therefore:
$$\Delta W(t) = \Delta \text{Cash} + \Delta \text{Futures}$$
$$\Delta W(t) = -2000000\Delta S(t) + (2000)(1000) \Delta K_{T}(t)$$
$$\Delta W(t) = (-2000000)(60 - 55) + (2000)(1000)(60 -55)$$
$$\Delta W(t) = 0$$
- This is an example of a **perfect hedge** and is unrealistic in practice due to the cost of carry rarely being equal to 0.

#### Basis Risk

- The **basis** is the difference between the spot and the futures prices and is denoted $b(t)$ (or $b_{T}(t)$ if explicitly denoting the futures expiry).
$$b(t) = S(t) - K_{T}(t)$$
- By assuming the cost of carry to be 0 in previous examples, the spot and futures price were assumed to be equal: $S(t) = K_{T}(t)$, and so the basis $b(t)$ was also assumed to be 0.
- Assuming a non-zero cost of carry, $c \not ={0}$, and using the formula from [futures prices](#futures-prices): $K_{T}(t) = e^{c(T-t)}S(t)$, the basis can be calculated by:
$$b(t) = S(t) - e^{c(T-t)}S(t)$$
$$b(t) =  \left(1 - e^{c(T-t)} \right)S(t)$$
- Using a [Taylor Series](https://mathworld.wolfram.com/TaylorSeries.html) approximation and more specifically the [Maclaurin Series](https://mathworld.wolfram.com/MaclaurinSeries.html) for $e^{x} = 1 + x + \frac{1}{2}x^{2} + \frac{1}{6}x^{3} + \frac{1}{24}x^{4}...$ where $x = c(T-t)$, the basis risk can be approximated by:
$$e^{c(T-t)} = 1 + c(T-t) + \text{error (H.O.T.)}$$
- Assuming the error (higher order terms) will be small for short-dated contracts or for low cost of carry:
  $$b(t) = [1-(1+c(T-t))]S(t)$$
  $$b(t) = -c(T-t)S(t)$$

##### Commodity Basis Risk

- For a commodity, the cost of carry $c$ is calculated by adding the interest rate $r$ and the storage costs $s$ and subtracting the convenience yield $y$:
$$c = r + s - y$$
- The basis can then be calculated by:
$$b(t) = -(r+s-y)(T-t)S(t)$$
$$b(t) = - \underbrace{r(T-t)S(t)}_{\text{Finance}} - \underbrace{s(T-t)S(t)}_{\text{Storage}} + \underbrace{y(T-t)S(t)}_{\text{Convenience}}$$
- As discussed in [futures price](#futures-prices), the arbitrage relationship $K_{T}(t) = e^{c(T-t)}S(t)$ is only an approximation as prices will fluctuate around this assumption in practice due to the forces of supply and demand.
  - For a commodity, the futures price $K_{T}(t)$ will fluctuate from the spot price $S(t)$ through the forces of supply and demand in combination with the finance, storage and convenience factors associated with the cost of carry.
- In summary, the basis for a commodities futures will be determind by:
  - Interest charges/rates
  - Local storage and transportation costs
  - Locally determined convenience yields
  - Fluctuations driven by supply and demand driven

##### Basis Risk Example

- Taking a long position in $N$ units of an asset asset hedged with a short futures positions in $N$ units, the change in value of the combined position between $t_{1}$ and $t_{2}$ can be denoted as $\Delta W(t)$:
$$\Delta W(t) = \Delta [\text{Cash Value}] + \Delta [\text{Futures Value}]$$
$$\Delta W(t) = N \Delta S - N \Delta K_{T}$$
$$\Delta W(t) = N(S(t_{2}) - S(t_{1})) - N(K_{T}(t_{2}) - K_{T}(t_{1}))$$
$$\Delta W(t) = N(S(t_{2}) - K_{T}(t_{2})) - N(S(t_{1}) - K_{T}(t_{1}))$$
$$\Delta W(t) = Nb(t_{2})- Nb(t_{1})$$
$$\Delta W(t) = \underbrace{N}_{\text{Position Size}} \times \underbrace{(b(t_{2}) - b(t_{1}))}_{\text{Basis Change}}$$
- In the case of a unitary hedge, i.e. purchasing enough futures contracts to completely offset the cash position in the underlying asset, the price risk is therefore replaced with basis risk.
- Basis risk is a lot smaller than price risk so from a risk management perspective, this is a good trade-off.
- A perfect unitary hedge is not achievable in practice due to the existence of futures basis and other market complexities, but futures hedging is still an effective tool for reducing price risk.