# Equities

- [Equities](#equities)
  - [Introduction](#introduction)
    - [Stock Markets](#stock-markets)
    - [Dividends](#dividends)
    - [Valuation](#valuation)
    - [Volatility](#volatility)
    - [Historical Price Analysis and Log-Returns](#historical-price-analysis-and-log-returns)

## Introduction

- **Common stock** denotes securities which imply an ownership position (equity) in a company. Usually this is just referred to as *stock*.
- The indivisible unit of a stock is a **share** (although *fractional shares* do exist) and the owners of a company's stock are called the *shareholders*.
- A **charter** or **certificate of incorporation** outlines the rights of the shareholders.
- Shareholders are paid **dividends** (depending on the company) out of the earnings.
- Shareholders also possess voting rights as specified by the company's charter.
- **Debt holders** receive interest payments before any dividends are paid by the company. They are the first to be compensated in the case of bankruptcy.#
- **Preferred stock holders** have next priority after the debt holders for receiving dividends and reimbursement in the case of liquidation of the company. However, they do not have voting rights and have limited potential for capital gain as their dividends are usually fixed.

### Stock Markets

- Shares in **privately held companies** are bought and sold in private deals with very little transparency to the public.
- **Publicly traded companies** are listed on prominent stock exchanges such as the New York Stock Exchange (NYSE), the NASDAQ, the London Stock Exchange, or on over the counter (OTC) markets.
  - **Over the counter (OTC) markets** consist of networks of dealers who make private transaction amongst themselves and with customers.

### Dividends

- The dividend policy will vary from company to company depending on the corporate strategy.
- Generally, more established companies will pay dividends whilst younger, growing companies will reinvest their earnings (R&D etc.) instead of paying dividends.
- Dividends are normally paid on a *per share* basis and therefore stock holders will receive a cash amount for each share they own.
- The **ex-dividend date** is the cut-off point for being eligible to receive dividends. Investors who purchase stock *on or after* the ex-dividend date are will not be paid dividends on their shares.
  - Due to market force, the share price drops by the value of the divided per share on the ex-dividend date.
- The **dividend yield** is the value of the dividends that a company pays out per year as a percentage of its share price.
  - If a stock, with price $S(t)$, pays dividends, the dividend yield can be modelled as a continuously compounded yield $y$, acting like an interest rate.
  - At time $t = 0$, with an initial allocation of $\alpha$ shares, and assuming all dividends are reinvested into the stock holding, the allocation at time $t$ is $\alpha e^{yt}$.
  - The investment at time $t$ is therefore $\alpha e^{yt}S(t)$.
  - Modelling the dividends with a continuous yield is most appropriate for stock indices or portfolios. For an individual stock, a more accurate model is to model the dividend as a lump sum payment.

### Valuation

- Supply and demand on the markets is the primary force behind the **share prices**. Valuation theory for stocks is based on the same core principle as bond valuation theory.
- The fair value of a stock is calculated as the present value of the stream of income the stock is expected to generate; however, unlike with bonds, the income stream is uncertain.
  - The discount factors in stock valuation must therefore incorporate the uncertainty of any future cash flows. Risk-free rates should not be used.
- The **dividend discount model** calculates the value as the present value of the stream of dividend payments. The **Modigliani-Miller Theorem** proposed that a company's dividend policy is immaterial to its value and the future earnings would be a better measure of a company's valuation.
- Most valuation models agree that the value of a company is predominantly determined by its future profitability.

### Volatility

- Relevant news being announced (by either the company themselves or by the media) can increase the volatility of company's share price.
- The volatility level of the majority of share prices is viewed as being too high to be solely based on expectations.
- Purely speculative activity, separate from economic fundamentals, is viewed as the main reason for the excess volatility on share prices.

### Historical Price Analysis and Log-Returns

- Unlike risk-free investments where future values are known with certainty, stock prices exhibit random movements that cannot be predicted deterministically.
- The historical behaviour of stock prices can be analysed statistically to inform mathematical models.

**Log-Returns Definition:**

For a stock with closing price $S_i$ on day $i$, the logarithmic (fractional) daily return is defined as:

$$L_i = \log\left(\frac{S_i}{S_{i-1}}\right) = \log S_i - \log S_{i-1}$$

**Empirical Observations:**

When histogramming daily log-returns for typical stocks, two key observations emerge:

1. **Daily log-returns are approximately normally distributed** - the histogram resembles a bell curve centered near zero.
2. **There appear to be no serial correlations** in the daily log-returns - knowing today's return provides no useful information for predicting tomorrow's return.

These empirical observations motivate the choice of **Geometric Brownian Motion (GBM)** as a mathematical model for stock price movements, where the log-price follows a Brownian motion with drift.

**Risk Aversion and Expected Returns:**

Since investors can obtain a guaranteed rate of return by depositing money in a bank, most investors are **risk-averse** and will only purchase risky assets (such as shares) if the expected (mean) return $\mu$ exceeds the risk-free rate.

Due to this widespread risk aversion, shares trade at prices such that expected returns are greater than the risk-free rate - the difference being compensation for bearing the additional risk.
