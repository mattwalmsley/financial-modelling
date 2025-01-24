# Decorators

- [Decorators](#decorators)
  - [Introduction](#introduction)
  - [Function Decorators](#function-decorators)
  - [Class Decorators](#class-decorators)
  - [Method Decorators](#method-decorators)
    - [The `@property` Decorator](#the-property-decorator)
    - [`@classmethod` and `@staticmethod` Decorators](#classmethod-and-staticmethod-decorators)

## Introduction

Decorators are a powerful feature in Python that modify the behaviour of functions or methods. They are often used to add functionality to existing code in a clean and readable way.

- **Function Decorators**: Used to modify or enhance functions.
- **Class Decorators**: Used to modify or enhance classes.
- **Method Decorators**: Used to modify or enhance methods within a class.

## Function Decorators

A function decorator is a function that takes another function as an argument and returns a new function with added or modified behaviour.

Example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```

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

Method decorators are used to modify or enhance methods within a class.

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
