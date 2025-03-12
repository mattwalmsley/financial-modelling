# Python Functions

- [Python Functions](#python-functions)
  - [Introduction](#introduction)
  - [Argument Passing](#argument-passing)
    - [Positional and Keyword Arguments](#positional-and-keyword-arguments)
    - [Positional-Only Arguments (`/`)](#positional-only-arguments-)
    - [`*args` and `**kwargs`](#args-and-kwargs)
      - [Unpacking with `*` and `**`](#unpacking-with--and-)
      - [Using `*args` for Positional Arguments](#using-args-for-positional-arguments)
      - [`*args` and Keyword-Only Arguments](#args-and-keyword-only-arguments)
        - [Mixing `*args` with a Regular Keyword Argument](#mixing-args-with-a-regular-keyword-argument)
        - [Enforcing Keyword-Only Arguments with `*`](#enforcing-keyword-only-arguments-with-)
      - [Mixing Positional-Only and Keyword Arguments](#mixing-positional-only-and-keyword-arguments)
        - [Mixing `*args`, `*`, and Keyword-Only Arguments](#mixing-args--and-keyword-only-arguments)
      - [Using `**kwargs` for Keyword Arguments](#using-kwargs-for-keyword-arguments)
      - [Mixing \*args and \*\*kwargs](#mixing-args-and-kwargs)
      - [Advanced Argument Mixing](#advanced-argument-mixing)
      - [Typical Usages of `*args` and `**kwargs`](#typical-usages-of-args-and-kwargs)
    - [Passing Immutable Objects as Arguments (Pass-by-Value-like Behaviour)](#passing-immutable-objects-as-arguments-pass-by-value-like-behaviour)
    - [Passing Mutable Objects as Arguments (Pass-by-Reference-like Behaviour)](#passing-mutable-objects-as-arguments-pass-by-reference-like-behaviour)
    - [Reassignment of Arguments](#reassignment-of-arguments)
    - [Behaviour of Mutable Default Arguments](#behaviour-of-mutable-default-arguments)
    - [Behaviour of Dynamic Default Arguments](#behaviour-of-dynamic-default-arguments)
  - [Function Annotations](#function-annotations)
    - [Function Annotation Syntax](#function-annotation-syntax)
    - [Accessing Annotations](#accessing-annotations)
    - [Typing Module and Advanced Annotations](#typing-module-and-advanced-annotations)
      - [Expression Function Annotations](#expression-function-annotations)
  - [Lambda Functions](#lambda-functions)
    - [Using Lambda Functions with Built-in Functions](#using-lambda-functions-with-built-in-functions)
    - [`lambda` versus `def` Functions](#lambda-versus-def-functions)
    - [When to Use Lambda Functions](#when-to-use-lambda-functions)
    - [When to Avoid Lambda Functions](#when-to-avoid-lambda-functions)
  - [Function Introspection](#function-introspection)
    - [Basic Function Attributes](#basic-function-attributes)
    - [Accessing Function Attributes](#accessing-function-attributes)
    - [Creating Function Attributes](#creating-function-attributes)
    - [Inspecting Function Signature (`inspect` module)](#inspecting-function-signature-inspect-module)
      - [Retrieving Source Code \& Bytecode using `inspect` and `dis`](#retrieving-source-code--bytecode-using-inspect-and-dis)
    - [Checking If an Object Is a Function](#checking-if-an-object-is-a-function)
  - [Built-In Functions](#built-in-functions)
    - [`map()`](#map)
    - [`zip()`](#zip)
      - [Using `zip()` with List Comprehensions](#using-zip-with-list-comprehensions)
    - [`filter()`](#filter)
      - [Using List Comprehension with `if` Instead of `filter()`](#using-list-comprehension-with-if-instead-of-filter)
  - [Reducing Functions (`functools.reduce`)](#reducing-functions-functoolsreduce)
    - [Built-in Reducing Functions in Python](#built-in-reducing-functions-in-python)
      - [`sum()`: Summation of Elements](#sum-summation-of-elements)
      - [`max()`: Maximum Value](#max-maximum-value)
      - [`min()`: Minimum Value](#min-minimum-value)
      - [`any()`: Checks for At Least One True Value](#any-checks-for-at-least-one-true-value)
      - [`all()`: Checks If All Values Are True](#all-checks-if-all-values-are-true)
      - [`str.join()`: Concatenates Strings](#strjoin-concatenates-strings)
  - [Partial Functions (`functools.partial`)](#partial-functions-functoolspartial)
  - [`operator` Module](#operator-module)
    - [Using `operator.add` with `reduce()`](#using-operatoradd-with-reduce)
    - [Example: Sorting with `itemgetter()`](#example-sorting-with-itemgetter)
    - [Example: Accessing Attributes with `attrgetter()`](#example-accessing-attributes-with-attrgetter)
  - [Closures](#closures)
    - [How Python Manages Closures: Cell Objects](#how-python-manages-closures-cell-objects)
    - [Closures with State](#closures-with-state)
    - [Practical Use Cases of Closures](#practical-use-cases-of-closures)
  - [Decorators](#decorators)

## Introduction

Functions are defined using the `def` keyword. A function can have positional arguments (`*args`), keyword arguments (`**kwargs`), default values, variable-length arguments, and keyword-only arguments.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob", "Hi"))  # Output: Hi, Bob!
```

- `name` and `message` are the **parameters** of the `greet` function.
  - Parameters are variables, local to their function.
- `"Alice"`, `"Bob"`, and `"Hi"` are the **arguments** that get passed to `greet` in this example.

## Argument Passing

- Python does not implement **pure** pass-by-value or pass-by-reference.
- Arguments are passed as references to objects.
  - The function receives a reference to the same object in memory.
- Mutability determines behaviour.
  - If the object is mutable, modifications within the function can affect the original object.
  - If the object is immutable, the function cannot alter the original object.

### Positional and Keyword Arguments

- The most common way of assigning arguments to parameters is using the *order* that the arguments are passed.
- A positional argument can be made optional by specifying a *default value* using `=`.
  - Parameters *without* a default value **cannot** be defined **after** parameters *with* a default value.
- Keyword arguments (named arguments) can be specified by using the parameter name with `=`, regardless of position and default argument.
  - Named arguments **cannot** be defined **after** unnamed arguments.

```python
def my_func(a, b, c = 100, d = 4):
    print(f"a={a} b={b} c={c} d={d}")

my_func(10, 20) # a=10 b=20 c=100 d=4
my_func(20, 10, 200) # a=20 b=10 c=200 d=4
my_func(20, b=10, d=10) # a=20 b=10 c=100 d=10
my_func(1, c=20, b=2, d=10) # a=1 b=2 c=20 d=10
```

### Positional-Only Arguments (`/`)

- Introduced in Python 3.8, the `/` in a function signature defines **positional-only** parameters.
- Parameters before `/` must be passed by position and cannot be assigned using keywords.

```python
def greet(name, /):
    print(f"Hello, {name}!")

greet("Alice")    # Hello, Alice
greet(name="Bob") # TypeError: greet() got some positional-only arguments passed as keyword arguments: 'name'
```

In the above example, name must be passed as a positional argument.

### `*args` and `**kwargs`

Python provides `*args` and `**kwargs` to handle variable-length arguments in functions.

#### Unpacking with `*` and `**`

- Python allows unpacking iterables (`*`) and dictionaries (`**`) when calling functions.
- See [Extended Unpacking](./python_2_variables.md#extended-unpacking---and--operators) for more details.

```python
def greet(first, last):
    print(f"Hello, {first} {last}!")

name_tuple = ("John", "Doe")
name_dict = {"last": "Doe", "first": "Jane"} # order is irrelevant here

greet(*name_tuple)  # Hello, John Doe!
greet(**name_dict)  # Hello, Jane Doe!
```

#### Using `*args` for Positional Arguments

- `*args` allows a function to accept any number of positional arguments.
- The arguments are passed as a tuple.
- No more positional arguments can be added after `*args`.
- The name `args` is a convention; any other name can be used.

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3))  # 6
print(add_numbers(10, 20))   # 30
```

#### `*args` and Keyword-Only Arguments

Python allows fine-grained control over function parameters using `*args` and the `*` syntax.

##### Mixing `*args` with a Regular Keyword Argument

Here, `*args` collects all positional arguments, but `d` must be passed as a keyword argument.

```python
def func(*args, d):
    print(f"Positional args: {args}")
    print(f"Keyword-only arg d: {d}")

func(1, 2, 3, d=4)  # Works fine
func(d=4)           # Works fine (args will be empty)
func(1, 2, 3, 4)    # TypeError: missing required keyword argument 'd'
```

Explanation:

- `*args` collects all positional arguments, so `d` must be explicitly passed as `d=value`.
- A `TypeError` occurs if `d` is missing or provided as a positional argument.

##### Enforcing Keyword-Only Arguments with `*`

The `*` in the parameter list forces all following arguments to be keyword-only.

```python
def func(*, d):
    print(f"Keyword-only arg d: {d}")

func(d=10)   # Works fine
func(10)     # TypeError: func() takes 0 positional arguments but 1 was given
```

Explanation:

- The `*` in the function signature means no positional arguments are allowed.
- Only explicitly named keyword arguments can be passed to the function.

#### Mixing Positional-Only and Keyword Arguments

- `/` makes `x`, `y` positional-only, meaning they must be passed without using keywords.
- `*` ensures `precision` is keyword-only, requiring explicit assignment.

```python
def divide(x, y, /, *, precision=2):
    return round(x / y, precision)

print(divide(10, 3, precision=4))  # 3.3333
print(divide(10, y=3, precision=4))  # TypeError: divide() got some positional-only arguments passed as keyword arguments: 'y'
```

##### Mixing `*args`, `*`, and Keyword-Only Arguments

- `*` forces all following arguments to be keyword-only.
- `*args` collects extra positional arguments, allowing flexibility.
- Combining `*args` with keyword-only parameters provides better control over function calls.
- When enforcing keyword-only arguments, `*args` allows additional positional arguments, while `*` alone does not.

```python
# a is a required positional argument.
# b is an optional positional argument with a default value of 1.
# * in the parameter list forces d and e to be keyword-only arguments.
# d is required and must be passed explicitly.
# e has a default value of True, so it is optional.
def func_one(a, b=1, *, d, e=True):
    print(f"a: {a}, b: {b}, d: {d}, e: {e}")
  
func_one(1, 2, d=3, e=4)  # a: 1, b: 2, d: 3, e: 4
func_one(1, d=3)          # a: 1, b: 1, d: 3, e: True

# a is a required positional argument.
# b is an optional positional argument with a default value of 1.
# *args collects any additional positional arguments into a tuple.
# d and e are keyword-only arguments (must be passed explicitly as d=value).
# e has a default value of True, making it optional.
def func_two(a, b=1, *args, d, e=True):
    print(f"a: {a}, b: {b}, d: {d}, e: {e}")

func_two(1, 2, 3, 4, d=5, e=6)  # a: 1, b: 2, d: 5, e: 6
func_two(1, d=5)                # a: 1, b: 1, d: 5, e: True
```

#### Using `**kwargs` for Keyword Arguments

- `**kwargs` allows passing any number of keyword arguments.
- The arguments are stored in a dictionary.
- No more keyword arguments can be added after `**kwargs`.
- The name `kwargs` is a convention; any other name can be used.

```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

#### Mixing *args and **kwargs

`*args` must come before `**kwargs` in function definitions.

```python
def example_function(a, b, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"Additional positional args: {args}")
    print(f"Additional keyword args: {kwargs}")

example_function(1, 2, 3, 4, name="Alice", age=25)
# a: 1, b: 2
# Additional positional args: (3, 4)
# Additional keyword args: {'name': 'Alice', 'age': 25}
```

#### Advanced Argument Mixing

Python allows mixing regular arguments, `*args`, `*`, and `**kwargs` in function definitions.

```python
def example_function_one(a, b, *args, c, d=4, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    print(f"Additional positional args: {args}")
    print(f"Additional keyword args: {kwargs}")

example_function_one(1, 2, 3, 4, c=5, d=6, name="Alice", age=25)
# a: 1, b: 2, c: 5, d: 6
# Additional positional args: (3, 4)
# Additional keyword args: {'name': 'Alice', 'age': 25}

def example_function_two(a, b, *, c, d=4, **kwargs):
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    print(f"Additional keyword args: {kwargs}")

example_function_two(1, 2, c=5, d=6, name="Alice", age=25)
# a: 1, b: 2, c: 5, d: 6
# Additional keyword args: {'name': 'Alice', 'age': 25}
```

#### Typical Usages of `*args` and `**kwargs`

- Allows subclasses to accept additional parameters while calling the parent class.
  - Inheritance with flexible arguments.

  ```python
  class Animal:
      def __init__(self, name, **kwargs):
          self.name = name
          self.attributes = kwargs

  class Dog(Animal):
      def __init__(self, name, breed, **kwargs):
          super().__init__(name, **kwargs)
          self.breed = breed

  dog = Dog("Buddy", "Labrador", age=3, vaccinated=True)
  print(dog.name, dog.breed, dog.attributes) # Buddy Labrador {'age': 3, 'vaccinated': True}
  ```

- Applications often interact with multiple data providers. `*args` and `**kwargs` help standardize API requests.
  - Allows functions to accept additional parameters without changing the function signature.Works with multiple data vendors (Bloomberg, Reuters, Interactive Brokers).
  - Allows additional API parameters without hardcoding them.

  ```python
  def fetch_market_data(symbol, *args, source="Bloomberg", **kwargs):
      print(f"Fetching {symbol} data from {source}.")
      print("Additional filters:", args)
      print("API parameters:", kwargs)

  fetch_market_data("EUR/USD", "intra-day", timeframe="1h", source="Reuters", adjust_for_dividends=True)
  # Fetching EUR/USD data from Reuters.
  # Additional filters: ('intra-day',)
  # API parameters: {'timeframe': '1h', 'adjust_for_dividends': True}
  ```

### Passing Immutable Objects as Arguments (Pass-by-Value-like Behaviour)

- When an immutable object is passed to a function, the object itself cannot be modified.
- Any attempt to alter it results in creating a new object.

```python
def modify_immutable(x):
    x += 10  # Creates a new integer object
    print("Inside function:", x)

value = 5
modify_immutable(value)
print("Outside function:", value)  # Original integer remains unchanged

# Output:
# Inside function: 15
# Outside function: 5
```

The variable `x` inside the function refers to a new integer, leaving the original value untouched.

### Passing Mutable Objects as Arguments (Pass-by-Reference-like Behaviour)

When a mutable object is passed, modifications to the object inside the function affect the original object.

```python
def modify_mutable(lst):
    lst.append(4)  # Modifies the original list
    print("Inside function:", lst)

my_list = [1, 2, 3]
modify_mutable(my_list)
print("Outside function:", my_list)  # Original list is modified

# Output:
# Inside function: [1, 2, 3, 4]
# Outside function: [1, 2, 3, 4]
```

The function operates on the same list object, so changes are reflected outside the function.

### Reassignment of Arguments

Reassigning an argument within a function does not affect the original object because the reassignment **only** changes the **local** reference.

```python
def reassign_argument(lst):
    lst = [4, 5, 6]  # Reassignment creates a new local reference
    print("Inside function:", lst)

my_list = [1, 2, 3]
reassign_argument(my_list)
print("Outside function:", my_list)  # Original list remains unchanged

# Output:
# Inside function: [4, 5, 6]
# Outside function: [1, 2, 3]
```

### Behaviour of Mutable Default Arguments

Mutable default arguments can lead to unexpected behaviour, as they are shared across function calls.

```python
# Incorrect implementation
def append_to_list(value, lst=[]):
    lst.append(value)  # Modifies the shared default list
    return lst

result1 = append_to_list(1)
result2 = append_to_list(2)
print(result1)  # [1, 2]
print(result2)  # [1, 2]
```

- `lst` is initialized as an empty list only once, during the function definition.
- Subsequent calls to `append_to_list` modify the same list object in memory, leading to unexpected results.

Use `None` as a placeholder and create a new instance of the mutable type inside the function.

```python
# Correct implementation:
def append_to_list(value, lst=None):
    if lst is None:
        lst = []  # Creates a new list for each call
    lst.append(value)
    return lst

result1 = append_to_list(1)
result2 = append_to_list(2)
print(result1)  # [1]
print(result2)  # [2]
```

- By using `None` as the default and creating a new list if `lst` is `None`, the function ensure that each call operates on its own independent list.
- This avoids the shared state problem.

### Behaviour of Dynamic Default Arguments

- Functions' default arguments are evaluated once when the modules is imported, not at each function call.
- This can lead to unintended behaviour when using mutable or dynamic default arguments.

```python
# Incorrect implementation
from datetime import datetime

def log_message(message: str, *, timestamp=datetime.utcnow()):  # Evaluated once at definition
    print(f"{timestamp}: {message}")

log_message("First log")  # Logs the same timestamp for every call
log_message("Second log")  # Still uses the old timestamp
```

- `datetime.utcnow()` is evaluated when the function is defined, not when it's called.
- Calls to `log_message()` without timestamp use the same stale value.

Use `None` as a placeholder and assign the value inside the function.

```python
# Correct implementation
def log_message(message: str, *, timestamp=None):  # Fresh value per call
    timestamp = timestamp or datetime.utcnow()  
    print(f"{timestamp}: {message}")

log_message("First log")  # Correctly logs the actual current timestamp
log_message("Second log")  # Uses a fresh timestamp
```

## Function Annotations

- Function annotations are a way to attach metadata to the parameters and return value of a function.
- These annotations do not affect the function's behaviour but provide additional information about the types of arguments or the return value.
- They are often used for documentation purposes, type checking, and to improve code readability.

### Function Annotation Syntax

Function annotations are written using a colon (`:`) after the parameter name for argument annotations, and an arrow (`->`) after the parameter list for return value annotations.

```python
def example_function(a: int, b: float, name: "Name for the output" = "Output") -> str:
    return f"{name} is {a + b}"

print(example_function(5, 10.5))  # Output: Output is 15.5
```

- `a: int` means the argument `a` is expected to be an integer.
- `b: float` means the argument `b` is expected to be a float.
- `name: "Name for the output" = "Output"` Annotations can be combined with default parameter values.
- `-> str` indicates that the function is expected to return a string.

Function annotations are not enforced at runtime.

- Python does not check whether the function arguments match their annotations.
- They are primarily used for documentation or by external tools (e.g., linters, type checkers like `mypy`).

```python
def divide(a: int, b: int) -> float:
    return a / b

# No error if 'b' is passed as a string
divide(5, "10")  # The program will run without error, but this is not recommended
```

### Accessing Annotations

- Function annotations are stored in the `__annotations__` attribute, which is a dictionary.
- This allows access to the annotations programmatically.

```python
def my_func(x: int, y: float) -> str:
    return str(x + y)

print(my_func.__annotations__)
# Output: {'x': <class 'int'>, 'y': <class 'float'>, 'return': <class 'str'>}
```

### Typing Module and Advanced Annotations

- The `typing` module allows more complex annotations, such as:
  - `Union`: To specify that a value could be one of multiple types.
  - `Optional`: A shorthand for `Union[X, None]`.
  - `Callable`: For annotating function signatures.
  - `List`, `Dict`, `Tuple`: For generic collections.

```python
from typing import Union, List

def process_data(data: Union[int, float]) -> str:
    return f"Processed: {data}"

def sum_values(numbers: List[int]) -> int:
    return sum(numbers)

def add(a: int, b: int) -> int:
    return a + b
```

`Callable` can be used to annotate function parameters or return types that are functions themselves.

```python
from typing import Callable

def apply_func(func: Callable[[int], int], value: int) -> int:
    return func(value)
```

In this example, `func` is expected to be a callable that takes an integer and returns an integer.

#### Expression Function Annotations

- Expression function annotations allow the use of arbitrary expressions as annotations rather than just simple types or classes.
- This is particularly useful for adding more dynamic or computed annotations, which might depend on the context or other factors.
- An expression can be anything from a constant value to a more complex expression (e.g., the result of a function or a mathematical calculation).

```python
def example(x: 2 + 3) -> int:
    return x * 2
```

In this case, the annotation `2 + 3` is an expression, and it evaluates to `5`, meaning the parameter `x` is annotated as `5`.

```python
from datetime import datetime

# Incorrect use of a expression function annotation
def log_event(event: str, timestamp: datetime = datetime.now()) -> str:
    return f"{event} occurred at {timestamp}"
```

Expression annotations are evaluated when the function is defined, not when it is called, similar to default arguments.

## Lambda Functions

- A *lambda function* is an anonymous (unnamed) function defined using the `lambda` keyword.
- It is often used for short, simple functions where defining a full function using `def` is unnecessary.
- Lambda functions are of type `function`.

```python
lambda parameter: expression
```

- A `lambda` function can have multiple parameters but only one expression.
- The colon, `:`, is needed even with zero parameters.
- The expression is evaluated and returned automatically (no need for `return`).
- Type annotations and assignments are not allowed in lambda functions.

```python
# takes two arguments x and y, and returns their sum.
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8

# A lambda function that squares its input.
square = lambda x: x**2
print(square(4))  # Output: 16

# A lambda function that checks if a number is even.
is_even = lambda x: x % 2 == 0
print(is_even(10))  # Output: True

# Annotations and assignments are not allowed in lambda functions.
lambda x: int : x*2 # SyntaxError: illegal target for annotation
lambda x : x = x + 5 # SyntaxError: cannot assign to lambda
```

### Using Lambda Functions with Built-in Functions

- `map()`: Apply a function to each element in an iterable.

    ```python
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, numbers))
    print(squared)  # Output: [1, 4, 9, 16, 25]
    ```

- `filter()`: Filter elements based on a condition.

    ```python
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(even_numbers)  # Output: [2, 4]
    ```

- `sorted()`: Sort based on a key function.

    ```python
    # The lambda p: p[1] extracts the second element of each tuple for sorting.
    points = [(2, 3), (1, 4), (5, 1)]
    sorted_points = sorted(points, key=lambda p: p[1])  # Sort by second element
    print(sorted_points)  # Output: [(5, 1), (2, 3), (1, 4)]

    # The lambda student: student["age"] extracts the "age" key for sorting.
    students = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 22},
        {"name": "Charlie", "age": 23}
    ]
    sorted_by_age = sorted(students, key=lambda student: student["age"])
    print(sorted_by_age)
    # Output:
    # [{'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
    ```

### `lambda` versus `def` Functions

| Feature                | `lambda` function                     | `def` function                  |
|------------------------|---------------------------------------|---------------------------------|
| Name                   | Anonymous (or assigned to a variable) | Has a name                      |
| Number of expressions  | Only one                              | Multiple expressions/statements |
| Readability            | Best for short operations             | Preferred for complex logic     |
| Can contain `return`?    | No (implicit return)                  | Yes                             |

### When to Use Lambda Functions

- When defining quick, simple functions.
- When using higher-order functions like `map()`, `filter()`, and `sorted()`.
- When defining one-time use functions that don't need a formal function name.

### When to Avoid Lambda Functions

- When the function contains multiple expressions or complex logic.
- When readability is compromised.
- When debugging, as lambda functions don't have names in error messages.

## Function Introspection

- Function introspection refers to examining function attributes at runtime. Python provides built-in attributes and modules such as `inspect` to retrieve metadata about functions, their parameters, annotations, and more.
- Common use cases of function introspection include:
  - **Debugging**: Retrieve function signatures and annotations dynamically.
  - **Meta-programming**: Modify or analyze functions at runtime.
  - **API Development**: Validate arguments dynamically.
  - **Documentation**: Extract function docstrings and annotations.

### Basic Function Attributes

Python functions are objects, and they have built-in attributes that store useful metadata.

| Attribute         | Description                                              |
|-------------------|----------------------------------------------------------|
| `__name__`        | Name of the function                                     |
| `__doc__`         | Docstring of the function                                |
| `__annotations__` | Dictionary of parameter and return annotations           |
| `__defaults__`    | Tuple of default argument values                         |
| `__kwdefaults__`  | Dictionary of default values for keyword-only arguments  |
| `__code__`        | `code` object containing function's bytecode and metadata  |
| `__dict__`        | Dictionary for storing function attributes dynamically   |

### Accessing Function Attributes

Built-in attributes can be accessed using the dot notation.

```python
def add(a: int, b: int = 10) -> int:
    """Returns the sum of two numbers."""
    return a + b

print(add.__name__)         # 'add'
print(add.__doc__)          # 'Returns the sum of two numbers.'
print(add.__annotations__)  # {'a': <class 'int'>, 'b': <class 'int'>, 'return': <class 'int'>}
print(add.__defaults__)     # (10,)
```

`dir()` is a built-in function that will return a list of valid attributes for an object

```python
print(dir(add))
# ['__annotations__',
#  '__builtins__',
#  '__call__',
#  '__class__',
#  '__closure__',
#  '__code__',
#  '__defaults__',
#  '__delattr__',
#  '__dict__',
#  '__dir__', etc. etc.
```

### Creating Function Attributes

Custom function attributes can be created dynamically.

```python
def my_func(a, b):
    return a + b

my_func.category = 'math'  # Add a new attribute to the function
my_func.sub_category = 'arithmetic'

print(my_func.category)  # math
print(my_func.sub_category)  # arithmetic
```

### Inspecting Function Signature (`inspect` module)

The `inspect` module provides powerful tools for *introspecting* function signatures.

```python

import inspect

def example(x: int, y: float = 3.5, *args, z: str = "default", **kwargs) -> bool:
    pass

# Getting Function Signature
sig = inspect.signature(example)
print(sig)
# (x: int, y: float = 3.5, *args, z: str = 'default', **kwargs) -> bool

# Accessing Individual Parameters
for name, param in sig.parameters.items():
    print(f"{name}: {param.kind}, default={param.default}, annotation={param.annotation}")

# x: POSITIONAL_OR_KEYWORD, default=<class 'inspect._empty'>, annotation=<class 'int'>
# y: POSITIONAL_OR_KEYWORD, default=3.5, annotation=<class 'float'>
# args: VAR_POSITIONAL, default=<class 'inspect._empty'>, annotation=<class 'inspect._empty'>
# z: KEYWORD_ONLY, default=default, annotation=<class 'str'>
# kwargs: VAR_KEYWORD, default=<class 'inspect._empty'>, annotation=<class 'inspect._empty'>
```

| Parameter Kind          | Description                                                   |
|-------------------------|---------------------------------------------------------------|
| POSITIONAL_OR_KEYWORD   | Can be passed as a positional or keyword argument.            |
| VAR_POSITIONAL (*args)  | Collects extra positional arguments.                          |
| KEYWORD_ONLY            | Must be passed as a keyword argument.                         |
| VAR_KEYWORD (**kwargs)  | Collects extra keyword arguments.                             |
| POSITIONAL_ONLY         | Can only be passed as a positional argument, not by keyword.  |

#### Retrieving Source Code & Bytecode using `inspect` and `dis`

Python allows extracting the function's source code and compiled bytecode.

```python
def add(a: int, b: int = 10) -> int:
    """Returns the sum of two numbers."""
    return a + b

#Getting Function Source Code
import inspect
print(inspect.getsource(add))
# def add(a: int, b: int = 10) -> int:
#     """Returns the sum of two numbers."""
#     return a + b

# Getting Function Bytecode
import dis
dis.dis(add)
#  2           0 LOAD_FAST                0 (a)
#              2 LOAD_FAST                1 (b)
#              4 BINARY_ADD
#              6 RETURN_VALUE
```

### Checking If an Object Is a Function

- `callable(obj)`: Checks if an object can be called like a function (e.g., functions, lambdas, and objects with `__call__` method).
- `isinstance(obj, types.FunctionType)`: Specifically verifies if an object is a function (excluding classes and callable objects).
- `inspect.isfunction(obj)`: Checks if an object is a function.
- `inspect.ismethod(obj)`: Checks if an object is a method.

```python
import types
import inspect

def add(a: int, b: int = 10) -> int:
    """Returns the sum of two numbers."""
    return a + b

print(callable(add))  # True
print(isinstance(add, types.FunctionType))  # True


print(inspect.isfunction(add))  # True
print(inspect.ismethod(add))  # False
```

## Built-In Functions

- Python provides several built-in functions to work with iterables in a functional style.
- `map()`, `zip()`, and `filter()` allow iterables to be processed or combined in a more concise and efficient way than using traditional loops.

| Function | Purpose                                                | Return Type | Example Use Case                                                                 |
|----------|--------------------------------------------------------|-------------|----------------------------------------------------------------------------------|
| `map()`  | Applies a function to all items in an iterable         | Iterator    | Transforming each element of an iterable (e.g., squaring numbers)                |
| `zip()`  | Combines multiple iterables into tuples                | Iterator    | Pairing items from two or more iterables (e.g., combining names and ages)        |
| `filter()`| Filters items from an iterable based on a condition   | Iterator    | Removing elements that do not satisfy a condition (e.g., filtering even numbers) |

- Often more memory efficient than using explicit `for` loops, especially when working with large datasets, because they return iterators instead of creating a full list in memory.
- Support a functional style of programming, where transformations or filters are applied to iterables in a declarative manner.
- Since these functions return iterators, you often need to convert them to a `list` (or other collection types) to use their results.

### `map()`

`map(func, *iterables)` applies a given function (`func`) to all items in a variable number of `iterables` (such as lists or tuples), and returns a `map` object (an iterator) that yields the results.

```python
# Applying a function to square numbers
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x ** 2, numbers)
print(list(squares))  # Output: [1, 4, 9, 16, 25]
```

The returned `map` object (an iterator) must be converted to a `list` or another iterable type to access its values (using `list()` or `tuple()`).

```python
# Adding corresponding elements from two lists
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [5, 7, 9]
```

The iterator stops as soon as one of the iterables has been exhausted - i.e. the shortest iterable determines the length of the resulting map.

```python
# Adding corresponding elements from two lists
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [9, 8, 7]
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))  # Output: [10, 10, 10]
```

### `zip()`

`zip(*iterables, strict=False)` combines multiple `iterables` element-wise into tuples, creating an iterator of tuples where each tuple contains the elements at the same position from each iterable.

```python
Copy
Edit
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
combined = zip(names, ages)
print(list(combined))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

- `zip()` stops when the shortest iterable is exhausted.
- To zip iterables of different lengths and keep the longer ones intact, use `itertools.zip_longest()` from the `itertools` module.
- Like `map()`, `zip()` returns an iterator, so the result will need converting to a `list` or another iterable to process the values.

```python
# Zipping three iterables
names = ['Alice', 'Bob', 'Dave']
scores = [90, 85]
subjects = ['Math', 'Science']
combined = zip(names, scores, subjects)
print(list(combined))  # Output: [('Alice', 90, 'Math'), ('Bob', 85, 'Science')]
```

#### Using `zip()` with List Comprehensions

`zip()` is especially useful in [list comprehensions](./python_1_style_syntax.md#list-comprehension) for efficiently iterating over multiple iterables at once. It helps in element-wise operations, such as combining, transforming, or filtering paired elements from different lists.

```python
# Creating a Dictionary from Two Lists
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Using zip() inside a dictionary comprehension
person = {key: value for key, value in zip(keys, values)}
print(person)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}


# Pairwise Element Operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Element-wise sum using list comprehension and zip()
sums = [x + y for x, y in zip(list1, list2)]
print(sums)  # Output: [5, 7, 9]
```

### `filter()`

`filter(function or None, iterable)` filters elements from a single `iterable` based on a given `function` that takes a single argument. It returns a `filter` object, which is an iterator of the items that evaluate to `True` (truthy) when passed to the function.

```python
# Filtering even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))  # Output: [2, 4, 6]
```

- If the function is `None`, `filter()` will remove all elements that are "falsy" (e.g., `None`, `False`, `0`, `""` etc.).
- As with map() and zip(), filter() returns an iterator, so you'll need to convert it to a list or another iterable type to view the result.

```python
# Filtering out all falsy values from a list
values = [0, '', 'Hello', None, True]
non_falsy = filter(None, values)
print(list(non_falsy))  # Output: ['Hello', True]
```

#### Using List Comprehension with `if` Instead of `filter()`

List comprehensions can replace `filter()` by incorporating an `if` condition directly.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Using filter()
even_numbers_filter = list(filter(lambda x: x % 2 == 0, numbers))

# Equivalent List Comprehension
even_numbers_lc = [x for x in numbers if x % 2 == 0] # Avoids the need for lambda functions.

print(even_numbers_filter)  # Output: [2, 4, 6]
print(even_numbers_lc)      # Output: [2, 4, 6]
```

## Reducing Functions (`functools.reduce`)

Reducing functions combine an iterable recursively into a single result. The most common reducing function in Python is `functools.reduce()`.

```python
functools.reduce(function, iterable[, initial])
```

- Applies a `function` cumulatively to the items of the `iterable`.
- The `function` must take exactly 2 positional arguments.
- Starts by applying the `function` to the first two elements of the `iterable` to get the first *result*, then applies the `function` again to the *result* and the *next element*, and so on.
- If `initial` is provided, it is placed before the items of the `iterable` in the calculation, and serves as a default when the    `iterable` is empty.

Example: Sum of a List

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce() to compute the sum
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15 ((((1+2)+3)+4)+5)
```

Example: Finding the Maximum Value

```python
from functools import reduce

values = [3, 7, 2, 9, 5]

max_value = reduce(lambda x, y: x if x > y else y, values)
print(max_value)  # Output: 9
```

Example: Factorial Using Reduce

```python
from functools import reduce

factorial = reduce(lambda x, y: x * y, range(1, 6))
print(factorial)  # Output: 120 (1 * 2 * 3 * 4 * 5)
```

Example: Using `initial` Argument

```python
from functools import reduce

values = [1, 2, 3, 4, 5]
value = reduce(lambda x, y: x + y, values, 10) # will start with 10
print(value)  # Output: 25 (10 + 1 + 2 + 3 + 4 + 5)
```

### Built-in Reducing Functions in Python

Python has several built-in reducing functions that perform common reduction tasks efficiently.

#### `sum()`: Summation of Elements

Computes the sum of all elements in an iterable.

```python
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)  # Output: 15
```

Equivalent to:

```python
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
```

#### `max()`: Maximum Value

Finds the largest element in an iterable.

```python
values = [10, 20, 5, 40, 15]
largest = max(values)
print(largest)  # Output: 40
```

Equivalent to:

```python
from functools import reduce
largest = reduce(lambda x, y: x if x > y else y, values)
```

#### `min()`: Minimum Value

Finds the smallest element in an iterable.

```python
values = [10, 20, 5, 40, 15]
smallest = min(values)
print(smallest)  # Output: 5
```

Equivalent to:

```python
from functools import reduce
smallest = reduce(lambda x, y: x if x < y else y, values)
```

#### `any()`: Checks for At Least One True Value

Returns `True` if any element in the iterable evaluates to `True`.

```python
booleans = [False, False, True, False]
result = any(booleans)
print(result)  # Output: True
```

Equivalent to:

```python
from functools import reduce
result = reduce(lambda x, y: x or y, booleans)
```

#### `all()`: Checks If All Values Are True

Returns `True` if all elements in the iterable evaluate to `True`.

```python
booleans = [True, True, False, True]
result = all(booleans)
print(result)  # Output: False
```

Equivalent to:

```python
from functools import reduce
result = reduce(lambda x, y: x and y, booleans)
```

#### `str.join()`: Concatenates Strings

Joins a sequence of strings into a single string.

```python
words = ["Hello", "world", "!"]
sentence = " ".join(words)
print(sentence)  # Output: "Hello world !"
```

Equivalent to:

```python
from functools import reduce
sentence = reduce(lambda x, y: x + " " + y, words)
```

## Partial Functions (`functools.partial`)

- Partial functions allow fixing some arguments of a function, creating a new function with fewer parameters.
  - In other words, they provide interfaces to functions with some arguments pre-filled.
- Custom partial functions can be defined as follows:

```python
def my_func(a, b, c):
    return a + b + c

# partial function
def fn(b, c):
    return my_func(10, b, c)

print(fn(20, 30))  # Output: 60

# lambda partial function
f = lambda b, c: my_func(10, b, c)
print(f(20, 30))  # Output: 60
```

Alternatively, the `functools.partial` function can be used to create partial functions more concisely.

- Creates a function with pre-filled arguments.
- Returns a new `function` object.
- `functools.partial(function, *args, **kwargs)`

```python
def my_func(a, b, c):
    return a + b + c

f = functools.partial(my_func, 10) # 10 passed as first positional argument (a)

print(f(20, 30))  # Output: 60
```

Example: Fixing Base for `int()`

```python
from functools import partial

# Create a function to convert binary strings to integers
binary_to_int = partial(int, base=2)

print(binary_to_int("1010"))  # Output: 10
print(binary_to_int("1111"))  # Output: 15
```

Example: Using `partial` with `sorted()`

```python
from functools import partial

data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sort_by_age = partial(sorted, key=lambda x: x[1])

print(sort_by_age(data))  
# Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```

## `operator` Module

The `operator` module provides function equivalents of standard operators, making functional programming cleaner and often faster.

| Operator | Function Equivalent | Example |
|----------|---------------------|---------|
| `+`      | `operator.add`      | `add(3, 5)` → `8` |
| `-`      | `operator.sub`      | `sub(10, 4)` → `6` |
| `*`      | `operator.mul`      | `mul(3, 4)` → `12` |
| `/`      | `operator.truediv`  | `truediv(8, 2)` → `4.0` |
| `//`     | `operator.floordiv` | `floordiv(9, 2)` → `4` |
| `%`      | `operator.mod`      | `mod(10, 3)` → `1` |
| `**`     | `operator.pow`      | `pow(2, 3)` → `8` |
| `==`     | `operator.eq`       | `eq(5, 5)` → `True` |
| `!=`     | `operator.ne`       | `ne(4, 5)` → `True` |
| `<`      | `operator.lt`       | `lt(3, 5)` → `True` |
| `<=`     | `operator.le`       | `le(5, 5)` → `True` |
| `>`      | `operator.gt`       | `gt(5, 3)` → `True` |
| `>=`     | `operator.ge`       | `ge(5, 5)` → `True` |
| `is`     | `operator.is_`      | `is_(a, b)` → `True if a is b` |
| `is not` | `operator.is_not`   | `is_not(a, b)` → `True if a is not b` |
| `and`    | `operator.and_`     | `and_(True, False)` → `False` |
| `or`     | `operator.or_`      | `or_(True, False)` → `True` |
| `not`    | `operator.not_`     | `not_(True)` → `False` |

Other Useful operator Functions:

| Function                            | Description                                | Example                                      |
|-------------------------------------|--------------------------------------------|----------------------------------------------|
| `operator.itemgetter(i)`            | Gets item at index `i` (returns `callable`)| `itemgetter(1)([4, 7, 9])` → `7`             |
| `operator.attrgetter(attr)`         | Gets an attribute (returns `callable`)     | `attrgetter('age')(person)` → `person.age`   |
| `operator.methodcaller(m, *args, **kwargs)` | Calls a method on an object | `methodcaller("upper")("hello")` → `"HELLO"` |
| `operator.getitem(obj, key)`        | Gets an item from a collection | `getitem([10, 20, 30], 1)` → `20` |
| `operator.setitem(obj, key, value)` | Sets an item in a collection | `setitem(my_dict, "a", 42)` → `my_dict["a"] = 42` |
| `operator.delitem(obj, key)`        | Deletes an item from a collection | `delitem(my_list, 2)` → `del my_list[2]` |

### Using `operator.add` with `reduce()`

```python
from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]

# Equivalent to reduce(lambda x, y: x + y, numbers)
result = reduce(operator.add, numbers)
print(result)  # Output: 15
```

### Example: Sorting with `itemgetter()`

```python
from operator import itemgetter

data = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]

# Sort by second item (age)
sorted_data = sorted(data, key=itemgetter(1))
print(sorted_data)  
# Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
Example: Accessing Attributes with attrgetter()
```

### Example: Accessing Attributes with `attrgetter()`

```python
from operator import attrgetter

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 25), Person("Bob", 30), Person("Charlie", 20)]

# Sort by age
sorted_people = sorted(people, key=attrgetter("age"))
print([(p.name, p.age) for p in sorted_people])
# Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```

## Closures

- A *closure* is a function that retains access to variables from its enclosing lexical [scope](./python_1_style_syntax.md#scope), even after the enclosing function has finished executing.
  - Closures are created when a nested function captures and remembers variables from its outer function.
  - If a variable is used in a code block but not defined there, it is a *free variable*.
- A closure consists of:
  1. An enclosing function that defines variables.
  2. A nested function that captures and uses those variables.
  3. The nested function is returned, keeping access to the enclosing variables.

```python
def outer_function(msg):
    greeting = f"Hello {msg}"  # Enclosing variable
    def inner_function():
        print(greeting)  # Bound to 'greeting' from outer_function (free variable)
    return inner_function  # Returns inner function as a closure

closure = outer_function("Python")
closure()  # Output: Hello Python
```

- `inner_function` retains access to `greeting` even after `outer_function` has executed.
- The value of `greeting` is shared between two scopes:
  - It exists in `outer_function`, but `inner_function` continues referencing it.

### How Python Manages Closures: Cell Objects

Python does not copy the enclosing variables into the inner function. Instead, it creates an intermediary cell object to store references to those variables.

```python
def outer():
    x = "Hello"  # Enclosing variable
    y = 10  # Enclosing variable

    def inner():
        print(x)  # Accesses 'x' via a cell object
        print(y)  # Accesses 'y' via a cell object

    return inner

closure_func = outer()
print(closure_func.__closure__)  
# Output: (<cell at 0x...: str object at 0x...>, <cell at 0x...: int object at 0x...>)

print(closure_func.__closure__[0].cell_contents)
print(closure_func.__closure__[1].cell_contents)
# Output:
# Hello
# 10
```

- `__closure__` holds one or more cell objects, each referencing an enclosed variable.
- The inner function references this cell object rather than directly accessing `x`.
- This mechanism allows closures to retain access to variables even after the enclosing function has returned.

```python
def outer():
    a = "Hello" # not part of the closure
    x = 10  # Enclosing variable

    def inner():
        print(x)  # Accesses 'x' via a cell object

    return inner

closure_func = outer()
print(closure_func.__closure__)  
# Output: (<cell at 0x...: int object at 0x...>,)

print(closure_func.__closure__[0].cell_contents)
# Output: 10
```

- `a` is not part of the closure because it is not used in the inner function.
- Hence, only `x` is stored in the cell object.

### Closures with State

Closures can maintain state across multiple calls and share the extended scope.

```python
def counter():
    count = 0  # Enclosing variable

    def increment():
        nonlocal count  # Modify the free variable with nonlocal
        count += 1
        return count

    def decrement():
        nonlocal count  # Modify the same free variable
        count -= 1
        return count

    return increment, decrement

increment, decrement = counter()
print(increment())  # Output: 1
print(increment())  # Output: 2
print(decrement())  # Output: 1
```

- `increment` remembers the value of `count` between calls.
- `nonlocal` allows modifying the `count` variable from the enclosing scope.
- `increment` and `decrement` share the same `count` variable.

### Practical Use Cases of Closures

**Function factory**: closures can be used to generate functions dynamically.

```python
def power(exponent):
    def calculate(base):
        return base ** exponent  # Captures exponent from outer function
    return calculate

square = power(2)
cube = power(3)

print(square(4))  # Output: 16
print(cube(2))    # Output: 8
```

**Replacing simple classes**: closures can replace simple classes that maintain state.

```python
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def multiply(self, x):
        return x * self.factor

double = Multiplier(2)
triple = Multiplier(3)

print(double.multiply(5))  # Output: 10
print(triple.multiply(5))  # Output: 15

# Equivalent using closures
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15
```

## Decorators

- A *decorator* is a function that takes another function, method, or class as input and extends or modifies its behaviour without altering its code.
- Defined using `@decorator_name` syntax before a function, method, or class definition.
- Commonly used for logging, access control, memoization, and more.
- Since decorators return modified functions, methods, or classes, they demonstrate Python’s ability to treat these as first-class objects.
- For a deeper dive, see the [Decorators section](./python_5_decorators.md).
