# Bonds

- Bonds can be regarded as a *debt instrument*, whereby the "owner" of the bond is also the "owner" of a debt.
  - Debt can therefore be traded on the bond and money markets.
- Bonds are created when a **bond issuer** first offers bonds for sale on a market. These bonds are then purchased by **bond holders** (also known as **bond buyers** ).
- The price of the bond represents the amount loaned to the bond issuer by the bond holder - i.e. the debt.
- The price of a bond (i.e. the principal of the loan) is called the **par value** or **face value**.

  ![Bond Process](images/bond-process.png "Bond Process")

- Bonds can be bought and sold after issue on the markets and will have a **market value** - this is rarely the same as the par value.

## Bond Pricing Model

- There will be specified points of time in the future where interest will be paid. These can be denoted as $t_1$, $t_2$, ... , $t_N$.
- The interest payments, commonly called **coupons**, made at these points in time can be denoted $c_1$, $c_2$, ... , $c_N$.
  - *N.B. The **coupon rate** is the annualised interest rate that a bond pays, allowing for bonds with different periodic interest payments to be compared.*
- The payment $c_N$ at time $t_N$ is the par value.
- The bond holder receives this stream of payments and the bond can be valued through [discounted cash flow analysis](2_interest-rates.md#discounted-cash-flow-analysis).
- The value of the bond, $P$, is the present value of the coupons and par value:

$$P = \sum_{i=1}^{N}d(t_i)c_i$$

- The bond value, $P$, is the **dirty price** as it has not taken into account the accrued interest from the earliest coupon, $c_1$. Bonds on the secondary market do not trade at the dirty price.

## Yield to Maturity

- A bond's yield is a measure of its return on investment and can be measured in different ways.
- A simple measure of yield is the coupon rate paid by the security.
- The **current yield** is the annual coupon value divided by the price of the bond.
- The most commonly used yield is the **yield to maturity**, defined as a specific interest rate, $y$, at which the market price of a bond would be recovered if all payments were discounted by it.
- With coupons $c_1$ to $c_J$ paid at times $T_1$ to $T_J$ (assuming that $C_J$ is the par value paid at time $T_J$), we can define the market value of a bond for an annually compounded yield to maturity, $P$, as follows:

$$P = \sum_{j=1}^{J}\frac{c_j}{(1 + y)^{T_j}}$$

- For a periodically compounded yield to maturity, $y$, with $m$ periods per year, the bond price is as follows:

$$P = \sum_{j=1}^{J}\frac{c_j}{(1 + \frac{y}{m})^{mT_j}}$$

