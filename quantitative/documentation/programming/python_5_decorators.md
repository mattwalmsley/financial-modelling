# Decorators

- [Decorators](#decorators)
  - [Introduction](#introduction)
  - [Function-Based Decorators](#function-based-decorators)
    - [Preserving Function Metadata (`__name__`, `__doc__`)](#preserving-function-metadata-__name__-__doc__)
    - [Decorating Classes](#decorating-classes)
    - [Decorating Methods](#decorating-methods)
      - [The `@property` Decorator](#the-property-decorator)
      - [`@classmethod` and `@staticmethod` Decorators](#classmethod-and-staticmethod-decorators)
  - [Class-Based Decorators](#class-based-decorators)
    - [Class-Based Class Decorators](#class-based-class-decorators)
  - [Stacking Multiple Decorators](#stacking-multiple-decorators)
  - [Memoization with Decorators](#memoization-with-decorators)
    - [Using `functools.lru_cache`for Memoization](#using-functoolslru_cachefor-memoization)
  - [Decorator Parameters](#decorator-parameters)
  - [Dispatching](#dispatching)
    - [Single Dispatch (Type-Based Dispatching)](#single-dispatch-type-based-dispatching)
    - [Multi Dispatch (Multiple Argument Type-Based Dispatching)](#multi-dispatch-multiple-argument-type-based-dispatching)
    - [Value-Based Dispatching](#value-based-dispatching)
    - [Method Dispatching in Class Decorators](#method-dispatching-in-class-decorators)
    - [Summary of Dispatching Methods in Decorators](#summary-of-dispatching-methods-in-decorators)
  - [Dispatching with Metaclasses](#dispatching-with-metaclasses)
    - [Type-Based Dispatching in a Metaclass](#type-based-dispatching-in-a-metaclass)
      - [Advantages of Dispatching with Metaclasses](#advantages-of-dispatching-with-metaclasses)
    - [Value-Based Dispatching with Metaclasses](#value-based-dispatching-with-metaclasses)
      - [Advantages of Value Dispatching with Metaclasses](#advantages-of-value-dispatching-with-metaclasses)

## Introduction

Decorators are a powerful feature in Python that modify the behaviour of functions, classes or methods. They are often used to add functionality to existing code in a clean and readable way.

- **Function Decorators**: Used to modify or enhance functions.
- **Class Decorators**: Used to modify or enhance classes.
- **Method Decorators**: Used to modify or enhance methods within a class.

Common notation for decorators is the `@` symbol followed by the decorator class/function name, placed above the function or class to be decorated.

- For a function-based decorator `my_decorator` which decorates `my_func`, the syntax `my_func = my_decorator(my_func)` can be used to decorate the function.
- However the `@` symbol, placed above the object to be decorated, provides a more concise and convenient way to decorate functions.
- Similarly, as described in the [classes as decorators](#class-based-decorators) section, a class `MyDecorator` can be used
  as a decorator by implementing the `__call__` method and placing `@MyDecorator()` above the object to be decorated.

## Function-Based Decorators

- A function-based decorator is a function that takes another function (e.g. `get_greeting`) as an argument for the parameter `func` and returns a closure (`wrapper`) that extends or modifies the behaviour of the original function (`get_greeting`).
- The closure usually accepts any combination of parameters (`*args, **kwargs`), and will call and returns the result of `func`, the original function (`get_greeting`), using the arguments passed to the closure.
- After decoration, calling the original function name (`get_greeting`) will now call the `wrapper` function, allowing additional logic to be executed before and/or after the original function runs.

Example:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result 
    return wrapper

@my_decorator
def get_greeting(name):
    print("Function called, preparing greeting...")
    return f"Hello {name}!"

print(get_greeting("World"))
# Output:
# Something is happening before the function is called.
# Function called, preparing greeting...
# Something is happening after the function is called.
# Hello World!
```

Alternatively, the same effect can be achieved without the need for the `@` symbol by using the following syntax:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result 
    return wrapper

def get_greeting(name):
    print("Function called, preparing greeting...")
    return f"Hello {name}!"

get_greeting = my_decorator(get_greeting)

print(get_greeting("World"))
# Output:
# Something is happening before the function is called.
# Function called, preparing greeting...
# Something is happening after the function is called.
# Hello World!
```

### Preserving Function Metadata (`__name__`, `__doc__`)

Without handling metadata, the decorated function will have the name and docstring of the `wrapper` instead of the original function.

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        """Wrapper function that modifies behaviour of the decorated function."""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result  
    return wrapper  # Returns the closure

@my_decorator
def get_greeting(name):
    """Returns a greeting message."""
    print("Function called, preparing greeting...")
    return f"Hello {name}!"

print(get_greeting("World"))

# Output:
# Something is happening before the function is called.
# Function called, preparing greeting...
# Something is happening after the function is called.
# Hello World!
print(get_greeting.__name__)  # Output: wrapper
print(get_greeting.__doc__)   # Output: Wrapper function that modifies behaviour of the decorated function.
```

Use `functools.wraps(func)` to preserve `__name__` and `__doc__`.

```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        """Wrapper function that modifies behaviour of the decorated function."""
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result  
    return wrapper  # Returns the closure

@my_decorator
def get_greeting(name):
    """Returns a greeting message."""
    print("Function called, preparing greeting...")
    return f"Hello {name}!"

print(get_greeting("World"))

# Output:
# Something is happening before the function is called.
# Function called, preparing greeting...
# Something is happening after the function is called.
# Hello World!
print(get_greeting.__name__)  # Output: get_greeting
print(get_greeting.__doc__)   # Output: Returns a greeting message.
```

The `functools.wraps` function is a decorator itself that takes the original function (`func`) as an argument and copies the metadata from the original function to the closure (`wrapper`).

### Decorating Classes

A class decorator is a function that takes a class as an argument and returns a new class with added or modified behaviour.

```python
def my_class_decorator(cls):
    class WrappedClass(cls):
        def new_method(self):
            return "New method added!"
    return WrappedClass

@my_class_decorator
class MyClass:
    def original_method(self):
        return "Original method"

obj = MyClass()
print(obj.original_method())  # Output: Original method
print(obj.new_method())       # Output: New method added!
```

### Decorating Methods

Method decorators are used to modify or enhance methods within a class and work in the same was as regular function decorators.

#### The `@property` Decorator

The `@property` decorator defines methods in a class that can be accessed like attributes. This is useful for implementing getters and setters in a Pythonic way.

- **Getter**: Use the `@property` decorator to define a method that will be accessed like an attribute.
- **Setter**: Use the `@<property_name>.setter` decorator to define a method that sets the value of the property.
  - Validation can then be implemented when setting the property.

Example:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

person = Person("Alice")

# Accessing the property
print(person.name)  # Output: Alice

# Setting the property
person.name = "Bob"
print(person.name)  # Output: Bob

# Attempting to set an invalid value
try:
    person.name = ""
except ValueError as e:
    print(e)  # Output: Name cannot be empty
```

#### `@classmethod` and `@staticmethod` Decorators

Utility methods related to the class that do not modify its state.

- Class Methods: Use the `@classmethod`decorator.
  - Take the class (`cls`) as the first parameter.
  - Used to modify class-level attributes, create alternative constructors, or provide behaviour tied to the class rather than any instance.
- Static Methods: Use the `@staticmethod` decorator.
  - Do not take `self` or `cls`.
  - Used for utility functions that are logically related to the class but don't require access to instance or class-specific data.

```python
class MathOperations:
    pi = 3.14

    @classmethod
    def circle_area(cls, radius):
        return cls.pi * radius ** 2

    @staticmethod
    def add(a, b):
        return a + b

# Using Class and Static Methods
print(MathOperations.circle_area(5))  # Output: 78.5
print(MathOperations.add(5, 3))       # Output: 8
```

## Class-Based Decorators

A class can be used as a decorator by implementing the `__call__` method. This allows the class instance to behave like a function, modifying the decorated object's behaviour.

```python
import time

class Timer:
    def __init__(self, label):
        self.label = label  # Store a label for the timer

    def __call__(self, func):
        """Makes the class instance callable, turning it into a decorator."""
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)  # Call the original function
            end = time.time()
            print(f"{self.label}: Execution took {end - start:.4f} seconds")
            return result
        return wrapper  # Returns the modified function

@Timer("Sorting Function")  # Equivalent to Timer("Sorting Function").__call__(sort_numbers)
def sort_numbers(numbers):
    return sorted(numbers)

# Calling the decorated function
print(sort_numbers([3, 1, 4, 1, 5, 9, 2, 6]))
# Output (example timing will vary):
# Sorting Function: Execution took 0.0001 seconds
# [1, 1, 2, 3, 4, 5, 6, 9]
```

- `Timer("Sorting Function")` is instantiated, storing `label = "Sorting Function"`.
- When `@Timer("Sorting Function")` is applied, Python calls `Timer("Sorting Function").__call__(sort_numbers)`, which returns `wrapper`.
- Calling `sort_numbers([...])` actually calls `wrapper`, which measures execution time and prints the `result`.

### Class-Based Class Decorators

A class-based decorator can be used to modify another class.

```python
class InstanceWrapper:
    """Class decorator that wraps instances of a class."""
    def __init__(self, cls):
        self.cls = cls  # Stores the original class

    def __call__(self, *args, **kwargs):
        """Intercepts class instantiation and modifies the instance."""
        instance = self.cls(*args, **kwargs)  # Creates an instance
        instance.decorated = True  # Adds a new attribute
        return instance  # Returns the modified instance

@InstanceWrapper
class Car:
    def __init__(self, model):
        self.model = model

c = Car("Ford")
print(c.model)      # Output: Ford
print(c.decorated)  # Output: True
```

- `InstanceWrapper` stores the original class.
- When `Car` is instantiated, `__call__` creates an instance of `Car`, adds an attribute, and returns it.
- The decorated attribute is dynamically added to all `Car` instances.

Alternatively, the `__call__` method on `InstanceWrapper` can be used to modify the `Car` instance directly.

```python
c = InstanceWrapper(Car)("Ford")
print(c.model)      # Output: Ford
print(c.decorated)  # Output: True
```

## Stacking Multiple Decorators

- Multiple decorators can be applied to a single function by stacking them in order, with the topmost decorator being applied first.
- Each decorator wraps the function returned by the decorator below it.

```python
def dec_1(func):
    def wrapper():
        print("Running dec_1")
        return func()
    return wrapper

def dec_2(func):
    def wrapper():
        print("Running dec_2")
        return func()
    return wrapper

@dec_1
@dec_2
def my_func():
    print("Running my_func")

my_func()
# Output:
# Running dec_1
# Running dec_2
# Running my_func
```

The above example is equivalent to:

```python
my_func = dec_1(dec_2(my_func))
```

The order in which the `wrapper` calls `func` in each decorator is also important.

```python
def dec_1(func):
    def wrapper():
        result = func() # result = dec_2(my_func)
        print("Running dec_1")
        return result
    return wrapper

def dec_2(func):
    def wrapper():
        result = func() # result = my_func()
        print("Running dec_2")
        return result
    return wrapper

@dec_1
@dec_2
def my_func():
    print("Running my_func")

my_func()
# Output:
# Running my_func
# Running dec_2
# Running dec_1
```

## Memoization with Decorators

- *Memoization* is an optimization technique that caches function results to avoid redundant computations.
- A decorator can implement memoization by storing previous function calls and their results in a dictionary.
- This is useful for expensive computations, such as recursive functions (e.g., Fibonacci sequences).

```python
import functools

def memoize(func):
    cache = {}  # Dictionary to store computed results

    @functools.wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]  # Return cached result       

    return wrapper

@memoize
def fibonacci(n):
    """Returns the nth Fibonacci number."""

    print("Computing:", n)
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
# Output: 
# Computing: 6
# Computing: 5
# Computing: 4
# Computing: 3
# Computing: 2
# Computing: 1
# Computing: 0
# 8

print(fibonacci(7)) # only computes the new value
# Output:
# Computing: 7
# 13
```

- The `fibonacci` function computes each value once and then retrieves subsequent calls from the cache.
- This reduces time complexity from $O(2^{n})$ to $O(n)$ for recursive functions like `fibonacci`.

### Using `functools.lru_cache`for Memoization

Instead of manually implementing caching, Python provides `functools.lru_cache`, which automates memoization using a *least recently used* style cache.

```python
import functools

@functools.lru_cache(maxsize=None)  # Unlimited cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55
```

Key Benefits of `functools.lru_cache`

- Handles caching automatically—no need for a custom dictionary.
- Supports optional maxsize to limit cache memory usage.
- Thread-safe and optimally manages cache invalidation.

## Decorator Parameters

- Basic decorators apply fixed logic to functions.
- Parameterized decorators allow customization, making them more flexible.
- Example use cases:
  - Logging levels (`@log(level="DEBUG")`)
  - Access control (`@requires_role("admin")`)
  - Function retries (`@retry(max_attempts=3)`)

An alternative approach to using the `@` symbol for parameterized decorators is to use the following syntax:

```python
# Instead of using @repeat(3), a decorator can be applied manually as follows:
import functools

def repeat(func, times):  # Single function taking both the function and parameter
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(times):
            func(*args, **kwargs)
    return wrapper  # Returns the modified function

def greet(name):
    """Greets the user."""
    print(f"Hello, {name}!")

# Manually applying the repeat function
greet = repeat(greet, 3)  # Equivalent to @repeat(3)

greet("Alice")

# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

The `@decorator` syntax requires a callable decorator function that only takes the function as an argument.

- A standard decorator has **two** levels:
  - A *decorator* function that takes func as an argument.
  - A *wrapper* function that modifies func’s behaviour.
- A decorator with parameters has **three** levels:
  - **Outer function (decorator factory):** Accepts parameters for the decorator and returns a decorator.
  - **Middle function (decorator)**: Accepts the function being decorated.
  - **Inner function (wrapper)**: Executes the logic and modifies behaviour.

```python
import functools

def repeat(times):  # Outer function (decorator factory): accepts decorator arguments
    def decorator(func):  # Middle function: accepts the target function
        @functools.wraps(func)
        def wrapper(*args, **kwargs):  # Inner function: modifies behaviour
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator  # repeat (decorator factory) returns the actual decorator

@repeat(3)  # Calls repeat(3), which returns the decorator
def greet(name):
    """Greets the user."""
    print(f"Hello, {name}!")

greet("Alice")

# Execution Flow
# @repeat(3) → Calls repeat(3), returning decorator.
# decorator(greet) → Returns wrapper.
# greet("Alice") → Calls wrapper, which loops times times.

# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

## Dispatching

- *Dispatching* is dynamically selecting and applying different function implementations based on input types, argument values, or other conditions.
- This technique is commonly used in generic functions, method overloading, and dynamic behaviour modification.

### Single Dispatch (Type-Based Dispatching)

- Uses `functools.singledispatch` to select function implementations based on the type of the first argument.
- Registers additional implementations using `@func.register(type)`.
- Ensures type-based function overloading within a single function name.

```python
from functools import singledispatch

@singledispatch
def process(value):
    raise NotImplementedError("Unsupported type")

@process.register(int)
def _(value): # registered function name is not relevant
    return f"Processing integer: {value * 2}"

@process.register(str)
def _(value):
    return f"Processing string: {value.upper()}"

@process.register(list)
def _(value):
    return f"Processing list: {len(value)} elements"

print(process(10))         # Output: Processing integer: 20
print(process("hello"))    # Output: Processing string: HELLO
print(process([1, 2, 3]))  # Output: Processing list: 3 elements
print(process.registry) # {<class 'object'>: <function process at 0x765bb4f0dbc0>, <class 'int'>: <function _ at 0x765bb4f0e0c0>, <class 'str'>: <function _ at 0x765bb4f0e160>, <class 'list'>: <function _ at 0x765bb4f0e200>}
```

Explanation:

- The `@singledispatch` decorator creates a generic function (process).
- `@process.register(type)` maps types to different function implementations.
- At runtime, the correct function is executed based on the type of the first argument.

### Multi Dispatch (Multiple Argument Type-Based Dispatching)

- Uses `multipledispatch` (third-party package) to dispatch functions based on multiple argument types.
- Allows method overloading by defining multiple versions of the same function.
- Unlike `singledispatch`, all argument types are considered when selecting a function.

```python
from multipledispatch import dispatch

@dispatch(int, int)
def add(a, b):
    return a + b

@dispatch(str, str)
def add(a, b):
    return a + " " + b

@dispatch(list, list)
def add(a, b):
    return a + b

print(add(3, 5))       # Output: 8
print(add("Hello", "World"))  # Output: Hello World
print(add([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]
```

- The `@dispatch` decorator registers multiple versions of `add()` for different argument types.
- At runtime, Python selects the correct implementation based on all argument types.
- Useful for handling operations that should behave differently depending on types.

### Value-Based Dispatching

- Dispatches function behaviour based on argument values instead of types.
- The decorator inspects an argument (e.g., priority, feature flags) to modify execution.
- Often used for feature toggles or priority-based execution.

```python
def priority_dispatch(func):
    def wrapper(priority, *args, **kwargs):
        if priority == "high":
            print("Executing high-priority task")
        elif priority == "low":
            print("Executing low-priority task")
        else:
            print("Executing default task")
        return func(*args, **kwargs)
    return wrapper

@priority_dispatch
def run_task(task):
    print(f"Running: {task}")

run_task("high", "Data Processing")  
# Output:  
# Executing high-priority task  
# Running: Data Processing
```

- The decorator checks the priority argument before executing `run_task()`.
- Adjusts execution based on the argument value, not its type.
- Can be extended for logging, access control, or dynamic behaviour selection.

### Method Dispatching in Class Decorators

- A class-based decorator modifies methods dynamically when applied to a function.
- Uses `__call__()` to control execution based on method arguments.
- Often used for permission systems or role-based access control.

```python
class RoleBasedAccess:
    """Class decorator that modifies access based on user role."""
    def __init__(self, func):
        self.func = func

    def __call__(self, user_role, *args, **kwargs):
        if user_role == "admin":
            print("Admin access granted.")
            return self.func(*args, **kwargs)
        else:
            print("Access denied.")
            return None

@RoleBasedAccess
def secure_function():
    print("Performing a sensitive operation")

secure_function("admin")  # Output: Admin access granted. Performing a sensitive operation
secure_function("guest")  # Output: Access denied.
```

- The class-based decorator intercepts function execution and checks the user role.
- Grants or denies access based on the user_role argument.
- Can be used for security enforcement, rate limiting, or logging.

### Summary of Dispatching Methods in Decorators

| Dispatch Type  | Mechanism                                      | Example Use Case                               |
|----------------|------------------------------------------------|-----------------------------------------------|
| Single Dispatch| Dispatches based on the type of the first argument | Overloading functions for different types      |
| Multi Dispatch | Dispatches based on the types of multiple arguments | Overloading functions with multiple arguments  |
| Value Dispatch | Dispatches based on argument values            | Priority-based execution, feature toggling     |
| Method Dispatch| Dispatches methods in class decorators         | Role-based access control, permission systems  |

## Dispatching with Metaclasses

- Metaclasses are classes for classes: they control the creation and behaviour of classes.
- A dispatching metaclass can dynamically modify the class methods or attributes based on type or value.
- Dispatching using metaclasses is a more advanced pattern, often used for building frameworks or controlling class behaviour globally.
- A metaclass can modify methods during the class definition, allowing dynamic dispatch based on conditions or argument types.

### Type-Based Dispatching in a Metaclass

In this example, the metaclass dispatches different methods based on the type of an argument.

```python
class DispatchMeta(type):
    def __new__(cls, name, bases, dct):
        # Define method dispatching based on argument types
        def dispatch_method(self, arg):
            if isinstance(arg, int):
                return f"Integer: {arg * 2}"
            elif isinstance(arg, str):
                return f"String: {arg.upper()}"
            else:
                return "Unsupported type"

        dct['dispatch_method'] = dispatch_method
        return super().__new__(cls, name, bases, dct)

class DispatcherClass(metaclass=DispatchMeta):
    pass

obj = DispatcherClass()
print(obj.dispatch_method(5))      # Output: Integer: 10
print(obj.dispatch_method("hello"))  # Output: String: HELLO
print(obj.dispatch_method([1, 2]))  # Output: Unsupported type
```

- `DispatchMeta` is a metaclass that overrides `__new__` to add the `dispatch_method` dynamically to the class.
- The method `dispatch_method` checks the type of the argument and behaves accordingly.
- The behaviour is controlled at the class level, and new instances of `DispatcherClass` have the method with type dispatching.

#### Advantages of Dispatching with Metaclasses

- **Global control**: A metaclass operates at the class level, so you can globally modify the behaviour of all instances of a class.
- **Dynamic behaviour**: By inspecting class attributes or arguments, metaclasses allow you to introduce dynamic, type-based dispatching logic that applies to all methods of a class.
- **Framework and API development**: Metaclasses are powerful for building custom frameworks where classes may need special dispatching behaviour.

### Value-Based Dispatching with Metaclasses

This example shows a metaclass that dispatches methods based on values, not just types.

```python
class ValueDispatchMeta(type):
    def __new__(cls, name, bases, dct):
        def process_value(self, value):
            if value == "high":
                return "Processing high priority task"
            elif value == "low":
                return "Processing low priority task"
            else:
                return "Processing default task"

        dct['process_value'] = process_value
        return super().__new__(cls, name, bases, dct)

class TaskProcessor(metaclass=ValueDispatchMeta):
    pass

task = TaskProcessor()
print(task.process_value("high"))  # Output: Processing high priority task
print(task.process_value("low"))   # Output: Processing low priority task
print(task.process_value("medium"))  # Output: Processing default task
```

- `ValueDispatchMeta` is a metaclass that defines a method `process_value` based on argument values.
- The method dispatches different behaviors depending on the value passed (`"high"`, `"low"`, or any other value).
- The class `TaskProcessor` inherits from `ValueDispatchMeta`, and its instances use the `process_value` method with value-based dispatching.

#### Advantages of Value Dispatching with Metaclasses

- **Fine-grained control**: By dispatching on argument values, you can handle complex behaviour or modify the class methods dynamically.
- **Use case flexibility**: Ideal for situations where the dispatch behaviour needs to be determined by specific values (e.g., task priorities, status codes, etc.).
- **Centralized logic**: Dispatch logic is encapsulated at the class level, so all methods of the class benefit from this centralized control.
