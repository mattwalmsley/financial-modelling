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
    - [Objects Created Dynamically](#objects-created-dynamically)
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

- Python caches integers in the range `[-5, 256]` during startup.
- When variables are assigned values within this range, Python reuses the same object in memory.

```python
a = 10
b = 10
print(id(a), id(b))  # Same memory address
```

Small integers are frequently used, so caching them reduces memory overhead and speeds up execution.
Counterexample:

```python
x = 257
y = 257
print(id(x), id(y))  # Different memory addresses
```

Integers outside the [-5, 256] range are not interned and are created as separate objects.

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

Explicit interning can be helpful for performance when working with large datasets of repetitive strings.

### Objects Created Dynamically

- For objects created dynamically (e.g., via operations or function calls), Python does not reuse memory unless explicitly optimized.

```python
# Static Creation (Interned Object)
x = 10 # Interned small integer
y = 10 # Points to the same interned integer object as x
a = int("10")  # Also an interned small integer
b = int("10")  # Points to the same interned integer object as a
print(id(x), id(y))  # Same memory address
print(id(a), id(b))  # Same memory address

# Dynamic Creation (Non-Interned Object)
def get_integer(n: str) -> int:
    return int(n) / 2

x = get_integer("10")  # Created dynamically from a string
y = get_integer("10")  # Another dynamically created integer from a string

print(x,y) # 5.0 5.0 # Same values
print(id(x), id(y))  # Different memory addresses
```

- Even though x and y have the same value (`10`), the `int()` function in combination with the `/` operator creates new objects during runtime.
- N.B. The `int()` function by itself will still create a shared reference.

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
- Objects with a `__del__` method require special handling, as finalizers can complicate garbage collection.

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

- Initialize Variables
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
