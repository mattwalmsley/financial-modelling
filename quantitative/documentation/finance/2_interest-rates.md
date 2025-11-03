# Interest Rates

- [Interest Rates](#interest-rates)
  - [Introduction](#introduction)
  - [Assumptions](#assumptions)
  - [Term Structure](#term-structure)
  - [Investment Returns](#investment-returns)
    - [Gross Return](#gross-return)
    - [Net Return](#net-return)
    - [Annual Compounding](#annual-compounding)
    - [Future Value](#future-value)
    - [Periodic Compounding](#periodic-compounding)
    - [Interest Rate Conversions](#interest-rate-conversions)
    - [Continuous Compounding](#continuous-compounding)
  - [Time Value of Money](#time-value-of-money)
  - [Present Value](#present-value)
  - [Discount Factors](#discount-factors)
  - [Discounted Cash Flow Analysis](#discounted-cash-flow-analysis)
  - [Simple Interest](#simple-interest)
  - [Day Count Conventions](#day-count-conventions)
  - [LIBOR](#libor)
  - [Federal Funds Rate](#federal-funds-rate)
  - [SONIA](#sonia)
    - [SONIA Compounded in Arrears](#sonia-compounded-in-arrears)
  - [SOFR](#sofr)
    - [Compound SOFR](#compound-sofr)
      - [Issues with Compounding in Arrears](#issues-with-compounding-in-arrears)
    - [Credit Sensitive Alternatives to SOFR](#credit-sensitive-alternatives-to-sofr)

## Introduction

- Interest rates are measures of the price charged in the economy to borrow money.
- Terminology:
  - The charge levied to borrow money is called **interest**.
  - **Principal** is the amount of money borrowed in a loan.
  - The **interest rate** is the fraction of the principal of a loan that will be charged as interest per unit time.
  - An **annual interest rate** is an interest rate for which the implicit time unit is one year.
- Simple formula:
  - Principal _X_ at annual interest rate $r$
  - Total one year interest is $rX$
  - Total debt after one year, assuming no payments and annual compounding, is $X + rX$
  - This can be written as $(1 + r)X$
- Interest rates are determined by market activity.
  - Prices are negotiated between borrowers and lenders of money.
  - Borrowers want to borrow money as cheaply as possible, so will take the lowest interest rate available.
  - Lenders want to earn the highest possible rate, but have the risk of the borrowers defaulting.
    - Lenders (and investors) therefore require more compensation for loaning to riskier borrowers.
    - Riskier investments require a higher interest rate.
  - The market for borrowers and lenders is usually divided into two types:
    - **Money Market** for short term loans, primarily up to 12 months.
    - **Bond Market** for debt with terms longer than 12 months.
- Interest rates are also heavily influenced by the actions of governments and central banks who sent a base rate of interest.
  - Other interest rate levels are then realized as adjustments (spreads) to the central bank's base rate, by factoring in risk characteristics.
- Risk free interest rate
  - Theoretical rate of interest for a risk free investment.
  - In the real-world the **Secured Overnight Financing Rate (SOFR)** is used.
  - Core concept used for derivatives pricing.

## Assumptions

- These assumptions hold true unless stated otherwise:
  - Interest rates are risk free (usually referred to as the risk-free rate).
  - Term structures are flat (very little variation between short and long-term yields, usually indicative of the market being unsure about the future direction of the economy).
  - Interest rates are continuously compounded.
  - Interest rates are constant in time.
  - The variable $r$ will be used to represent interest rates, which are understood to be _deterministic_, a _constant function of time/term_, and a _risk-free continuously compounded_ rate.
- These assumptions lead to a crude model of interest rates, but will be sufficient for non-fixed income products.
- The following products will deviate from these assumptions (where stated):
  - **Bonds and interest rate products** (fixed-income) - the compounding convention will usually be the same as the frequency of the coupon payments and the term structures are not assumed to be flat.
  - **Swaps** (closely related to fixed income products) - the compounding convention will be semi-annually or quarterly and will be not be constant with time.

## Term Structure

- Risks are different for different loan terms, with longer terms carrying higher interest rates.
- Interest rates are a function of the **loan term** (the duration of time the loan is held).
- $r(t)$ is used to denote the interest rate for borrowing money over a loan term $t$.
- The function $r(t)$ can be used to represent the following:
  - An interest rate with the term to maturity $t$.
  - The interest rate observed on market at time $t$, referred to as calendar time.
- The notation $r(t, T)$ is used to denote the interest rate maturing at date $T$, observed at time $t$. This implies that the term to maturity is $T - t$.

## Investment Returns

- Interest rates quantify a return on an investment for an investor.
- Let $V(t)$ represent the value of an investment at time $t$.
- The return on the investment at time $t + \tau$ can be represented with the _gross return_ and the _net return_.
  - $Net Return = Gross Return -1$

### Gross Return

- Measures what an investment returns as a fraction of the initial investment.
- Between time $t$ and time $t + \tau$, the gross return is $\frac{V(t + \tau)}{V(t)}$.

### Net Return

- Measures the profit an investment has earned as a fraction of the initial investment.
- Between time $t$ and time $t + \tau$, the net return is $\frac{V(t + \tau) - V(t)}{V(t)}$.

### Annual Compounding

- Interest earned is calculated on the current amount at the end of each year, rather than the principal at inception. This leads to an increase in the interest earned every year.
- Example
  - $X$ is invested for two years at interest rate $r(2)$ which is annually compounded.
  - After one year, the total investment value is $(1 + r(2))X$ and this then becomes the principal on which interest is charged for the second year.
  - Therefore, after two years, the investment value is $(1 + r(2))(1 + r(2))X$.
  - This can be written as $(1 + r(2))^2X$.

### Future Value

- The value of an investment after a term with a fixed interest rate, assuming all returns are reinvested at the same interest rate.
- Let $r(t)$ be the annual interest rate which is compounded for a loan term of $t$ years.
- Let $P_0$ be the initial investment.
- The future value of $P_0$, at time $t$ is:
$$P(t)=(1 + r(t))^tP_0$$

### Periodic Compounding

- Interest is compounded with frequency $m$ if the interest is reinvested with the principal $m$ times per year.
- Denoting $r_m(t)$ to be the interest rate compounded $m$ times per year with term $t$.
- In each compounding period ($m$ times per year), the earned interest is $\frac{r_m(t)X}{m}$.
- The value of the investment after one period is $X + \frac{r_m(t)X}{m} \equiv \left(1 + \frac{r_m(t)}{m}\right)X$.
- The interest earned in the second period is calculated by applying the interest rate to the combined principal and interest earned so far is $\frac{r_m(t)}{m}\left(1 + \frac{r_m(t)}{m}\right)X$.
- The value of the investment after two periods is $\left(1 + \frac{r_m(t)}{m}\right)X + \frac{r_m(t)}{m}\left(1 + \frac{r_m(t)}{m}\right)X \equiv \left(1 + \frac{r_m(t)}{m}\right)^2X$.
- The future value of an investment $X$ in $t$ years:
$$P(t)=\left(1 + \frac{r_m(t)}{m}\right)^{mt}X$$

### Interest Rate Conversions

- For an investment $X$ with future value $P(t)$ in $t$ years, the gross return is defined as:
$$\frac{P(t)}{X} \equiv \frac{\left(1 + \frac{r_m(t)}{m}\right)^{mt}X}{X} \equiv \left(1 + \frac{r_m(t)}{m}\right)^{mt}$$
- Interest rates are considered to be _equivalent_ if they lead to the same total return, i.e the same gross or net return.
- For two interest rates $r_m(t)$ and $r_k(t)$, equate the gross returns of 1 USD to express $r_m(t)$ in terms of $r_k(t)$:
$$\left(1 + \frac{r_m(t)}{m}\right)^{mt} = \left(1 + \frac{r_k(t)}{k}\right)^{kt} \Rightarrow r_m(t) = m\left(1 + \frac{r_k(t)}{k}\right)^{\frac{k}{m}} - m$$

### Continuous Compounding

- Instantaneous compounding of all interest income - as soon as interest is paid, new interest is paid on it.
- Mathematically, this is the limit of periodic compounding as the period goes to 0 or the frequency goes to infinity.
- This provides a useful approximation as the accuracy can be optimised by choosing the continuously compounded rate that corresponds to a prevailing periodically compounded rate.
  - To change from periodic compounding to continuous compounding, set the limit of the compounding frequency $m$, to infinity:
$$\lim_{m \to \infty}\left(1 + \frac{r}{m}\right)^{mt} = e^{rt} \Rightarrow P(t) = e^{rt}X$$
  - With $r_c$ as the continuously compounded risk-free rate and $r_a$ as the annually compounded risk-free rate, equate the future values of 1 USD in a similar approach to periodically compounded in interest rates:
$$e^{r_ct} = (1 + r_a)^t \Rightarrow r_ct = log((1 + r_a)^t) \Rightarrow r_c = log(1 + r_a)$$

## Time Value of Money

- Concept that the value of 1 USD today is more than the value of 1 USD in a year's time.
  - This because of the opportunity cost associated with not receiving the 1 USD today.
- Interest rates are closely linked to the time value of money as the annual interest received on 1 USD can be viewed as a component of the opportunity cost.

## Present Value

- The present value $PV$ of an investment $X$, valued at time $t$, is the amount that should be invested today, accounting for prevailing interest rates, so that at time $t$, the investment of value $PV$ is worth $X$.
- Assuming a prevailing risk-free, annually compounded interest rate $r$:
$$(1 + r)^tPV = X \Rightarrow PV = \frac{X}{(1 + r)^t}$$
- For a periodically compounded interest rate $r_m$, with compounding frequency $m$:
$$\left(1 + \frac{r_m}{m}\right)^{mt}PV = X \Rightarrow PV = \frac{X}{\left(1 + \frac{r_m}{m}\right)^{mt}}$$
- For a continuously compounded interest rate $r_c$:
$$e^{r_ct}PV = X \Rightarrow PV = e^{-r_ct}X$$
- For example, to find the continuously compounded interest rate $r_c$ that is equivalent to semi-annual interest rate $r_2$, equate the future values of a 1 USD investment with the two interest rates:
$$e^{r_ct} = \left(1 + \frac{r_2}{2}\right)^{2t} \Rightarrow r_ct = log\left(\left(1 + \frac{r_2}{2}\right)^{2t}\right) \Rightarrow r_c = 2log\left(1 + \frac{r_2}{2}\right)$$

## Discount Factors

- The present value, $PV = \frac{X}{(1 + r)^t}$, can be viewed as a discounted value of X, assuming that $(1 + r)^t > 1$.
- Discounted value and present value can be used interchangeably.
- Rewriting present value as a function of time gives $PV = d(t)X$ where the discount factor can be expressed as $d(t) = \frac{1}{(1 +r)^t}$.
- The future value at time $t$ of a 1 USD investment today is $(1 + r)^t$ which is the reciprocal of $d(t)$, i.e. $\frac{1}{d(t)} = (1 + r)^t$.
  - Therefore, the future value of an investment $P_0 = X$ today is:
$$P(t) = \frac{1}{d(t)}X = (1 + r)^tX$$
- Discount factors can be expressed in terms of interest rates with different compounding convention.
  - For periodically compounded rates: $d(t) = \frac{1}{\left(1 + \frac{r_m}{m}\right)^{mt}}$.
  - For continuously compounded rates: $d(t) = e^{-r_{c}t}$.

## Discounted Cash Flow Analysis

- For an asset that pays amounts $c_1, c_2, \dots, c_N$ (cash flows) at respective times $t_1, t_2, \dots, t_N$, an individual payment $c_i$ will be made at time $t_i$.
- To value the asset, the present value of a stream of cash flows needs to be calculated.
- The present value of an individual payment $c_i$ with discount factor $d(t_i)$ is $d(t_i)c_i$.
- Model the present value of a stream of cash flows as the present value of an individual cash flow - i.e. the total amount that needs to be invested today to replicate the stream of cash flows.
- Each cash flow is independent so the present value of the cash flow stream is the sum of the cash flows of the individual payment: $PV = d(t_1)c_1 + d(t_2)c_2 + \dots + d(t_N)c_N$. More generally, this can be written as:
$$PV = \sum_{i=1}^{N} d(t_i)c_i$$
- For annual compounding where $r(t_i)$ is the annually compounded rate for term $t_i$, the present value is:
$$PV = \sum_{i=1}^{N} \frac{c_i}{(1 + r(t_i))^{t_i}}$$
- For continuous compounding where $\rho(t_i)$ is the continuously compounded rate for term $t_i$, the present value is:
$$PV = \sum_{i=1}^{N} e^{-\rho(t_i)t_i}c_i$$

## Simple Interest

- Simple interest does not involve compounding - the interest amount is only levied on the original principal.
- For example, a simple interest rate of 7% on a 10,000 USD principal would pay 700 USD for every year of the term.
- Therefore, for a principal amount $F$, a simple interest rate $r$, over a term $T$, the total interest can be expressed as $rTF$.
  - Similarly, the total investment value (principal and interest) is $F + rTF \equiv (1 + rT)F$.
  - It should be noted that the term does not have to be an integer and that simple interest rates are offered used on terms that are less than a year.

## Day Count Conventions

- The term of an investment is calculated by dividing the number of days by annual day count.
- In short-term money markets, there are 2 major day count conventions:
  - **actual/360** for most markets, including USD.
  - **actual/365** for mainly GBP markets.

## LIBOR

**Retired in 2021 for non-USD currencies and 2023 for USD.**

- The London Interbank Offered Rate (LIBOR) was a benchmark interest rate at which major global banks lent to each other over the short-term.
- LIBOR wass produced for the following currencies:
  - USD
  - EUR
  - GBP
  - JPY
  - CHF
- The Intercontinental Exchange (ICE) asked the 16 member banks for each currency what they would charge other banks for short-term unsecured loans and then calculated LIBOR based on [Waterfall Methodology](https://www.theice.com/publicdocs/USD_LIBOR_Methodology.pdf).
  - Both the highest four rates, and the lowest four rates were removed before an average was taken of the middle 8 rates to obtain the published LIBOR.
  - This method is known as taking a trimmed mean.
- LIBOR terms range from overnight to 1 year and will take into account market conditions as well as an inherit credit risk, due to the chance the bank will not pay back the loan.
- LIBOR provides an indication of the health of the banking sector.
- Following the 2008 Financial Crisis, the _LIBOR Scandal_ came to light and the transition to new and improved interest rate benchmarks began. These new benchmarks are known as Alternative Reference Rates (ARRs).
  - In 2018, the US interbank lending market had to dropped to only 5 billion USD, down from pre 2008 Financial Crisis levels of 100 billion USD. This is a very small market to base a global benchmark on.

## Federal Funds Rate

- The US central bank is known as The Federal Reserve or "The Fed".
- The Fed implements monetary policy by influencing short-term interest rates. This is done as follows:
  - Every US bank must keep a set percentage of their deposits in reserve in an account with the Fed.
  - In order to keep the reserve amount in their Fed account above the minimum level, a bank may have to borrow money (unsecured) from another bank's Fed account.
  - This market is known as the Federal Funds Market and the overnight rate at which the lending bank loans to the borrowing bank is known as the Federal Funds Rate.
  - The target Fed Funds Rate is set by the Federal Open Markets Committee (FOMC).
  - The Fed does not directly set the Fed Funds Rate, but engineers the effective fed funds rate, which is realized on the markets, by buying and selling US Government debt securities from banks.

## SONIA

- The Sterling Overnight Index Average (SONIA) will replace LIBOR as the risk free rate for short-term borrowing in the GBP sector.
- Based on actual transactions unlike LIBOR, with daily transactions in the market totalling 40 billion GBP (April 2021).
- SONIA has no term structure (overnight only) so provides minimal credit risk exposure even though it is based on unsecured transactions.
- Published since 1997 with the Bank of England taking responsibility for the rate in 2016.
- Measured by collecting data on rates that banks are able to borrow funds from other financial institutions.
  - Eligible transaction must be over 25 million GBP, unsecured, and have 1 day term to maturity.
  - The trimmed mean is then calculated from the eligible transactions (mean after the highest and lowest 25% is removed).

### SONIA Compounded in Arrears

- Given SONIA is an overnight interest rate, it must be extended to a term rate to be used with products that have a term to maturity. This term rate is known as SONIA Compounded in Arrears.
- See official documentation [here](https://www.bankofengland.co.uk/markets/sonia-benchmark/sonia-key-features-and-policies).
- The SONIA Compounded Index measures the return on an investment made at overnight SONIA each business day with daily compounding.
- The SONIA Compounded Index is defined as $I(t)$ on a business date $t$  where $S(t)$ is the SONIA rate for date $t$ and $\tau(t)$ is the number of calendar days between business dates $t$ and $t + 1$:
$$I(t + 1) = I(t) \times \left(1 + \frac{S(t)\tau(t)}{365}\right)$$
- An iterative approach is taken by taking the value calculated for $I(t + 1)$ and substituting it back into the formula in place of $I(t)$. This leads to:
$$I(t + m) = I(t) \times \left(1 + \frac{S(t)\tau(t)}{365}\right) \times \dots \times \left(1 + \frac{S(t + m - 1)\tau(t + m - 1)}{365}\right)$$
- The Compounded SONIA rate $S(T,U)$ where $d$ is the **calendar days** between **business dates** $T$ and $U$ is defined as:
$$S(T,U) = \left(\frac{I(U)}{I(T)} - 1 \right) \times \frac{365}{d}$$
- SONIA compounded in arrears over a term (between business dates $T$ and $U$) is the effective term rate (simply compounded) that is equivalent to rolling over an overnight loan at the SONIA rate over the term.

## SOFR

- The Secured Overnight Financing Rate (SOFR) has been selected as the alternative reference rate to replace LIBOR for the USD sector.
- SOFR is published  by the Federal Reserve and is an overnight rate based on transaction in money markets (financing rates paid in the overnight US Treasury repo market), similar to SONIA.
  - **Repo** is shorthand for **repurchase agreements**  and hence the US Treasury repo market refers to the repo agreements that have US Treasury securities as collateral.
  - Repurchase Agreements are short term deals between two parties where cash is exchanged for an asset with an agreement to reverse the exchange at a set future date. Upon the termination of the contract, the cash borrower (asset seller) buys the asset back for the original price in addition to interest at the **repo rate**.
  - A repurchase agreement allows one counterparty to receive a loan by putting up an asset as collateral.
  - **Overnight repos** have a termination date on the following day whereas **term repos** have longer durations. The overnight repo market is much larger than the term repo market (the US Treasury repo market has a daily transaction volume ~ 1 trillion USD).
- The US Treasury repo market has various segments including bilateral deals and tri-party repos with a third intermediary party (usually, the Bank Of New York Mellon).
  - The wide variety of segments allow for a clearer picture of the market when calculating SOFR.
- SOFR is calculated using the volume weighted median of the rates across all the segments of the overnight US Treasury repo market.
- The Federal Reserve Bank Of New York is responsible for collecting the dat and repo rates. SOFR is then published on the day after collection (i.e. the day on which the overnight transactions mature/reach termination).

### Compound SOFR

- SOFR must be converted to a term rate for products that have a maturity any longer than one day, similar to SONIA.
- SOFR can be compounded in arrears and in advance - the construction of these is the same in both directions.
  - The 'in advance' calculation is done before the loan term using the SOFR rates that have prevailed prior to the start date.
  - The 'in arrears' calculation is performed at maturity using the SOFR rates in effect over the duration of the actual loan term.
- SOFR compounded in arrears/advance is calculated in the same way as SONIA compounded in arrears where $S(t)$ is overnight SOFR for date $t$ and $\tau(t)$ is the number of **calendar days** between **business dates** $t$ and $t + 1$:
$$I(t + m) = I(t) \times \Pi_{j=0}^{m-1}\left(1 + \frac{S(t + j)\tau(t + j)}{360}\right)$$
- Compounded SOFR over $d$ calendar dates between $T$ to $U$ is therefore:
$$S(T,U) = \left(\frac{I(U)}{I(T)} - 1 \right) \times \frac{360}{d}$$
- The only difference between the calculation for SONIA and SOFR is the annual day count convention (365 vs 360 respectively).

#### Issues with Compounding in Arrears

- The interest charge will not be determined until the end of the loan period, when the payment is due. This can cause difficulty for some borrowers.
- Regulators have proposed some solutions:
  - A 'look back' structure where the rates used for calculating the compound rates are lagged by a set number of days.
  - Delaying the settlement date (when the payment is due) after the fixing date of the rate.

### Credit Sensitive Alternatives to SOFR

- SOFR has minimal sensitivity to the credit markets which has delayed the uptake of SOFR by banks in the business loan market.
- **AMERIBOR** is a USD rate that is similar to SONIA but based on unsecured transactions.
- Other alternatives include:
  - ICE Bank Yield Index
  - BSBY (Bloomberg)
  - IHS Markit Credit Spread Adjustment
