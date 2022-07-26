# Interest Rates

- [Interest Rates](#interest-rates)
  - [Introduction](#introduction)
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

## Term Structure

- Risks are different for different loan terms, with longer terms carrying higher interest rates.
- Interest rates are a function of the **loan term** (the duration of time the loan is held).
- $r(t)$ is used to denote the interest rate for borrowing money over a loan term $t$.
- The function $r(t)$ can be used to represent the following:
  - An interest rate with the term to maturity, $t$.
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
  - To change from periodic compounding to continuous compounding, set the limit of the compounding frequency, $m$, to infinity:
$$\lim_{m \to \infin}\left(1 + \frac{r}{m}\right)^{mt} = e^{rt} \Rightarrow P(t) = e^{rt}X$$
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
- For example, to find the continuously compounded interest rate $r_c$ that is equivalent to semi-annual interest rate $r_2$, equate the future values of a $1 investment with the two interest rates:
$$e^{r_ct} = \left(1 + \frac{r_2}{2}\right)^{2t} \Rightarrow r_ct = log\left(\left(1 + \frac{r_2}{2}\right)^{2t}\right) \Rightarrow r_c = 2log\left(1 + \frac{r_2}{2}\right)$$

## Discount Factors

- The present value, $PV = \frac{X}{(1 + r)^t}$, can be viewed as a discounted value of X, assuming that $(1 + r)^t > 1$.
- Discounted value and present value can be used interchangeably.
- Rewriting present value as a function of time, we get $PV = d(t)X$ where we can express the discount factor as $d(t) = \frac{1}{(1 +r)^t}$.
- The future value at time $t$ of a 1 USD investment today is $(1 + r)^t$ which is the reciprocal of $d(t)$, i.e. $\frac{1}{d(t)} = (1 + r)^t$.
  - We can therefore say the future value of an investment $P_0 = X$ today is:
$$P(t) = \frac{1}{d(t)}X = (1 + r)^tX$$
- Discount factors can be expressed in terms of interest rates with different compounding convention.
  - For periodically compounded rates: $d(t) = \frac{1}{\left(1 + \frac{r_m}{m}\right)^{mt}}$.
  - For continuously compounded rates: $d(t) = e^{-r_ct}$.

## Discounted Cash Flow Analysis

- For an asset that pays amounts $c_1, c_2, ..., c_N$ (cash flows) at respective times $t_1, t_2, ..., t_N$, we can say that an individual payment $c_i$ will be made at time $t_i$.
- To value the asset, we need to know the present value of a stream of cash flows.
- The present value of an individual payment $c_i$ with discount factor $d(t_i)$ is $d(t_i)c_i$.
- Model the present value of a stream of cash flows as the present value of an individual cash flow - i.e. the total amount that needs to be invested today to replicate the stream of cash flows.
- Each cash flow is independent so the present value of the cash flow stream is the sum of the cash flows of the individual payment: $PV = d(t_1)c_1 + d(t_2)c_2 + ... + d(t_N)c_N$. More generally, this can be written as:
$$PV = \sum_{i=1}^{N} d(t_i)c_i$$
- For annual compounding where $r(t_i)$ is the annually compounded rate for term $t_i$, the present value is:
$$PV = \sum_{i=1}^{N} \frac{c_i}{(1 + r(t_i))^{t_i}}$$
- For continuous compounding where $\rho(t_i)$ is the continuously compounded rate for term $t_i$, the present value is:
$$PV = \sum_{i=1}^{N} e^{-\rho(t_i)t_i}c_i$$