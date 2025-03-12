# Decorators

- [Decorators](#decorators)
  - [Introduction](#introduction)
  - [Function Decorators](#function-decorators)
    - [Preserving Function Metadata (`__name__`, `__doc__`)](#preserving-function-metadata-__name__-__doc__)
  - [Class Decorators](#class-decorators)
  - [Method Decorators](#method-decorators)
    - [The `@property` Decorator](#the-property-decorator)
    - [`@classmethod` and `@staticmethod` Decorators](#classmethod-and-staticmethod-decorators)

## Introduction

Decorators are a powerful feature in Python that modify the behaviour of functions, classes or methods. They are often used to add functionality to existing code in a clean and readable way.

- **Function Decorators**: Used to modify or enhance functions.
- **Class Decorators**: Used to modify or enhance classes.
- **Method Decorators**: Used to modify or enhance methods within a class.

Common notation for decorators is the `@` symbol followed by the decorator function name, placed above the function or class to be decorated.

- For a decorator function `my_decorator` which decorates `my_func`, the syntax `my_func = my_decorator(my_func)` can be used to decorate the function.
- However the `@` symbol provides a more concise and convenient way to decorate functions.

## Function Decorators

- A function decorator is a function that takes another function (e.g. `get_greeting`) as an argument for the parameter `func` and returns a closure (`wrapper`) that extends or modifies the behaviour of the original function (`get_greeting`).
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

## Class Decorators

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

## Method Decorators

Method decorators are used to modify or enhance methods within a class and work in the same was as [function decorators](#function-decorators).

### The `@property` Decorator

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

### `@classmethod` and `@staticmethod` Decorators

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
