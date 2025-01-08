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
      - [Lambda Functions](#lambda-functions)
    - [Loops](#loops)
      - [`while` Loops](#while-loops)
      - [`for` Loops](#for-loops)
      - [Loops with `else`](#loops-with-else)
    - [Exception Handling](#exception-handling)
    - [Classes](#classes)
      - [Creating an Instance (Object)](#creating-an-instance-object)
      - [Class Attributes vs Instance Attributes](#class-attributes-vs-instance-attributes)
      - [Methods](#methods)
      - [Special Methods (*Dunder* Methods)](#special-methods-dunder-methods)
      - [Inheritance](#inheritance)
      - [The `super()` Function](#the-super-function)
      - [Method Resolution Order (MRO)](#method-resolution-order-mro)
      - [Encapsulation and Access Modifiers](#encapsulation-and-access-modifiers)
        - [Accessing Private Attributes](#accessing-private-attributes)
      - [Decorators in Python](#decorators-in-python)
        - [Function Decorators](#function-decorators)
        - [Class Decorators](#class-decorators)
        - [Method Decorators](#method-decorators)
          - [The `@property` Decorator](#the-property-decorator)
          - [`@classmethod` and `@staticmethod` Decorators](#classmethod-and-staticmethod-decorators)
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

#### Lambda Functions

A **lambda function** is a small anonymous function defined using the `lambda` keyword. It can take any number of arguments but has only one expression. Lambda functions are useful when you need a short, throwaway function.

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

### Loops

Loops in Python are used to iterate over a block of code multiple times. The two main types of loops are `while` loops and `for` loops.

#### `while` Loops

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

#### `for` Loops

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

You can use `break` to exit a for loop early.

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

### Exception Handling

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

### Classes

In Python, classes are used to create user-defined data structures. A class defines a blueprint for objects, encapsulating data (attributes) and behaviour (methods). Objects created from a class are called **instances**.

Classes in Python are defined using the `class` keyword, followed by the class name and a colon. By convention, class names are written in *PascalCase*.

```python
class ClassName:
    # Class attributes (optional)
    
    # Constructor
    def __init__(self, parameters):
        # Instance attributes
        self.attribute = value
    
    # Methods
    def method_name(self, parameters):
        # Code for method

# Example
class Dog:
    # Constructor to initialize the class
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed

    # Method to describe the dog
    def describe(self):
        return f"{self.name} is a {self.breed}."

    # Method to make the dog bark
    def bark(self):
        return f"{self.name} says woof!"
```

- `__init__` is the constructor method used to initialize the `Dog` class with attributes `name` and `breed`.
- The `self` parameter represents the specific instance of the class that is being created or accessed.
- `describe` and `bark` are methods that provide behaviour for `Dog` instances.

#### Creating an Instance (Object)

To create an instance of a class, call the class using parentheses `()`. This triggers the `__init__` method.

```python
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.describe())  # Output: Buddy is a Golden Retriever.
print(dog1.bark())      # Output: Buddy says woof!
```

- `dog1` is an instance of the `Dog` class.
- The methods of `Dog` using the dot notation `dog1.describe()`

#### Class Attributes vs Instance Attributes

- Instance attributes are unique to each instance (object) and are defined inside the `__init__` method using `self`.
- Class attributes are shared among all instances of a class. They are defined directly inside the class body.

```python
class Dog:
    species = "Canine"  # Class attribute, shared by all instances.

    def __init__(self, name):
        self.name = name  # Instance attribute, unique to each instance.

# Accessing Attributes
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine
print(dog1.name)     # Output: Buddy
print(dog2.name)     # Output: Max
```

#### Methods

Methods are functions that are defined inside a class and belong to class instances. They always take self as the first parameter, which refers to the instance calling the method.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    # Method to calculate area
    def area(self):
        return 3.14 * self.radius ** 2

# Calling Methods
circle = Circle(5)
print(circle.area())  # Output: 78.5
```

#### Special Methods (*Dunder* Methods)

Special methods (also called dunder methods, short for "double underscore") define behaviour for built-in Python operations, such as initialization, representation, addition, and more. They are surrounded by double underscores (e.g., `__init__`, `__str__`, `__add__`).

- `__init__` Constructor method that initializes an object.
- `__str__` Defines how an object is represented as a string.
- `__repr__` Provides a formal string representation of the object (often used for debugging).

```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book({self.title}, {self.author})"

# Using Dunder Methods
book = Book("1984", "George Orwell")
print(book)            # Output: '1984' by George Orwell
print(repr(book))      # Output: Book(1984, George Orwell)
```

#### Inheritance

Inheritance allows a class to inherit attributes and methods from another class. The class that is inherited from is called the parent or superclass, and the class that inherits is called the child or subclass.

```python
class ParentClass:
    # Parent class code

class ChildClass(ParentClass):
    # Child class code

# Example
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound."

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        return f"{self.name} barks."

# Using Inheritance
dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks
# Here, the Dog class overrides the speak method from the Animal class.
```

#### The `super()` Function

The `super()` function allows you to call methods from the parent class in a child class. This is useful for extending or modifying behaviour in subclasses without completely overriding the parent method.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent constructor
        self.breed = breed
# super() is used to call the __init__ method of the parent class Animal.
```

#### Method Resolution Order (MRO)

When using `super()`, Python follows the Method Resolution Order (MRO) to determine the order in which classes are searched for a method. The MRO is especially important in multiple inheritance scenarios.

The MRO can be viewed using the `__mro__` attribute or the `mro()` method.
It ensures that each class in the hierarchy is only called once.

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    def method(self):
        print("D method")
        super().method()

d = D()
d.method()
# Output:
# D method
# B method
# C method
# A method

# The MRO for class D is D -> B -> C -> A
print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
```

#### Encapsulation and Access Modifiers

Encapsulation is the concept of bundling data (attributes) and methods together and restricting access to certain components of an object.

- Public attributes/methods: Accessible from outside the class (default behaviour).
- Protected attributes/methods: Prefixed with a single underscore (`_`), indicating they are intended for internal use or subclasses but not enforced as private.
- Private attributes/methods: Prefixed with a double underscore (`__`), making them inaccessible from outside the class.

```python
class Person:
    def __init__(self, name, address, ssn):
        self.name = name  # Public attribute
        self._address = address  # Public attribute
        self.__ssn = ssn  # Private attribute
    
    def get_ssn(self):
        return self.__ssn

person = Person("Alice", "30 Garden Street", "123-45-6789")

# Public attribute
print(person.name)              # Output: Alice

# Protected attribute (accessible, but not recommended directly)
print(person._age)              # Output: 30 Garden Street

# Private attribute (accessed via public method)
print(person.get_ssn())         # Output: 123-45-6789
```

##### Accessing Private Attributes

Private attributes cannot be directly accessed from outside the class. However, Python allows you to access private attributes using a **name-mangling** mechanism:

```python
print(person._Person__age)  # Output: 30
```

#### Decorators in Python

Decorators are a powerful feature in Python that allow you to modify the behaviour of functions or methods. They are often used to add functionality to existing code in a clean and readable way.

- **Function Decorators**: Used to modify or enhance functions.
- **Class Decorators**: Used to modify or enhance classes.
- **Method Decorators**: Used to modify or enhance methods within a class.

##### Function Decorators

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

##### Class Decorators

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

##### Method Decorators

Method decorators are used to modify or enhance methods within a class.

###### The `@property` Decorator

The `@property` decorator allows you to define methods in a class that can be accessed like attributes. This is useful for implementing getters and setters in a Pythonic way.

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

###### `@classmethod` and `@staticmethod` Decorators

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
