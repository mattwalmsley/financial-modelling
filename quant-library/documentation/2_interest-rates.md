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
- Between time $t$ and time $t + \tau$, the gross return is $\frac{V(t + \tau)}{V(t)}$

### Net Return

- Measures the profit an investment has earned as a fraction of the initial investment.
- Between time $t$ and time $t + \tau$, the net return is $\frac{V(t + \tau) - V(t)}{V(t)}$

### Annual Compounding

- Interest earned is calculated on the current amount at the end of each year, rather than the principal at inception. This leads to an increase in the interest earned every year.
- Example
  - $X$ is invested for two years at interest rate $r(2)$ which is annually compounded.
  - After one year, the total investment value is $(1 + r(2))X$ and this then becomes the principal on which interest is charged for the second year.
  - Therefore, after two years, the investment value is $(1 + r(2))(1 + r(2))X$.
  - This can be written as $(1 + r(2))^2X$

### Future Value

- The value of an investment after a term with a fixed interest rate, assuming all returns are reinvested at the same interest rate.
- Let $r(t)$ be the annual interest rate which is compounded for a loan term of $t$ years.
- Let $P_0$ be the initial investment.
- The future value of $P_0$, at time $t$ is:
$$P(t)=(1 + r(t))^tP_0$$

### Periodic Compounding

- Interest is compounded with frequency $m$ if the interest is reinvested with the principal $m$ times per year.
- We denote $r_m(t)$ to be the interest rate compounded $m$ times per year with term $t$.
- In each compounding period ($m$ times per year), the earned interest is $\frac{r_m(t)X}{m}$
- The value of the investment after one period is $X + \frac{r_m(t)X}{m} \equiv \left(1 + \frac{r_m(t)}{m}\right)X$
- The interest earned in the second period is calculated by applying the interest rate to the combined principal and interest earned so far is $\frac{r_m(t)}{m}\left(1 + \frac{r_m(t)}{m}\right)X$.
- The value of the investment after two periods is $\left(1 + \frac{r_m(t)}{m}\right)X + \frac{r_m(t)}{m}\left(1 + \frac{r_m(t)}{m}\right)X \equiv \left(1 + \frac{r_m(t)}{m}\right)^2X$
- The future value of an investment $X$ in $t$ years:
$$P(t)=\left(1 + \frac{r_m(t)}{m}\right)^{mt}X$$

### Interest Rate Conversions

- For an investment $X$ with future value $P(t)$ in $t$ years, we can define the gross return as:
$$\frac{P(t)}{X} \equiv \frac{\left(1 + \frac{r_m(t)}{m}\right)^{mt}X}{X} \equiv \left(1 + \frac{r_m(t)}{m}\right)^{mt}$$
- Interest rates are considered to be _equivalent_ if they lead to the same total return, i.e the same gross or net return.
- For two interest rates $r_m(t)$ and $r_k(t)$, we can equate the gross returns of \$1 to express $r_m(t)$ in terms of $r_k(t)$:
$$\left(1 + \frac{r_m(t)}{m}\right)^{mt} = \left(1 + \frac{r_k(t)}{k}\right)^{kt} \Rightarrow r_m(t) = m\left(1 + \frac{r_k(t)}{k}\right)^{\frac{k}{m}} - m$$

### Continuous Compounding

- Instantaneous compounding of all interest income - as soon as interest is paid, new interest is paid on it.
- Mathematically, this is the limit of periodic compounding as the period goes to 0 or the frequency goes to infinity.
- This provides a useful approximation as the accuracy can be optimised by choosing the continuously compounded rate that corresponds to a prevailing periodically compounded rate.
  - We can change from periodic compounding to continuous compounding by increasing the compounding frequency, $m$, to infinity:
$$\lim_{m \to \infin}\left(1 + \frac{r}{m}\right)^{mt} = e^{rt} \Rightarrow P(t) = e^{rt}X$$
  - With $r_c$ as the continuously compounded risk-free rate and $r_a$ as the annually compounded risk-free rate, we can equate the future values of \$1 in a similar approach to periodically compounded in interest rates:
$$e^{r_ct} = (1 + r_a)^t \Rightarrow r_ct = log((1 + r_a)^t) \Rightarrow r_c = log(1 + r_a)$$

## Time Value of Money

- Concept that the value of \$1 today is more than the value of \$1 in a year's time.
  - This because of the opportunity cost associated with not receiving the \$1 today.
- Interest rates are closely linked to the time value of money as the annual interest received on \$1 can be viewed as a component of the opportunity cost.

### Present Value

- The present value $PV$ of an investment $X$, valued at time $t$, is the amount that should be invested today, accounting for prevailing interest rates, so that at time $t$, the investment of value $PV$ is worth $X$.
- Assuming a prevailing risk-free, annually compounded interest rate $r$:
$$(1 + r)^tPV = X \Rightarrow PV = \frac{X}{(1 + r)^t}$$
- For a periodically compounded interest rate $r_m$, with compounding frequency $m$:
$$\left(1 + \frac{r_m}{m}\right)^{mt}PV = X \Rightarrow PV = \frac{X}{\left(1 + \frac{r_m}{m}\right)^{mt}}$$
- For a continuously compounded interest rate $r_c$:
$$e^{r_ct}PV = X \Rightarrow PV = e^{-r_ct}X$$
