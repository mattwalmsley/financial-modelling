# Financial Interview Questions

## Bond Pricing

1. **A semi-annual coupon bond maturing in 3 years has a face value of \$1,000 and a couple rate of 14\%. Calculate the price of the bond if the yield to maturity is 4.5\% (assume semi-annual compounding).**

    $$P_0 = \sum_{j=1}^{n}{\frac{C}{(1 + i)^j}} + \frac{FV}{(1 + i)^n}$$

    Where $P_0$ is the price of the bond and $FV$ is the face value of the bond.

    The coupon payment $C$ is:
    $$\frac{14\% \times \$1,000}{2} = \$70$$

    The yield to maturity $i$ with semi-annual compounding is:
    $$\frac{4.5\%}{2} = 2.25\% = 0.0225$$

    The total number of periods $n$ is

    $$3 \text{ years} * 2 = 6 \text{ years}$$

    Now we can calculate the price of the bond:

    ```math
    \begin{aligned}
    P_0 &= \sum_{j=1}^{6}{\frac{70}{(1 + 0.0225)^j}} + \frac{1000}{(1 + 0.0225)^6} \\\\
    &= \frac{70}{(1.0225)^1} + \frac{70}{(1.0225)^2} + \frac{70}{(1.0225)^3} + \frac{70}{(1.0225)^4} + \frac{70}{(1.0225)^5} + \frac{70}{(1.0225)^6} + \frac{1000}{(1.0225)^6} \\\\
    &= 1263.84
    \end{aligned}
    ```

    Thus, the price of the bond is approximately \$1,263.84.

2. **Calculate the annualised discount and bond equivalent yield of a Treasury bill with a face value of \$1,000 purchased for \$935 that matures in 189 days.**

    The annualised discount yield is calculated as:

    $$i_\text{discount yield} = \frac{FV - P_0}{FV} \times \frac{360}{n}$$

    Where $i_\text{discount yield}$ is the annualised discount yield, $FV$ is the face value, $P_0$ is the purchase price, and $n$ is the time to maturity in days.

    ```math
    \begin{aligned}
    i_\text{discount yield} &= \frac{1000 - 935}{1000} \times \frac{360}{189} \\\\
    &= 0.1238095 \\\\
    &\approx 12.38\%
    \end{aligned}
    ```

    Similarly, the bond equivalent yield is calculated as:

    $$i_\text{bond equivalent yield} = \frac{FV - P_0}{P_0} \times \frac{365}{n}$$

    Where $i_\text{bond equivalent yield}$ is the annualised bond equivalent yield, $FV$ is the face value, $P_0$ is the purchase price, and $n$ is the time to maturity in days.

    ```math
    \begin{aligned}
    i_\text{bond equivalent yield} &= \frac{1000 - 935}{935} \times \frac{365}{189} \\\\
    &= 0.1342557 \\\\
    &\approx 13.43\%
    \end{aligned}
    ```

3. **A 10-year maturity bond with a 7\% annual coupon and a face value of \$1,000 is currently priced at \$655.15. Calculate the rate of return if the bond is sold next year for \$750.00.**

    The rate of return can be calculated using the formula:

    $$\text{Rate of Return} = \frac{C + (P_{t+1} - P_t)}{P_t}$$

    Where $C$ is the annual coupon payment, $P_{t+1}$ is the selling price in 1 year, and $P_{t}$ is the current price.

    The annual coupon payment $C$ is:

    $$7\% \times \$1,000 = \$70$$

    Now we can calculate the rate of return:

    ```math
    \begin{aligned}
    \text{Rate of Return} &= \frac{70 + (750 - 655.15)}{655.15} \\\\
    &= 0.251622 \\\\
    &\approx 25.16\%
    \end{aligned}
    ```
