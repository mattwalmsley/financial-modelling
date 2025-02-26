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
    - [Behaviour of Default Mutable Arguments](#behaviour-of-default-mutable-arguments)

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
Copy
Edit
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

### Behaviour of Default Mutable Arguments

Default mutable arguments can lead to unexpected behaviour, as they are shared across function calls.

```python
# Poor implementation
def append_to_list(value, lst=[]):
    lst.append(value)  # Modifies the shared default list
    return lst

result1 = append_to_list(1)
result2 = append_to_list(2)
print(result1)  # [1, 2]
print(result2)  # [1, 2]

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
