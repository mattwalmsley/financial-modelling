# Python: Object-Orientated Programming

## Four Principles of Object-Orientated Programming

### Encapsulation

- Bundling data and methods that operate on that data within one unit. Example: a class `Car` encapsulating attributes like `model` and methods like `drive()`.

### Abstraction

- Hiding the complex implementation details and showing only the necessary features of an object. Example: Using a `Vehicle` class without knowing its internal engine mechanics for method `start_engine()`.

### Inheritance

- Creating new classes from existing ones, inheriting their attributes and methods. Example: a `Truck` class inheriting from the `Vehicle` class.

### Polymorphism

- The ability of objects to take on multiple forms based on their context. Example: a `Shape` class with different subclasses like `Circle` and `Rectangle`, each implementing a `calculate_area()` method differently.

## Defining a Python Class

```python
class NameOfClass():

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def some_method(self):
        # perform some action
        print(self.param1)
```

## Inheritance and Polymorphism

```python
class Animal():

    def __init__(self):
        print("Created Animal")

    def speak():
        raise NotImplementedError("Subclass must implement this abstract method.")

    def sleep():
        print("Sleeping")
        
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Created Dog")
        
    def speak():
        print("Woof")

    def eat():
        print("Dog eats")

class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Created Cat")
        
    def speak():
        print("Meow")

dog = Dog()
cat = Cat()

dog.speak() # prints 'Woof'
dog.sleep() # prints 'Sleeping'
dog.eat() # prints 'Dog eats'

cat.speak() # prints 'Meow'
cat.sleep() # prints 'Sleeping'

# prints 'Woof' and then 'Meow'
for animal in [dog, cat]:
    animal.speak()
```

## Special Methods

See [Special Method Names](https://docs.python.org/3/reference/datamodel.html#special-method-names) documentation.

```python
class Book():

    # __init__ is a special method for initialising the object
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ is a special method that dictates how an object should be printed
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __len__ is a special method that returns the length of an object
    def __len__(self):
        return pages

book = Book("My Book", "Me", 100)

print(book) # prints 'My Book by Me'
print(len(book)) # prints 100

```
