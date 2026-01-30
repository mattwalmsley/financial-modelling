# Interview Preparation

- [Interview Preparation](#interview-preparation)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
  - [Object-Orientated Programming](#object-orientated-programming)
    - [Classes versus Objects](#classes-versus-objects)
  - [C#](#c)
    - [Reference versus Value types](#reference-versus-value-types)
    - [Usage of ref and out Parameters](#usage-of-ref-and-out-parameters)
    - [Destructors](#destructors)
    - [Non-Generic Collection Types](#non-generic-collection-types)
      - [`ArrayList`](#arraylist)
      - [`Hashtable`](#hashtable)
      - [`Queue`](#queue)
      - [`Stack`](#stack)
      - [`SortedList`](#sortedlist)
      - [`SortedDictionary`](#sorteddictionary)
    - [Indexers](#indexers)
  - [Python](#python)
    - [Mutable and Immutable Types](#mutable-and-immutable-types)
    - [Time Complexity of Common Python Data Structures](#time-complexity-of-common-python-data-structures)
      - [List](#list)
      - [Dictionary](#dictionary)
        - [Notes on Common Dictionary Operations](#notes-on-common-dictionary-operations)
        - [Other Dictionary Operations](#other-dictionary-operations)
        - [Valid Keys for Dictionary Types](#valid-keys-for-dictionary-types)
      - [Set](#set)
        - [Set Operations and Time Complexity](#set-operations-and-time-complexity)
        - [Note on Set Sizes](#note-on-set-sizes)

## Data Structures

## Algorithms

## Object-Orientated Programming

### Classes versus Objects

- **Class**: A blueprint defining properties and methods for objects, outlining what objects created from the class will contain and can do.
- **Object**: An *instance* of a class, a concrete entity with actual values for properties, capable of performing actions defined by the class.

## C\#

### Reference versus Value types

- **Reference types**: Store a reference (memory address) to the actual data, which is allocated on the *heap*. Multiple variables can point to the same object in memory, so changes to one variable affect all others referencing that object. Examples include classes, arrays, and strings.
- **Value types:** Store the actual data directly on the *stack*, meaning each variable has its own copy. Changes made to one variable do not affect others. Examples include `struct`, `enum`, and primitive types like `int`, `bool`, and `double`.

### Usage of ref and out Parameters

- `ref`: Passes a reference to an existing variable, allowing the method to modify the variable directly. The variable must be initialized before being passed to the method, ensuring it already holds a value that the method can work with.
- `out`: Must be initialized inside the method before returning, allowing the method to output a value. The variable passed to the method does not need to be initialized beforehand.

### Destructors

- A special method in C# that is called automatically when an object is being garbage collected. - Used to perform cleanup operations, such as releasing unmanaged resources.
- A destructor has the same name as the class, prefixed with a tilde, `~`, and cannot be called directly or have parameters.
- Destructors are rarely needed in C# because the garbage collector automatically handles memory management. For managing unmanaged resources, it's better to implement the IDisposable interface and use the Dispose method.

```csharp
class Example {

  ~Example() {
    Console.WriteLine("Destructor has been called.");
  }
}
```

### Non-Generic Collection Types

#### `ArrayList`

A dynamically resizing array that can store items of any type. It provides methods to add, remove, and search for items.

```csharp
ArrayList list = new ArrayList();
list.Add(1);
list.Add("Hello");
list.Add(3.14);
```

#### `Hashtable`

A collection that stores key-value pairs, where keys and values can be of any type. It provides quick access to values based on keys.

```csharp
Hashtable table = new Hashtable();
table["key1"] = "value1";
table["key2"] = 42;
```

#### `Queue`

A first-in, first-out (FIFO) collection that stores items in the order they are added.

```csharp
Queue queue = new Queue();
queue.Enqueue(1);
queue.Enqueue(2);
int item = (int)queue.Dequeue();
```

#### `Stack`

A last-in, first-out (LIFO) collection that stores items in the reverse order they are added.

```csharp
Stack stack = new Stack();
stack.Push(1);
stack.Push(2);
int item = (int)stack.Pop();
```

#### `SortedList`

A collection that stores key-value pairs sorted by the keys in ascending order based on their natural ordering (e.g., numerical order for numbers, alphabetical order for strings). Keys and values can be of any type, and the list maintains the order of keys, allowing fast lookups and retrieval of items in sorted order.

```csharp
SortedList sortedList = new SortedList();
sortedList.Add("key1", "value1");
sortedList.Add("key2", 42);
```

#### `SortedDictionary`

A collection that stores key-value pairs sorted by the keys. Similar to SortedList, but uses a dictionary-based approach, providing efficient lookups, insertions, and deletions.

```csharp
SortedDictionary<string, int> sortedDict = new SortedDictionary<string, int>();
sortedDict["key1"] = 1;
sortedDict["key2"] = 2;
```

### Indexers

- Allow objects to be indexed in a similar way to arrays. They enable access to elements within an object using square brackets `[]`.
- An indexer is defined with the `this` keyword followed by parameters within square brackets. The parameters typically represent indices, and the return type specifies the type of data the indexer will return.
- Multiple indexers can be defined in the same class, as long as they have different parameter types.

```csharp
public class SampleCollection
{
    private string[] elements = new string[10];

    // Indexer definition
    public string this[int index]
    {
        get { return elements[index]; }
        set { elements[index] = value; }
    }
}
```

## Python

### Mutable and Immutable Types

- **Mutable Types**: Objects that can be changed after they are created. Examples include lists, dictionaries, and sets.
  - Example:

    ```python
    my_list = [1, 2, 3]
    my_list.append(4)  # my_list is now [1, 2, 3, 4]
    ```

- **Immutable Types**: Objects that cannot be changed after they are created. Examples include integers, floats, strings, and tuples.
  - Example:

    ```python
    my_tuple = (1, 2, 3)
    # my_tuple[0] = 4  # This will raise a TypeError
    ```

### Time Complexity of Common Python Data Structures

#### List

| Operation                 | Time Complexity | Notes                   |
| ------------------------- | --------------- | ----------------------- |
| `my_list.append(item)`    | **O(1)**        | Fast                    |
| `my_list.pop()`           | **O(1)**        | Fast                    |
| `my_list.insert(0, item)` | **O(n)**        | Slow (shifts all items) |
| `my_list.pop(0)`          | **O(n)**        | Slow (shifts all items) |
| `my_list[index]`          | **O(1)**        | Fast                    |
| `item in my_list`         | **O(n)**        | Slow (requires looping) |

Use `collections.deque` for fast operations at the beginning of a sequence.

#### Dictionary

Dictionaries are meant for grouping or accumulating values based on a key. Python "dictionaries" are called hash maps (or sometimes "associative arrays") in many other programming languages.

| Operation                     | Time Complexity | Notes                    |
| ----------------------------- | --------------- | ------------------------ |
| `mapping[key] = value`        | **O(1)**        | Inserting/updating       |
| `mapping[key]`                | **O(1)**        | Reading/Lookup           |
| `mapping.get(key)`            | **O(1)**        | Safe Lookup              |
| `mapping.pop(key)`            | **O(1)**        | Remove and Return        |
| `key in mapping`              | **O(1)**        | Membership test          |
| `for k, v in mapping.items()` | **O(n)**        | Explicit looping is slow |

Hashing ensures dictionaries are very fast at all operations related to key lookups.

##### Notes on Common Dictionary Operations

- **Inserting/updating** requires a hash lookup to find the key's position, and if it's a new key, it might involve updating the hash table's structure slightly.
- **Reading/Lookup** is extremely efficient. It's a direct lookup and is nearly as fast as the membership test.
- **Safe Lookup** is similar to `mapping[key]`, but with a slight overhead due to the default value handling mechanism.
- **Remove and Return** involves a lookup to find the key, removal from the hash table, and sometimes reorganization, which can make it marginally slower than the others.
- **Membership tests** are typically the fastest operation. This involves a direct hash lookup without modifying the dictionary.

##### Other Dictionary Operations

| Operation                   | Time Complexity | Explanation       |
| --------------------------- | --------------- | ----------------- |
| `next(iter(mapping))`       | **O(1)**        | Get first item    |
| `next(reversed(mapping))`   | **O(1)**        | Get last item     |
| `value in mapping.values()` | **O(n)**        | Value containment |
| `mapping.update(iterable)`  | **O(k)**        | Add **k** items   |

Key lookups are **O(1)**, but value lookups (`value in my_dict.values()`) are **O(n)** due to looping over the whole dictionary.

##### Valid Keys for Dictionary Types

- Dictionary keys must be of a type that is hashable and immutable. Common valid key types include:
  - Integers
  - Floats
  - Strings
  - Tuples (if they contain only hashable types)

  - Example:

    ```python
    my_dict = {
        1: "integer key",
        3.14: "float key",
        "key": "string key",
        (1, 2): "tuple key"
    }
    ```

  - Invalid keys:

    ```python
    # my_dict = {[1, 2]: "list key"}  # This will raise a TypeError because lists are mutable
    ```

#### Set

| Operation              | Time Complexity | Notes                 |
| ---------------------- | --------------- | --------------------- |
| `my_set.add(item)`     | **O(1)**        | Add (no error raised) |
| `my_set.remove(item)`  | **O(1)**        | Remove (error raised) |
| `my_set.discard(item)` | **O(1)**        | Safe Remove           |
| `item in my_set`       | **O(1)**        | Membership test       |
| `for item in my_set:`  | **O(n)**        | For sets of size n    |

##### Set Operations and Time Complexity

| Big O    | Operation      | Explanation               |
| -------- | -------------- | ------------------------- |
| **O(n)** | `set1 & set2`  | **Intersection**          |
| **O(n)** | `set1 \| set2` | **Union**                 |
| **O(n)** | `set1 ^ set2`  | **Symmetric Difference**  |
| **O(n)** | `set1 - set2`  | **Asymmetric Difference** |

##### Note on Set Sizes

The `O(n)` complexity of these operations assumes that the sets are of the same size. If the sets are different sizes:

- **Intersection (`set1 & set2`)**:
  - Returns elements common to both sets. The complexity depends on the size of the smaller set.
  - The operation only needs to iterate through the smaller set and check for membership in the larger set. Therefore, complexity is proportional to the size of the smaller set.
- **Union (`set1 | set2`)**:
  - Combines all unique elements from both sets. The complexity depends on the size of the larger set.
  - The operation combines all elements from both sets. Complexity depends on the larger set because all elements must be added to the result.
- **Symmetric Difference (`set1 ^ set2`)**:
  - Returns elements in either set but not in both. Complexity depends on the size of both sets.
  - The complexity depends on both set sizes since all elements from both sets are checked and processed.
- **Asymmetric Difference (`set1 - set2`)**:
  - Returns elements in `set1` that are not in `set2`. Complexity depends on the size of `set1`.
  - The operation iterates through `set1` and removes elements present in `set2`. Complexity depends on the size of `set1`.

Using smaller or well-partitioned sets can improve efficiency for large-scale computations.
