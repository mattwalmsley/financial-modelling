# Python: Basics

- [Python: Basics](#python-basics)
  - [Style and Syntax](#style-and-syntax)
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
      - [Built-in Functions](#built-in-functions)
  - [Data Types](#data-types)
    - [Integers](#integers)
    - [Floating Points](#floating-points)
    - [Strings](#strings)
    - [Lists](#lists)
    - [Dictionaries](#dictionaries)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Booleans](#booleans)

## Style and Syntax

See [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/) for best practices.

### Naming Conventions

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

### Python Comments

Comments in Python are used to explain code and are ignored by the interpreter during execution. They are **removed at compile time**, meaning they do not affect the performance or behaviour of the program.

Comments start with a hash symbol `#` and extend to the end of the line. Multiple lines can be commented by starting every line with the hash symbol.

```python
# This is a single-line comment

# This is a 
# multi-line comment

x = 42  # You can also comment at the end of a line
```

### Multi-Line Statements in Python

In Python, there are two ways to create multi-line statements: using implicit and explicit line continuation.

#### Implicit Line Continuation

Python automatically allows multi-line statements when they are inside certain delimiters such as parentheses `()`, brackets `[]`, or curly braces `{}`. This method does not require any special characters to indicate line continuation.

```python
result = (1 + 2 + 3 +
            4 + 5 + 6)

my_list = [1, 2, 3,
            4, 5, 6]

my_dict = {'a': 1, 'b': 2,
            'c': 3, 'd': 4}
```

#### Explicit Line Continuation

Python uses the backslash `\` character to explicitly continue a statement onto the next line. This is useful when a statement is long but does not fit into the implicit categories (like when you're outside of parentheses or brackets).

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6
```

Explicit line continuation with a backslash is generally discouraged if implicit continuation can be used instead, as it leads to cleaner and more readable code.

#### Multi-line Strings in Python

Python supports multi-line strings using triple quotes (`'''` or `"""`). These strings preserve line breaks and formatting.

```python
multi_line_string = """This is a multi-line string.
It spans multiple lines,
and preserves line breaks."""
```

Triple quotes preserve newlines, but parentheses and backslashes allow multi-line string concatenation without newlines.

Multi-line strings are **not** comments as they are **not** removed at compile time but can be used for annotating code - such as a [Docstring](https://peps.python.org/pep-0257/).

### Conditionals

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

#### Comparison Operators

- `==` Equal to
- `!=` Not equal to
- `>` Greater than
- `<` Less than
- `>=` Greater than or equal to
- `<=` Less than or equal to

#### Logical Operators

- `and` Returns `True` if both statements are true.
- `or` Returns `True` if at least one statement is true.
- `not` Returns `True` if the statement is false.

#### Ternary Conditional Operator

Python supports a shorthand way to write conditionals using the ternary operator:

```python
x = 10
result = "Greater than 5" if x > 5 else "Not greater than 5"
print(result)
```

### Functions

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

#### Built-in Functions

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

## Data Types

### Integers

```code
int

3
300
3000
```

### Floating Points

```python
float

2.3
4.7
23.21
```

### Strings

```python
str

"hello"
"hello world"
```

### Lists

```python
list

[10, 20, 30] # homogenous types
[10, "hello", 2.3] # heterogeneous type
```

### Dictionaries

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
