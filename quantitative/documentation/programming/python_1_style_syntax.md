# Python Style and Syntax

See [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) for best practices.

- [Python Style and Syntax](#python-style-and-syntax)
  - [Objects](#objects)
  - [Data Types](#data-types)
    - [Introduction](#introduction)
    - [Integers (`int`)](#integers-int)
      - [Types of Integers](#types-of-integers)
      - [Integer Operations](#integer-operations)
      - [Large Integers](#large-integers)
      - [Integer Size \& Memory Usage](#integer-size--memory-usage)
      - [Integer Representation](#integer-representation)
      - [Integer Common Methods](#integer-common-methods)
    - [Fractions (`fractions.Fraction`)](#fractions-fractionsfraction)
      - [Creating Fractions](#creating-fractions)
      - [Operations with Fractions](#operations-with-fractions)
      - [Fractions Use Cases](#fractions-use-cases)
      - [Representing Irrational Numbers with Fractions](#representing-irrational-numbers-with-fractions)
    - [Floating-Points (`float`)](#floating-points-float)
      - [Float Bit Layout Example](#float-bit-layout-example)
      - [Floats Precision and Rounding Errors](#floats-precision-and-rounding-errors)
      - [Float Equality Testing](#float-equality-testing)
      - [Coercing Floats to Integers](#coercing-floats-to-integers)
      - [Rounding Floats (`round()`)](#rounding-floats-round)
      - [Special Floating-Point Values](#special-floating-point-values)
      - [Float Use Cases](#float-use-cases)
    - [Decimals (`decimals.Decimal`)](#decimals-decimalsdecimal)
      - [Decimal Context and Precision/Rounding Settings](#decimal-context-and-precisionrounding-settings)
      - [Working with `Decimal` Rounding Methods](#working-with-decimal-rounding-methods)
      - [Rounding Mechanisms in `decimal.Decimal`](#rounding-mechanisms-in-decimaldecimal)
      - [Decimal Arithmetic Operations](#decimal-arithmetic-operations)
      - [Comparing Decimals with Floating-Points](#comparing-decimals-with-floating-points)
      - [Performance Considerations When Using Decimal](#performance-considerations-when-using-decimal)
    - [Complex Numbers (`complex`)](#complex-numbers-complex)
      - [Creating Complex Numbers](#creating-complex-numbers)
      - [Accessing Complex Number Components](#accessing-complex-number-components)
      - [Complex Number Operations](#complex-number-operations)
      - [Conjugate and Magnitude of Complex Numbers](#conjugate-and-magnitude-of-complex-numbers)
      - [Complex Functions (`cmath`)](#complex-functions-cmath)
      - [Complex Number Performance Considerations](#complex-number-performance-considerations)
    - [Booleans (`bool`)](#booleans-bool)
      - [Creating Boolean Values](#creating-boolean-values)
      - [Boolean Operators](#boolean-operators)
      - [Boolean Algebra Properties in Python](#boolean-algebra-properties-in-python)
        - [Commutativity](#commutativity)
        - [Associativity](#associativity)
        - [Distributivity](#distributivity)
        - [De Morgan’s Theorem](#de-morgans-theorem)
      - [Chained Boolean Comparisons](#chained-boolean-comparisons)
      - [Boolean Precedence](#boolean-precedence)
      - [Short-Circuiting](#short-circuiting)
      - [Using Booleans in Control Flow](#using-booleans-in-control-flow)
    - [Tuples (`tuple`)](#tuples-tuple)
      - [Creating Tuples](#creating-tuples)
      - [Accessing Tuple Elements](#accessing-tuple-elements)
      - [Tuple Packing and Unpacking](#tuple-packing-and-unpacking)
      - [Common Uses of Tuples](#common-uses-of-tuples)
      - [Tuple Methods](#tuple-methods)
    - [Named Tuples (`collections.namedtuple`)](#named-tuples-collectionsnamedtuple)
      - [Modifying and Extending Named Tuples](#modifying-and-extending-named-tuples)
      - [Docstrings in namedtuple](#docstrings-in-namedtuple)
      - [Default Values for Named Tuples](#default-values-for-named-tuples)
    - [Strings (`str`)](#strings-str)
    - [Lists (`list`)](#lists-list)
      - [Lists of Tuples](#lists-of-tuples)
    - [Comparing Tuples, Lists, and Strings](#comparing-tuples-lists-and-strings)
    - [Dictionaries (`dict`)](#dictionaries-dict)
    - [Sets](#sets)
  - [Naming Conventions](#naming-conventions)
  - [Python Comments](#python-comments)
  - [Multi-Line Statements in Python](#multi-line-statements-in-python)
    - [Implicit Line Continuation](#implicit-line-continuation)
    - [Explicit Line Continuation](#explicit-line-continuation)
    - [Multi-line Strings in Python](#multi-line-strings-in-python)
  - [Docstrings](#docstrings)
    - [Docstring Syntax](#docstring-syntax)
    - [Types of Docstrings](#types-of-docstrings)
      - [Function Docstrings](#function-docstrings)
      - [Class Docstrings](#class-docstrings)
    - [Module Docstrings](#module-docstrings)
    - [Accessing Docstrings](#accessing-docstrings)
      - [Using the `__doc__` attribute:](#using-the-__doc__-attribute)
    - [Conventions for Writing Docstrings](#conventions-for-writing-docstrings)
    - [Docstring Style Guides](#docstring-style-guides)
  - [Conditionals](#conditionals)
    - [Ternary Conditional Operator](#ternary-conditional-operator)
  - [Functions](#functions)
    - [Functions as Objects](#functions-as-objects)
      - [`my_func` versus `my_func()`](#my_func-versus-my_func)
    - [Higher-Order Functions](#higher-order-functions)
    - [Built-in Functions](#built-in-functions)
  - [Loops](#loops)
    - [`while` Loops](#while-loops)
    - [`for` Loops](#for-loops)
      - [Loops with `else`](#loops-with-else)
    - [List Comprehension](#list-comprehension)
      - [List Comprehension Comparison to Regular `for` Loop](#list-comprehension-comparison-to-regular-for-loop)
  - [Exception Handling](#exception-handling)
  - [Scope](#scope)
    - [Local Scope](#local-scope)
    - [Global/Module Scope](#globalmodule-scope)
      - [The `global` Keyword](#the-global-keyword)
    - [Non-Local Scope (Enclosing Scope)](#non-local-scope-enclosing-scope)
    - [Scope Resolution Order (LEGB Rule)](#scope-resolution-order-legb-rule)
    - [Variables in Loops](#variables-in-loops)

## Objects

- In Python, *almost everything* is an object, including numbers, strings, functions, and even classes.
- Every object is an instance of a class, which defines its behaviour and attributes:
  - Functions are instances of `function`.
  - Built-in types (`int`, `str`, `list`, etc.) and user-defined classes are instances of `type`.
- Objects have the following properties:
  - **Identity** - A unique memory address, retrievable with `id(obj)`.
  - **Type** - The class it is an instance of, given by `type(obj)`.
  - **Value** - The data it holds, which may be *mutable* or *immutable*.
- Python treats all objects as *first-class objects*, meaning they can be:
  - Assigned to variables.
  - Passed as arguments to functions.
  - Returned from functions.
  - Stored in data structures such as lists and dictionaries.
- Variables store references to objects rather than the objects themselves.
- Since functions are objects, they can be passed as arguments and returned from other functions.

## Data Types

### Introduction

- Numerical Python types:
  - **Boolean truth values** where $0$ is `False` and $1$ is `True` are `bool` types.
  - **Integer numbers** ($\mathbb{Z}$) such as $0, \pm1, \pm2, \pm3,...$ are `int` types.
  - **Rational numbers** ($\mathbb{Q}$) where $\left\{ \frac{p}{q} \mid p, q \in \mathbb{Z}, q \neq 0 \right\}$ are `fractions.Fraction` types.
  - **Real numbers** ($\mathbb{R}$) such as $0, -1, 0.125, \frac{1}{3}, \pi$ are `float` or `decimal.Decimal` types.
  - **Integer numbers** ($\mathbb{C}$) where $\{a + bi \mid a,b \in \mathbb{R}\}$ are `complex` types.

### Integers (`int`)

- An integer in Python is a whole number without a decimal point.
- Integers can be positive, negative, or zero.
- Integers in Python are immutable, so that their value cannot be changed once they are created. Any operation on an integer creates a new object.

Integers are created by simply assigning a number to a variable.

```python
a = 42  # Positive integer
b = -10  # Negative integer
c = 0  # Zero
```

#### Types of Integers

- **Decimal**: Regular base-10 integers (`5`, `100`, `-3`).
- **Binary**: Represented by prefix `0b` or `0B` (`0b1010`).
- **Octal**: Represented by prefix `0o` or `0O` (`0o12`).
- **Hexadecimal**: Represented by prefix `0x` or `0X` (`0x1f`).

```python
binary = 0b1010  # 10 in decimal/base-10
octal = 0o12  # 10 in decimal/base-10
hexadecimal = 0x1f  # 31 in decimal/base-10
```

#### Integer Operations

- Arithmetic operations:
  - Addition: `+`
  - Subtraction: `-`
  - Multiplication: `*`
  - Division: `/`
  - Modulus: `%`
  - Exponentiation: `**`
  - Floor division: `//`

    ```python
    a = 10
    b = 2
    
    c1 = a + b  # 12 (int)
    c2 = a - b  # 8 (int)
    c3 = a * b  # 20 (int)
    c4 = a / b  # 5.0 (float)

    x = 10
    y = 3
    z1 = a // b  # 3 (int)
    z2 = a % b  # 1 (int)
    z3 = a ** b  # 1000 (int)
    ```

The equation: `a = b * (a // b) + a % b` is helpful to remember when dealing with modulus and floor divisions integer operations (holds for both positive and negative integers).

- Comparison operators:
  - Equals: `==`
  - Not equals: `!=`
  - Greater than: `>`
  - Less than: `<`
  - Great than or equal: `>=`
  - Less than or equal: `<=`

    ```python
    a = 10
    b = 20
    print(a == b)  # False
    print(a < b)  # True
    ```

- Bitwise operations:
  - AND: `&`
  - OR: `|`
  - XOR: `^`
  - NOT: `~`
  - left shift: `<<`
  - right shift: `>>`

    ```python
    a = 5  # 0b0101
    b = 3  # 0b0011
    and_op = a & b  # 0b0001 (1 in decimal)
    or_op = a | b  # 0b0111 (7 in decimal)
    xor_op = a ^ b  # 0b0110 (6 in decimal)
    ```

#### Large Integers

- Python supports arbitrarily large integers, allowing them to grow beyond typical 32-bit or 64-bit integer limits.
- No need for special data types or libraries to handle large numbers.
- Operations on large integers take more time due to increased memory usage and processing.

```python
large_num = 123456789123456789123456789
print(large_num)
```

#### Integer Size & Memory Usage

- Arbitrary Precision: Python 3 integers (`int`) have no fixed size limit; they grow dynamically as needed.
- No Overflow: Unlike languages with `int32` or `int64`, Python automatically expands integers beyond typical limits.
- Memory Overhead: Python integers use more memory than C/C++ integers due to object metadata and dynamic storage.
- Memory Growth: Larger integers require more memory; use `sys.getsizeof(x)` to check storage size.

```python
import sys
print(sys.getsizeof(0))       # 24
print(sys.getsizeof(1))       # 28
print(sys.getsizeof(10**10))  # 32
print(sys.getsizeof(10**100)) # Increases with size
```

Python's integer system is flexible but comes at the cost of memory and performance for very large numbers.

#### Integer Representation

- The built-in `int()` function can represent a value as an integer.
- If the argument is a string, it must represent a valid integer (base-10 by default). Otherwise, it raises a `ValueError`.
  - `int()` takes a second parameter for the `base`.
- When applied to a float, `int()` truncates the decimal portion (does not round).
- Booleans values, `True` and `False`, are also accepted by `int()`.

```python
int('42') # 42 (base-10 by default)
int('1010', 2) # 10 (base-2)
int('A12F', base=16) # 41263 (base-16)

int('B', 11) # ValueError

int(3.14) # 3
int(10.9) # 10
int(-10.9) # -10

int(True) # 1
int(False) # 0
```

#### Integer Common Methods

`bin(x)`: Returns the binary representation of an integer

```python
bin(10) # 0b1010
```

`oct(x)`: Returns the octal representation of an integer

```python
oct(10) # 0o12
```

`hex(x)`: Returns the hexadecimal representation of an integer

```python
hex(10) # 0xa
```

`abs(x)`: Returns the absolute value of x.

```python
abs(-10)  # 10
```

`pow(x, y)`: Returns x raised to the power y.

```python
pow(2, 3)  # 8
```

`divmod(x, y)`: Returns a tuple (quotient, remainder) for integer division.

```python
divmod(10, 3)  # (3, 1)
```

### Fractions (`fractions.Fraction`)

- The `fractions.Fraction` class in Python provides exact rational number representation by storing numbers as numerator/denominator pairs.
- Unlike floating-point numbers (`float`), which can introduce precision errors, `Fraction` maintains precise arithmetic results.

#### Creating Fractions

A Fraction object can be created from integers (`int`), strings (`str`), floats (`float`), or another `Fraction`:

```python
from fractions import Fraction

f1 = Fraction(3, 4)  # 3/4
f2 = Fraction('1.5')  # 3/2
f2 = Fraction('1/5')  # 1/5
f3 = Fraction(0.1)  # Approximates 0.1 as a fraction
```

#### Operations with Fractions

Fractions support arithmetic operations while maintaining exact values:

```python
sum_f = Fraction(1, 3) + Fraction(1, 6)  # 1/2
prod_f = Fraction(2, 5) * Fraction(3, 4)  # 6/20 -> 3/10
```

`Fraction` also supports comparison, reduction to simplest form, and conversion to floats (`float(f)`).

#### Fractions Use Cases

- Financial and scientific calculations requiring precision.
- Mathematical problems involving fractions without floating-point rounding errors.
- Converting recurring decimals into exact fractions.

#### Representing Irrational Numbers with Fractions

- Irrational numbers like $\pi$ and $\sqrt{2}$ cannot be exactly represented as Fraction because they have non-repeating, infinite decimal expansions.
- `Fraction` can however approximate irrational numbers to a desired accuracy using float or decimal values.

```python
from fractions import Fraction
import math

approx_pi = Fraction(math.pi).limit_denominator(1000)  # Best fraction approximation within denominator ≤ 1000
print(approx_pi)  # Output: 355/113 (a well-known approximation of π)
```

- The `limit_denominator(n)` method finds the best fractional approximation within a given denominator limit.
- $\frac{355}{113}$ is a well-known close approximation of $\pi$.

### Floating-Points (`float`)

- Python's `float` type is based on the *IEEE 754 double-precision (64-bit)* floating-point standard, which represents real numbers approximately using binary fractions.
- This allows for a wide range of values but introduces precision limitations due to finite storage.
- A 64-bit (8-byte) float consists of:
  - 1-bit sign (positive or negative)
  - 11-bit exponent (scales the number, e.g. -5 is the exponent in 1.5E-5)
  - 52-bit fraction (mantissa) (stores significant digits)

    | **Component**       | **Bit Length** | **Purpose** |
    |---------------------|----------------|-------------|
    | Sign Bit            | 1 bit          | Determines whether the number is positive (`0`) or negative (`1`). |
    | Exponent            | 11 bits        | Stores the exponent with a **bias of 1023** (used for scaling). |
    | Mantissa (Fraction) | 52 bits        | Stores the significant digits of the number (in binary). |

This structure enables approximately 15 - 17 significant decimal digits of precision and an exponent range of about $\pm10^{308}$.

#### Float Bit Layout Example

- Step 1: Convert `-13.625` to binary
  - Integer part: `13` → `1101` in binary  
  - Fractional part: `0.625` → `0.101` in binary  
  - Combined: `1101.101`  
- Step 2: Normalize to scientific notation
  - Convert to binary scientific notation:  $1101.101_2 = 1.101101_2 \times 2^3$
  - Mantissa: `1.101101...` (drop leading `1`, store `101101...`)
  - Exponent: `3` (biased using *bias 1023* → `3 + 1023 = 1026`)
- Step 3: Encode into *IEEE 754* format

    | **Component**             | **Binary Representation**                              | **Value** |
    |---------------------------|--------------------------------------------------------|-------------|
    | Sign Bit                  | `1`                                                    | Negative number |
    | Exponent (11-bit, biased) | `10000000010`                                          | $1026_{10} = 10000000010_{2}$|
    | Mantissa (52-bit)         | `1011010000000000000000000000000000000000000000000000` | Fractional part |

#### Floats Precision and Rounding Errors

Some decimal numbers cannot be exactly represented as binary fractions, leading to small rounding errors.

```python
print(0.1 + 0.2)  # Output: 0.30000000000000004
```

- `0.1` and `0.2` do not have exact binary representations, causing slight inaccuracies.
- `math.isclose(a, b)` is recommended for float comparisons instead of `==`.

#### Float Equality Testing

- Floating-point numbers in Python follow the IEEE 754 standard, which can introduce small precision errors.
- As a result, direct equality comparisons using == can be unreliable.
- Due to floating-point rounding, 0.1 + 0.2 evaluates to 0.30000000000000004, not exactly 0.3.

    ```python
    print(0.1 + 0.2 == 0.3)  # False
    ```

- The `math.isclose()` function allows for tolerance-based comparisons and is the recommended approach for float comparisons.
  - Accepts a *relative* tolerance or an *absolute* tolerance.
  - Absolute Tolerance (`abs_tol`) ensures numbers are close within a fixed range, useful for very small values.
  - Relative Tolerance (`rel_tol`) ensures numbers are close relative to their size, useful for large values.
  - The default is `rel_tol`$=1e-9$ and `abs_tol`$=0.0$.

    ```python
    import math

    print(math.isclose(0.1 + 0.2, 0.3))  # True

    a = 1000000.0
    b = 1000000.1

    # Absolute tolerance: checks if |a - b| < abs_tol
    print(math.isclose(a, b, abs_tol=0.2))  # True (difference is 0.1, within 0.2)

    # Relative tolerance: checks if |a - b| / max(|a|, |b|) < rel_tol
    print(math.isclose(a, b, rel_tol=1e-7))  # False (relative difference too large)

    # Relative tolerance: 1e-5 (checks relative difference)
    # Absolute tolerance: 1e-7 (ensures a small fixed margin)
    print(math.isclose(0.0000001, 0.0000002, rel_tol=1e-5, abs_tol=1e-7))  # True

    # Here, relative tolerance alone would fail, but abs_tol allows for small absolute differences.
    print(math.isclose(1000000.0, 1000000.1, rel_tol=1e-9, abs_tol=0.2))  # True
    ```

- `abs()` can be used to compare the absolute difference with a small tolerance threshold.
  - This can work well when the floats being compared have a similar scale.

    ```python
    def nearly_equal(a, b, tol=1e-9):
        return abs(a - b) < tol

    print(nearly_equal(0.1 + 0.2, 0.3))  # True
    ```

- The direct value equality comparison (`==`) can be used to compare integers with floats and when numbers are the exact result of a computation
When comparing integers stored as floats:

    ```python
    print(1.0 == 1)  # True

    x = 0.5 * 2
    print(x == 1.0)  # True
    ```

#### Coercing Floats to Integers

Python provides multiple ways to handle floating-point numbers when converting them to integers or adjusting their values.

- Truncation `math.trunc()`
  - Removes the decimal part and returns the integer portion (toward zero).
  - Equivalent to `int()` in behaviour.
  - python
- Floor `math.floor()`
  - Rounds down to the nearest integer.
  - Works for both positive and negative numbers.
- Ceiling `math.ceil()`
  - Rounds up to the nearest integer

```python
import math

# Truncation
print(math.trunc(4.9))  # 4
print(math.trunc(-4.9)) # -4
print(int(-4.9)) # -4 (same as truncation)

# Floor
print(math.floor(4.9)) # 4
print(math.floor(-4.9)) # -5

# Ceiling
print(math.ceil(4.1)) # 5
print(math.ceil(-4.1)) # -4
```

#### Rounding Floats (`round()`)

- `round(x, ndigits)` rounds to the nearest integer (or specified decimal places).
- When `ndigits` is negative, rounds to the nearest multiple of `10`, `100`, etc.
- Ties/halfway values ($.5$) round to the nearest even least significant digit (Bankers' rounding).
  - As defined in *IEEE 754* standard.
- Return types:
  - `round(x)` returns an `int`
  - `round(x, n)` returns the same type as `x` (even if `n` is `0`)
- Floating point precision also needs to be considered.
  - Python rounds `-12.35` to `-12.3` because `-12.35` is internally represented in binary as `-12.349999999999998`, which is slightly below `-12.35`.

```python
import decimal

# Rounding
print(round(4.6)) # 5  (normal rounding)
print(round(4.456, 2)) # 4.46 (round to 2 decimal places)

# Rounding with negative ndigits
print(round(12345, -1))  # 12350  (round to nearest 10)
print(round(12345, -2))  # 12300  (round to nearest 100)
print(round(12345, -3))  # 12000  (round to nearest 1000)
print(round(12345, -4))  # 10000  (round to nearest 10000)
print(round(-12345, -2))  # -12300
print(round(-98765, -3))  # -99000

# Rounding Ties (Bankers' Rounding)
print(round(5.5)) # 6  (rounds up, 6 is even)
print(round(4.5)) # 4  (rounds down, 4 is even)
print(round(1.35, 1)) # 1.4 (round up to 1 decimal places, 4 is even)
print(round(1.25, 1)) # 1.2 (round down to 1 decimal places, 2 is even)
print(round(-1.25, 1)) # -1.2 (round up to 1 decimal places, 2 is even)
print(round(-1.35, 1)) # -1.4 (round down to 1 decimal places, 4 is even)

# Rounding Return Types
print(round(10.0, 0)) # 10.0 (float)
print(round(10.0, 1)) # 10.0 (float)
print(round(10.0)) # 10 (int)

# Floating point precision with rounding instead of bankers' rounding
x = 12.35
print(decimal.Decimal(x)) # 12.3499999999999996447286321199499070644378662109375
print(round(x, 1)) # 12.3

y = 12.55
print(decimal.Decimal(y)) # 12.550000000000000710542735760100185871124267578125
print(round(y, 1)) # 12.6

z = 12.25
print(decimal.Decimal(z)) # 12.25 (can be accurately stored in binary)
print(round(z, 1)) # 12.2 (uses bankers' rounding)
```

#### Special Floating-Point Values

```python
import math

print(math.inf)  # Infinity
print(-math.inf)  # Negative Infinity
print(math.nan)  # Not-a-Number (NaN)
```

- Infinity (`inf`) results from division by zero (`1.0 / 0.0`).
- `NaN` (Not-a-Number) represents undefined operations (`0.0 / 0.0`).

#### Float Use Cases

- Scientific computing where approximate real-number arithmetic is sufficient.
- Machine learning, simulations, and graphics where fast computations matter more than perfect precision.
- When exact values are needed, alternatives like decimal.Decimal or fractions.Fraction should be used.

### Decimals (`decimals.Decimal`)

- `Decimal` class in Python (from the `decimal` module) provides arbitrary precision arithmetic.
- Repeated arithmetic operations on floating-points will result i precision issues.
  - Using `float` types to sum a billion financial transactions of £100.01 will lead to a result that is off by over £1000.
- Constructing from a String (Recommended)
  - Ensures exact representation without floating-point errors.
  - Best practice for financial and high-precision applications.

    ```python
    from decimal import Decimal

    d1 = Decimal('0.1')  # Exact 0.1
    d2 = Decimal('3.14159265358979323846')  # Arbitrary precision
    print(d1, d2)  # 0.1  3.14159265358979323846
    ```

- Constructing from an Integer
  - Converts an `int` directly to `Decimal` without precision issues.

    ```python
    d3 = Decimal(42)  # Exact integer conversion
    print(d3)  # 42
    ```

- Constructing from a Float (Not Recommended)
  - Using a `float` introduces floating-point errors because `float` is stored in binary.

    ```python
    d4 = Decimal(0.1)  # Not exact
    print(d4)  # 0.10000000000000000555111512312578 (Precision issue)
    ```

- Constructing from a Tuple
  - Uses a tuple `(sign, digits, exponent)` where:
    - `sign`: `0` for positive, `1` for negative.
    - `digits`: Tuple of integer digits.
    - `exponent`: Power of ten for scaling.

    ```python
    d5 = Decimal((0, (1, 2, 3, 4, 5), -2))  # 123.45
    print(d5)  # 123.45
    ```

#### Decimal Context and Precision/Rounding Settings

- Custom precision and rounding modes can be set globally using `decimal.getcontext()`.
  - `decimal.getcontext()` has return type `decimal.Context`
- A local context can also be set to use a temporary precision/rounding setting.
  - This is done by `decimal.localcontext(ctx=None)` which has return type `decimal.ContextManager`.
  - `ctx` is copied to create a new context.
  - If `ctx` is `None`, a copy of the default context is used.
- Context precision affects mathematical operations on `Decimal` types but not the `Decimal()` constructor.

```python
import decimal
from decimal import Decimal

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a) # 0.12345 precision=2 does not affect storage

x = Decimal('1.25')
y = Decimal('1.35')

# global context
g_ctx = decimal.getcontext()
g_ctx.prec = 5  # Set precision to 5 significant digits
g_ctx.rounding = decimal.ROUND_HALF_EVEN # Set rounding mechanism
g_ctx.rounding = 'ROUND_HALF_EVEN' # Set rounding mechanism from string

# local context
with decimal.localcontext() as ctx:
    type(ctx) # ctx has type decimal.Context when used with a with statement
    ctx.prec = 2
    ctx.rounding = decimal.ROUND_HALF_UP
    decimal.getcontext() # returns the local context when called from the with block
    print(id(ctx) == id(decimal.getcontext())) # true

    c = a + b
    print(c) = 0.25 # addition operation is affected by precision (s significant digits)

    print(round(x, 1)) # 1.3 - rounds half up (local)
    print(round(y, 1)) # 1.4 - rounds half up (local)

print(round(x, 1)) # 1.2 - rounds half even (global)
print(round(y, 1)) # 1.4 - rounds half even (global)

print(c) # 0.25
# c was created in a context with precision=2 so is still 0.25 even though precision in global context is 5 significant digits
```

#### Working with `Decimal` Rounding Methods

- `Decimal` provides precise control over rounding using methods such as `quantize()` and `to_integral_value()`.
- These allow rounding to specific decimal places or whole numbers with different rounding modes.

- `quantize()`
  - Rounds a `Decimal` to a fixed number of decimal places.
  - Requires a `Decimal` argument specifying the target precision.
  - A `rounding` mode must be specified if the result is ambiguous.

  ```python
  from decimal import Decimal, ROUND_HALF_EVEN
  print(Decimal('1.235').quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))  # 1.24
  print(Decimal('-1.235').quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN))  # -1.24
  ```

- `to_integral_value()`
  - Rounds a `Decimal` to an integer using the specified rounding mode.
  - Equivalent to `quantize(Decimal('1'), rounding=...)` but more efficient.

  ```python
  from decimal import Decimal, ROUND_FLOOR
  print(Decimal('2.9').to_integral_value(rounding=ROUND_FLOOR))  # 2
  print(Decimal('-2.9').to_integral_value(rounding=ROUND_FLOOR))  # -3
  ```

- `normalize()`
  - Removes trailing zeros while maintaining precision.

  ```python
  print(Decimal('1.2300').normalize())  # 1.23
  ```

- `adjusted()`
  - Returns the exponent of the `Decimal`, useful for understanding magnitude.

  ```python
  print(Decimal('123.45').adjusted())  # 2 (since 1.2345 × 10^2)
  ```

#### Rounding Mechanisms in `decimal.Decimal`

`Decimal` uses Bankers' rounding (round half to even) by default, but different rounding modes can be specified:

- `ROUND_CEILING`: Rounds towards positive infinity (always up).

    ```python
    from decimal import Decimal, ROUND_CEILING
    print(Decimal('1.1').to_integral_value(rounding=ROUND_CEILING))  # 2
    print(Decimal('-1.1').to_integral_value(rounding=ROUND_CEILING))  # -1
    ```

- `ROUND_DOWN`: Rounds towards zero (truncates the decimal part).

    ```python
    from decimal import Decimal, ROUND_DOWN
    print(Decimal('1.99').to_integral_value(rounding=ROUND_DOWN))  # 1
    print(Decimal('-1.99').to_integral_value(rounding=ROUND_DOWN))  # -1
    ```

- `ROUND_FLOOR`: Rounds towards negative infinity (always down).

    ```python
    from decimal import Decimal, ROUND_FLOOR
    print(Decimal('-1.1').to_integral_value(rounding=ROUND_FLOOR))  # -2
    ```

- `ROUND_HALF_DOWN`: Rounds to the nearest neighbour, ties go towards zero.

    ```python
    from decimal import Decimal, ROUND_HALF_DOWN
    print(Decimal('1.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN)) # 1.5
    print(Decimal('-2.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN)) # -2.5
    ```

- `ROUND_HALF_EVEN`: Rounds to the nearest neighbour, ties go to the nearest even number (Bankers' Rounding).

    ```python
    from decimal import Decimal, ROUND_HALF_EVEN
    print(Decimal('1.25').quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))  # 1.2
    print(Decimal('2.25').quantize(Decimal('0.1'), rounding=ROUND_HALF_EVEN))  # 2.2
    ```

- `ROUND_HALF_UP`: Rounds to the nearest neighbour, ties go away from zero.

    ```python
    from decimal import Decimal, ROUND_HALF_UP
    print(Decimal('1.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)) # 1.6
    print(Decimal('-2.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)) # -2.6
    ```

- `ROUND_UP`: Rounds away from zero (like `ceil` for positives, `floor` for negatives).

    ```python
    from decimal import Decimal, ROUND_UP
    print(Decimal('1.1').to_integral_value(rounding=ROUND_UP)) # 2
    print(Decimal('-1.1').to_integral_value(rounding=ROUND_UP)) # -2
    ```

- `ROUND_05UP`: Rounds away from zero only if the last digit before rounding is 0 or 5; otherwise, rounds towards zero.

    ```python
    from decimal import Decimal, ROUND_05UP
    print(Decimal('1.05').quantize(Decimal('0.1'), rounding=ROUND_05UP)) # 1.1
    print(Decimal('1.04').quantize(Decimal('0.1'), rounding=ROUND_05UP)) # 1.0
    ```

#### Decimal Arithmetic Operations

`Decimal` supports addition, subtraction, multiplication, division, and exponentiation, all with exact precision.

```python
a = Decimal('1.1')
b = Decimal('2.2')

print(a + b) # 3.3 (exact, unlike float)
print(a - b) # -1.1
print(a * b) # 2.42
print(a / b) # 0.5 (exact division)
print(a ** 2) # 1.21
```

- The div `//` and mod `%` operators work differently with `Decimal` types.
- The following equation is still satisfied: `n = d * (n // d) + (n % d)`
  - The div operator `//` performs truncation division, which always rounds towards zero.
  - The result for the mod operator will then satisfy the above equation.

```python
from decimal import Decimal

print(10 // 3) # 3 for integer
print(Decimal(10) // Decimal(3)) # 3 for Decimal

print(-10 // 3) # -4 for integer (floor division)
print(Decimal(-10) // Decimal(3)) # -3 for Decimal (truncation division)

print(-135 // 4) # -34 for integer
print(Decimal(-135) // Decimal(4)) # -33 for Decimal

print(-135 % 4) # 1 for integer
print(Decimal(-135) // Decimal(4)) # -3 for Decimal
```

The `math` module can accept `Decimal` types but will convert `Decimal` types to `float` types so introduce floating-point precision errors.

#### Comparing Decimals with Floating-Points

```python
print(Decimal('0.1') + Decimal('0.2') == Decimal('0.3'))  # True
print(0.1 + 0.2 == 0.3)  # False (float precision issue)
```

#### Performance Considerations When Using Decimal

- Slower than `float`
  - Decimal provides higher precision but at the cost of performance.
  - Operations on Decimal are significantly slower than equivalent float operations.
- Higher memory usage
  - Decimal stores numbers as a tuple of sign, coefficient, and exponent, requiring more memory than `float`.
- Context overhead
  - `decimal.getcontext()` manages precision, rounding, and traps, which adds processing overhead.
  - Changing context settings frequently can further impact performance.
- Conversion cost
  - Converting between `float` and `Decimal` is expensive due to internal representation differences.
  - Prefer constructing `Decimal` directly from strings to avoid floating-point inaccuracies.

### Complex Numbers (`complex`)

The complex type in Python represents numbers with a real and an imaginary part, following the form $z = a + bj$ where $a$ is the *real* part and $b$ is the *imaginary* part.

#### Creating Complex Numbers

Defined using `j`, `J` or `complex(real, imag)`.

```python
z1 = 3 + 4j
z2 = complex(3, 4) # Equivalent to 3 + 4j
```

#### Accessing Complex Number Components

Use `.real` and `.imag` attributes.

```python
print(z1.real) # 3.0
print(z1.imag) # 4.0
```

#### Complex Number Operations

Supports arithmetic like addition, subtraction, multiplication, and division.

```python
z1 = 1 + 2j
z2 = 3 + 4j
print(z1 + z2) # (4+6j)
print(z1 * z2) # (5+10j)
print(z1 + 3) # (4+2j)
print(z1 * 3) # (3+6j)
```

Equality operators `==` and `!=` are supported but are subject to similar precious errors that `float` types are.

#### Conjugate and Magnitude of Complex Numbers

- `conjugate()` returns the complex conjugate.
- `abs(z)` computes the magnitude (modulus).

```python
z = 3 + 4j
print(z.conjugate())  # (3-4j)
print(abs(z)) # 5.0
```

#### Complex Functions (`cmath`)

The `cmath` module provides mathematical functions for complex numbers, as opposed to `math` functions which will not work with complex numbers.

```python
import cmath

z = 1 + 1j
print(cmath.exp(z)) # e^(1 + j)
print(cmath.sqrt(z)) # sqrt(1 + j)
print(cmath.phase(z)) # Argument (angle in radians)
```

#### Complex Number Performance Considerations

- Uses two float values internally.
- More computationally expensive than real-only arithmetic.
- Avoid unnecessary conversions between float and complex.

### Booleans (`bool`)

- The `bool` type in Python represents Boolean values:
  - `True` (equivalent to `1`)
  - `False` (equivalent to `0`)
- `bool` as a subclass of `int`
  - `True` behaves like `1` and `False` behaves like `0`.
  - This allows Boolean values to be used in arithmetic operations.

```python
print(issubclass(bool, int)) # True
print(isinstance(True, bool)) # True
print(isinstance(True, int)) # True

print(True + 2) # 3
print(False * 5) # 0
print(True == 1) # True
print(False == 0) # True
print(False < True) # True
```

#### Creating Boolean Values

- `True` and `False` are built-in constants and point to fixed memory addresses over the lifetime of the application (singletons).
  - Comparing `bool` types can be done with the identity operator (`is`) or the value equality operator (`==`).
  - `True` and `1` are not the same objects, they have different memory addresses.
- The `bool()` constructor converts objects to `True` or `False` based on their [truthiness](./python_4_object_orientated.md#truthiness).
  - Most values will evaluate to `True` other than those which evaluate to `False`:
    - The None object: `None`
    - Zero in any numeric type: `0`, `0.0`, `0+0j` etc.
    - Empty sequences (lists, tuples, string etc.): `[]`, `()`, `''` etc.
    - Empty mapping types (dictionary, set etc.): `{}`
    - Custom classes that implements a `__bool__` or  `__len__` method that returns `False` or `0`.

```python
print(id(True) == id(1)) # False
print(id(False) == id(0)) # False

print(bool(0)) # False
print(bool(1)) # True
print(bool(-1)) # True
print(bool([])) # False (empty list)
print(bool([1, 2])) # True (non-empty list)
print(bool(None)) # False
print(bool('abc')) # True
```

#### Boolean Operators

Boolean operators are used to perform logical operations and comparisons in Python. They evaluate expressions and return `True` or `False` based on the conditions.

- **Comparison Operators**: These operators compare two values and return a Boolean result.

  - `==` Equal to
  - `!=` Not equal to
  - `>` Greater than
  - `<` Less than
  - `>=` Greater than or equal to
  - `<=` Less than or equal to

  ```python
  print(5 > 3)   # True
  print(10 == 5) # False
  print(2 != 4)  # True

  print(5 > 3 == True) # True
  print(id(5 > 3) == id(True)) # True
  print(5 > 3 is True) # True
  ```

- **Logical Operators** `not`, `and` and `or`: These operators combine multiple Boolean expressions and return a Boolean result.
  - `not x`: Evaluates the statement (`bool(x)`) and then inverts the boolean result. Returns `True` if the statement evaluates to `False` (and vice versa).
  - `x and y`: Evaluates `x` first. If `x` is falsy (i.e., evaluates to `False`), returns `x` immediately. Otherwise, evaluates and returns `y`. This is known as [short-circuiting](#short-circuiting).
  - `x or y`: Evaluates `x` first. If `x` is truthy (i.e., evaluates to `True`), returns `x` immediately. Otherwise, evaluates and returns `y`. This is also [short-circuiting](#short-circuiting) behaviour.

  ```python
  print(True and False)  # False
  print(True or False)   # True
  print(not True)        # False

  print(not 'abc') # False
  print(1 or 0) # 1
  print([1,0] and ['a']) # ['a']
  ```

These operators are essential for control flow and decision-making in Python programs.

#### Boolean Algebra Properties in Python

These transformations are useful in simplifying boolean expressions and logical conditions in Python programs.

##### Commutativity

The commutative property states that the order of operands does not affect the result. This applies to both `and` and `or`:

```python
A = True
B = False

print(A and B == B and A)  # True
print(A or B == B or A)  # True
```

##### Associativity

The associative property states that grouping of operations does not affect the result. This allows parentheses to be rearranged without changing the output:

```python
A = True
B = False
C = True

print((A and B) and C == A and (B and C))  # True
print((A or B) or C == A or (B or C))  # True
```

##### Distributivity

The distributive property allows expansion of expressions using and over or (or vice versa), similar to algebraic distribution:

```python
A = True
B = False
C = True

print(A and (B or C) == (A and B) or (A and C))  # True
print(A or (B and C) == (A or B) and (A or C))  # True
```

##### De Morgan’s Theorem

De Morgan’s laws describe how negation (`not`) interacts with `and` and `or`:

- `not (A and B) == (not A) or (not B)`
- `not (A or B) == (not A) and (not B)`

```python
A = True
B = False

print(not (A and B) == (not A or not B))  # True
print(not (A or B) == (not A and not B))  # True
```

#### Chained Boolean Comparisons

Python allows chaining of comparison operators, providing a more concise and readable alternative to multiple boolean expressions.



```python
# Instead of writing:
if 3 < x and x < 5:
  pass

# it can be written as:
if 3 < x < 5:
  pass
```

The expression `3 < x < 5` is equivalent to `(3 < x) and (x < 5)`, but avoids redundant evaluation of `x`.

This syntax is valid for any number of comparisons, e.g.:

```python
if 1 <= x < 10 != y:
  pass

# which expands to:
if (1 <= x) and (x < 10) and (10 != y):
  pass
```

#### Boolean Precedence

Python evaluates boolean expressions based on the following precedence order (highest to lowest):

  1. Parentheses: `()`
  2. Comparison Operators: `<`, `>`, `<=`, `>=`, `==`, `!=`, `in`, `is`
  3. Logical NOT: `not` (logical NOT)
  4. Logical AND: `and` (logical AND)
  5. Logical OR: `or` (logical OR)

Since `and` has higher precedence than `or`, combed expressions must be carefully structured:

```python
print(True or False and False)  # True (AND first, then OR)
print(not True or True)  # True (NOT first, then OR)
print(not (True or False))  # False (Parentheses change order)
```

Using parentheses is important for the readability of code - do not rely on boolean precedence alone.

#### Short-Circuiting

Short-circuiting is an optimization where Python stops evaluating an expression as soon as the result is determined:

- `and` short-circuits (stops early) if the first operand is `False` (since the result must be `False`).
- `or` short-circuits (stops early) if the first operand is `True` (since the result must be `True`).

```python
def expensive_check():
    print("Expensive check executed")
    return True

print(False and expensive_check())  # False (Short-circuits, function not called)
print(True or expensive_check())  # True (Short-circuits, function not called)
```

This behaviour improves efficiency by avoiding unnecessary function calls or computations. It is also useful when checking conditions safely:

```python
value = None
if value is not None and value > 10:  # Avoids TypeError if value is None
    print("Greater than 10")
```

Short-circuiting ensures that `value > 10` is never evaluated when value is `None`, preventing an error.

#### Using Booleans in Control Flow

`if`, `while`, and other control structures rely on Boolean evaluation.

```python
if True:
    print("This executes")  # Runs

if 0:
    print("This does not execute")  # Doesn't run
```

Short-circuiting allows conditional execution in a compact form, replacing traditional `if`...`else` statements.

```python
a = 1
b = 4
if b:
    print(a / b)
else:
    print(0)  # Default behaviour

# Shortened equivalent:
print(b and a/b)
```

- If `b` is truthy, `a/b` is evaluated and returned.
- If `b` is falsy (`0`, `None`, etc.), `b` itself is returned, preventing division by zero.
- This approach relies on short-circuiting to ensure that `a/b` is never evaluated when `b` is zero.

However, if `b` is `0`, the expression returns `0`, which may not be the intended output so a safer alternative using *undefined* can be defined:

```python
a = 1
b = 0
print((b and a/b) or "undefined") # undefined
```

- If `b` is `0`, `"undefined"` (or any fallback value) is returned instead.
- The `or` operator ensures that if `b` and `a/b` evaluates to `0` or `None`, the alternative value is used.

```python
s1 = None
s2 = ''
s3 = 'abc'
print((s1 and s1[0]) or 'n/a') # n/a
print((s2 and s2[0]) or 'n/a') # n/a
print((s3 and s3[0]) or 'n/a') # a
```

- If `s1` is `None`, `'n/a'` (or any fallback value) is returned instead.
- If `s2` is an empty string, `'n/a'` (or any fallback value) is returned instead.
- If `s3` is a non-empty string, the first character of `s3` is returned.
- The `or` operator ensures that if `s1` and `s1[0]`, or `s2` and `s2[0]`, evaluates to `None` or an empty string, the alternative value `'n/a'` is used.

### Tuples (`tuple`)

- A tuple is an immutable, ordered collection of elements:
  - *Immutable*: The data structure and contents of a tuple never change once created..
  - *Ordered*: Tuples can represent data records, where the position of each element has meaning.
- Tuples can store *heterogeneous* data, meaning they can contain different types.
- If all elements within a tuple are hashable, the tuple itself is hashable and can be used as a dictionary key.
- Tuples are defined by commas (`,`) rather than parentheses (`()`), though parentheses improve readability and are required in some cases.
- Elements in a tuple are accessed using indexing.

#### Creating Tuples

Basic tuple definition:

```python
london = 'London', 'UK', 8_000_000  # A tuple with three elements
southampton = ('Southampton', 'UK', 250_000)  # Parentheses improve readability

# Accessing elements by index
city = london[0]
country = london[1]
population = london[2]
print(city, country, population)  # London UK 8000000
```

Single-element tuple: (A trailing comma is required)

```python
t = (42,)  # Correct: Tuple with one element
t = 42,    # Also correct

t = (42)   # Incorrect: This is just an integer
```

Empty tuple: (Parentheses are required)

```python
t = ()  # The only way to define an empty tuple
```

#### Accessing Tuple Elements

Indexing:

```python
t = (10, 20, 30)
print(t[1])  # 20
```

Slicing:

```python
print(t[:2])  # (10, 20)
```

Iterating:

```python
t = ('apple', 'banana', 'cherry')

for item in t:
    print(item)
# Output:
# apple
# banana
# cherry
```

Using `enumerate()` to get both index and value:

```python
Copy code
for index, value in enumerate(t):
    print(f"Index {index}: {value}")
# Output:
# Index 0: apple
# Index 1: banana
# Index 2: cherry
```

#### Tuple Packing and Unpacking

Packing (Assigning multiple values at once):

```python
t = 'apple', 'banana', 'cherry'  # Tuple packing
```

Unpacking (Extracting values into variables):

```python
a, b, c = t  # a = 'apple', b = 'banana', c = 'cherry'
```

Using `*` for iterable unpacking:

```python
t = 1, 2, 3, 4, 5
a, b, *c = t   # a = 1, b = 2, c = [3, 4, 5]
a, *_, e = t   # a = 1, e = 5 (using `_` as a dummy variable)
```

#### Common Uses of Tuples

- Returning multiple values from functions.
- As dictionary keys, since they are immutable.
- Representing fixed collections of data, where element positions hold meaning.

Example: Returning multiple values from a function

```python
Copy code
def get_coordinates():
    return 51.5074, -0.1278  # Latitude and longitude of London

lat, lon = get_coordinates()
print(lat, lon)  # 51.5074 -0.1278
```

#### Tuple Methods

Since tuples are immutable, they provide only a limited set of methods:

- `.count(x)` – Returns the number of occurrences of x in the tuple.
- `.index(x)` – Returns the index of the first occurrence of x.

```python
t = (1, 2, 3, 2, 2, 4)
print(t.count(2))  # 3
print(t.index(3))  # 2 (first occurrence)
```

### Named Tuples (`collections.namedtuple`)

- Named tuples provide a way to define lightweight, immutable, and self-documenting data structures.
  - Can be used instead of custom classes for storing simple data.
- Unlike regular tuples, elements can be accessed by name as well as by index.
- Defined using `collections.namedtuple`, which acts as a `class` factory and generates a subclass of `tuple`.
- When called, `namedtuple` returns a `class` type and takes the following arguments:
  - `typename`: The name of the named tuple type.
  - `field_names`: An ordered list of field names as strings or an iterable of strings.
    - Fields names can be any [valid variable name](#naming-conventions) but cannot start with an underscore `_`.
  - For example:
    - `namedtuple('A', ['x', 'y', 'z'])`
    - `namedtuple('A', ('x', 'y', 'z')`
    - `namedtuple('A', 'x, y, z')`
    - `namedtuple('A', 'x y z')`

```python
from collections import namedtuple

# Define a named tuple type
City = namedtuple('City', ['name', 'country', 'population'])

# Create an instance
london = City(name='London', country='UK', population=8_000_000)

# Access by index or attribute name
print(london[0], london.name)  # London London
print(london[1], london.country)  # UK UK
print(london.population)  # 8000000
print(type(london))  # <class '__main__.City'>
print(isinstance(london, tuple))  # True
```

Named tuples are immutable given they inherit from `tuple`, so assigning new values to fields is not allowed.

```python
london.population = 9_000_000  # AttributeError: can't set attribute
```

- The `rename=True` keyword argument allows `namedtuple` to automatically rename invalid or duplicate field names.
- Renamed fields are given sequential names: `_0`, `_1`, etc.
- Useful when generating named tuples dynamically from sources with potentially invalid field names (e.g., user input, CSV headers).
- Without `rename=True`, invalid field names would raise a `ValueError`.

```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'name'], rename=True)

print(Person._fields)  # Output: ('name', 'age', '_2')

p = Person('Alice', 30, 'Duplicate')
print(p)  # Output: Person(name='Alice', age=30, _2='Duplicate')
```

#### Modifying and Extending Named Tuples

Since named tuples are immutable, elements cannot be directly changed, but a modified copy can be created with `_replace()`:

```python
PersonDefault = namedtuple('Person', ['name', 'age', 'city'])
p = PersonDefault('Alice', 30, 'London')  
print(p)  # Person(name='Alice', age=30, city='London')

p2 = p._replace(age=31)  
print(p2)  # Person(name='Alice', age=31, city='London')
print(p is p2)  # False
```

A named tuple can be extended by creating a new subclass with additional fields:

```python
print(p._fields)  # ('name', 'age', 'city') 
ExtendedPerson = namedtuple('ExtendedPerson', p._fields + ('email',))
p_ext = ExtendedPerson('Alice', 30, 'London', 'alice@example.com')

print(p_ext)  # ExtendedPerson(name='Alice', age=30, city='London', email='alice@example)
```

#### Docstrings in namedtuple

A `namedtuple` automatically generates a default docstring for the class and its fields.

```python
from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])

print(Person.__doc__) # 'Person(name, age)'

print(Person.name.__doc__) # 'Alias for field number 0'
```

Since the default docstring is simple, a custom docstring can be set manually:

```python
Person.__doc__ = 'Represents a person with a name and age.'
Person.name.__doc__ = 'The name of the person.'

print(Person.__doc__)  # 'Represents a person with a name and age.'
print(Person.name.__doc__)  # 'The name of the person.'
```

This is useful for improving code readability and documentation.

#### Default Values for Named Tuples

From Python 3.7 onwards, default values can be provided for named tuple fields using the `defaults` keyword argument.

```python
Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown", 0, "Unknown"])
p_default = Person()  
print(p_default)  # Person(name='Unknown', age=0, city='Unknown')
print(p_default._field_defaults) # {'name': 'Unknown', 'age': 0, 'city': 'Unknown'}
```

### Strings (`str`)

```python
str

'hello'
"hello world"
```

### Lists (`list`)

```python
list

[10, 20, 30] # homogenous types
[10, "hello", 2.3] # heterogeneous type
```

#### Lists of Tuples

```python
london = ('London', 'UK', 8_000_000) # heterogeneous tuple
southampton = ('Southampton', 'UK', 250_000)
paris = ('Paris', 'France', 2_000_000)

cities = [london, southampton, paris] # homogenous list
```

### Comparing Tuples, Lists, and Strings

- Tuples, lists, and strings are all ordered sequences, meaning element positions matter.
  - This allows for indexing and iteration.
- Tuples and lists can store *heterogeneous* (mixed types) or *homogeneous* (same type) elements.
  - Lists are more commonly homogeneous, especially when elements are passed to functions via iteration.
- Strings are always homogeneous, consisting only of characters.
- Tuples and strings are *immutable*, while lists are *mutable*:
  - The length and order of a tuple or string are fixed and cannot be changed.
  - Lists can be modified by adding, removing, or changing elements.

| Feature                                | Tuple | List | String |
|----------------------------------------|:-----:|:----:|:------:|
| Mutable (Can be modified)              | ❌    | ✅   | ❌     |
| Ordered (Elements maintain position)   | ✅    | ✅   | ✅     |
| Indexable (Supports [] indexing)       | ✅    | ✅   | ✅     |
| Iterable (Can loop over elements)      | ✅    | ✅   | ✅     |
| Heterogeneous (Mixed data types allowed)| ✅    | ✅   | ❌     |
| Homogeneous (Same data types allowed)  | ✅    | ✅   | ✅     |
| Length can change (Supports resizing)  | ❌    | ✅   | ❌     |
| Order can change (Elements can be rearranged) | ❌    | ✅   | ❌     |

### Dictionaries (`dict`)

```python
dict

{"key1": "value1",
"key2": "value2"}
```

### Sets

```python
set

{"a", "b", "c"}
```

## Naming Conventions

Identifiers in Python are names used to identify variables, functions, classes, modules, and other objects. These names must follow certain rules and conventions.

- Identifiers **must start** with a letter (a-z, A-Z) or an underscore (`_`).
- Subsequent characters can be letters, digits (0-9), or underscores.
- Python identifiers are **case-sensitive** (e.g., `variable` and `Variable` are different).

```python
my_variable = 10
_variable = 5
myVar123 = 'hello'
```

| Identifier                  | Example            | Case Style           | Description                                                                                                   |
|:---------------------------:|:------------------:|:--------------------:|---------------------------------------------------------------------------------------------------------------|
| Public variable             | `variable`         | snake_case           | A variable that can be accessed from outside the class or module.                                             |
| Protected variable          | `_variable`        | snake_case           | Indicates that a variable is intended for internal use within a class or module (not strictly enforced).      |
| Private variable            | `__variable`       | snake_case           | A variable that is intended to be private to the class. Name mangling occurs (e.g., `__ClassName__variable`). |
| Special (*dunder*) variable | `__name__`         | snake_case           | Variables reserved for built-in functionalities that should not be created by users to avoid naming conflicts.|
| Public method               | `method()`         | snake_case           | A method that can be accessed from outside the class.                                                         |
| Protected method            | `_method()`        | snake_case           | Indicates that a method is intended for internal use within a class or module.                                |
| Private method              | `__method()`       | snake_case           | A method that is intended to be private to the class.                                                         |
| Special (*dunder*) method   | `__init__()`       | snake_case           | Methods reserved for built-in functionalities that should not be created by users to avoid naming conflicts.  |
| Constants                   | `CONSTANT_NAME`    | SCREAMING_SNAKE_CASE | Typically written in all uppercase with words separated by underscores.                                       |
| Class names                 | `ClassName`        | PascalCase           | Follow the CapitalizedWords convention (also known as CamelCase).                                             |
| Module names                | `module_name`      | snake_case           | Should be short and all lowercase; underscores can be used to improve readability.                            |
| Package names               | `packagename`      | lowercase            | Should be all lowercase and can include underscores if necessary.                                             |
| Function names              | `function_name`    | snake_case           | Should be all lowercase with words separated by underscores.                                                  |

## Python Comments

Comments in Python are used to explain code and are ignored by the interpreter during execution. They are **removed at compile time**, meaning they do not affect the performance or behaviour of the program.

Comments start with a hash symbol `#` and extend to the end of the line. Multiple lines can be commented by starting every line with the hash symbol.

```python
# This is a single-line comment

# This is a 
# multi-line comment

x = 42  # Can also comment at the end of a line
```

## Multi-Line Statements in Python

In Python, there are two ways to create multi-line statements: using implicit and explicit line continuation.

### Implicit Line Continuation

Python automatically allows multi-line statements when they are inside certain delimiters such as parentheses `()`, brackets `[]`, or curly braces `{}`. This method does not require any special characters to indicate line continuation.

```python
result = (1 + 2 + 3 +
            4 + 5 + 6)

my_list = [1, 2, 3,
            4, 5, 6]

my_dict = {'a': 1, 'b': 2,
            'c': 3, 'd': 4}
```

### Explicit Line Continuation

Python uses the backslash `\` character to explicitly continue a statement onto the next line. This is useful when a statement is long but does not fit into the implicit categories (like when outside of parentheses or brackets).

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6
```

Explicit line continuation with a backslash is generally discouraged if implicit continuation can be used instead, as it leads to cleaner and more readable code.

### Multi-line Strings in Python

Python supports multi-line strings using triple quotes (`'''` or `"""`). These strings preserve line breaks and formatting.

```python
multi_line_string = """This is a multi-line string.
It spans multiple lines,
and preserves line breaks."""
```

Triple quotes preserve newlines, but parentheses and backslashes allow multi-line string concatenation without newlines.

Multi-line strings are **not** comments as they are **not** removed at compile time but can be used for annotating code - such as a [Docstring](https://peps.python.org/pep-0257/).

## Docstrings

A docstring (documentation string) is a special type of string used to document Python functions, classes, modules, and methods that provides an easy way to embed documentation directly in the code.

### Docstring Syntax

- Docstrings are written inside triple quotes: """ docstring """ or ''' docstring '''.
- Triple quotes allow docstrings to span multiple lines.
- The docstring should be placed immediately after the definition of a function, class, or module.

```python
def example_function():
    """This function does nothing but demonstrate docstring syntax."""
    pass
```

### Types of Docstrings

#### Function Docstrings

Provide a description of the function's purpose, parameters, and return values.

```python
def add(a, b):
    """Returns the sum of two numbers a and b."""
    return a + b
```

#### Class Docstrings

Describe the class’s purpose, its attributes, and methods.

```python
class MyClass:
    """This is a sample class for demonstration."""
    def __init__(self, name):
        self.name = name
```

### Module Docstrings

- Describe the module's purpose and its functions, classes, and methods.
- Typically placed at the top of the module file.

```python
"""This module handles basic arithmetic operations."""
```

### Accessing Docstrings

Call the `help()` function to access the docstring of any function, class, or module.

```python
help(add)  # Displays the docstring for the add function
```

#### Using the `__doc__` attribute:

Access the docstring directly using the `__doc__` attribute.

```python
print(add.__doc__)  # Output: Returns the sum of two numbers a and b.
```

### Conventions for Writing Docstrings

Function/Method docstrings: Should describe the function’s purpose, parameters, return values, and possible exceptions.

```python
def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters:
    a (int, float): The first number.
    b (int, float): The second number.

    Returns:
    int, float: The product of a and b.
    """
    return a * b
```

Class docstrings: Should describe the class’s purpose, attributes, and provide examples of usage.

```python
class Calculator:
    """
    A simple calculator class.

    Attributes:
    result (float): Stores the result of the last operation.

    Methods:
    add(x, y): Adds two numbers.
    """
    def __init__(self):
        self.result = 0
```

### Docstring Style Guides

[PEP 257](https://peps.python.org/pep-0257/): The official style guide for Python docstrings. Some key recommendations:

- Docstrings should be enclosed in triple quotes.
- For one-liners, the closing quotes should be on the same line.
- The docstring should begin with a short description of the object’s purpose.
- For longer docstrings, include a description of parameters, return values, and exceptions.

## Conditionals

Conditionals are used to execute certain blocks of code based on specific conditions. In Python, the main conditional statements are `if`, `elif`, and `else`.

```python
if condition:
    # code to execute if condition is True
elif another_condition:
    # code to execute if another_condition is True
else:
    # code to execute if none of the above conditions are True

x = 10
if x < 5:
    print("x is less than 5")
    if x < 2:
        print("x is less than 2")
    else:
        print("x is less than 5 and greater or equal to 2")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is greater than 5")
```

### Ternary Conditional Operator

Python supports a shorthand way to write conditionals using the ternary operator:

```python
x = 10
result = "Greater than 5" if x > 5 else "Not greater than 5"
print(result)
```

## Functions

- Functions are reusable blocks of code that perform a specific task.
- They help in organizing code and avoiding repetition. In Python, functions can be defined using the `def` keyword.
- The [functions](./python_3_functions.md) chapter provides a detailed overview of functions in Python.

```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!
```

Functions can accept parameters, which are specified in parentheses. They can be required or optional (with default values).

```python
def add(a, b=5):
    return a + b

# Calling the function
print(add(3))     # Output: 8 (3 + 5)
print(add(3, 4))  # Output: 7 (3 + 4)
```

Functions can return values using the return statement. If no return statement is provided, the function returns `None`.

```python
def square(x):
    return x ** 2

result = square(4)
print(result)  # Output: 16
```

### Functions as Objects

Functions in Python are objects of type `function`. This allows functions to be assigned to variables, stored in data structures, or passed around like any other object:

```python
def multiply(x, y):
    return x * y

# Assigning function to a variable
operation = multiply
print(operation(3, 4))  # Output: 12
```

#### `my_func` versus `my_func()`

- `my_func` refers to the function object itself. It can be assigned to a variable or passed as an argument without executing it.
- `my_func()` calls the function, executing its code and returning the result.

```python
def say_hello():
    return "Hello!"

print(say_hello)   # Output: <function say_hello at 0x...> (Function object)
print(say_hello()) # Output: Hello! (Function executed)
```

### Higher-Order Functions

Since functions are objects, they can be passed as arguments to other functions and returned as results:

```python
def apply_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

print(apply_twice(increment, 3))  # Output: 5 (3 → 4 → 5)
```

### Built-in Functions

Python has many built-in functions that are readily available for use. Some commonly used built-in functions include:

- `len()` Returns the length of an object (string, list, etc.).

    ```python
    print(len("Hello"))  # Output: 5
    ```

- `max()` Returns the largest item in an iterable or the largest of two or more arguments.

    ```python
    print(max(3, 7, 2))  # Output: 7
    ```

- `min()` Returns the smallest item in an iterable or the smallest of two or more arguments.

    ```python
    print(min(3, 7, 2))  # Output: 2
    ```

- `sum()` Sums the items of an iterable from left to right.

    ```python
    print(sum([1, 2, 3, 4]))  # Output: 10
    ```

- `sorted()` Returns a new sorted list from the items in an iterable.

    ```python
    print(sorted([3, 1, 4, 2]))  # Output: [1, 2, 3, 4]
    ```

- `type()` Returns the type of an object.

    ```python
    print(type(10))  # Output: <class 'int'>
    ```

For a comprehensive list of built-in functions in Python, visit the official documentation: [Python Built-in Functions](https://docs.python.org/3/library/functions.html).

## Loops

Loops in Python are used to iterate over a block of code multiple times. The two main types of loops are `while` loops and `for` loops.

### `while` Loops

A `while` loop repeatedly executes a block of code as long as the specified condition is `True`.

```python
while condition:
    # code to execute

i = 1
while i <= 5:
    print(i)
    i += 1
# This will output:
# 1
# 2
# 3
# 4
# 5
```

A `while True` loop is an infinite loop because the condition is always True. It keeps running until a break statement is encountered, which is often used to exit the loop based on some condition.

```python
while True:
    user_input = input("Enter something (or 'q' to quit): ")
    if user_input == 'q':
        break
    print(f"You entered: {user_input}")
# In this example, the loop will continue indefinitely until the user enters 'q'.
```

The `break` statement exits the loop prematurely when a certain condition is met.

```python
i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
# Output:
# 1
# 2
```

The `continue` statement skips the rest of the code in the current iteration and moves to the next iteration.

```python
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Output:
# 1
# 2
# 4
# 5
```

### `for` Loops

A `for` loop iterates over a sequence (like a `list`, `tuple`, or `string`) or any iterable object. It repeats the block of code once for each item in the sequence.

```python
for variable in iterable:
    # code to execute

for i in range(1, 6):
    print(i)
# Output:
# 1
# 2
# 3
# 4
# 5
```

Use `break` to exit a for loop early.

``` python
for i in range(1, 6):
    if i == 3:
        break
    print(i)
# Output:
# 1
# 2
```

The `continue` statement skips the current iteration and moves to the next one.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# Output:
# 1
# 2
# 4
# 5
```

#### Loops with `else`

Both `while` and `for` loops can have an `else` clause. The `else` block executes if the loop finishes normally (i.e., without hitting a break).

```python
for i in range(1, 4):
    print(i)
    if i % 5 == 0:
        break
else:
    print("Loop finished")
# Output:
# 1
# 2
# 3
# Loop finished

for i in range(1, 4):
    print(i)
    if i % 2 == 0:
        break
else:
    print("Loop finished")
# Output:
# 1
# 2

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished")
# Output:
# 1
# 2
# 3
# Loop finished

i = 1
while i <= 3:
    print(i)
    if i % 2 == 0:
        break
    i += 1
else:
    print("Loop finished")
# Output:
# 1
# 2
```

### List Comprehension

List comprehensions are compact and efficient ways to create new lists by applying an expression to each item in an iterable, optionally filtering items based on a condition. It is typically used to replace simple for loops that build lists.

- Key benefits of list comprehensions include:
  - **Concise**: More compact and readable than traditional for loops.
  - **Performance**: List comprehensions are often faster than using regular for loops due to optimizations.
  - **Functional Style**: Helps write cleaner code by encapsulating the loop, expression, and filtering in a single
- While list comprehensions are concise, they can sometimes sacrifice readability if the expression becomes too complex. In such cases, using regular for loops may be preferable.

```python
[expression for item in iterable]
```

- `expression`: The value or operation applied to each item in the iterable.
- `item`: The current element being processed from the iterable.
- `iterable`: The collection being iterated over (e.g., list, range, etc.).

Creating a list of squares from a range of numbers:

```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

Creating a list of even numbers from a range:

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

Creating a list of numbers that are divisible by both 2 and 3:

```python
div_by_2_and_3 = [x for x in range(20) if x % 2 == 0 and x % 3 == 0]
print(div_by_2_and_3)  # Output: [0, 6, 12, 18]
```

Applying an operation on each element of an iterable (e.g., converting strings to uppercase):

```python
words = ['hello', 'world', 'python']
upper_words = [word.upper() for word in words]
print(upper_words)  # Output: ['HELLO', 'WORLD', 'PYTHON']
```

Creating a 2D matrix and flattening it:

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in matrix for item in sublist]
print(flat)  # Output: [1, 2, 3, 4, 5, 6]
```

#### List Comprehension Comparison to Regular `for` Loop

```python
# regular for loop:
squares = []
for x in range(5):
  squares.append(x**2)

# list comprehension:
squares = [x**2 for x in range(5)]
```

## Exception Handling

The `try`, `except`, `else`, `finally` blocks in Python provide a powerful way to handle exceptions and ensure that certain code runs regardless of whether an error occurs. They allow for structured error handling and clean up of resources.

1. **`try` block**: Contains code that may potentially raise an exception.
2. **`except` block**: This handles the exception if one occurs in the `try` block.
3. **`else` block** (Optional): Runs if no exceptions are raised in the `try` block.
4. **`finally` block** (Optional): Always runs, regardless of whether an exception was raised or not. Typically used for clean-up tasks.

```python
try:
    # Code that might raise an exception
except ExceptionType:
    # Code that runs if the specific exception occurs
else:
    # Code that runs if no exceptions were raised
finally:
    # Code that always runs

try:
    result = 10 / 2  # This will not raise an exception
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Division successful, result is {result}")
finally:
    print("This always runs.")
# Output:
# Division successful, result is 5.0
# This always runs.

try:
    result = 10 / 0  # This raises a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Division successful, result is {result}")
finally:
    print("This always runs.")
# Output:
# Cannot divide by zero.
# This always runs.
```

## Scope

- *Scope* defines the visibility and lifetime of names (variable bindings) within an application.
- *Namespaces* are mappings of variable names to objects. Each scope corresponds to a namespace that determines where a name can be accessed.
- *Variable Bindings* associate names with objects. Rebinding a variable updates the reference in the current namespace without modifying the object itself.
- Python has three main scopes for resolving variable names:
  - **Local Scope**: Variables defined inside a function exist only within that function’s execution context.
  - **Enclosing (Non-Local) Scope**: Variables in outer (non-global) functions are accessible to inner functions but not modifiable without nonlocal.
  - **Global Scope**: Variables defined at the module level exist throughout the application unless shadowed by local bindings.
- The *LEGB Rule* (*Local* → *Enclosing* → *Global* → *Built-in*) determines the order of name resolution in Python.

### Local Scope

A variable assigned inside a function is local to that function and cannot be accessed outside it.

```python
a = 10

def reference_func():
    print(a)  # Accesses the global variable 'a'


def assignment_func():
    x = 10  # Local variable, due to assignment inside the function
    print(x)

print(x)  # NameError: name 'x' is not defined
```

- Local variables are created when the function is called and destroyed when it returns.
- Every function call creates a new local scope and local variables are assigned to that scope.
  - This is how recursion works, as each recursive call creates a new scope with its own variables.
- All local variables defined inside the function cannot be accessed outside the function.
- When a function finishes running, the function’s local scope is destroyed, and the reference count to variables in higher scopes are decremented.

### Global/Module Scope

- The *global scope* refers to the top-level scope of a module (i.e., a single .py file). It spans the entire module but does not extend across multiple modules in the same application.
- Python does not have a truly global scope that spans multiple files.
  - Each module has its own independent global scope.
  - A global variable in one module is not automatically available in another module unless explicitly imported.
- The only exception to Python’s module-based scoping are the *built-in objects*, which contain universally available objects such as:
  - `True`, `False`, `None`
  - `int`, `str`, `dict`, `list`, `set`, etc.
  - Built-in callables like `print`, `len`, `range`, `id`, etc.

Example: Global Variables Are Module-Specific

```python
# file1.py
a = 42  # Global in file1.py
```

```python
# file2.py
print(a)  # NameError: name 'a' is not defined

import a from file1
print(a)  # 42 (a from the file1 module scope and print from the built-in scope)
```

Built-in functions can be reassigned, but it is not recommended to do so.

```python
x = [1, 2, 3]
print(len(x)) # 3

def len(x):
    return "Hello"  # Redefining len (masking - not a good practice)

print(len(x)) # Hello (len now refers to the len function in module scope)

del len # Deletes the local len function
print(len(x))  # 42 (print now refers to the built-in function)
```

- The variable `x` is global only within `file1.py` and is not available in `file2.py` unless explicitly imported.
- Inside a function, a global variable can be accessed but not modified unless declared with `global`.

```python
x = 10  # Global variable

def update_x():
    global x  # Needed to modify x
    x = 20

update_x()
print(x)  # 20
```

- Minimize use of global variables to avoid unintended side effects.
- Use module-level constants (e.g., MAX_VALUE = 100) for readability.
- If needed across modules, import explicitly (e.g., `from config import SOME_GLOBAL`).

#### The `global` Keyword

The `global` keyword allows modifying a global variable from within a function.

```python
x = 10  # Global variable

def mask_variable():
    x = 20  # Local variable masks global x
    print(x)

def modify_global():
    global x  # Refers to global x
    x += 5
    print(x)


mask_variable() # 20 (Local variable)
print(x)  # 10 (Global variable)

modify_global() # 15 (Modified globally)
print(x)  # 15 (Modified globally)
```

- Without `global`, assigning to `x` inside `modify_global()` would create a new local variable (masking).
- Global variables persist throughout the program’s execution.

### Non-Local Scope (Enclosing Scope)

- Refers to variables in an enclosing function (not global).
- Used inside nested functions to access and modify variables from an outer function.
- Declared using the `nonlocal` keyword.
  - Python will look for variables defined with `nonlocal` in the enclosing local scopes chain until it first encounters the specified variable name.
  - Only local scopes will be searched, not the global scope.

```python
x = 'Hello' # Global variable
def outer():
    x = 10 # local variable masking global x
    y = 20
    z = 30

    def inner():
        nonlocal x  # Refers to 'x' in outer()
        x += 5
        y = 10 # Creates a new local variable 'y' in inner()
        print(f"inner_x: {x}")
        print(f"inner_y: {y}")
        print(f"inner_z: {z}")  # Accesses 'z' from outer()

        def inner_inner():
            global x # Refers to 'x' in global scope
            nonlocal y  # Refers to 'y' in inner()
            nonlocal z  # Refers to 'z' in outer()
            x = "Hello from inner_inner"
            y += 1
            z -=1
            print(f"inner_inner_x: {x}")
            print(f"inner_inner_y: {y}")
            print(f"inner_inner_z: {z}")

        inner_inner()

    inner()

    print(f"outer_x: {x}")
    print(f"outer_y: {y}")
    print(f"outer_z: {z}")

print(f"global_x: {x}")
outer()
print(f"global_x: {x}")
# global_x: Hello
# inner_x: 15
# inner_y: 10
# inner_z: 30
# inner_inner_x: Hello from inner_inner
# inner_inner_y: 11
# inner_inner_z: 29
# outer_x: 15
# outer_y: 20
# outer_z: 29
# global_x: Hello from inner_inner
```

- `nonlocal` allows modifying a variable from an enclosing (but not global) scope.
- Without `nonlocal`, assigning to `x` inside `inner()` would create a new local variable, leaving `x` in `outer()` unchanged.
- This is useful for maintaining state across function calls within a [closure](./python_3_functions.md#closures).

### Scope Resolution Order (LEGB Rule)

Python resolves variable names in the following order:

1. Local – Inside the current function.
2. Enclosing – Inside the enclosing function (for nested functions).
3. Global/Module – Defined at the top level of the script/module.
4. Built-in – Python’s built-in functions (e.g., `len`, `sum`).

```python
x = 'global'

def outer():
    x = 'enclosing'

    def inner():
        x = 'local'
        print(x)  # Resolves to 'local'

    inner()
    print(x)  # Resolves to 'enclosing'

outer()
print(x)  # Resolves to 'global'
```

- This order ensures the most specific scope is used first.
- If a variable is not found in the local scope, Python checks the enclosing scope, then the global scope, and finally the built-in scope.

### Variables in Loops

Variables defined in loops **are** accessible outside the loop (as long as the variable is assigned in the loop before the variable is accessed outside the loop).

```python
for i in range(10):
    x = i + 1

print(x)  # 10 (x is accessible outside the loop)
```

This convention differs to C# and Java where variables defined in loops are not accessible outside the loop.
