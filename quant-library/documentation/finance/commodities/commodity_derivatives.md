# Commodity Derivatives

- [Commodity Derivatives](#commodity-derivatives)
  - [Introduction to Derivative Products](#introduction-to-derivative-products)
    - [Forward Contracts](#forward-contracts)
    - [Futures](#futures)
    - [Swaps](#swaps)
      - [Application of Swaps in Commodity Markets](#application-of-swaps-in-commodity-markets)
      - [Structure of Swap Products](#structure-of-swap-products)
    - [Options](#options)
    - [Exotic Options](#exotic-options)
      - [Binary Options (Digital Options)](#binary-options-digital-options)
      - [Barrier Options](#barrier-options)
      - [Spread Options](#spread-options)
      - [Average Rate Options (Avros)](#average-rate-options-avros)
  - [Valuation of Derivatives](#valuation-of-derivatives)

## Introduction to Derivative Products

In commodities trading, forward contracts, futures , swaps, and options are used to speculate and secure prices for delivery at a future point in time, offering price certainty and risk management. These products are discussed more generally in sections: [Forwards, Futures, and Swaps](./7_forwards_futures_swaps.md) as well as [Options](./9_options.md)

### Forward Contracts

- Forward contracts are agreements to buy or sell a commodity at a future date for a price agreed upon today.
- These contracts are negotiated directly between the buyer and seller, often over-the-counter (OTC), and involve a binding commitment that cannot be easily exited without mutual agreement.
- A variation called a "floating forward" sets the price at the point of delivery, often based on a pre-agreed formula, such as the average of daily spot prices before settlement.

### Futures

- Futures are standardized contracts traded on organized exchanges like the CME Group, providing similar economic outcomes as forwards but with key differences in trading and margin requirements.
- Unlike forwards, futures contracts require an initial margin deposit (about 5% of the contract's market value) and are subject to ongoing margin adjustments based on market movements.
- Futures also ensure standardization in the quality and grade of the underlying commodity, such as specific requirements for the delivery of metals like gold.
- Most futures contracts (approximately 95%) are closed before their expiry, as they are typically used for risk management rather than physical delivery.

### Swaps

- Swaps are financial agreements where two parties exchange cash flows based on different price indices, typically involving one party paying a fixed rate and the other a variable or floating rate.
- These contracts are usually negotiated over-the-counter (OTC) and are based on a notional amount that sets the magnitude of the cash flows, though the notional amount itself is not exchanged.
- The main motivation for entering into a swap is risk management. For example, a company that regularly purchases a commodity at market prices might enter into a swap to hedge against potential price increases.
  - In this arrangement, the company would pay a fixed rate and receive cash flows based on market price movements, transferring the price risk to the counterparty, often an investment bank.
  - The bank, in turn, may offset this exposure by entering into a similar, opposite swap transaction and make a profit from the bid-offer spread.

#### Application of Swaps in Commodity Markets

- Swaps are used across various commodity markets to manage price risk:
  - Gold: Involves paying a fixed lease rate and receiving a variable lease rate.
  - Base Metals: A common swap might involve paying a fixed aluminum price and receiving the average price of near-dated aluminum futures, known as an "Asian swap" when the floating rate is based on an average price over a period.

#### Structure of Swap Products

- Swaps can start two days after trading (spot starting) or at a future date (forward starting).
- The frequency of cash flow settlements can vary between 1 and 12 months, depending on the terms negotiated between the parties.
- A unique feature of commodity swaps, particularly relevant in "Asian swaps," is the use of an average rate for the floating leg, which aligns with the average price exposures that many commodity hedgers face.
- Swaps are traded on a bid-offer spread basis.
- The market convention is that the buyer receives a stream of variable cash flows in exchange for a fixed rate, while the seller delivers floating cash flows and receives a fixed rate.
- Although terms like "buy" and "sell" are used, it's clearer to specify who pays and who receives the fixed rate to avoid confusion.

### Options

- Options provide a flexible alternative to forward contracts in commodities trading.
- While forward contracts lock the buyer into a fixed price, which can be unprofitable if the market price drops, options offer the buyer protection with the ability to benefit if the market moves in their favour.

> An option is a financial derivative that grants the buyer the right, but not the obligation, to buy or sell a commodity at a predetermined price (the strike price) on or before a specific date.

- Options come in two primary forms:
  - **Call Option**: Grants the right to buy the underlying commodity at the strike price.
  - **Put Option**: Grants the right to sell the underlying commodity at the strike price.
- The exercise price, or strike price, is negotiated between the buyer and seller.
- Options can be either physically settled, where the commodity is actually delivered, or cash-settled, where the difference between the strike price and the market price at expiration is paid in cash.
- Options can be exercised in different ways depending on their style:
  - **European**: Exercised only on the maturity date.
  - **American**: Exercised at any time before maturity.
  - **Bermudan**: Exercised on specific dates prior to maturity.
- The value of an option depends on its relationship to the market price:
  - **In-the-Money (ITM)**: The strike price is more favourable than the current market price.
  - **Out-of-the-Money (OTM)**: The strike price is less favourable than the current market price.
  - **At-the-Money (ATM)**: The strike price is equal to the current market price.
u- Options are purchased for a premium, which reflects their value and potential to protect against unfavourable market movements or to capitalize on favourable ones.
- Options can be employed in various strategies depending on the user's goals:
  - **Directional Exposure**: For speculating on market movements. For example, buying a call option to profit from an expected rise in gold prices.
  - **Implied Volatility Trading**: Focusing on the option’s behaviour before maturity, trading on the volatility itself.
  - **Hedging**: Offering a flexible risk management tool, often preferred over forwards for their ability to limit downside risk while allowing for upside potential.
  - **Outperformance**: Options can be used to achieve returns above certain benchmarks, like using options on gold to outperform standard interest rates.

### Exotic Options

Exotic options differ from standard American and European options, featuring unique profit and loss structures. Each type of exotic option introduces specific characteristics and complexities, making them useful in different derivative structures and market conditions. Key types include:

#### Binary Options (Digital Options)

 These options resemble simple bets where the buyer pays a premium and receives a fixed return if the option is exercised, regardless of the spot price. Unlike traditional options, the payout is a fixed amount of money, not dependent on the market value at the time of exercise.

#### Barrier Options

These involve a standard option that can be either cancelled (knock-out) or activated (knock-in) if the underlying asset's price hits a certain level, known as a barrier or trigger. Barriers can be standard (placed out-of-the-money) or reverse (placed in-the-money).

![Barrier Options](images/barrier-options.png "Barrier Options")

#### Spread Options

These options pay off based on the price difference between two assets relative to a pre-set strike price. They are particularly popular in commodities, where they can hedge or speculate on the price difference between inputs and outputs, locations, or delivery dates.

#### Average Rate Options (Avros)

These are the most common commodity options, with payoffs based on the average price over a set period rather than the price at maturity. They align with physical supply contracts, reducing volatility effects but also limiting benefits from sudden price drops. Average rate options usually have lower premiums compared to equivalent European options due to the averaging effect.

## Valuation of Derivatives

- Commodities cannot be modelled as a future stream of cash flows, unlike bonds and stocks. Discounted cash flow analysis is therefore not used for pricing commodities.
- Market forces of supply and demand determine commodity prices; however, there are identifiable trends in commodity price time series, and other market driven features relating to seasonality.
- **Benchmarks** exist for certain assets to help with the valuation of non-homogenous products, e.g. crude oil is often priced relative to a futures contract on a Brent Blend.
  - A globally accepted benchmark will facilitate trading for different grades of a commodity.
  - E.g. a popular iron ore benchmark has a grade of 62% (i.e. the ore contains 62% iron, Fe). The traded grades of iron ore will vary from 30% to the mid 60% and be priced relative to the 62% benchmark price.