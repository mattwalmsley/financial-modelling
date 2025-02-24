# Python Functions

- [Python Functions](#python-functions)
  - [Introduction](#introduction)
  - [Argument Passing](#argument-passing)
    - [Positional and Keyword Arguments](#positional-and-keyword-arguments)
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
