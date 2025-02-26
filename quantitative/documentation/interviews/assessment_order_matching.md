# Stock Trading Order Matching

## Overview

You are processing a set of records representing a day of trading activity in a market between buyers and sellers. Each record represents an order and needs to be processed according to the given rules to compute:

- **Profit**: The total profit from successful trade matches.
- **Long Exposure**: The total value of unmatched buy orders.
- **Short Exposure**: The total value of unmatched sell orders.

## Input Format

Each record follows this format:

```text
<Share> <Action_1> <Size_1> <Price_1> [<Action_2> <Size_2> <Price_2> ...]
```

Example

```text
COMPANY1 OFFER 10 25 BID 20 45
```

### Definitions

- **Share**: A company name without spaces.
- **Action**: The type of order, which can be one of:
  - `BUY`: The trader is buying shares immediately.
  - `SELL`: The trader is selling shares immediately.
  - `BID`: A buy order left in the market to be matched later.
  - `OFFER`: A sell order left in the market to be matched later.
- **Size**: The number of shares in the order.
- **Price**: The price per share.

A single record can contain multiple orders for the same share.

## Order Matching Rules

Orders are processed in sequence, and matching follows these principles:

1. **Matching Criteria**:
   - A trade occurs when a `BUY` or `BID` matches an `OFFER` or `SELL` with the same or a *better price*.
   - A *better price* means:
     - For buy orders (`BUY`/`BID`): Lower price is better.
     - For sell orders (`SELL`/`OFFER`): Higher price is better.
2. Order Execution Rules:
   - Orders with matching prices are fulfilled in *first-come, first-serve* (FIFO) order.
   - If an order can only be partially fulfilled, the remaining part stays in the market.
   - Profit from a transaction is calculated as:
     - Profit(`BUY`) = `BID` price - `OFFER` price
     - Profit(`SELL`) = `BID` price - `SELL` price
   - If an order matches an order of the same type (e.g., BUY vs. BID), no trade occurs.
3. Unmatched Orders (Exposure Calculation):
   - Any remaining buy orders (both BUY and BID) contribute to long exposure, calculated as:
    $$ \text{Long Exposure} = \sum(\text{Size} \times \text{Price}) \text{ of unmatched buy orders}$$
   - Any remaining sell orders (both SELL and OFFER) contribute to short exposure, calculated as:
    $$ \text{Short Exposure} = \sum(\text{Size} \times \text{Price}) \text{ of unmatched sell orders}$$

## Task

Implement the function:

```csharp
(int profit, int longExposure, int shortExposure) Trade(List<string> records)
```

### Function Parameters

- `records`: A list of strings, where each string represents an order record.

### Return Value

A tuple containing:

- `profit` (`int`): The total profit from matched trades.
- `longExposure` (`int`): The total value of unmatched buy orders.
- `shortExposure` (`int`): The total value of unmatched sell orders.

## Example Input and Output

### Example 1

Input:

```text
COMPANY1 OFFER 10 25
COMPANY1 BUY 10 20
```

Output:

```text
(0, 200, 0)
```

Explanation:

- The `COMPANY1 BUY 10 20` does not match `COMPANY1 OFFER 10 25` since the buy price (`20`) is lower.
- The buy order remains unmatched, adding long exposure = $10 \times 20 = 200$.
- The sell order also remains unmatched, but short exposure is not counted for unmatched offers that failed to trade.

### Example 2

Input:

```text
COMPANY1 BUY 10 20 SELL 5 25 OFFER 10 18 BID 5 28
```

Output:

```text
(35, 0, 0)
```

Explanation:

- The `BID 5 @ 28` matches `OFFER 5 @ 18`, generating profit: $(28 - 18) \times 5 = 50$.
- The `BUY 10 @ 20` matches `SELL 5 @ 25`, generating profit: $(25 - 20) \times 5 = 25$.
- Total profit = $50 - 25 = 35$.
- No unmatched orders remain, so long exposure = $0$, short exposure = $0$.

### Example 3

Input:

```text
COMPANY2 SELL 27 1
COMPANY1 BID 5 20 OFFER 5 25
COMPANY3 BID 3 120 OFFER 7 150
COMPANY4 BID 10 140 BID 7 150 OFFER 14 180
COMPANY2 BID 25 3 OFFER 25 6
COMPANY5 BID 21 65 OFFER 35 85
COMPANY6 BID 50 80 OFFER 100 90
COMPANY7 BID 200 13 OFFER 100 19
COMPANY8 BID 55 25 OFFER 80 30
COMPANY5 BUY 50 100
COMPANY9 SELL 100 67
COMPANY1 BUY 5 30
COMPANY8 SELL 5 30
COMPANY4 BUY 2 200
COMPANY3 BUY 2 150
COMPANY7 SELL 50 11
COMPANY6 BUY 200 100
COMPANY9 BID 1000 77 OFFER 500 88
```

Output:

```text
(2740 , 11500, 152)
```

## Constraints & Assumptions

- The input list is non-empty and contains valid order formats.
- The function should be efficient and handle up to $10^{5}$ orders.
- Orders should be stored efficiently (e.g., using priority queues or FIFO queues for matching).

## Bonus Challenge (Optional)

- Extend the solution to support multiple shares being processed concurrently.
- Optimize the matching mechanism for faster performance in large datasets.
