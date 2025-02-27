# Python Functions

- [Python Functions](#python-functions)
  - [Introduction](#introduction)
  - [Argument Passing](#argument-passing)
    - [Positional and Keyword Arguments](#positional-and-keyword-arguments)
    - [`*args` and `**kwargs`](#args-and-kwargs)
      - [Unpacking with `*` and `**`](#unpacking-with--and-)
      - [Using `*args` for Positional Arguments](#using-args-for-positional-arguments)
      - [`*args` and Keyword-Only Arguments](#args-and-keyword-only-arguments)
        - [Mixing `*args` with a Regular Keyword Argument](#mixing-args-with-a-regular-keyword-argument)
        - [Enforcing Keyword-Only Arguments with `*`](#enforcing-keyword-only-arguments-with-)
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

  fetch_market_data("EUR/USD", "intraday", timeframe="1h", source="Reuters", adjust_for_dividends=True)
  # Fetching EUR/USD data from Reuters.
  # Additional filters: ('intraday',)
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
