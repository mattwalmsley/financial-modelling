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
    - [Strings (`str`)](#strings-str)
    - [Lists (`list`)](#lists-list)
    - [Dictionaries (`dict`)](#dictionaries-dict)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Booleans](#booleans)
  - [Naming Conventions](#naming-conventions)
  - [Python Comments](#python-comments)
  - [Multi-Line Statements in Python](#multi-line-statements-in-python)
    - [Implicit Line Continuation](#implicit-line-continuation)
    - [Explicit Line Continuation](#explicit-line-continuation)
    - [Multi-line Strings in Python](#multi-line-strings-in-python)
  - [Conditionals](#conditionals)
    - [Comparison Operators](#comparison-operators)
    - [Logical Operators](#logical-operators)
    - [Ternary Conditional Operator](#ternary-conditional-operator)
  - [Functions](#functions)
    - [Functions as Objects](#functions-as-objects)
      - [`my_func` versus `my_func()`](#my_func-versus-my_func)
    - [Higher-Order Functions](#higher-order-functions)
    - [Built-in Functions](#built-in-functions)
    - [Lambda Functions](#lambda-functions)
  - [Loops](#loops)
    - [`while` Loops](#while-loops)
    - [`for` Loops](#for-loops)
      - [Loops with `else`](#loops-with-else)
  - [Exception Handling](#exception-handling)

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
int("42") # 42 (base-10 by default)
int("1010", 2) # 10 (base-2)
int("A12F", base=16) # 41263 (base-16)

int("B", 11) # ValueError

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
f2 = Fraction("1.5")  # 3/2
f2 = Fraction("1/5")  # 1/5
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

    d1 = Decimal("0.1")  # Exact 0.1
    d2 = Decimal("3.14159265358979323846")  # Arbitrary precision
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
    print(Decimal('1.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN))  # 1.5
    print(Decimal('-2.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_DOWN))  # -2.5
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
    print(Decimal('1.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))  # 1.6
    print(Decimal('-2.55').quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))  # -2.6
    ```

- `ROUND_UP`: Rounds away from zero (like `ceil` for positives, `floor` for negatives).

    ```python
    from decimal import Decimal, ROUND_UP
    print(Decimal('1.1').to_integral_value(rounding=ROUND_UP))  # 2
    print(Decimal('-1.1').to_integral_value(rounding=ROUND_UP))  # -2
    ```

- `ROUND_05UP`: Rounds away from zero only if the last digit before rounding is 0 or 5; otherwise, rounds towards zero.

    ```python
    from decimal import Decimal, ROUND_05UP
    print(Decimal('1.05').quantize(Decimal('0.1'), rounding=ROUND_05UP))  # 1.1
    print(Decimal('1.04').quantize(Decimal('0.1'), rounding=ROUND_05UP))  # 1.0
    ```

#### Decimal Arithmetic Operations

`Decimal` supports addition, subtraction, multiplication, division, and exponentiation, all with exact precision.

```python
a = Decimal("1.1")
b = Decimal("2.2")

print(a + b)  # 3.3 (exact, unlike float)
print(a - b)  # -1.1
print(a * b)  # 2.42
print(a / b)  # 0.5 (exact division)
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
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True
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

### Strings (`str`)

```python
str

"hello"
"hello world"
```

### Lists (`list`)

```python
list

[10, 20, 30] # homogenous types
[10, "hello", 2.3] # heterogeneous type
```

### Dictionaries (`dict`)

```python
dict

{"key1": "value1",
"key2": "value2"}
```

### Tuples

```python
tuple

(10, "hello", 2.3) # usually heterogeneous
```

### Sets

```python
set

{"a", "b", "c"}
```

### Booleans

```python
bool

True
False
```

## Naming Conventions

Identifiers in Python are names used to identify variables, functions, classes, modules, and other objects. These names must follow certain rules and conventions.

- Identifiers **must start** with a letter (a-z, A-Z) or an underscore (`_`).
- Subsequent characters can be letters, digits (0-9), or underscores.
- Python identifiers are **case-sensitive** (e.g., `variable` and `Variable` are different).

```python
my_variable = 10
_variable = 5
myVar123 = "hello"
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

### Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

### Logical Operators

- `and` Returns `True` if both statements are true.
- `or` Returns `True` if at least one statement is true.
- `not` Returns `True` if the statement is false.

### Ternary Conditional Operator

Python supports a shorthand way to write conditionals using the ternary operator:

```python
x = 10
result = "Greater than 5" if x > 5 else "Not greater than 5"
print(result)
```

## Functions

Functions are reusable blocks of code that perform a specific task. They help in organizing code and avoiding repetition. In Python, functions can be defined using the `def` keyword.

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
Copy code
def square(x):
    return x ** 2

result = square(4)
print(result)  # Output: 16
```

### Functions as Objects

Functions in Python are objects of type function. This allows functions to be assigned to variables, stored in data structures, or passed around like any other object:

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

### Lambda Functions

A **lambda function** is a small anonymous function defined using the `lambda` keyword. It can take any number of arguments but has only one expression. Lambda functions are useful for short, throwaway functions.

```python
lambda arguments: expression
```

The function evaluates the expression and returns the result.

```python
# Lambda to add two numbers
add = lambda x, y: x + y

# Calling the lambda function
print(add(3, 5))  # Output: 8
```

Lambda functions are commonly used with higher-order functions such as `map()`, `filter()`, and `sorted()`.

```python
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))

print(squares)  # Output: [1, 4, 9, 16]
```

```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4, 6]
```

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
