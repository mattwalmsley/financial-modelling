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