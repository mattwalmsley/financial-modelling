# Mathematical Interview Questions

- [Mathematical Interview Questions](#mathematical-interview-questions)
  - [Calculus](#calculus)
    - [Differentiation](#differentiation)
    - [Integration](#integration)
  - [Probability](#probability)
    - [Continuous Random Variables](#continuous-random-variables)
    - [Transformations of Continuous Random Variables](#transformations-of-continuous-random-variables)

## Calculus

### Differentiation

- Differentiate $f(x) = \log(x^3 + 2x^2 -4)$ (chain rule and logarithm differentiation).

```math
\begin{aligned}
f'(x) &= \frac{d}{dx} \left( \log(x^3 + 2x^2 -4) \right) \\\\
&= \frac{1}{x^3 + 2x^2 -4} \cdot \frac{d}{dx} (x^3 + 2x^2 -4) \\\\
&= \frac{1}{x^3 + 2x^2 -4} \cdot (3x^2 + 4x) \\\\
&= \frac{3x^2 + 4x}{x^3 + 2x^2 -4}
\end{aligned}
```

- Differentiate $f(x) = (x^4 + 2x^2 -2)e^x$ (product rule and exponential differentiation).

```math
\begin{aligned}
f'(x) &= \frac{d}{dx} \left( (x^4 + 2x^2 -2)e^x \right) \\\\
&= \frac{d}{dx} (x^4 + 2x^2 -2) \cdot e^x + (x^4 + 2x^2 -2) \cdot \frac{d}{dx} (e^x) \\\\
&= (4x^3 + 4x)e^x + (x^4 + 2x^2 -2)e^x \\\\
&= \left( 4x^3 + 4x + x^4 + 2x^2 -2 \right)e^x \\\\
&= \left(x^4 + 4x^3 + 2x^2 + 4x -2\right)e^x
\end{aligned}
```

- Differentiate $f(x) = \frac{log(x)}{5+e^x}$ (quotient rule).

```math
\begin{aligned}
f'(x) &= \frac{d}{dx} \left( \frac{\log (x)}{5+e^x} \right) \\\\
&= \frac{(5+e^x) \cdot \frac{d}{dx} (\log (x)) - \log (x) \cdot \frac{d}{dx} (5+e^x)}{(5+e^x)^2} \\\\
&= \frac{(5+e^x) \cdot \frac{1}{x} - \log (x) \cdot e^x}{(5+e^x)^2} \\\\
&= \frac{\frac{5+e^x}{x} - \log (x) e^x}{(5+e^x)^2} \\\\
&= \frac{5 + e^x - x \log (x) e^x}{x(5+e^x)^2}
\end{aligned}
```

- Differentiate $f(x) = e^{-x^2}$  (chain rule and exponential differentiation).

```math
\begin{aligned}
f'(x) &= \frac{d}{dx} \left( e^{-x^2} \right) \\\\
&= e^{-x^2} \cdot \frac{d}{dx} (-x^2) \\\\
&= e^{-x^2} \cdot (-2x) \\\\
&= -2x e^{-x^2}
\end{aligned}
```

- Differentiate $f(x) = \frac{e^{-x^2}}{x}$ (quotient rule, chain rule, and exponential differentiation).

```math
\begin{aligned}
f'(x) &= \frac{d}{dx} \left( \frac{e^{-x^2}}{x} \right) \\\\
&= \frac{x \cdot \frac{d}{dx} (e^{-x^2}) - e^{-x^2} \cdot \frac{d}{dx} (x)}{x^2} \\\\
&= \frac{x \cdot (-2x e^{-x^2}) - e^{-x^2} \cdot 1}{x^2} \\\\
&= \frac{-2x^2 e^{-x^2} - e^{-x^2}}{x^2} \\\\
&= \frac{e^{-x^2}(-2x^2 - 1)}{x^2} \\\\
&= -\frac{(2x^2 + 1)e^{-x^2}}{x^2}
\end{aligned}
```

### Integration

- Integrate $\int_0^\infty{(1+x)e^{-2x} \, dx}$ (integration by parts).

```math
\begin{aligned}
u &= 1 + x \quad & dv &= e^{-2x} \, dx \\\\
\frac{du}{dx} &= 1 \quad & v &= -\frac{1}{2} e^{-2x} \\\\
\end{aligned}
```

```math
\begin{aligned}
\int_0^\infty{(1+x)e^{-2x} \, dx} &= \left[ (1+x) \cdot \left(-\frac{1}{2} e^{-2x}\right) \right]_0^\infty - \int_0^\infty \left(-\frac{1}{2} e^{-2x}\right) \, dx \\\\
&= \left[ -\frac{1+x}{2} e^{-2x} \right]_0^\infty + \frac{1}{2} \int_0^\infty e^{-2x} \, dx \\\\
&= \left[0 - \left(-\frac{1}{2}\right)\right] + \frac{1}{2} \left[ \left(-\frac{1}{2} e^{-2x}\right) \right]_0^\infty \\\\
&= \frac{1}{2} + \frac{1}{2} \left(0 - \left(-\frac{1}{2}\right)\right) \\\\
&= \frac{3}{4}
\end{aligned}
```

- Integrate $\int_{-\infty}^{\infty}{x^5 e^{-\frac{x^2}{2}} \, dx}$ (odd function with symmetric limits).
  - Integration of an odd function over symmetric limits results in zero.
  - An odd function is defined as a function $f(x)$ that satisfies the condition $f(-x) = -f(x)$ for all $x$ in its domain.
  - An even function is defined as a function $f(x)$ that satisfies the condition $f(-x) = f(x)$ for all $x$ in its domain.
  - $x^5$ is an odd function and $e^{-\frac{x^2}{2}}$ is an even function, thus their product $x^5 e^{-\frac{x^2}{2}}$ is an odd function.

```math
\begin{aligned}
\int_{-\infty}^{\infty}{x^5 e^{-\frac{x^2}{2}} \, dx} &= 0
\end{aligned}
```

- Integrate $\int_0^\infty{x e^{-\frac{x^2}{2}} \, dx}$ (integration by recognition).

```math
\begin{aligned}
\int_0^\infty{x e^{-\frac{x^2}{2}} \, dx} &= \left[ -e^{-\frac{x^2}{2}} \right]_0^\infty \\\\
&= 0 - (-1) \\\\
&= 1
\end{aligned}
```

## Probability

### Continuous Random Variables

- Suppose a continuous random variable $X$ has the probability density function (pdf):

$$f_X(x) = \begin{cases}  Ce^{-x} & 0 \leq x \leq 1 \\ 0 & \text{otherwise} \end{cases}$$

where $C$ is a constant.

Sketching the pdf:

![C exp[-x] Distributions](../../images/distribution_for_C_exp[-x].png "C exp[-x] Distributions")

The cumulative distribution function (CDF) is given by:

```math
\begin{aligned}
F_X(x) &= \int_{-\infty}^{x} f_X(x') \, dx' \\\\
&= \begin{cases}  0 & x < 0 \\\\  \int_{0}^{x} Ce^{-x'} \, dx' & 0 \leq x \leq 1 \\\\  \int_{0}^{1} Ce^{-x'} \, dx' & x > 1 \end{cases} \\\\
&= \begin{cases}  0 & x < 0 \\\\  C \left[ -e^{-x'} \right]_{0}^{x} & 0 \leq x \leq 1 \\\\  C \left[ -e^{-x'} \right]_{0}^{1} & x > 1 \end{cases} \\\\
&= \begin{cases}  0 & x < 0 \\\\  C (1 - e^{-x}) & 0 \leq x \leq 1 \\\\  C (1 - e^{-1}) & x > 1 \end{cases}
\end{aligned}
```

The value of $C$ can be found by ensuring that the total probability is 1:

```math
\begin{aligned}
\int_{0}^{1} Ce^{-x} \, dx &= 1 \\\\
C \left[ -e^{-x} \right]_{0}^{1} &= 1 \\\\
C (1 - e^{-1}) &= 1 \\\\
C &= \frac{1}{1 - e^{-1}}
\end{aligned}
```

The expected value $E[X]$ is given by:

```math
\begin{aligned}
E[X] &= \int_{0}^{1} x f_X(x) \, dx \\\\
&= \int_{0}^{1} x \cdot \frac{1}{1 - e^{-1}} e^{-x} \, dx \\\\
&= \frac{1}{1 - e^{-1}} \int_{0}^{1} x e^{-x} \, dx \\\\
\end{aligned}
```

Using integration by parts to solve $\int_{0}^{1} x e^{-x} \, dx$:

```math
\begin{aligned}
u &= x \quad & dv &= e^{-x} \, dx \\\\
\frac{du}{dx} &= 1 \quad & v &= -e^{-x} \\\\
\end{aligned}
```

```math
\begin{aligned}
\int_{0}^{1} x e^{-x} \, dx &= \left[ -x e^{-x} \right]_{0}^{1} - \int_{0}^{1} -e^{-x} \, dx \\\\
&= \left[ -x e^{-x} \right]_{0}^{1} + \left[ -e^{-x} \right]_{0}^{1} \\\\
&= \left( -1 \cdot e^{-1} - 0 \right) + \left( -e^{-1} + 1 \right) \\\\
&= -e^{-1} - e^{-1} + 1 \\\\
&= 1 - 2e^{-1}
\end{aligned}
```

Thus, the expected value is:

```math
\begin{aligned}
E[X] &= \frac{1}{1 - e^{-1}} (1 - 2e^{-1}) \\\\
&= \frac{1 - 2e^{-1}}{1 - e^{-1}} \\\\
&= 0.41802
\end{aligned}
```

The standard deviation $\sigma_X$ is given by:

```math
\begin{aligned}
\sigma_X &= \sqrt{E[X^2] - (E[X])^2} \\\\
\end{aligned}
```

Where $E[X^2]$ is calculated as:

```math
\begin{aligned}
E[X^2] &= \int_{0}^{1} x^2 f_X(x) \, dx \\\\
&= \int_{0}^{1} x^2 \cdot \frac{1}{1 - e^{-1}} e^{-x} \, dx \\\\
&= \frac{1}{1 - e^{-1}} \int_{0}^{1} x^2 e^{-x} \, dx \\\\
\end{aligned}
```

Using integration by parts twice to solve $\int_{0}^{1} x^2 e^{-x} \, dx$:

```math
\begin{aligned}
u &= x^2 \quad & dv &= e^{-x} \, dx \\\\
\frac{du}{dx} &= 2x \quad & v &= -e^{-x} \\\\
\end{aligned}
```

```math
\begin{aligned}
\int_{0}^{1} x^2 e^{-x} \, dx &= \left[ -x^2 e^{-x} \right]_{0}^{1} - \int_{0}^{1} -2x e^{-x} \, dx \\\\
&= \left[ -x^2 e^{-x} \right]_{0}^{1} + 2 \int_{0}^{1} x e^{-x} \, dx \\\\
&= \left( -1 \cdot e^{-1} - 0 \right) + 2 (1 - 2e^{-1}) \\\\
&= -e^{-1} + 2 - 4e^{-1} \\\\
&= 2 - 5e^{-1}
\end{aligned}
```

Thus, $E[X^2]$ is:

```math
\begin{aligned}
E[X^2] &= \frac{1}{1 - e^{-1}} (2 - 5e^{-1}) \\\\
&= \frac{2 - 5e^{-1}}{1 - e^{-1}}
\end{aligned}
```

Finally, substituting back to find $\sigma_X$:

```math
\begin{aligned}
\sigma_X &= \sqrt{\frac{2 - 5e^{-1}}{1 - e^{-1}} - \left(\frac{1 - 2e^{-1}}{1 - e^{-1}}\right)^2} \\\\
&= \sqrt{\frac{(2 - 5e^{-1})(1 - e^{-1}) - (1 - 2e^{-1})^2}{(1 - e^{-1})^2}} \\\\
&= \frac{\sqrt{(2 - 5e^{-1})(1 - e^{-1}) - (1 - 2e^{-1})^2}}{1 - e^{-1}} \\\\
&= 0.11254
\end{aligned}
```

### Transformations of Continuous Random Variables

Two independent continuous random variables $X_1$ and $X_2$ both have the following probability density function:

$$f_X(x) = \begin{cases}  \sqrt{\frac{2}{\pi}}e^{-\frac{x^{2}}{2}} & x \geq 0 \\ 0 & \text{otherwise} \end{cases}$$

**Question 1:** Determine the probability density function of ${X_1}^2$, using the assumption that $g(x) = x^2$ is a strictly monotonically increasing function for all $x$ where $f_X(x) > 0$.

**Solution:**

Using the transformation formula for densities, if $Y = g(X)$ where $g$ is strictly monotonically increasing, then:

$$f_Y(y) = f_X(g^{-1}(y))\,\left|\frac{d}{dy}g^{-1}(y)\right|$$

For $Y = X_1^2$:

- $g(x) = x^2$ which is strictly monotonically increasing for $x \geq 0$ (as given in the assumption)
- The inverse function is $g^{-1}(y) = \sqrt{y}$ for $y \geq 0$ (since $x \geq 0$)
- The derivative of the inverse is $\frac{d}{dy}g^{-1}(y) = \frac{1}{2\sqrt{y}}$

Therefore:

```math
\begin{aligned}
f_Y(y) &= f_X(\sqrt{y}) \cdot \left|\frac{1}{2\sqrt{y}}\right| \text{ for } y \geq 0 \\\\
&= \sqrt{\frac{2}{\pi}}e^{-\frac{(\sqrt{y})^{2}}{2}} \cdot \frac{1}{2\sqrt{y}} \\\\
&= \sqrt{\frac{2}{\pi}}e^{-\frac{y}{2}} \cdot \frac{1}{2\sqrt{y}} \\\\
&= \frac{1}{\sqrt{2\pi y}}e^{-\frac{y}{2}} \text{ for } y \geq 0
\end{aligned}
```

Thus, the probability density function of $Y = X_1^2$ is:

$$\boxed{f_Y(y) = \begin{cases}  \frac{1}{\sqrt{2\pi y}}e^{-\frac{y}{2}} & y \geq 0 \\ 0 & \text{otherwise} \end{cases}}$$

This is a **chi-squared distribution with 1 degree of freedom**, denoted $Y \sim \chi^2(1)$.

Determine the probability density function of $Z = {X_1}^2 + {X_2}^2$

Since $X_1$ and $X_2$ are independent, $Y_1 = X_1^2$ and $Y_2 = X_2^2$ are also independent (transformations of independent random variables remain independent).

For the sum of two independent continuous random variables, we use the convolution formula:

$$f_Z(z) = \int_{-\infty}^{\infty} f_{Y_1}(y_1)\, f_{Y_2}(z - y_1)\, dy_1$$

Given that both $Y_1$ and $Y_2$ have the same pdf (from Question 1):

$$f_{Y_i}(y) = \begin{cases}  \frac{1}{\sqrt{2\pi y}}e^{-\frac{y}{2}} & y \geq 0 \\ 0 & \text{otherwise} \end{cases}$$

For $Z = Y_1 + Y_2$ to be positive, we need $Y_1 \geq 0$ and $Y_2 \geq 0$, which means $Z \geq 0$.

For a given $z \geq 0$, the valid range of integration is where both:

- $y_1 \geq 0$
- $z - y_1 \geq 0$ (i.e., $y_1 \leq z$)

Therefore, the integration limits are from $0$ to $z$ (when $z \geq 0$):

```math
\begin{aligned}
f_Z(z) &= \int_{0}^{z} \frac{1}{\sqrt{2\pi y_1}}e^{-\frac{y_1}{2}} \cdot \frac{1}{\sqrt{2\pi (z-y_1)}}e^{-\frac{z-y_1}{2}} \, dy_1 \\\\
&= \frac{1}{2\pi} e^{-\frac{z}{2}} \int_{0}^{z} \frac{1}{\sqrt{y_1(z-y_1)}} \, dy_1 \\\\
\end{aligned}
```

To evaluate $\int_{0}^{z} \frac{1}{\sqrt{y_1(z-y_1)}} \, dy_1$, we use the substitution $y_1 = z\sin^2(\theta)$:

```math
\begin{aligned}
dy_1 &= 2z\sin(\theta)\cos(\theta) \, d\theta \\\\
\sqrt{y_1(z-y_1)} &= \sqrt{z\sin^2(\theta) \cdot z\cos^2(\theta)} = z\sin(\theta)\cos(\theta)
\end{aligned}
```

When $y_1 = 0$: $\sin^2(\theta) = 0$, so $\theta_1 = 0$

When $y_1 = z$: $\sin^2(\theta) = 1$, so $\theta_2 = \frac{\pi}{2}$

```math
\begin{aligned}
\int_{0}^{z} \frac{1}{\sqrt{y_1(z-y_1)}} \, dy_1 &= \int_{0}^{\pi/2} \frac{2z\sin(\theta)\cos(\theta)}{z\sin(\theta)\cos(\theta)} \, d\theta \\\\
&= \int_{0}^{\pi/2} 2 \, d\theta \\\\
&= 2 \cdot \frac{\pi}{2} \\\\
&= \pi
\end{aligned}
```

Therefore:

```math
\begin{aligned}
f_Z(z) &= \frac{1}{2\pi} e^{-\frac{z}{2}} \cdot \pi \\\\
&= \frac{1}{2} e^{-\frac{z}{2}} \text{ for } z \geq 0
\end{aligned}
```

Thus, the probability density function of $Z = X_1^2 + X_2^2$ is:

$$\boxed{f_Z(z) = \begin{cases}  \frac{1}{2} e^{-\frac{z}{2}} & z \geq 0 \\ 0 & \text{otherwise} \end{cases}}$$

This is a **chi-squared distribution with 2 degrees of freedom**, denoted $Z \sim \chi^2(2)$, which is also an **exponential distribution** with rate parameter $\lambda = \frac{1}{2}$.
