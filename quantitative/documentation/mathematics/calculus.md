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
  - [Stochastic Calculus](#stochastic-calculus)

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

## Stochastic Calculus

Stochastic Calculus

4.1     The standard definition of an integral
                                                     Rb
Let us recall the standard definition of the integral a f (x)dx, where f : [a, b] → R is a real valued
function on [a, b]. To define the integral we need the following construction.

   1. Choose any n − 1 (interior) points from [a, b] such that

                                     a = x0 < x1 < . . . , xn−1 < xn = b.
                                  Pn−1
   2. Consider the integral sum      i=0 f (ξi )∆xi , where ∆xi = xi+1 − xi and ξi ∈ [xi , xi+1 ] (and is
      arbitrary otherwise).

   3. Set δ = max0≤i≤n−1 ∆xi .

   4. Finally, the integral of the function f (x) over [a, b] is, by definition, the limit of the integral
      sum (if this limit exists):
                                      Z b                 n−1
                                                  def
                                                          X
                                          f (x)dx = lim        f (ξi )∆xi
                                        a                   δ→0
                                                                  i=0
                                                                                          Pn−1
Theorem 4.1.1. If f (x) is a continuous function on [a, b], then the limit limδ→0            i=1 f (ξi )∆xi
exists (and does not depend on the choice of xi , ξi , 0 ≤ i ≤ n).


4.2     Stochastic integrals (the Ito integrals)
Before we define the stochastic integral (also called the Ito integral) we have to recall several
properties of normal random variables and of the Wiener process which will paly a very important
role in the study of these integrals.

   1. If Z1 , Z2 , . . . , Zn are independent normal random variables, Zi ∼ N (µi , σi2 ), then
                                         n
                                         X                Xn      n
                                                                  X
                                                  Zi ∼ N (   µi ,   σi2 ).                           (4.1)
                                            i=1             i=1     i=1


   2. As usual, we denote by W (t) ≡ Wt the standard Wiener process. By the definition of the
      Wiener process the following properties hold:
      1. W (0) = 0

                                                       43
       2. W (t + s) − W (t) ∼ N (0, s) if s > 0.
       3. Let t0 = 0 < t1 < t2 < ... · · · < tn−1 < tn = t be any points from the interval [0, t]. Set

                         ∆Wi = W (ti+1 ) − W (ti ), i = 0, 1 . . . , n − 1 and ∆ti = ti+1 − ti .     (4.2)

       Then ∆Wi , i = 0, 1, ..., n − 1 are independent normal random variables, ∆Wi ∼ N (0, ∆ti ).

Our goal is to define
     Rt
  1. 0 f (s)dWs , where f (s) is a “usual” function (not random). This is a relatively simple case
     of a stochastic integral.
     Rt
  2. 0 f (Ws )dWs - the stochastic integral of a function of a Wiener process which is a somewhat
     more complicated case.

                            Rt
Stochastic integral          0 f (s)dWs

Definition 4.2.1. Let t0 = 0 < t1 < t2 < · · · < tn = t be a sequence of points in [0, t] and define
δ = maxi ∆ti . Then
                               Z t                  n−1
                                                    X
                                   f (s)dWs = lim       f (ti )∆Wi                             (4.3)
                                           0                   δ→0
                                                                     i=0

if this limit exists.

Theorem 4.2.2. If f (x) is differentiable and f ′ (x) is a continuous function then the limit in (4.3)
exists.

    Let us consider several simple examples.

Example 4.2.3. f (x) = c (constant), then
                            Z t                          n−1
                                                         X                               n−1
                                                                                         X
                                  cdWs =       lim             c∆Wi = c       lim              ∆Wi
                             0             maxi ∆ti →0                     maxi ∆ti →0
                                                         i=0                             i=0

where as above ∆Wi = W (ti+1 ) − W (ti ). Since
           n−1
           X
                  ∆Wi = (W (t1 ) − W (t0 )) + (W (t2 ) − W (t1 )) + · · · + (W (tn ) − W (tn−1 ))
            i=0
                          = W (tn ) − W (t0 ) = W (t)
                                   Pn−1              Pn−1
we see that limmaxi ∆ti →0           i=0 ∆Wi =           i=0 ∆Wi = W (t) and therefore
                                                  Z t
                                                         cdWs = cW (t).
                                                     0

Remark 4.2.4. Always remember the identity
                  n−1
                  X
                         (bi+1 − bi ) = (b1 − b0 ) + (b2 − b1 ) + · · · + (bn − bn−1 ) = bn − b0 .
                   i=0

We use it in the above example with bi = W (ti ).

                                                               44
Example 4.2.5.                                    (
                                                   1,              0 ≤ x < 1.5,
                                          f (x) =
                                                   −1,             1.5 ≤ x ≤ 2.
Then
               Z 2                   Z 1.5          Z 2
                      f (s)dWs =         f (s)dWs +      f (s)dWs
                  0                 0                1.5
                                   Z 1.5        Z 2
                                 =       dWs −      dWs = W (1.5) − (W (2) − W (1.5))
                                      0                 1.5
                                 = 2W (1.5) − W (2)
         Rb
We use   a dWs = W (b) − W (a).

    Question What is the distribution of this integral? Denote Y ≡ W (1.5) − (W (2) − W (1.5))?
    Answer Since W (1.5) ∼ N (0, 1.5), W (2) − W (1.5) ∼ N (0, 0.5) and these random variable-
sare independent, their difference Y ∼ N (0, 2). (This is a particular case of (4.1). Explain this
statement.)

Exercise 4.2.6.                                  
                                                 1,
                                                                  0 ≤ x < 1,
                                          f (x) = 2,               1 ≤ x < 1.5,
                                                 
                                                  −1.5,            1.5 ≤ x ≤ 3.
                                                 
                                R3
What is the distribution of      0 f (s)dWs ?

                                                                         Rt
4.2.1     The distribution of the random variable                         0
                                                                              f (s)dWs
              Rt
The integral 0 f (s)dWs is a random variable because it is defined as a limit of a sum of random
variables.
Question What is the distribution of this random variable?
    It is remarkable that this question has a simple answer. Namely, our next theorem states that
this random variable has a normal distribution and, moreover, it is relatively easy to compute the
parameters of this distribution. We shall see later that this fact plays a very important role in
constructing solutions to some it turns out questions arising in financial mathematics.
                  Rt                 R            
                                         t
Theorem 4.2.7. 0 f (s)dWs ∼ N 0, 0 (f (s))2 ds .

Proof. By the definition of a limit,
                                          Z t                  n−1
                                                               X
                                                 f (s)dWs ≃          f (ti )∆Wi
                                             0                 i=0

 Since ∆Wi are independent random variablesand ∆Wi = W (ti+1 )−W (ti ) ∼ N (0, ∆ti ) the random
variablesf (ti )∆Wi ) also are independent and f (ti )∆Wi ∼ N (0, f (ti )2 ∆ti ).
    (Note that the last statement makes use of the fact that f (ti ) are not random variables!)
    Next, due to property (4.1) we conclude that
                      n−1
                      X                      n−1
                                             X                                    n−1
                                                                                  X
                            f (ti )∆Wi ∼           N (0, f (ti )2 ∆ti ) = N (0,         f (ti )2 ∆ti ).
                      i=0                    i=0                                  i=0

                                                              45
But, by Theorem 4.1.1,
                                                         n−1
                                                         X                         Z t
                                                                    2
                                                  lim          f (ti ) ∆ti =                f (s)2 ds
                                         maxi ∆ti →0                                   0
                                                         i=0

which finishes the proof.

Exercise 4.2.8. Find the distributions of the random variables defined in the examples of the previous
section.
                                                  Rt                          Rt
4.2.2     Stochastic integrals                     0
                                                     f (Ws )dWs and            0
                                                                                   f (s, Ws )dWs
As before, let 0 = t0 < t1 < · · · < tn−1 < tn = t and δ = max0≤i≤n−1 (ti+1 − ti ).

Definition 4.2.9. Let f : R → R be a function. If the limit limδ→0 n−1
                                                                         P
                                                                           i=0 f (W (ti ))∆Wi exists,
then we say that
                              Z b                   n−1
                                                    X
                                   f (Wt )dWt = lim     f (W (ti ))∆Wi .                       (4.4)
                                             a                   δ→0
                                                                        i=0
                       Rb
Similarly, we define    a f (t, Wt )dWt by

                                 Z b                                   n−1
                                                                       X
                                             f (t, Wt )dWt = lim              f (ti , W (ti ))∆Wi ,                                     (4.5)
                                     a                          δ→0
                                                                        i=0

if the limit in (4.5) exists.

Theorem 4.2.10. Suppose that the function f : R → R is bounded and continuous. Then the limit
in (4.4) exists.

Remark 4.2.11. The existence of integrals (4.4) and (4.5) can be proved under much milder
conditions. However, in this course, we don’t discuss them.

   The just defined integral is of course again a random variable. But unlike in Theorem 4.2.7, it
may be very difficult to find the distribution of this random variable.
   We finish this section by stating two properties of these stochastic integrals.

Theorem 4.2.12.
                             Z b                                        Z b                          
                        E            f (Wt )dWt              = 0 and E                 f (t, Wt )dWt        =0                          (4.6)
                                 a                                                 a


         Z b                       Z b                                      Z b                                Z b
                                                         2
   Var          f (Wt )dWt       =               E[f (Wt ) ]dt and Var                     f (t, Wt )dWt       =         E[f (t, Wt )2 ]dt.
           a                             a                                         a                                a
                                                                                                                                        (4.7)

    Explanation
    First, let us introduce notations which will make our calculation less cumbersome. We set
Wi ≡ W (ti ) , fi ≡ f (Wi ) , ∆Wi ≡ W (ti+1 ) − W (ti ).
    Since Wi and ∆Wi are independent, also the random variables fi = f (W (ti )) and ∆Wi are
independent. Hence

                       E(fi ∆Wi ) = E(fi ) × E(∆Wi ) = 0 because E(∆Wi ) = 0.                                                           (4.8)

                                                                  46
It is now obvious that
                                      n−1                       n−1
                                                        !
                                      X                         X
                               E               fi ∆Wi       =         E (fi ∆Wi ) = 0
                                         i=0                    i=0
                              R                                           P                        
                                   b                                             n−1
and (4.6) follows because E        a f (Wt )dWt         = limδ→0 E               i=0 f (W (ti ))∆Wi       .
   To explain (4.7), note that if i < j then

           Cov(fi ∆Wi , fj ∆Wj ) = E[fi ∆Wi × fj ∆Wj ] = E[fi ∆Wi fj ] × E(∆Wj ) = 0

where the expectation factorizes because ∆Wj is independent of the other three random variables.
We thus have that
                                 n−1
                                               ! n−1
                                  X                 X
                           Var       f (Wi )∆Wi =      Var(fi ∆Wi )                        (4.9)
                                      i=0                             i=0
                                   n−1
                                   X                            n−1
                                                                X
                              =          E(fi2 ∆Wi2 ) =               E(fi2 ) × E(∆Wi2 )                      (4.10)
                                   i=0                          i=0
                                   n−1
                                   X
                              =          E(fi2 ) × ∆ti                                                        (4.11)
                                   i=0
                                      Rb           2
The last sum converges,
                        as δ → 0, P a E[(f (Wt ) ]dt and
                                   to                     this implies (4.7) because
      Rb                               n−1
Var a f (Wt )dWt = limδ→0 Var          i=0 f (W (ti ))∆Wi .

Remark 4.2.13. 1. In the above computation, we use E[∆Wi2 ] = ti+1 − ti = ∆ti .
   2. We use the following fact which you are supposed to know from second year probability
courses: if X1 , ..., Xn are such that Cov(Xi , Xj ) = 0 when i ̸= j then
                                           n            n
                                                 !
                                          X            X
                                     Var      Xi =        Var(Xi ).
                                                 i=1              i=1


4.3     The ‘usual’ differential of a function
Suppose F (x) is a function F : R → R and F ′ (x) is continuous.
Definition 4.3.1. dF (x) = F ′ (x)dx ( here dx is “small” ).
    Explanation dF (x) is the linear part of the increment ∆F (x) = F (x + ∆x) − F (x). By the
Taylor formula,
                                                           1
                           F (x + dx) = F (x) + F ′ (x)dx + F ′′ (θ)dx2 ,               (4.12)
                                                           2
where θ is (unknown) point in (x, x + dx) if dx > 0 and θ ∈ (x + dx, x) if dx < 0.
    The important fact is that the difference between ∆F (x) = F (x + dx) − F (x) and dF (x) =
 ′
f (x)dx is much smaller than dx (when dx is a small number). More precisely,
                                    ∆F (x) − dF (x)
                                                    → 0 as dx → 0.
                                          dx
Indeed, it follows from (4.12) that ∆F (x) − dF (x) = F (x + dx) − F (x) − F ′ (x)dx = 21 F ′′ (θ)dx2
and hence
                          ∆F (x) − dF (x)    1
                                           = F ′′ (θ)dx → 0 as dx → 0.
                                 dx          2

                                                            47
                           √                                         1
Example 4.3.2. F (x) =         x. Then F (1) = 1, F ′ (x) = 12 x− 2 , F ′ (1) = 12 .

                                ∆F (1) = F (1 + dx) − F (1) ≃ F ′ (1)dx.

Since F (x + dx) − F (x) ≃ dF (x), we have

                          F (1 + 0.05) = F (1) + dF (1),         (with dx = 0.05).

That is
                            √                                     0.05
                                1 + 0.05 ≃ 1 + dF (1) = 1 +            = 1.025.
                                                                    2
      Remark ∆x = dx. Indeed, in this case F (x) = x, F ′ (x) = 1 and ∆F (x) = ∆x = x + dx − x =
dx.


4.4       The stochastic case
Question What is dF (Wt )? Here F : R → R and Wt is the standard Wiener process.

4.4.1     Ito’s formula for F (Wt )
Note that if g(x) is a differentiable function, then

                                       dF (g(x)) = F ′ (g(x))g ′ (x)dx                       (4.13)

However
                                                                 dW (t)
                                     dF (W (t)) ̸= F ′ (W (t))          dt,
                                                                  dt
since the derivative dWdt(t) does not exists.
    Next, (4.13) can be rewritten as

                        dF (g(x)) = F ′ (g(x))dg(x),        since dg(x) = g ′ (x)dx.         (4.14)

Can we state that
                                      dF (W (t)) = F ′ (W (t))dW (t)?
The answer is NO! The correct answer is given by Ito’s lemma.

Lemma 4.4.1. (Ito’s lemma) Let F (x) be a function F : R → R which has two derivatives
F ′ (x), F ′′ (x) and F ′′ (x) is continuous. Then

                                                           1
                                  dF (Wt ) = F ′ (Wt )dWt + F ′′ (Wt )dt.                    (4.15)
                                                           2
Remark 4.4.2. By definition, dWt ≡ ∆Wt ≡ W (t + dt) − W (t).

      Explanation The main explanation of the Ito formula is due to the following theorem.

Theorem 4.4.3. Suppose that F (x) has two continuous and bounded derivatives: F ′ (x), F ′′ (x).
Then                                    Z b
                                                         1 b ′′
                                                          Z
                                             ′
                F (W (b)) − F (W (a)) =     F (Ws )dWs +     F (Ws )ds.                (4.16)
                                         a               2 a

                                                      48
   (Note: we shall not prove this theorem but you are supposed know this statement.)
   Let us now compare (4.16) with the following relation which you have discussed in the Calculus
courses. Namely, you know of course that
                                                   Z b
                                   F (b) − F (a) =     F ′ (x)dx.
                                                                a
Moreover, if a function g(x), g : R 7→ R, has a continuous derivative g ′ (x) then
                          Z b                     Z b
                                ′       ′
   F (g(b)) − F (g(a)) =      F (g(x))g (x)dx =       F ′ (g(x))dg(x) (since dg(x) = g ′ (x)dx).
                             a                              a
However, (4.16) tells us that
                                                                    Z b
                                 F (W (b)) − F (W (a)) ̸=                 F ′ (Wt )dWt .
                                                                     a
(And this happens because W ′ (t) does not exist!)

4.4.2    One useful corollary of the Ito formula
Corollary 4.4.4. Equation (4.16) can be rearranged as follows:
                  Z b
                                                             1 b ′′
                                                               Z
                      F ′ (Ws )dWs = F (W (b)) − F (W (a)) −     F (Ws )ds.                  (4.17)
                    a                                        2 a
                 Rb
Example 4.4.5. a dWs = Wb − Wa . Here F (x) = x, F (Wt ) = Wt , F ′ (Wt ) = 1. So
                             Z b                Z b
                                 F ′ (Ws )dWs =     dWs = Wb − Wa .
                                     a                  a
This is a particular case of (4.17).
Example 4.4.6. F (x) = x2 . We have F ′ (x) = 2x, F ′′ (x) = 2 and so (4.17) now reads
                Z b
                                             1 b
                                               Z
                                 2       2
                    2Ws dWs = Wb − Wa −            2ds = Wb2 − Wa2 − (b − a).
                 a                           2 a
In particular,                            Z t
                                                     1     1
                                             Ws dWs = Wt2 − t.
                                           0         2     2

                                         IMPORTANT CONCLUSION

We know that, by definition,
                           Z t                                       n−1
                                                                     X
                                     f (Ws )dWs =      lim                  f (Wi )∆Wi .
                                 0                  maxi ∆ti →0
                                                                     i=0
To compute this stochastic integral in terms of the ordinary integral one can do the following:
   1. Find F (x) such that F ′ (x) = f (x).
           Rt                                 Rt
   2. Then 0 f (Ws )dWs = F (Wt ) − F (0) − 12 0 f ′ (Ws )ds.
This is what we did in the examples considered above.
Exercise
       R t4.4.7. Compute the following stochastic integrals:
             3
   (a) 0 Ws dWs
       Rt
   (b) 0 eWs dWs .


                                                       49
4.4.3    One more explanation of Ito’s formula
The material of this subsection is not examinable. It is here for those who want to know more. By
Taylor’s formula,
                                                    1             1
                    F (x + dx) − F (x) = F ′ (x)dx + F ′′ (x)dx2 + F (3) (θ)dx3                   (4.18)
                                                    2             3!
As usual, θ is not known but this does not matter since we suppose that F (3) (x) = F ′′′ (x) is bounded:
| F (3) (x) |< Constant. We can use (4.18) (taking into account that W (t + dt) = W (t) + dW (t))
to obtain
                                                    1                1
          F (Wt + dWt ) − F (Wt ) = F ′ (Wt )dWt + F ′′ (Wt )dWt2 + F (3) (θ)(dWt )3 .             (4.19)
                                                    2                3!
Note that E(dWt2 ) = E((Wt+dt − Wt )2 ) = dt (by the definition of the Wiener process). Note also
that E(| dWt |3 ) = c(dt)3/2 , where c is a constant.
    So Ito’s lemma (see Lemma 4.4.1) does the following: it tells us that we can replace dWt2 in
(4.19) by dt and we can drop (dWt )3 since the expectation of | dWt |3 is much smaller than dt.
                                                             q
Exercise 4.4.8. Compute E(| dWt |3 ). Thus show that c = 2 π2
                      R∞
Hint: E(| dWt |3 ) = −∞ | x |3 fdWt (x)dx. It is convenient to write h for dt (that is h = dt) and
W (t + h) − W (t) for dWt . So
                                                            1      x2
                                   fW (t+h)−W (t) (x) = √       e− 2h .
                                                            2πh
Setting y = √xh (change of variable), we obtain
                  Z ∞                             Z ∞
                           1      −x
                                     2        1                   2
                       3
                      x √       e  2h  dx = √         h3/2 y 3 e−y /2 dy
                   0       2πh                2π 0
                                                      Z ∞                  r
                                                   1              2          2 3/2
                                          = h3/2 √         y 3 e−y /2 dy =     h
                                                   2π 0                      π
                     R∞ 3                   q                     q
Thus E(| dWt | ) = 2 0 x fdWt (x)dx = 2 π dt . So c = 2 π2 .
               3                               2 3/2



4.4.4    Ito’s formula for F (t, Wt )
Let F (t, x) be a function of t and x, F : R2 → R.
Lemma 4.4.9. (Ito’s formula for F (t, Wt ))
                               ∂F (t, Wt ) 1 ∂ 2 F (t, Wt )
                                                           
                                                                   ∂F (t, Wt )
               dF (t, Wt ) =               +           2      dt +             dWt                (4.20)
                                   ∂t        2 ∂Wt                   ∂Wt
Remarks 4.4.10.    1. Here and throughout the rest of the course, we assume that all the deriva-
    tives we need exist, are continuous functions, and have all the properties we may want them
    to have.
   2. Even though the notations we use in (4.20) should be easy to understand, here is an additional
      explanation of their meaning:
                     ∂F (t, Wt )   ∂F (t, x)            ∂ 2 F (t, Wt )   ∂ 2 F (t, x)
                                 =           |x=Wt ,                   =              |x=Wt .
                       ∂Wt           ∂x                     ∂Wt2             ∂x2
                                                                          2
Example 4.4.11. F (t, x) = t2 + x2 . We have ∂F       ∂F       ∂ F
                                             ∂t = 2t, ∂x = 2x, ∂x2 = 2. So

                                 dF (t, Wt ) = (2t + 1)dt + 2Wt dWt .

                                                   50
4.4.5     The chain rule
Suppose that Yt is a stochastic process and that

                                      dYt = a(t, Yt )dt + σ(t, Yt )dWt ,                       (4.21)

where a and σ are ”good” functions. Then

                                              1 ∂2F
                                                                     
                                          ∂F            ∂F                         ∂F
                      dF (t, Yt ) =          + σ2  2 +a                   dt + σ       dWt .   (4.22)
                                          ∂t  2 ∂Yt     ∂Yt                        ∂Yt

Here
                                             ∂F    ∂F (t, Yt )
                                                 ≡              ,
                                              ∂t        ∂t
                                             ∂F    ∂F (t, Yt )
                                                 ≡              ,
                                             ∂Yt       ∂Yt
                                            ∂2F    ∂ 2 F (t, Yt )
                                                 ≡                .
                                            ∂Yt2       ∂Yt2

   Note that Ito’s formula for F (t, Wt ) is a particular case of the Chain rule:

                                                     1 ∂2F
                                                             
                                                ∂F                        ∂F
                           dF (t, Wt ) =           +              dt +        dWt .
                                                ∂t   2 ∂Wt2               ∂Wt

4.4.6     How to remember (4.22) and similar formulae?
   1. Know Taylor’s formula up to order 2:

                                  ∂F      ∂F      1 ∂2F 2    ∂2F         1 ∂2F 2
                    dF (t, x) =      dt +    dx +       dx +      dxdt +       dt .            (4.23)
                                  ∂t      ∂x      2 ∂x2      ∂x∂t        2 ∂t2
                  ∂F (t,x) ∂F ∂F (t,x)
        Here ∂F
             ∂t ≡   ∂t , ∂x ≡   ∂x , . . .

   2. Use the following formal rules when you replace x by Wt or Yt :

        (a) dWt2 = dt;
        (b) dtdWt = 0, dt2 = 0.

Example 4.4.12. Replace x in (4.23) by Wt . Then

                               ∂F        ∂F         1 ∂2F
                  dF (t, Wt ) =   dt +      dWt +            dt + 0 + 0
                               ∂t       ∂Wt         2 ∂Wt2
                                 ∂F (t, Wt ) 1 ∂ 2 F (t, Wt )
                                                             
                                                                     ∂F (t, Wt )
                             =              +            2      dt +             dWt
                                     ∂t       2 ∂Wt                     ∂Wt

which is Ito’s lemma for F (t, Wt ).

Example 4.4.13. Replace x in (4.23) by Yt . Note that, according to the second rule

                           (dYt )2 = a2 dt2 + 2aσdtdWt + σ 2 dWt2 = σ 2 dt.

                                                     51
Here we use equation (4.21). So

                                      ∂F      ∂F        1 ∂2F
                         dF (t, Yt ) =   dt +     dYt +       dY 2 + 0 + 0
                                      ∂t      ∂Yt       2 ∂Yt2 t
                                      ∂F      ∂F                  1 ∂2F 2
                                    =    dt +     (adt + σdWt ) +        σ dt         (4.24)
                                      ∂t      ∂Yt                 2 ∂Yt2

Hence the chain rule:
                                                        1 ∂2F 2
                                                                
                                            ∂F   ∂F                       ∂F
                        dF (t, Yt ) =          +     a+        σ   dt + σ     dWt .
                                            ∂t   ∂Yt    2 ∂Yt2            ∂Yt

Exercise 4.4.14. Compute dF (t, g(Wt )).

     Remark The (4.24) above contains two zeros. This is because

                            dtdYt = dt · (adt + σdWt ) = 0 and dt2 = 0

So
                             ∂ 2 F (t, Yt )               ∂ 2 F (t, Yt ) 2
                                            dtdYt = 0 and               dt = 0
                                ∂t∂Yt                          ∂t2




                                                       52
4.5     Stochastic differential equations
Definition 4.5.1. A stochastic differential equation (SDE) is the equation of the form

                                   dYt = a(t, Yt )dt + σ(t, Yt )dWt ,                            (4.25)

where a(t, Yt ), σ(t, Yt ) are given (random) functions and Yt = Y (t) is an unknown random process.
   Remark We have seen (4.25) before: equation (4.21).
Definition 4.5.2. We say that Y (t) is a solution to (4.25) with initial value Y (0), if for t ≥ 0
                                        Z t               Z t
                       Y (t) = Y (0) +      a(s, Ys )ds +     σ(s, Ys )dWs .                     (4.26)
                                            0                    0

     Terminological remarks
     Y (t) solving (4.25) is said to be a diffusion process.
     a(t, Yt ) is called the drift and σ(t, Yt ) is the volatility of the diffusion process.
     Note that (4.26) is obtained from (4.25) by integrating both parts of (4.25). If σ ≡ 0, then (4.25)
becomes dYt = a(t, Yt )dt and is equivalent to Yt′ = a(t, Yt )− the ordinary differential equation (but
still, Y (t) is a random process if a is a random process).

4.5.1    Simple examples of SDEs
Example 4.5.3. The following relation is the simplest example of a SDE

                                       dYt = dWt , Y (0) = 0.
                 Rt
Then Yt = Y (0) + 0 dWs = Wt − W0 = Wt . Thus Yt in this case is the Wiener process.
Example 4.5.4.
                                   dYt = µdt + σdWt , Y (0) = 1,
where µ and σ are constants. Then
                                                   Z t           Z t
                                 Y (t) = Y (0) +         µds +         σdWs
                                                    0             0

and we obtain
                                        Y (t) = 1 + µt + σWt ,
which is the Brownian motion starting from 1.
Exercise 4.5.5. dYt = e−t dt + 2tdWt . State the distribution of Yt if Y (0) = −1.
Exercise 4.5.6. dYt = e−t dt + 2tdWt . Find d(Yt2 ).


4.6     Important examples of stochastic differential equations
4.6.1    The stochastic differential equation for the price of a share
Let S(t) be a random process describing the price of a share. How does the difference between S(t)
and S(t + dt) behave?
    A simple model for dS(t) = S(t + dt) − S(t) is

                                  dS(t) = S(t) · adt + S(t) · ξ(dt),                             (4.27)

                                                   53
where a is a parameter (usually a > 0) and ξ(dt) is a random ”noise”. The term S(t) · adt
pushes the price up, while ξ(dt) may be ≥ 0 or < 0. We choose ξ(dt) = σdWt , where Wt is the
standard Wiener process and σ is a constant (whiich may be negative). Then we obtain the following
stochastic differential equation (SDE) :

                                      dS(t) = aS(t)dt + σS(t)dWt                                       (4.28)

Assuming that S(0) = S0 is given, how do we solve this SDE?

The first solution to (4.28)
Theorem 4.6.1. The solution to (4.28) is given by

                                                           σ2
                                          St = S0 e(a− 2 )t+σWt .

Proof. Rewrite (4.28) as follows:

                                 dSt
                                     = adt + σdWt          with S(0) = S0                              (4.29)
                                 St

Note that the left hand side of (7.3) resembles the differential d ln S(t) (but in fact it is not equal
to this differential as will be seen below). So, let us compute d ln S(t) using the chain rule version
of Ito’s lemma.
    Recall that the differential of a function F (St ) (which is is good enough, say has two continuous
derivatives) can be computed as follows:

                                                          1
                                 dF (St ) = F ′ (St )dSt + F ′′ (St )(dSt )2 .
                                                          2

In our case F (x) = ln x and so F ′ (x) = (ln x)′ = x1 , F ′′ (x) = (ln x)′′ = − x12 and (dSt )2 = σ 2 St2 dt.
Hence
                         1                        1 1          2 2            σ2
             d ln(St ) = (aSt dt + σSt dWt ) −           ×  σ   S t dt = (a −    )dt + σdWt .
                         St                       2 St2                        2
Remark. We now see that indeed d ln(St ) ̸= adt + σdWt .
  Integrating both parts of the last display formula, we obtain
               Z t             Z t                                Z t              Z t
                                     σ2                                  σ2
                  d ln(Su ) =   ((a − )du + σdWu ) =                 (a − )du +          σdWu
                0             0      2                             0     2           0

and hence
                                                                σ2
                                   ln(St ) − ln(S0 ) = (a −        )t + σWt
                                                                2
or, equivalently,
                           St       σ2                                   σ2
                              = e(a− 2 )t+σWt       and St = S0 e(a− 2 )t+σWt .
                           S0


    A random variable distributed as eX , where X ∼ N (µ, σ 2 ) is said to have LogNormal(µ, σ‘2 )
distribution. Thus, St ∼ LogNormal((a − σ 2 /2t), σ 2 t). The process St is said to be Geometric
Brownian Motion with drift parameter a and volatility parameter σ. We often denote the drift
parameter by µ instead of a.

                                                      54
The second solution to (4.28)
This approach to solving (4.28) is slightly more difficult than the first one. It can be viewed as a
useful exercise illustrating one more way in which the Ito formula can be used.
    Plan: the main steps of the second solution.
   1. Suppose that S(t) can be found in the form S(t) = f (t, Wt ), where f (t, x) is a function of
      two variables, t and x.

   2. Use Ito’s lemma and substitute S(t) in (4.28) by f (t, Wt ) and dS(t) by df (t, Wt ).

   3. Then see whether you can find f (t, x).
                                                             2
Theorem 4.6.2. f (t, x) = S0 eµt+σx , where µ = a − σ2 and S0 = S(0).
Proof. Step 1. By Ito’s lemma,

                                 ∂f (t, Wt ) 1 ∂ 2 f (t, Wt )
                                                             
                                                                     ∂f (t, Wt )
                 df (t, Wt ) =              +            2      dt +             dWt           (4.30)
                                     ∂t       2 ∂Wt                    ∂Wt

Substituting the left side of (4.28) by (4.30) we get

                                  1 ∂2f
                                        
                           ∂f                    ∂f
                               +           dt +      dWt = af dt + σf dWt ,                    (4.31)
                            ∂t    2 ∂Wt2        ∂Wt

where we write f for f (t, Wt ). Equating the coefficients in front of dWt in both sides of (4.31), we
get
                                       ∂f (t, Wt )
                                                   = σf (t, Wt )                                (4.32)
                                          ∂Wt
Rewrite (4.32) as
                                           fx′ (t, x) = σf (t, x)                              (4.33)
We use here the notation fx′ = ∂f
                                ∂x . Fix t, then (4.33) is the simplest linear equation (known to you
from the course Differential Equations). It has the general solution of the form

                                            f (t, x) = c(t)eσx .                               (4.34)

Remark: you can check this by substituting this expression into (4.33). Do it!
    Note that c(t) in (4.34) is an unknown function of t. It remains to find it.
    Step 2. To find c(t), we shall use another relation which follows from (4.31). Namely, we equate
the coefficients in front of dt on both sides of (4.31) and get
                                                1 ′′
                                    ft′ (t, x) + fxx (t, x) = af (t, x).                       (4.35)
                                                2
Next, it follows from (4.34) that
                                           ft′ (t, x) = c′ (t)eσx                              (4.36)
                                           ′′
                                          fxx (t, x) = σ 2 c(t)eσx                             (4.37)
Substituting (4.36) and (4.37) into (4.35) we get
                                               1
                                    c′ (t)eσx + σ 2 c(t)eσx = ac(t)eσx
                                               2
and so
                                                          σ2
                                          c′ (t) = (a −      )c(t)                             (4.38)
                                                          2

                                                    55
                                                                               σ2
which is the same type of equation as before. Hence c(t) = c0 e(a− 2 )t , where c0 = c(0). Finally,
                                                                              σ2
                             f (t, x) = c0 eµt+σx ,        where µ = a −         .
                                                                              2


We have thus proved that S(t) can be found in the form S(t) = f (t, Wt ), namely:
                                   S(t) = f (t, Wt ) = c0 eµt+σWt .
Since S(0) = c0 , we get c0 = S0 and finally
                                         S(t) = S0 eµt+σWt .
Remarks 4.6.3.      1. We use the following fact: if
                                                y ′ (x) = αy(x)                               (4.39)
        then
                                  y(x) = ceαx ,        where c is a constant.                 (4.40)

  2. If c in (4.40) depends on, say, t (as in (4.34)) then this means that we are, for some reason,
     considering a ”family of solutions” with t being the parameter of the family.
  3. (4.39) and (4.40) were used to solve (4.33) and (4.38). They will be used also in the next
     example.

4.6.2     The Ornstein-Uhlenbeck process (OUP)
Definition 4.6.4. We say that r(t) is the OUP if
                                     dr = −a(r − µ)dt + σdWt                                  (4.41)
where a, µ, σ are the parameters of the model.
    In our applications, the parameters a, µ, and σ will be positive: a > 0, µ > 0, σ > 0. However,
the solution that we discuss below is valid for arbitrary values of these parameters.
    Before solving (4.41), let us consider the case when σ = 0. We then have dr = −a(r − µ)dt,
and since dr = r′ dt we obtain the following ordinary differential equation:
                                           r′ = −a(r − µ).                                    (4.42)
Then (r − µ)′ = −a(r − µ), (as (r − µ)′ = r′ − µ′ = r′ ) and hence
                              r − µ = ce−at ,     or       r(t) = µ + ce−at .
It is useful to note that if a > 0 then e−at → 0 as t → ∞ and hence r(t) → µ. Note also that
r(t) = µ is a solution to (4.42). (See the sketch of the graph of r(t) in the hand-written version of
these Notes.)
     If a > 0 then the solution r(t) = µ is the so called stable solution.
Theorem 4.6.5. Suppose that r(t) is a random process which satisfies the equation
                                    dr = −a(r − µ)dt + σdWt .
Then                                                                   Z t
                                                      −at        −at
                          r(t) = µ + (r(0) − µ)e            + σe             eas dWs .
                                                                        0

                                                      56
Proof. We shall be looking for a function u(t) such that

                                           r(t) − µ = u(t)e−at                             (4.43)

Then u(t) = eat (r(t) − µ). By Ito’s lemma, we compute

                        du(t) = aeat (r − µ)dt + eat dr
                              = aeat (r − µ)dt + eat (−a(r − µ)dt + σdWt )
                              = σeat dWt
        Rt         R t as
Hence   0 du(s) = σ 0 e dWs , or equivalently,
                                                        Z t
                                    u(t) − u(0) = σ           eas dWs                      (4.44)
                                                         0

It follows from (4.43) that r(0) − µ = u(0). So (4.44) can be rewritten as
                                       Z t                        Z t
                       u(t) = u(0) + σ     eas dWs = r(0) − µ + σ     eas dWs
                                           0                            0

and we obtain (again due to (4.43)) that
                                                      Z t         
                                    −at                     as
                       r(t) = µ + e       r(0) − µ + σ     e dWs
                                                        0
                                                                Z t
                                    −at           −at       −at
                            = r(0)e     + µ(1 − e ) + σe            eas dWs
                                                                 0
                                                           Z t
                            = (r(0) − µ)e−at + µ + σe−at       eas dWs
                                                                  0




Some comments
  1. The most important step in the proof of this theorem is the “guess” (4.43). There is a good
     reason for this guess but we shall not discuss it here. However, you are required to know and
     be able to reproduce the above proof.

  2. To compute du(t), we use the chain rule. In fact we derive it. Namely, if dr = −a(r − µ)dt +
     σdWt and u = f (t, r), then
                                                             1 ′′
                                       du = ft′ dt + fr′ dr + frr (dr)2 .
                                                             2
      In our case u(t) = f (t, r) = eat (r − µ) and therefore
                                          ∂ at
                                   ft′ =    (e (r − µ)) = aeat (r − µ),
                                         ∂t
                                          ∂ at
                                   fr′ =     (e (r − µ)) = eat ,
                                         ∂r
                                     ′′
                                   frr  = 0.

      This explains the second step.
                                                                            2
      Remark. We use the notation ft′ = ∂f    ′   ∂f        ′′   ∂ f
                                        ∂t , fr = ∂r , and frr = ∂r2 .



                                                   57
58