# Bonds

- [Bonds](#bonds)
  - [Introduction](#introduction)
  - [Bond Pricing Model](#bond-pricing-model)
  - [Yield to Maturity](#yield-to-maturity)
  - [Yield Curves](#yield-curves)
    - [Discount and Spot Rate Curves](#discount-and-spot-rate-curves)
    - [Building a Yield Curve](#building-a-yield-curve)
  - [Bootstrapping Spot Curves](#bootstrapping-spot-curves)
    - [Example](#example)

## Introduction

- Bonds can be regarded as a *debt instrument*, whereby the "owner" of the bond is also the "owner" of a debt. Debt can therefore be traded on the bond and money markets.
- Bonds are created when a **bond issuer** first offers bonds for sale on a market. These bonds are then purchased by **bond holders** (also known as **bond buyers** ).
- The price of the bond represents the amount loaned to the bond issuer by the bond holder - i.e. the debt.
- The price of a bond (i.e. the principal of the loan) is called the **par value** or **face value**.

  ![Bond Process](../images/bond-process.png "Bond Process")

- Bonds can be bought and sold after issue on the markets and will have a **market value** - this is rarely the same as the par value.

## Bond Pricing Model

- There will be specified points of time in the future where interest will be paid. These can be denoted as $t_1$, $t_2$, \dots , $t_N$.
- The interest payments, commonly called **coupons**, made at these points in time can be denoted $c_1$, $c_2$, \dots , $c_N$.
  - *N.B. The **coupon rate** is the annualised interest rate that a bond pays, allowing for bonds with different periodic interest payments to be compared.*
- The payment $c_N$ at time $t_N$ is the par value.
- The bond holder receives this stream of payments and the bond can be valued through [discounted cash flow analysis](2_interest-rates.md#discounted-cash-flow-analysis).
- The value of the bond $P$, is the present value of the coupons and par value:

$$P = \sum_{i=1}^{N}d(t_i)c_i$$

- The bond value $P$ is the **dirty price** as it has not taken into account the accrued interest from the earliest coupon $c_1$. Bonds on the secondary market do not trade at the dirty price.

## Yield to Maturity

- A bond's yield is a measure of its return on investment and can be measured in different ways.
- A simple measure of yield is the coupon rate paid by the security.
- The **current yield** is the annual coupon value divided by the price of the bond.
- The most commonly used yield is the **yield to maturity**, defined as a specific interest rate $y$, at which the market price of a bond would be recovered if all payments were discounted by it.
- With coupons $c_1$ to $c_J$ paid at times $T_1$ to $T_J$ (assuming that $C_J$ is the par value paid at time $T_J$), the market value of a bond for an annually compounded yield to maturity $P$ can be defined as follows:

$$P = \sum_{j=1}^{J}\frac{c_j}{(1 + y)^{T_j}}$$

- For a periodically compounded yield to maturity $y$, with $m$ periods per year, the bond price is as follows:

$$P = \sum_{j=1}^{J}\frac{c_j}{(1 + \frac{y}{m})^{mT_j}}$$

## Yield Curves

- A yield curve quantifies the relationship between the return of a fixed income security and its term.
- On any single yield curve, the different instruments displayed should be *equivalent* (have the same credit quality), differing only by maturity. For example, yields on US Treasury Bonds should not be displayed on the same yield curve as yields for highly distressed corporate bonds.

  ![Typical Yield Curve](../images/yield-curve.png "Typical Yield Curve")

- **N.B.** The commonly referenced US Treasury yield curve is constructed using yields to maturity and is ***not*** a spot rate curve.

### Discount and Spot Rate Curves

- Discount curves are one of the primary application of yield curves.
- A discount curve is the relation between time $T$ and the discount factor $d(T)$, which corresponds to discounting back from any value of $T$.
- A continuously compounded **spot rate curve** is a special kind of yield curve where the discount factor for a continuously compounded interest rate is used for the yield curve $y(T)$:
$$d(T) = e^{-y(T)T}$$
- For a term $T$, the present value of 1 USD paid at time $T$ can be represented as $d(T)$.
  - Similarly, a spot rate $y(T)$ can be defined as the interest rate a credit issuer would charge for a loan over a term $T$ (even if there is no such instrument currently trading on the markets).
  - The corresponding spot rate curve $y(T)$ can also be expressed in terms of the discount curve $d(T)$:
$$y(T) = -\frac{\log(d(T))}{T}$$

### Building a Yield Curve

- For $N$ fixed income securities with maturities at times $T_{1}, T_{2}, \dots, T_{N}$, the yields are calculated from the respective market prices as: $y(T_{1}), y(T_{2}), \dots, y(T_{N})$.
- The times $T_{1}$ to $T_{N}$ are known as the **tenors** and are usually the maturities or expiration dates of the traded calibration instruments.
- Interpolation is used to extend the yield curve from a finite set of tenors to the entire interval $T_{1}$ to $T_{N}$.

## Bootstrapping Spot Curves

- Building a yield curve from real market data.
- For a collection of $N$ bonds with maturities at times $T_{1} < T_{2} < \dots < T_{N}$, and observable market prices $P_{1}, P_{2}, \dots, P_{N}$:
  - The discount curve $d(T)$ for $T \le T_{1}$ is calculated first to discount the coupons of bond 1 and find $P_{1}$.
  - The discount curve $d(T)$ for $T_{1} \le T \le T_{2}$ is calculated next using the values for $T \le T_{1}$ to discount the coupons of bond 2 and find $P_{2}$.
  - This process is repeated through all $N$ bonds to calculate $d(T)$ for $T \le T_{N}$.

### Example

- In this example, there are 3 bonds:

|        |      Coupon      | Face Value | Time to Maturity | Market Price |
| ------ |:----------------:|:----------:|:----------------:|:------------:|
| Bond 1 |       Zero       | 1,000 USD  |      6 Months    |    985 USD   |
| Bond 2 | 5% (Semi-Annual) | 10,000 USD |      1 Year      |  10,124 USD  |
| Bond 3 |    7% (Annual)   | 10,000 USD |      2 Years     |  10,507 USD  |

- The tenors for the yield curve will be the maturities of the bonds: $T_{1} = 0.5$, $T_{2} = 1$ and $T_{3} = 2$.
- The market prices of the bonds are used to calibrate the discount factors $d(T_{1})$, $d(T_{2})$ and $d(T_{3})$, or equivalently, the yields $y(T_{1})$, $y(T_{2})$ and $y(T_{3})$.

$$
P_{1} = d(0.5)(1000)  d(0.5) = \frac{985}{1000} \\
\Longrightarrow \boxed{d(0.5) = 0.985} \\
\text{Using } y(T) = -\frac{\log(d(T))}{T} \\
\Longrightarrow y(0.5) = -\frac{\log(0.985)}{0.5} \\
\boxed{y(0.5) = 3.0\%}
$$

- Bond 2 has a semi-annual coupon of 5% so there is a payment in 6 months ($T = 0.5$) and a payment in 1 year ($T = 1$).
- Using the discount factor $d(0.5)$ to discount the coupon payment in 6 months, and then using the bond price to calibrate the discount factor $d(1)$:

$$
P_{2} = d(0.5)\left(\frac{10000 \times 5\%}{2}\right) + d(1)\left(\frac{10000 \times 5\%}{2} + 10000\right) \\
d(1) = \frac{10124 - (0.985 \times 250)}{10250} \\
\boxed{d(1) = 0.9637} \\
y(1) = -\frac{\log(0.9637)}{1} \\
\boxed{y(1) = 3.7\%}
$$

- Similar to bond 2, the discounting equation for the market price of bond 3 is:

$$
P_{3} = d(1)(10000 \times 7\%) + d(2)((10000 \times 7\%) + 10000) \\
d(2) = \frac{10507- (0.9637 \times 700)}{10700} \\
\boxed{d(2) = 0.9189} \\
y(2) = -\frac{\log(0.9189)}{2} \\
\boxed{y(2) = 4.2\%}
$$

- The discount factor for $d(1.5)$ can now be linearly interpolated using the yield curve values $y(1)$ and $y(2)$:

$$
Using \space d(T) = e^{-y(T)T} \\
d(1.5) = e^{-y(1.5) \times 1.5} \\
y(1.5) = \frac{y(1) + y(2)}{2} \\
\boxed{y(1.5) = 3.95\%} \\
d(1.5) = e^{-(0.0395 \times 1.5)} \\
\boxed{d(1.5) = 0.942}
$$

- The price of a 2 year bond with a 100,000 USD face value and a 7% coupon paid semi-annually can be calculated as follows:

$$
\begin{aligned}
P_{1.5} &= d(0.5)\left(\frac{100000 \times 7\%}{2}\right) + d(1)\left(\frac{100000 \times 7\%}{2}\right) + d(1.5)\left(\frac{100000 \times 7\%}{2}\right)+ d(2)\left(\frac{100000 \times 7\%}{2} + 100000\right) \\
&= (0.985 \times 3500) + (0.9637 \times 3500) + (0.942 \times 3500) + (0.9189 \times 103500) \\
&= \boxed{105,224 \text{ USD}}
\end{aligned}
$$
