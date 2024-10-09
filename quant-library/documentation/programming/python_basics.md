# Python: Basics

- [Python: Basics](#python-basics)
  - [Syntax](#syntax)
    - [Naming Conventions](#naming-conventions)
      - [General Rules](#general-rules)
    - [Python Comments](#python-comments)
    - [Multi-Line Statements in Python](#multi-line-statements-in-python)
      - [Implicit Line Continuation](#implicit-line-continuation)
      - [Explicit Line Continuation](#explicit-line-continuation)
      - [Multi-line Strings in Python](#multi-line-strings-in-python)
  - [Data Types](#data-types)
    - [Integers](#integers)
    - [Floating Points](#floating-points)
    - [Strings](#strings)
    - [Lists](#lists)
    - [Dictionaries](#dictionaries)
    - [Tuples](#tuples)
    - [Sets](#sets)
    - [Booleans](#booleans)

## Syntax

### Naming Conventions

Identifiers in Python are names used to identify variables, functions, classes, modules, and other objects. These names must follow certain rules and conventions.

#### General Rules

- Identifiers **must start** with a letter (a-z, A-Z) or an underscore (`_`).
- Subsequent characters can be letters, digits (0-9), or underscores.
- Python identifiers are **case-sensitive** (e.g., `variable` and `Variable` are different).

```python
my_variable = 10
_variable = 5
myVar123 = "hello"
```



Use snake_case for variables and functions.
Use UPPER_SNAKE_CASE for constants.
Use PascalCase for classes.
Prefix with a single underscore (_) for private variables, and double underscores (__) for name mangling.

### Python Comments

Comments in Python are used to explain code and are ignored by the interpreter during execution. They are **removed at compile time**, meaning they do not affect the performance or behavior of the program.

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

