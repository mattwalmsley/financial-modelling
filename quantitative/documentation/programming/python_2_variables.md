# Python Variables

- [Python Variables](#python-variables)
  - [Introduction](#introduction)
  - [Immutable Types](#immutable-types)
  - [Mutable Types](#mutable-types)
  - [Mixing Mutable and Immutable Types](#mixing-mutable-and-immutable-types)
  - [Shared References and Memory Address Reuse](#shared-references-and-memory-address-reuse)
    - [Small Integers: Object Interning](#small-integers-object-interning)
    - [Strings: String Interning](#strings-string-interning)
    - [Tuples: Shared References for Immutable Components](#tuples-shared-references-for-immutable-components)
    - [Explicit Interning with `sys.intern`](#explicit-interning-with-sysintern)
  - [Equality](#equality)
    - [`==` Operator](#-operator)
    - [`is` Operator](#is-operator)
    - [Special Cases in Equality](#special-cases-in-equality)
      - [Example: Comparing Integers and Floats](#example-comparing-integers-and-floats)
  - [Garbage Collection](#garbage-collection)
    - [Reference Counting](#reference-counting)
      - [Example of Reference Counting](#example-of-reference-counting)
    - [Cyclic Garbage Collector](#cyclic-garbage-collector)
      - [Example of Cyclic Garbage Collection](#example-of-cyclic-garbage-collection)
  - [The `None` Object](#the-none-object)
    - [Effects of Setting a Variable to `None`](#effects-of-setting-a-variable-to-none)
    - [When to Use `None`](#when-to-use-none)
    - [`None` with Booleans](#none-with-booleans)
  - [Peephole Optimisation](#peephole-optimisation)
    - [Examples of Peephole Optimisations](#examples-of-peephole-optimisations)
      - [Constant Folding](#constant-folding)
      - [Unused Code Removal](#unused-code-removal)
      - [Redundant Operations Elimination](#redundant-operations-elimination)
      - [Simplifying Expressions](#simplifying-expressions)
      - [Membership Test Optimisations](#membership-test-optimisations)
  - [Packing and Unpacking Iterables](#packing-and-unpacking-iterables)
    - [Packed Values](#packed-values)
    - [Unpacking Values](#unpacking-values)
      - [Unpacking in Loops](#unpacking-in-loops)
      - [Unpacking with Dictionaries and Sets](#unpacking-with-dictionaries-and-sets)
      - [Variable Reassignment Using Unpacking](#variable-reassignment-using-unpacking)
      - [Extended Unpacking (`*`  and `**` Operators)](#extended-unpacking---and--operators)
    - [Nested Unpacking](#nested-unpacking)
  - [Callables](#callables)

## Introduction

- In Python, every variable refers to an object stored in memory
  - Variables are therefore references (or pointers) to memory addresses.
  - Multiple variables can reference the same object, and changes to the object through one variable will be reflected in all variables that reference it.
- Python objects are classified as *mutable* or *immutable* based on whether their content can be modified after creation.
- The `id()` function can be used to find the memory address (*base-10*) of a variable.
  - The `hex()` function can change the *base-10* number to *hexadecimal*.

## Immutable Types

Immutable objects cannot be changed after they are created, i.e. if an immutable type is modified, a new object is created in memory.

Examples of immutable types:

- Numeric types: `int`, `float`, `complex`
- Boolean: `bool`
- Strings: `str`
- Tuples: `()`
- Frozen sets
- User-defined classes (if class prevents mutation)

```python
x = 10  # Immutable integer created at memory address 0x1000
y = x # y and x both reference the same object at memory address 0x1000

y = 20  # A new object at memory address 0x2000 is created for y with the value 20
print(hex(id(x))) # x remains as 10 at memory address 0x1000
```

## Mutable Types

Mutable objects can be modified after they are created, i.e. no new object is created when a mutable object is modified.

Examples of mutable types:

- Lists: `[]`
- Dictionaries: `{}`
- Sets: `set`
- User-defined classes (if class allows mutation)

```python
my_list = [1, 2, 3]  # Mutable list created at memory address 0x1000
my_list_2 = my_list # my_list_2 and my_list both reference the same object at memory address 0x1000

my_list_2.append(4)  # The same list object at 0x1000 is modified
print(my_list)  # Output: [1, 2, 3, 4]
print(my_list_2)  # Output: [1, 2, 3, 4]

# Using the + operator creates a new list (with a new memory address)
new_list = my_list + [5]
print(my_list)  # Output: [1, 2, 3, 4] (original list remains unchanged)
print(new_list)  # Output: [1, 2, 3, 4, 5] (new list with added element)
```

## Mixing Mutable and Immutable Types

Mutable and immutable types can be used within the same data structure.

A tuple is an immutable type so its contents cannot be changed after it is created. However, if a tuple contains mutable types (such as lists), the contents of those mutable types can be modified.

```python
# Create a tuple containing two lists
my_tuple = ([1, 2], [3, 4])

# The tuple itself is immutable
try:
    my_tuple[0] = [5, 6]  # This will raise a TypeError
except TypeError as e:
    print(e)  # Output: 'tuple' object does not support item assignment

# However, the lists inside the tuple are mutable
my_tuple[0].append(3)
my_tuple[1].remove(4)

print(my_tuple)  # Output: ([1, 2, 3], [3])
```

## Shared References and Memory Address Reuse

- The same memory address may be reused under certain conditions, resulting in shared references.
- For immutable objects (e.g., integers, strings, tuples), Python can reuse the same memory address to save memory and improve performance.

### Small Integers: Object Interning

- Python caches a global list of integers in the range `[-5, 256]` during startup.
- Integers in this range are *singleton* objects.
- When variables are assigned values within this range, Python reuses the same object in memory.

Small integers are frequently used, so caching them reduces memory overhead and speeds up execution.

```python
a = 10
b = 10
print(id(a), id(b))  # Same memory address
```

Integers outside the [-5, 256] range are not interned and are created as separate objects.

```python
x = 257
y = 257
print(id(x), id(y))  # Different memory addresses
```

Dynamically creating small integers will still point to the same interned integer object.

```python
# Static Creation (Interned Object)
x = 10 # Interned small integer
y = 10 # Points to the same interned integer object as x

# a and b also points to the same interned integer object in memory as x and y
a = int("10")
b = int("10")
print(id(x), id(y), id(a), id(b))  # Same memory address

def get_half(n: str) -> int:
    return int(n) / 2

x = get_half("20")  # Created float from a string
y = get_half("20")  # Another float created from a string

print(x,y) # 10.0 10.0 # Same values

# Different memory addresses due to being floats
print(id(x), id(y))  # Different memory addresses
print(type(x), type(y))

# converted to an int, will point to same memory address
print(id(int(x)), id(int(y)))  # Same memory addresses
```

### Strings: String Interning

- Python reuses memory for string literals (strings that are hard-coded in the source code) to save memory.
- Strings that are:
  - Short
  - Comprised of alphanumeric characters
  - Internally consistent with [identifier naming rules](./python_1_style_syntax.md#naming-conventions) (e.g., `s1 = "hello"`, but not `s2="23hello"`)

```python
s1 = "hello"
s2 = "hello"
print(id(s1), id(s2))  # Same memory address

s1 = "hello world!"
s2 = "hello world!"
print(id(s1), id(s2))  # Different memory addresses
```

Strings are immutable, so reusing them is safe and efficient.

### Tuples: Shared References for Immutable Components

Python may reuse memory for tuples containing shared references to other immutable objects.

```python
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(id(t1), id(t2))  # Same memory address
```

Tuples are immutable, and reusing memory for identical tuples avoids duplication.

### Explicit Interning with `sys.intern`

Strings can be explicitly interned using the `sys.intern` function, which forces Python to reuse memory.

```python

import sys
s1 = sys.intern("long string that is not automatically interned")
s2 = sys.intern("long string that is not automatically interned")
print(id(s1), id(s2))  # Same memory address
```

Explicit interning can be helpful for performance when working with large datasets of repetitive strings or for quickly comparing two strings by checking for identity equality instead of a slower character-by-character value equality check.

## Equality

There are two types of equality checks: `==` and `is`.

### `==` Operator

- The `==` operator checks for **value** equality.
- It compares the values of two objects to determine if they are equivalent.
- The negated value check: `!=`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True (values are the same)
```

`a` and `b` are two different lists with the same values. The `==` operator returns `True` because the values in the lists are equal.

### `is` Operator

- The `is` operator checks for identity equality.
- It compares the memory addresses of two objects to determine if they are the same object.
- The negated identity check: `is not`

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # Output: False (different objects in memory)

c = a
print(a is c)  # Output: True (same object in memory)
```

- `a` and `b` are two different list objects with the same values, so `a is b` returns `False`.
- `c` is assigned to `a`, so `a is c` returns `True` because they reference the same object in memory.

### Special Cases in Equality

When comparing different types, Python's `==` operator can still return `True` if the values are considered equivalent, even if the types are different.

#### Example: Comparing Integers and Floats

```python
x = 10
y = 10.0

print(x == y)  # Output: True (values are considered equivalent)
print(x is y)  # Output: False (different objects and types in memory)
```

- `x` is an integer (`int`) with the value `10` and `y` is a float (`float`) with the value `10.0`.
- The `==` operator returns `True` because the values are considered equivalent, even though they are of different types.
- The `is` operator returns `False` because `x` and `y` are different objects in memory and have different types.

## Garbage Collection

- Garbage collection in Python is the process of automatically freeing memory by deleting objects that are no longer in use. Python primarily uses reference counting and a cyclic garbage collector to manage memory.
- When the reference count drops to zero, the memory for the object is immediately deallocated.
- However, reference counting cannot handle circular references, where two or more objects refer to each other but are no longer accessible from the rest of the program.
- Python includes a cyclic garbage collector as part of its GC module to detect and collect objects involved in reference cycles.
  - This collector works in addition to reference counting to clean up circular references.

### Reference Counting

Reference counting is a technique where each object has an associated counter that tracks the number of references to it. When an object's reference count drops to zero, it means the object is no longer in use and can be safely deleted.

#### Example of Reference Counting

```python
import sys

# Create an object
a = [1, 2, 3]
print(sys.getrefcount(a))  # Output: 2 (one from 'a' and one from getrefcount)

# Create another reference to the same object
b = a
print(sys.getrefcount(a))  # Output: 3 (one from 'a', one from 'b', and one from getrefcount)

# Delete one reference
del b
print(sys.getrefcount(a))  # Output: 2 (one from 'a' and one from getrefcount)

# Delete the remaining reference
del a
# Now the reference count is 0, and the object is garbage collected
```

**Note**: The `sys.getrefcount()` function creates an additional reference to the object when it is called, which can affect the reference count. To avoid this, use the `ctypes` module to get the reference count without creating an additional reference:

```python
import ctypes

# Create an object
a = [1, 2, 3]

# Get the reference count without creating an additional reference
memory_address = id(a) # this does create a reference to a, but this reference is removed upon id() returning the address
ref_count = ctypes.c_long.from_address(memory_address).value 
print(ref_count)  # Output: 1 (only one reference from 'a')
```

### Cyclic Garbage Collector

- Python's cyclic garbage collector is designed to detect and collect objects that are part of reference cycles (i.e., objects that reference each other but are not reachable from any other part of the program).
- The garbage collector periodically identifies unreachable objects and reclaims their memory.
- Objects with a `__del__` method require special handling, as finalisers can complicate garbage collection.

#### Example of Cyclic Garbage Collection

```python
import gc

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a circular reference
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# Manually break the circular reference
node1 = None
node2 = None

# Force garbage collection
gc.collect()
```

In this example, `node1` and `node2` reference each other, creating a cycle. When `node1` and `node2` are set to `None`, the reference count for both objects drops, but they are not immediately collected because they reference each other. The cyclic garbage collector detects this cycle and collects the objects.

## The `None` Object

`None` is a built-in *singleton* object that represents the absence of a value or a null reference. Assigning `None` to a variable does not delete the variable but changes its reference to point to the `None` object in memory.

### Effects of Setting a Variable to `None`

- Breaks the variable's reference to the original memory address
  - The variable no longer references its original object.
  - If no other references to the original object exist, it becomes eligible for garbage collection.
- Updates the variable's reference
  - The variable now points to the memory location of the `None` object.
  - The `None` object is a singleton, meaning it always occupies the same memory address.
- Does not delete the variable
  - Setting a variable to `None` does not remove it. The variable still exists and can be reassigned to a new value later.

```python
x = [1, 2, 3] # x references a list (mutable)
y = 10  # y references an int (immutable)

id(my_int) == id(my_array) # false

my_int = None
my_array = None
id(my_int) == id(my_array) # true, as x and y reference None object
my_int is my_array # true, as same reference
```

### When to Use `None`

- Initialise Variables
  - Use `None` as a placeholder for variables before assigning them meaningful values.
- Explicitly reset a variable to indicate it is no longer being used.
- Function Defaults
  - Use `None` as a default argument in functions to indicate the absence of a value.

### `None` with Booleans

- In a boolean context (e.g., inside an if statement), None evaluates to False.
- This should be used with caution as `None`, `True`, and `False` are distinct singleton objects in Python.

```python
None is False # False, identity (memory address) is different
None == False # False, value equality is different
if not None:
    print("None evaluates to False in boolean context")
```

## Peephole Optimisation

- Python (specifically CPython) performs small-scale optimizations at the bytecode level, known as *peephole* optimizations.
- These optimisations occur at the *bytecode compilation phase*, before the code is executed, and aim to make the generated bytecode more efficient.
- Peephole optimisation works by looking at a "window" of a few instructions at a time (a "peephole") in the generated bytecode.
- The optimiser analyses and possibly replaces these instructions with more efficient or simplified equivalents.

### Examples of Peephole Optimisations

#### Constant Folding

If a Python expression involves constants, the optimiser will precompute the result and replace the expression with the computed constant.

```python
 # numeric calculations
x = 3 + 4

# short sequences with length < 20
y = (1, 2) * 3
z = 'abc' * 2
```

After peephole optimisation, it would be replaced with:

```python
x = 7
y = (1, 2, 1, 2, 1, 2)
z = 'abcabc'
```

#### Unused Code Removal

If there is code that does not affect the program's output (e.g., an unused variable or operation), the peephole optimiser will remove it.

```python
x = 5
y = 10
s = x + y  # This will not be used anywhere else
```

After optimisation, the code might become:

```python
x = 5
y = 10
```

#### Redundant Operations Elimination

If there are redundant or repeated operations, the optimiser will attempt to eliminate them to save processing time.

```python
x = 5 * 1  # Redundant multiplication by 1
```

After optimisation, the code will become:

```python
x = 5
```

#### Simplifying Expressions

Some expressions, like certain arithmetic operations, may be simplified to a more efficient form.

```python
x = (a * 2) + (a * 2)
```

After optimisation, it could be simplified to:

```python
x = a * 4
```

#### Membership Test Optimisations

When performing a membership test using the `in` operator, Python checks if a value exists within a sequence, such as a list.

```python
e in [1, 2, 3] #list
```

Peephole optimization can help simplify a list membership test expressions by converting the relevant list into a tuple.

```python
e in (1, 2, 3)
```

- Lists are mutable, meaning the interpreter needs to account for possible modifications.
- Tuples are immutable, and optimisations can be made during the bytecode compilation phase, such as faster hash-based membership checks.

Python will optimize membership tests on mutable objects by converting mutable data structures to immutable ones. Constant lists will be converted to tuples and constant sets will be converted to frozensets.

However, sets and dictionaries offer faster membership tests than both lists and tuples:

- Sets and dicts in Python use a hash table internally.
- When checking membership (key in set or key in dict), Python can perform the lookup in $O(1)$ average time complexity, which is significantly faster than the $O(n)$ complexity of list or tuple membership tests.
- Lists and tuples require scanning through each element one-by-one to check if the item is present, whereas sets and dicts use their hash-based structure to quickly determine if an element exists.

## Packing and Unpacking Iterables

### Packed Values

- Packed values refer to values that are bundled together within an iterable.
- Any iterable is considered a packed value.
- Common examples of packed values include:
  - `list` and `tuple`: Ordered collections where elements are stored sequentially.
  - `dict` and `set`: Unordered collections that can still be unpacked.
  - Strings (`str`): Treated as sequences of characters.
- Packing occurs when multiple values are grouped together into a single variable.

### Unpacking Values

- *Unpacking* is the process of extracting individual elements from a packed value and assigning them to variables.
- The number of variables on the left side of the assignment must match the number of elements in the iterable.
- Assignment follows the positional order of elements in the packed value.
  - Similar to how a function assigns values to positional arguments.

```python
 # unpacking a list (right) with three values into a tuple (left) with three variables a, b, c
a, b, c = [1, 2, 3]

a, b, c = 10, 20, 'hello' # a = 10, b = 20, c = 'hello'

a, b, c = 'XYZ' # a = 'X', b = 'Y', c = 'Z'
```

#### Unpacking in Loops

Unpacking works with `for` loops to iterate over elements efficiently.

```python
for x in 10, 20, 'hello':
  print(x)
# 10
# 20
# 'hello'
```

Unpacking inside loops can handle tuples or lists of multiple values:

```python
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)
# 1 2
# 3 4
# 5 6
```

Unpacking a string character-by-character:

```python
for e in 'XYZ':
    print(e)
# X
# Y
# Z
```

#### Unpacking with Dictionaries and Sets

Dictionaries and sets are unordered, so unpacking may not always yield elements in a predictable order.

```python
d = {'key1': 1, 'key2': 2, 'key3': 3}

for e in d: # iterates through (unpacks) the keys
    print(e)
# key1
# key2
# key3

for e in d.values(): # iterates through the values
    print(e)
# 1
# 2
# 3

for e in d.items(): # iterates through the key-value pairs
    print(e)
# ('key1', 1)
# ('key2', 2)
# ('key3', 3)

s = {'python', 'java', 'c++'}

for e in s: # iterates through the elements
    print(e)
# python
# c++ (prints before java yet is defined after)
# java
```

#### Variable Reassignment Using Unpacking

Unpacking can be used to swap variable values efficiently.

```python
a = 10
b = 20

# traditional approach (Java/C# etc.)
tmp = a
a = b
b = tmp

# pythonic approach
a, b = b, a

# unpacking is done before assignment, hence d can be reassigned
a = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a, b, c, d = a
print(a, b, c, d) # a b c d
```

#### Extended Unpacking (`*`  and `**` Operators)

- The `*` operator can be used to unpack multiple elements into a single variable.
- This allows for flexible unpacking of iterables with varying lengths.
  - For example, unpacking the first element of a list while storing the rest in a separate variable.

```python
a, *b = [1, 2, 3, 4, 5]
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4, 5]

a, *middle, b = [10, 20, 30, 40, 50]
print(a)       # Output: 10
print(middle)  # Output: [20, 30, 40]
print(b)       # Output: 50
```

The`*` can also be used to unpack the right-hand side:

```python
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l) # [1, 2, 3, 4, 5, 6]
```

With unordered types such as `dict` and `set`, the order of unpacked elements may vary:

```python
s1 = {'a', 'b', 'c'}
a, *b = s1
print(a) # a
print(b) # ['b', 'c']

d1 = {'key1': 1, 'key2': 2, 'key3': 3}
d2 = {'key3': 3.5, 'key4': 4, 'key5': 5}
keys = {*d1, *d2}
print(keys) # {'key1', 'key2', 'key3', 'key4', 'key5'} (only one key3)
```

`**` can be used to unpack dictionaries and **cannot** be used on the left-hand side of an assignment:

```python
d1 = {'key1': 1, 'key2': 2, 'key3': 3}
d2 = {'key3': 3.5, 'key4': 4, 'key5': 5}
items = {**d1, **d2}
print(items) # {'key1': 1, 'key2': 2, 'key3': 3.5, 'key4': 4, 'key5': 5} (key3 overridden: last key3 value is used)

d = {'a': 1, 'b': 2}
print({'a': 10, 'c': 3, **d}) # {'a': 1, 'c': 3, 'b': 2} (d is unpacked and d overrides 'a' value)
print({**d, 'a': 10, 'c': 3}) # {'a': 10, 'b': 2, 'c': 3} (d is unpacked and 'a' value from d is overridden)
```

### Nested Unpacking

- Nested unpacking allows extracting values from nested iterables (lists, tuples, etc.) in a single step.
- Useful when working with structured data like lists of tuples or tuples of lists.

```python
(a, (b, c)) = (1, (2, 3))
print(a, b, c)  # Output: 1 2 3
```

Nested unpacking in loops works well when iterating over structured data:

```python
data = [(1, 2), (3, 4), (5, 6)]
for (a, b) in data:
    print(a, b)
# Output:
# 1 2
# 3 4
# 5 6
```

Using `*` in nested unpacking to capture extra values:

```python
(a, *b), c = (1, [2, 3, 4]), 5
print(a, b, c)  # Output: 1 [2, 3, 4] 5
```

Nested unpacking in dictionaries for extracting key-value pairs using `.items()`:

```python
d = {'a': (1, 2), 'b': (3, 4)}
for key, (x, y) in d.items():
    print(key, x, y)
# Output:
# a 1 2
# b 3 4
```

## Callables

A *callable* is any object in Python that can be called using parentheses `()`. This includes:

- **Functions**: regular functions defined using `def` or `lambda`.

  ```python
  Copy
  Edit
  def greet(name):
      return f"Hello, {name}!"

  print(greet("Alice"))  # Hello, Alice!
  print(callable(greet))  # True
  ```

- **Methods**: functions bound to a `class` instance.

  ```python
  Copy
  Edit
  class Person:
      def greet(self, name):
          return f"Hello, {name}!"

  p = Person()
  print(p.greet("Bob"))  # Hello, Bob!
  print(callable(p.greet))  # True
  ```

- **Classes**: calling a class creates an instance of the class by invoking its `__new__` and `__init__` methods.

  ```python
  class MyClass:
    def __init__(self, value):
        self.value = value

  obj = MyClass(10)  # Calls MyClass.__init__
  print(obj.value)   # 10
  ```

- Any object, such as an instance of a class, implementing the `__call__` method is callable.

  ```python
  class Multiplier:
      def __init__(self, factor):
          self.factor = factor

      def __call__(self, x):
          return x * self.factor

  double = Multiplier(2)
  print(double(5))  # 10
  ```

Use `callable(obj)` to check if an object can be called.

```python
def add(a, b):
    return a + b

print(callable(add))  # True
print(callable(10))   # False
```
