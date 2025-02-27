# Modules, Packages, and Namespaces

- [Modules, Packages, and Namespaces](#modules-packages-and-namespaces)
  - [Modules](#modules)
  - [Packages](#packages)
  - [Namespaces](#namespaces)
  - [Importing Modules and Packages](#importing-modules-and-packages)
  - [Relative vs Absolute Imports](#relative-vs-absolute-imports)


## Modules

A module is a single Python file (.py) that contains functions, classes, and variables. It is used for organizing code into reusable components and can be imported using `import module_name`.

**Example:**

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# Importing and using the module
import mymodule
print(mymodule.greet("Alice"))  # Hello, Alice!
```

## Packages

A package is a collection of modules organized in a directory containing an `__init__.py` file. The `__init__.py` file can initialize the package and define what gets imported when using `from package import *`. Packages enable hierarchical module organization.

**Example:**

```text
my_package/
│── __init__.py
│── module1.py
│── module2.py
```

```python
# module1.py
def func1():
    return "Function 1"

# Importing from a package
from my_package import module1
print(module1.func1())  # Function 1
```

## Namespaces

A namespace is a mapping of names to objects to avoid conflicts. Types of namespaces include:

- **Built-in Namespace:** Includes functions like `print()`, `len()`.
- **Global Namespace:** Defined at the module level.
- **Local Namespace:** Exists within functions/classes.
- **Enclosed Namespace:** Created by nested functions.

**Example:**

```python
x = 10  # Global namespace

def func():
    y = 5  # Local namespace
    print(x + y)  # Accessing global `x`

func()
```

## Importing Modules and Packages

- `import module`: Imports the whole module.
- `from module import function`: Imports a specific function.
- `from package import module`: Imports a module from a package.
- `import module as alias`: Renames a module for convenience.
- `from module import *`: Imports all public objects (not recommended).

**Example:**

```python
import math as m
print(m.sqrt(16))  # 4.0
```

## Relative vs Absolute Imports

- **Absolute Import:** Refers to the full path.

```python
from my_package.module1 import func1
```

- **Relative Import:** Uses `.` notation within packages.

```python
from .module1 import func1
```
