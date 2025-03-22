# Modules, Packages, and Namespaces

- [Modules, Packages, and Namespaces](#modules-packages-and-namespaces)
  - [Modules](#modules)
    - [Importing Modules](#importing-modules)
    - [Using `importlib` for Dynamic Importing](#using-importlib-for-dynamic-importing)
      - [Use Cases for `importlib`](#use-cases-for-importlib)
  - [Packages](#packages)
  - [Namespaces](#namespaces)
    - [Using `globals()` for the Global Namespace](#using-globals-for-the-global-namespace)
    - [Using `locals()` for Local Namespace](#using-locals-for-local-namespace)
    - [`locals()` versus `globals()`](#locals-versus-globals)
  - [Summary of Importing Modules and Packages](#summary-of-importing-modules-and-packages)
  - [Implicit Namespace Packages](#implicit-namespace-packages)

## Modules

- A module is a single Python file (`.py`) that contains functions, classes, and variables.
- It is used for organizing code into reusable components and can be imported using `import mymodule`.
- Modules are objects of type `module`.

**Example:**

```python
# mymodule.py
def greet(name):
    return f"Hello, {name}!"
```

```python
# Importing and using the module
import mymodule
print(mymodule.greet("Alice"))  # Hello, Alice!
```

### Importing Modules

- Modules are imported at runtime, unlike compiled languages where dependencies are typically resolved at compile-time.
- Python searches for modules in the directories listed in `sys.path`.
  - If a module isn't found in any of these directories, an `ImportError` will be raised.
- Modules are instantiated as objects upon their first import and Python maintains a single instance of that module within a process.
  - After the first import, Python creates a `module` type object, and a reference to that object is stored in `sys.modules` for future use.
- Upon importing a module for the first time, Python loads, compiles, and executes the module's source code to create the module's namespace (which includes functions, classes, and variables).
  - The built-in function `compile()` is used internally by Python to convert the module's source code into a bytecode object that can be executed.
  - The built-in function `exec()` is then used to execute the compiled bytecode within the module's own namespace.
    - The code in the module is executed as a script, but only once per process.
- References to the module are then stored in both the [global namespace dictionary](#using-globals-for-the-global-namespace) (`globals()`) of the current scope (if imported into that scope) and the *system module cache* (`sys.modules`).
  - This ensures that subsequent imports retrieve the same module instance rather than reloading it.

```python
import math as math1 # code in math.py is executed
import math as math2 # code in math.py is not executed

print(math1 is math2)  # True

import sys
print(sys.modules['math'])  # <module 'math' (built-in)>
print(globals()['math1'])  # <module 'math' (built-in)>
print(sys.modules['math'] is globals()['math1'])  # True
```

- `sys.modules` stores modules by their actual name.
  - When a module is imported, Python registers it in `sys.modules` under its original name (e.g., `'math'`).
  - This acts as a cache to avoid reloading the same module multiple times.
- `globals()` stores names assigned in the current namespace.
  - When importing a module using `import math as math1`, the module itself is still registered in `sys.modules` under `'math'`, but in the global namespace, it is assigned the name `'math1'`.
  - The `globals()` dictionary reflects variable names in the current module's global scope.

```python
from math import sqrt # code in math.py is executed but only sqrt is placed in the current namespace
from math import * # code in math.py is not executed but all public objects are placed in the current namespace

import sys
print(sys.modules['math'])  # <module 'math' (built-in)>
print(globals()['sqrt'])  # <built-in function sqrt>
print(globals()['pi']) # 3.141592653589793
print(globals()['math'])  # KeyError: 'math'
```

- After `sqrt` is imported, it is added to the current namespace (accessible via `globals()`), but the `math` module itself is not added to `globals()` unless explicitly imported with `import math`. Therefore, `globals()['math']` raises a `KeyError`.
- Wildcard importing (`from math import *`) should be used with caution as it can lead to namespace pollution and make it unclear where objects are defined.
  - `math` and `cmath` both have a `sqrt` function, so using `from math import *` followed by `from cmath import *` would overwrite the `sqrt` function from `math` with the one from `cmath`.
- Using aliases for imports can make it clear which objects are being used.
  - `from math import sqrt as math_sqrt`
  - `from cmath import sqrt as cmath_sqrt`

### Using `importlib` for Dynamic Importing

The `importlib` module provides a programmatic way to import modules in Python. It is a part of the standard library and offers functions that allow for dynamic imports and interactions with the import system. This can be useful in situations where modules need to be loaded based on user input or configuration at runtime, or if you need to access modules in a more fine-grained way than the standard import statement allows.

- **Dynamically import a module by name**: `importlib.import_module(name, package=None)`
  - The `name` argument is the name of the module to import, and the `package` argument allows for relative imports if the module is part of a package.

    ```python
    import importlib

    # Import the 'math' module dynamically
    math = importlib.import_module('math')

    print(math.sqrt(16))  # Output: 4.0

    # Importing module within a package in a nested structure
    my_module = importlib.import_module('.my_module', package='my_outer_package.my_inner_package')
    my_module_too = importlib.import_module('my_outer_package.my_inner_package.my_module')

    print(my_module is my_module_too)  # True
    ```

- **Reload a previously imported module**: `importlib.reload(module)`
  - This is useful when you want to re-execute a module's code after changes have been made, without restarting the Python interpreter.
  - This is particularly useful in interactive environments like Jupyter notebooks or during development when you want to reflect changes without exiting the session.

    ```python
    import importlib
    import math

    print(math.sqrt(16))  # Output: 4.0
    importlib.reload(math)
    print(math.sqrt(16))  # Output: 4.0 (but code is re-executed)
    ```

- **Find the module specification for a given module name**: `importlib.util.find_spec(name)`
  - This function can be used to check whether a module exists or to get more detailed information about the module.

    ```python
    import importlib.util

    # Check if 'math' module is available
    spec = importlib.util.find_spec('math')
    if spec is not None:
        print("Module found:", spec.name)
    else:
        print("Module not found")
    ```

#### Use Cases for `importlib`

- **Dynamic Imports**: When a module needs loading based on user input or external configuration.
- **Plugin Architecture**: When an application that supports plugins, `importlib` can be used to dynamically load plugin modules at runtime based on user choices or configuration files.
- **Reloading Modules**: During development or debugging, `importlib.reload()` can be used to reload a module and apply the latest changes without restarting the Python interpreter.
- **Handling Optional Dependencies:** In some cases, certain libraries should not be imported until they are needed. `importlib` allows you to conditionally import a module when it's required.

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

### Using `globals()` for the Global Namespace

- `globals()` returns a dictionary representing the global namespace of the current module.
- It allows dynamic access to global variables and functions.
- Used for introspection and modifying global variables dynamically.

Accessing and Modifying Global Variables

```python
x = 100

print(globals()["x"])  # 100
print(x is globals()["x"])  # True

globals()["x"] = 200  # Modifying a global variable dynamically
print(x)  # 200
```

Dynamically Creating Variables

```python
for i in range(3):
    globals()[f"var_{i}"] = i * 10

print(var_0, var_1, var_2)  # 0 10 20
```

- Modifying global variables dynamically is not recommended as it reduces code clarity.
- The use of `globals()` should be limited to *metaprogramming* or situations where dynamic modifications are necessary.
  - **Metaprogramming** is the practice of writing code that manipulates or generates other code at runtime, allowing programs to modify their own structure and behaviour dynamically.
- Instead of modifying global variables, function arguments or class attributes are preferred.

### Using `locals()` for Local Namespace

- `locals()` returns a dictionary of the local namespace, mapping variable names to their current values.
  - It is dynamically generated and reflects the current state of local variables at the time it is called.
  - Typically used for debugging, introspection, and dynamically modifying execution environments.
- In a function, `locals()` provides access to function-scoped variables, including arguments and local assignments.
- At the module level, `locals()` behaves the same as `globals()` since the module's *global* namespace is also its *local* namespace.
- Modifying the dictionary returned by `locals()` inside a function does not change local variables, as Python does not guarantee that changes will propagate.

```python
x = 10

def example(a, b):
    x = a + b
    y = x * 2
    print(locals())
    print(locals()['x'] is globals()['x'])

example(5, 3) 
# Output:
# {'a': 5, 'b': 3, 'x': 8, 'y': 16}
# False

print(locals()['x']) # 10
print(globals()['x']) # 10
print(locals()['x'] is globals()['x']) # True

print(globals()['example']) # <function example at 0x7f7d3c7b0f70>
print(locals()['example']) # <function example at 0x7f7d3c7b0f70>
print(locals()['example'] is globals()['example']) # True
```

### `locals()` versus `globals()`

- `globals()` provides the global namespace, while `locals()` provides the local namespace.
- `globals()` always reflects the current state of global variables and can be modified to change global values.
- `locals()` inside a function does not allow modifications to function variables but does reflect their state at the time of calling.

## Summary of Importing Modules and Packages

- `import module`: Imports the whole module.
- `from module import function`: Imports a specific function.
- `from package import module`: Imports a module from a package.
- `import module as alias`: Renames a module for convenience.
- `from module import *`: Imports all public objects (not recommended).

## Implicit Namespace Packages

versus standard package