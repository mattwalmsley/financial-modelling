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
      - [Conversion to Integer](#conversion-to-integer)
      - [Integer Common Methods](#integer-common-methods)
    - [Floating Points (`float`)](#floating-points-float)
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
binary = 0b1010  # 10 in decimal
octal = 0o12  # 10 in decimal
hexadecimal = 0x1f  # 31 in decimal
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

#### Conversion to Integer

Integers can be converted from strings or floats.

```python
str_num = "42"
int_num = int(str_num)  # 42

float_num = 3.14
int_from_float = int(float_num)  # 3
```

#### Integer Common Methods

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

### Floating Points (`float`)

```python
float

2.3
4.7
23.21
```

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
