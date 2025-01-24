# Python: Object-Orientated Programming

- [Python: Object-Orientated Programming](#python-object-orientated-programming)
  - [Four Principles of Object-Orientated Programming](#four-principles-of-object-orientated-programming)
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

## Four Principles of Object-Orientated Programming

1. Encapsulation
   - Bundling data and methods that operate on that data within one unit. Example: a class `Car` encapsulating attributes like `model` and methods like `drive()`.
2. Abstraction
   - Hiding the complex implementation details and showing only the necessary features of an object. Example: Using a `Vehicle` class without knowing its internal engine mechanics for method `start_engine()`.
3. Inheritance
   - Creating new classes from existing ones, inheriting their attributes and methods. Example: a `Truck` class inheriting from the `Vehicle` class.
4. Polymorphism
    - The ability of objects to take on multiple forms based on their context. Example: a `Shape` class with different subclasses like `Circle` and `Rectangle`, each implementing a `calculate_area()` method differently.

## Classes

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

### Creating an Instance (Object)

To create an instance of a class, call the class using parentheses `()`. This triggers the `__init__` method.

```python
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.describe())  # Output: Buddy is a Golden Retriever.
print(dog1.bark())      # Output: Buddy says woof!
```

- `dog1` is an instance of the `Dog` class.
- The methods of `Dog` using the dot notation `dog1.describe()`

### Class Attributes vs Instance Attributes

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

### Methods

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

### Inheritance

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

### The `super()` Function

The `super()` function allows methods from the parent class to be called in a child class. This is useful for extending or modifying behaviour in subclasses without completely overriding the parent method.

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

### Method Resolution Order (MRO)

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

### Encapsulation and Access Modifiers

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

#### Accessing Private Attributes

Private attributes cannot be directly accessed from outside the class. However, Python allows access to private attributes using a **name-mangling** mechanism:

```python
print(person._Person__age)  # Output: 30
```
