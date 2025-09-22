# Probability Theory

## Introduction

Modelling prices of financial assets requires the application of probability theory due to the random nature of price movements.

## Finite Probability Spaces

- A **sample space** is the of all outcomes within a random system where there are a finite set of outcomes. The sample space is denoted as $\Omega$.
- A typical outcome is denoted as $\omega$ and $\omega \in \Omega$ is used to indicate that $\omega$ is an **element** of the sample space $\Omega$.
- An **event** is a set of possible outcomes and (equivalently) an event of the sample space $\Omega$.

| Probability Theory | Set Theory |
|:------------------:|:----------:|
| Sample Space $\Omega$ | Universal Set $U$ |
| Outcome $\omega$ | Element $x$ |
| Event $A$ | Subset $A$ |

### Example: Tossing a Coin

- Tossing a coin three times can be modelled as a finite probability space.
- The sample space is given by:
  $$\Omega = \{ \omega_{hhh}, \omega_{hht}, \omega_{hth}, \omega_{htt}, \omega_{thh}, \omega_{tht}, \omega_{tth}, \omega_{ttt} \}$$
  where $h$ represents heads and $t$ represents tails.
- An example event $A$ is the set of outcomes where the first toss is heads:
  $$A = \{ \omega_{hhh}, \omega_{hht}, \omega_{hth}, \omega_{htt} \}$$