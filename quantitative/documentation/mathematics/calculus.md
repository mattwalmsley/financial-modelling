# Calculus

- [Calculus](#calculus)
  - [Differentiation](#differentiation)
    - [Constant Rule](#constant-rule)
    - [Power Rule](#power-rule)
    - [Product Rule](#product-rule)
    - [Quotient Rule](#quotient-rule)
    - [Chain Rule](#chain-rule)
    - [Exponential Differentiation](#exponential-differentiation)
    - [Natural Logarithm Differentiation](#natural-logarithm-differentiation)
  - [Integration](#integration)
    - [Integration by Parts](#integration-by-parts)
    - [Integration by Substitution](#integration-by-substitution)

## Differentiation

### Constant Rule

The constant rule states that the derivative of a constant function is zero. Mathematically, this is expressed as:
$$\frac{d}{dx} (c) = 0$$

where \( c \) is a constant.

### Power Rule

The power rule is a fundamental rule for differentiating functions of the form \( f(x) = x^n \), where \( n \) is any real number. The rule states that:
$$\frac{d}{dx} (x^n) = n x^{n-1}$$

### Product Rule

The product rule is used to differentiate functions that are the product of two or more functions. If you have two functions \( u(x) \) and \( v(x) \), the product rule states that:

$$\frac{d}{dx} (u(x) \cdot v(x)) = u'(x) \cdot v(x) + u(x) \cdot v'(x)$$

This is often remembered by the mnemonic "*first times the derivative of the second plus the second times the derivative of the first.*"

### Quotient Rule

The quotient rule is used to differentiate functions that are the quotient of two functions. If you have two functions \( u(x) \) and \( v(x) \), the quotient rule states that:

$$\frac{d}{dx} \left( \frac{u(x)}{v(x)} \right) = \frac{u'(x) \cdot v(x) - u(x) \cdot v'(x)}{(v(x))^2}$$

### Chain Rule

The chain rule is a formula for computing the derivative of the composition of two or more functions. If you have a function \( y = f(g(x)) \), the chain rule states that:

$$\frac{dy}{dx} = \frac{dy}{dg} \cdot \frac{dg}{dx}$$

### Exponential Differentiation

The rule for differentiating exponential functions is as follows:

$$\frac{d}{dx} ( e^{x} ) = e^{x}$$

For a more general exponential function $e^{u(x)}$, where $u(x)$ is a differentiable function of $x$, the differentiation is given by:

$$\frac{d}{dx} \left( e^{u(x)} \right) = e^{u(x)} \cdot \frac{du}{dx}$$

So, if we have a function like $e^{3x^2}$, we first find $\frac{du}{dx}$ where $u = 3x^2$:

$$\frac{du}{dx} = 6x$$

Then, applying the exponential differentiation rule, we get:

$$\frac{d}{dx} \left( e^{3x^2} \right) = e^{3x^2} \cdot 6x = 6x e^{3x^2}$$

### Natural Logarithm Differentiation

The simple rule for differentiating the natural logarithm function is as follows:

$$\frac{d}{dx} ( \ln(x) ) = \frac{1}{x}$$

Using this rule, we can derive the differentiation of more complex logarithmic functions. For example:

$$\frac{d}{dx} ( \ln(x^2) ) = \frac{d}{dx} (2 \ln(x)) =  2 \cdot \frac{d}{dx} (\ln(x)) = \frac{2}{x}$$

For a more complex function such as $\ln(x^3 + 2x^2 -4)$, we apply the chain rule which states that:

$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

where $u = x^3 + 2x^2 -4$. First, we find $\frac{du}{dx}$:

$$\frac{du}{dx} = 3x^2 + 4x$$

Now, applying the chain rule where $y = \ln(u)$, we have:

$$\frac{dy}{du} = \frac{1}{u} = \frac{1}{x^3 + 2x^2 -4}$$

Combining these results using the chain rule gives us:

$$\frac{d}{dx} \left( \ln(x^3 + 2x^2 -4) \right) = \frac{3x^2 + 4x}{x^3 + 2x^2 -4}$$

Thus, the derivative of the function $f(x) = \ln(x^3 + 2x^2 -4)$ is:

$$f'(x) = \frac{3x^2 + 4x}{x^3 + 2x^2 -4}$$

## Integration

Integration is the reverse process of differentiation. It involves finding the integral of a function, which can be thought of as the area under the curve of that function. The most common types of integrals are indefinite and definite integrals.

### Integration by Parts

Integration by parts is a technique used to integrate the product of two functions. It is based on the product rule for differentiation and is expressed by the formula:
$$\int u \, dv = uv - \int v \, du$$

The choice of $u$ and $dv$ is crucial for simplifying the integral. Generally, $u$ is chosen to be a function that becomes simpler when differentiated, and $dv$ is chosen to be a function that can be easily integrated.

For example, to integrate $\int_0^\infty{(1+x)e^{-2x} \, dx}$, we can set:

```math
\begin{aligned}
u &= 1 + x \quad & dv &= e^{-2x} \, dx \\\\
\frac{du}{dx} &= 1 \quad & v &= -\frac{1}{2} e^{-2x} \\\\
\end{aligned}
```

Then, applying the integration by parts formula:

```math
\begin{aligned}
\int_0^\infty{(1+x)e^{-2x} \, dx} &= \left[ (1+x) \cdot \left(-\frac{1}{2} e^{-2x}\right) \right]_0^\infty - \int_0^\infty \left(-\frac{1}{2} e^{-2x}\right) \, dx \\\\
&= \left[ -\frac{1+x}{2} e^{-2x} \right]_0^\infty + \frac{1}{2} \int_0^\infty e^{-2x} \, dx \\\\
&= [0] + \frac{1}{2} \left[ \left(-\frac{1}{2} e^{-2x}\right) \right]_0^\infty \\\\
&= \frac{1}{2} \left(0 - \left(-\frac{1}{2}\right)\right) \\\\
&= \frac{1}{4}
\end{aligned}
```

### Integration by Substitution

Integration by substitution is a technique used to simplify integrals by making a substitution that transforms the integral into a more manageable form. If $u = g(x)$, then $du = g'(x) \, dx$ and:

$$\int f(g(x)) g'(x) \, dx = \int f(u) \, du$$

This is based on the chain rule for differentiation where:

$$\frac{d}{dx} f(g(x)) = f'(g(x)) \cdot g'(x) \Leftrightarrow \int f(g(x)) \cdot g'(x) \, dx = f(g(x)) + C$$

For example, to integrate $\int{2x e^{x^2} \, dx}$, we can set:

```math
\begin{aligned}
u &= x^2 \quad & du &= 2x \, dx \\\\
\end{aligned}
```

Then, rewriting the integral in terms of $u$:

```math
\begin{aligned}
\int{2x e^{x^2} \, dx} &= \int{e^{u} \, du} \\\\
&= e^{u} + C \\\\
&= e^{x^2} + C
\end{aligned}
```