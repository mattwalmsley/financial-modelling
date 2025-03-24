# Namespaces, Modules, and Packages

- [Namespaces, Modules, and Packages](#namespaces-modules-and-packages)
  - [Namespaces](#namespaces)
    - [Using `globals()` for the Global Namespace](#using-globals-for-the-global-namespace)
    - [Using `locals()` for Local Namespace](#using-locals-for-local-namespace)
    - [`locals()` versus `globals()`](#locals-versus-globals)
  - [Modules](#modules)
    - [Importing Modules](#importing-modules)
    - [Using `importlib` for Dynamic Importing](#using-importlib-for-dynamic-importing)
      - [Use Cases for `importlib`](#use-cases-for-importlib)
  - [Packages](#packages)
    - [Importing Syntax Differences](#importing-syntax-differences)
      - [`import package1`](#import-package1)
      - [`import package1.module1`](#import-package1module1)
      - [`from package1 import module1`](#from-package1-import-module1)
      - [`from package1.module1 import func1`](#from-package1module1-import-func1)
      - [Summary of Importing Statements](#summary-of-importing-statements)
    - [Example Package Structure](#example-package-structure)
    - [Structuring Packages](#structuring-packages)
      - [Recommended Package Structure](#recommended-package-structure)
      - [Best Practices for Structuring Packages](#best-practices-for-structuring-packages)
    - [What to Put in __init__.py for a Package](#what-to-put-in-initpy-for-a-package)
      - [Example: Organising `__init__.py` for a Package with Multiple Modules](#example-organising-__init__py-for-a-package-with-multiple-modules)
        - [Option 1: Minimal `__init__.py` (Recommended for Simplicity)](#option-1-minimal-__init__py-recommended-for-simplicity)
        - [Option 2: Using `__all__` to Define a Public API](#option-2-using-__all__-to-define-a-public-api)
      - [Option 3: Importing Submodules in `__init__.py`](#option-3-importing-submodules-in-__init__py)
  - [Using `if __name__ == '__main__'`](#using-if-__name__--__main__)
  - [Creating a `__main__.py` File in a Package](#creating-a-__main__py-file-in-a-package)
  - [Implicit Namespace Packages](#implicit-namespace-packages)
    - [Example: Implicit Namespace Package Structure](#example-implicit-namespace-package-structure)
    - [Namespace Packages Across Multiple Locations](#namespace-packages-across-multiple-locations)
    - [Key Differences: Namespace Package vs. Regular Package](#key-differences-namespace-package-vs-regular-package)
    - [When to Use Implicit Namespace Packages](#when-to-use-implicit-namespace-packages)

## Namespaces

A namespace is a mapping of names to objects to avoid conflicts. Types of namespaces include:

- __Built-in Namespace__: Includes functions like `print()`, `len()`.
- __Global Namespace__: Defined at the module level.
- __Local Namespace__: Exists within functions/classes.
- __Enclosed Namespace__: Created by nested functions.

Example:

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
  - __Metaprogramming__ is the practice of writing code that manipulates or generates other code at runtime, allowing programs to modify their own structure and behaviour dynamically.
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

## Modules

- A module is a single Python file (`.py`) that contains functions, classes, and variables.
- It is used for organizing code into reusable components and can be imported using `import mymodule`.
- Modules are objects of type `module`.

Example:

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

- __Dynamically import a module by name__: `importlib.import_module(name, package=None)`
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

- __Reload a previously imported module__: `importlib.reload(module)`
  - This is useful when you want to re-execute a module's code after changes have been made, without restarting the Python interpreter.
  - Care needs to be taken as some usages may be referencing the previous import of the module.

    ```python
    # module1.py
    x = 5
    print("Module 1 loaded")
    ```

    ```python
    # module2.py
    import importlib

    module1 = importlib.import_module('module1') # Module 1 loaded

    print(module1.x) # 5
    module1.x = 10
    print(module1.x) # 10

    importlib.reload(module1) # Module 1 loaded
    print(module1.x) # 5
    ```

- __Find the module specification for a given module name__: `importlib.util.find_spec(name)`
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

- __Dynamic Imports__: When a module needs loading based on user input or external configuration.
- __Plugin Architecture__: When an application that supports plugins, `importlib` can be used to dynamically load plugin modules at runtime based on user choices or configuration files.
- __Reloading Modules__: During development or debugging, `importlib.reload()` can be used to reload a module and apply the latest changes without restarting the Python interpreter.
- __Handling Optional Dependencies__: In some cases, certain libraries should not be imported until they are needed. `importlib` allows you to conditionally import a module when it's required.

## Packages

- A package is a collection of modules organized within a directory that contains an `__init__.py` file.
- The `__init__.py` file serves to initialize the package and defines what code runs when the package is imported.
- Packages enable hierarchical organization of modules, allowing for better code structure and reusability.
  - A package can contain both modules and sub-packages.
- A package is a `module` type object, but unlike a regular module, it has a `__path__` attribute, which is a list containing the directory where the package is located.
- Modules and packages both have `__file__` and `__package__` attributes:
  - `__file__`: The absolute path to the module or package's file.
  - `__package__`: The fully qualified package name or an empty string if the module is at the top level.
- When importing sub-packages, the parent package must first be imported.
- Once a package is imported, it is stored in sys.modules, ensuring that subsequent imports retrieve the same instance rather than reloading it.

### Importing Syntax Differences

#### `import package1`

- This imports the package but does not automatically import its submodules.
- The package's `__init__.py` file is executed.
- Adds an entry for `'package1'` to `sys.modules`,and `globals()`.

#### `import package1.module1`

- This imports `module1` within `package1`, ensuring both `package1` and `package1.module1` are available.
- Adds entries to `sys.modules` for both `'package1'` and `'package1.module1'`.
- Adds `'package1'` to `globals()` for the current namespace but not `'package1.module1'`.
  - The module is only accessible via `package1.module1`.
- `package1.module1` exists inside `sys.modules` but is not directly accessible in `globals()` unless explicitly assigned.

#### `from package1 import module1`

- The `module1` submodule is imported into the current namespace.
- Adds both `'package1'` and `'package1.module1'` to `sys.modules`.
- Adds `'module1'` directly to `globals()` in the current namespace, but not `'package1'`.
- `module1` is now directly accessible in the namespace without needing `package1.module1`.

#### `from package1.module1 import func1`

- Only `func1` is imported into the current namespace.
- Adds both `'package1'` and `'package1.module1'` to `sys.modules` (since `module1` must be imported to extract `func1`).
- Adds `'func1'` directly to `globals()` in the current namespace but not `'module1'` or `'package1'`.
- The function `func1` is directly available in the namespace, but its parent module is not.

#### Summary of Importing Statements

| Import Statement                      | `sys.modules` Entries                  | `globals()` Entries |
|---------------------------------------|----------------------------------------|---------------------|
| `import package1`                     | `'package1'`                           | `'package1'`        |
| `import package1.module1`             | `'package1', 'package1.module1'`       | `'package1'`        |
| `from package1 import module1`        | `'package1', 'package1.module1'`       | `'module1'`         |
| `from package1.module1 import func1`  | `'package1', 'package1.module1'`       | `'func1'`           |

### Example Package Structure

```text
my_package/
│── __init__.py
│── module1.py
│── sub_package/
    │── __init__.py
    │── module2.py
```

```python
# module1.py
import os

print(f"module1 __file__: {__file__}")
print(f"module1 __package__: {__package__}")
```

```python
# sub_package/module2.py
import os

print(f"module2 __file__: {__file__}")
print(f"module2 __package__: {__package__}")
print(f"sub_package __path__: {__path__}")
```

Running `module1.py`:

```bash
$ python -m my_package.module1
module1 __file__: /path/to/my_package/module1.py
module1 __package__: my_package
```

- `__file__` gives the absolute path of `module1.py`.
- `__package__` is my_package since `module1.py` is inside `my_package`.

Running `module2.py`:

```bash
$ python -m my_package.sub_package.module2
module2 __file__: /path/to/my_package/sub_package/module2.py
module2 __package__: my_package.sub_package
sub_package __path__: ['/path/to/my_package/sub_package']
```

- `__file__` provides the absolute path of `module2.py`.
- `__package__` is `my_package.sub_package`, indicating its full package hierarchy.
- `__path__` is a list containing directories where `sub_package` can load additional modules.

### Structuring Packages

A well-structured package improves maintainability, readability, and scalability. Below are best practices, along with common pitfalls to avoid.

#### Recommended Package Structure

A typical Python package follows a structured hierarchy:

```text
my_package/
│── my_package/                 # Package directory (actual code lives here)
│   │── __init__.py             # Initializes the package
│   │── core.py                 # Core functionality
│   │── utils.py                # Helper functions
│   │── config.py               # Configuration settings
│   │── subpackage/             # Optional subpackage
│   │   │── __init__.py
│   │   │── submodule.py
│── tests/                      # Separate directory for tests
│   │── test_core.py
│   │── test_utils.py
│── examples/                   # Example scripts (optional)
│── docs/                       # Documentation (optional)
│── setup.py                    # Package metadata (for packaging)
│── requirements.txt            # Dependencies
│── README.md                   # Package description
│── .gitignore                  # Ignore unnecessary files
│── pyproject.toml              # Modern build system configuration (recommended)
│── LICENSE                     # Licensing information
```

#### Best Practices for Structuring Packages

- Keep Code Organized and Modular
  - Divide functionality into separate modules instead of a single large script.
  - Use sub-packages for logical grouping.
  - Place helper functions in a `utils.py` module instead of cluttering core modules.
- Use `__init__.py` Wisely
  - Every package must have an `__init__.py` file to be recognized as a package.
  - Keep `__init__.py` minimal—avoid importing everything inside it to prevent unnecessary dependencies.
  - ✅ Good Practice (keep it empty or import explicitly):

    ```python
    # my_package/__init__.py
    from .core import some_function  # Explicit import
    ```

  - ❌ Bad Practice (import everything blindly):

    ```python
    # Avoid this:
    from .core import *  # Pollutes namespace and causes unexpected behaviour
    ```

- Separate Tests from the Package Code
  - Keep test files outside the main package directory (e.g., `tests/`).
  - Use a consistent naming pattern (e.g., `test_*.py` for test files).
  - Use `pytest` or `unittest` for structured testing.

- Keep Configuration in a Separate File
  - Store constants, paths, or environment variables in a dedicated `config.py` file.
  - Use `.env` files or environment variables for sensitive information.

### What to Put in __init__.py for a Package

The `__init__.py` file is executed when a package is imported. It defines what happens during package initialization and controls which parts of the package are accessible at the top level.

- ✅ Good practices:
  - Keep it minimal to avoid unnecessary overhead.
  - Explicitly import only the necessary functions, classes, or submodules.
  - Use `__all__` to define a clean public API.
  - Initialize package-level variables or settings (if needed).
- ❌ Bad practices:
  - Avoid wildcard imports (`from module import *`), which can clutter the namespace.
  - Don't execute complex logic inside `__init__.py`.

#### Example: Organising `__init__.py` for a Package with Multiple Modules

Package Structure:

```text
my_package/
│── __init__.py
│── core.py
│── utils.py
│── config.py
│── sub_package/
│   │── __init__.py
│   │── submodule.py
```

Contents of Each Module

```python
# core.py
def main_function():
    return "This is the main function from core.py"
```

```python
# utils.py
def helper_function():
    return "This is a helper function from utils.py"
```

```python
# config.py
VERSION = "1.0.0"
DEBUG = True
```

```python
# sub_package/submodule.py
def submodule_function():
    return "This is a function from submodule.py"
```

##### Option 1: Minimal `__init__.py` (Recommended for Simplicity)

If the package is large and unnecessary imports should be avoided, only expose selected functions in `__init__.py`.

```python
# my_package/__init__.py
# Expose only selected functions
from .core import main_function
from .utils import helper_function

# Define package-level metadata
__version__ = "1.0.0"
```

Does not expose `config.py` or `sub_package` automatically.

```python
from my_package import main_function, helper_function
print(main_function())  # Output: This is the main function from core.py
print(helper_function())  # Output: This is a helper function from utils.py
```

##### Option 2: Using `__all__` to Define a Public API

```python
# my_package/__init__.py
from .core import main_function
from .utils import helper_function
from .config import VERSION

__all__ = ["main_function", "helper_function", "VERSION"]
```

Does not import `sub_package` unless explicitly done.

```python
from my_package import *  # Only imports what's in __all__
print(main_function())  # Works
print(VERSION)  # Works
```

#### Option 3: Importing Submodules in `__init__.py`

If the package has nested sub-packages that should be directly accessible.

```python
# my_package/__init__.py
from .core import main_function
from .utils import helper_function
from .config import VERSION
from .sub_package import submodule  # Exposing subpackage

__all__ = ["main_function", "helper_function", "VERSION", "submodule"]
```

Be cautious when importing sub-packages as they may depend on the main package and can cause circular imports.

```python
import my_package
print(my_package.submodule.submodule_function())  # Works!
```

## Using `if __name__ == '__main__'`

- The special variable `__name__` is automatically set by Python.
  - When a script is run directly, `__name__` is set to `'__main__'`.
  - When a script is imported as a module, `__name__` is set to the module’s name instead of "`__main__`".
- The `if __name__ == '__main__':` block ensures that specific code only runs when the script is executed directly, not when it is imported.
- This is commonly used for:
  - Writing test code inside a module.
  - Preventing unintended execution when a script is imported.
  - Defining a script entry point.

```python
# myscript.py
def greet():
    print("Hello!")

if __name__ == '__main__':
    greet()  # Runs only if myscript.py is executed directly
```

```python
# another_script.py
import myscript  # greet() does not execute on import
```

```bash
$ python myscript.py  
Hello!

$ python another_script.py  
```

`another_script.py` does not execute `greet()` because the `if __name__ == '__main__':` block prevents it from running when `myscript` is imported.

## Creating a `__main__.py` File in a Package

- A `__main__.py` file allows a package to be executed as a script using `python -m package_name`.
- When a package is run in this way, Python looks for `__main__.py` inside the package and executes it as the entry point.
- This is useful for making a package executable while still allowing its modules to be imported normally.

Package Structure:

```text
my_package/
│── __init__.py
│── __main__.py
│── module.py
```

```python
# my_package/__main__.py
print("Running my_package as a script")
```

Running the Package:

```bash
$ python -m my_package
Running my_package as a script
```

## Implicit Namespace Packages

*Implicit namespace packages* were introduced in PEP 420 (Python 3.3+) to allow package structures without requiring an `__init__.py` file. This enables more flexible package layouts, especially useful for namespace packages, where multiple directories contribute to the same package.

- How Implicit Namespace Packages Work
  - Any directory without an `__init__.py` file that contains Python modules can be treated as a package.
  - The package itself is a namespace package, meaning it may span multiple directories.
  - Python automatically recognizes and loads namespace packages when importing.

### Example: Implicit Namespace Package Structure

```text
namespace_pkg/
│── module1.py
│── sub_pkg/
    │── module2.py
```

No `__init__.py` in namespace_pkg/ or sub_pkg/

```python
# namespace_pkg/module1.py
def func1():
    return "Function 1 from module1"
```

```python
# namespace_pkg/sub_pkg/module2.py
def func2():
    return "Function 2 from module2"
```

Usage:

```python
import namespace_pkg.module1
import namespace_pkg.sub_pkg.module2

print(namespace_pkg.module1.func1())  # Output: Function 1 from module1
print(namespace_pkg.sub_pkg.module2.func2())  # Output: Function 2 from module2
```

Even without `__init__.py`, the package works!

### Namespace Packages Across Multiple Locations

Namespace packages allow multiple directories to contribute to the same package.

Example:

```text
/path1/namespace_pkg/module1.py
/path2/namespace_pkg/module2.py
```

If `/path1` and `/path2` are both in `sys.path`, Python treats `namespace_pkg` as a __merged package__.

### Key Differences: Namespace Package vs. Regular Package

| Feature                      | Regular Package (`__init__.py` exists) | Namespace Package (`__init__.py` missing) |
|------------------------------|:--------------------------------------:|:-----------------------------------------:|
| Defined by                   | Directory with `__init__.py`           | Directory without `__init__.py`           |
| Supports sub-packages        | ✅                                     | ✅                                        |
| Spans multiple locations     | ❌                                     | ✅                                        |
| Listed in `sys.modules`      | ✅                                     | ✅                                        |
| Contains `__file__` attribute| ✅     (points to `__init__.py`)       | ❌    (`__file__` is absent)              |

### When to Use Implicit Namespace Packages

- Large projects where different directories contribute to the same package.
- Namespace packages distributed across multiple locations (e.g., third-party plugins).
- Keeping package structures cleaner by removing unnecessary `__init__.py` files.

Avoid namespace packages if the package needs initialisation logic or metadata like `__file__`.
