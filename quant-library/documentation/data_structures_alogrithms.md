# Data Structures and Algorithms

## Introduction

Data structures and algorithms constitute fundamental concepts in computer science, forming the backbone of efficient software development.

Data structures serve as containers holding data in a structured format, enabling efficient storage, retrieval, and manipulation. Common examples include arrays, linked lists, stacks, queues, trees, graphs, and hash tables, each with distinct characteristics suited for various tasks.

Algorithms, on the other hand, are step-by-step procedures or recipes for solving computational problems. They define the logic and operations necessary to execute specific tasks, ranging from simple sorting and searching techniques to complex graph traversal and optimization algorithms. Efficient algorithms are crucial for solving problems in a timely manner.

Throughout these notes, various data structures and algorithms will be explored using examples written in Python, a versatile and widely-used programming language.

## Big O Notation

Big O notation is a mathematical tool used in computer science to describe the efficiency of algorithms. It focuses on the upper bound of an algorithm's runtime as the input size increases. In simpler terms, it tells us how long an algorithm will take to execute for larger datasets in the worst case scenario - e.g. having an array of descending integers and running a sorting algorithm to arrange integers in ascending order.

### $O(1)$

Constant time complexity. The algorithm's runtime or space usage does not depend on the input size.

```python
def constant_algo(items):
    return items[0]
```

### $O(n)$

Linear time complexity. The runtime or space usage grows linearly with the input size.

```python
def linear_algo(items):
    for item in items:
        print(item)
```

### $O(n^{2})$

Quadratic time complexity. Common in algorithms that involve nested iterations over the input data.

```python
def quadratic_algo(items):
    for item1 in items:
        for item2 in items:
            print(item1, item2)
```

### $O(\log n)$

Logarithmic time complexity. Commonly seen in algorithms that halve the search space in each step, such as binary search.

```python
def binary_search_algo(items, target):
    low, high = 0, len(items) - 1
    while low <= high:
        mid = (low + high) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

### $O(n \log n)$

Log-linear time complexity. Often seen in efficient sorting algorithms like mergesort and quicksort.

```python
def merge_sort_algo(items):
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left_half = merge_sort_algo(items[:mid])
    right_half = merge_sort_algo(items[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right
```

### $O(2^{n})$

Exponential time complexity. Typically found in algorithms that solve problems through brute force or recursion.

```python
def naive_fibonacci(n):
  if n <= 1:
    return n
  return naive_fibonacci(n-1) + naive_fibonacci(n-2)
```

### $O(n!)$

Factorial time complexity. The worst-case scenario for algorithms that generate all permutations of a set.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
```

## Data Structures

### Arrays

- Arrays are fundamental data structures in programming used to store collections of elements of the same type.
- They provide a *contiguous block of memory* to hold multiple variables.
- Arrays are widely used due to their efficiency in accessing elements by index and their ability to store data in a structured and ordered manner.

#### Visualizing Array in Memory

- A *contiguous block of memory* refers to a consecutive sequence of memory locations that are allocated to store the elements of the array.
- When an array is created, the programming language allocates a block of memory that is large enough to hold all the elements of the array.
  - The elements are stored in adjacent memory locations, meaning that the memory addresses of consecutive elements are contiguous, with no gaps between them.
- This contiguous arrangement allows for efficient access to array elements by index, as the position of each element in memory can be calculated based on its index and the size of each element.
  - Accessing adjacent memory locations typically results in better cache locality, which can lead to improved performance when accessing array elements sequentially.

#### Characteristics of Arrays

- **Fixed Size**: In most programming languages, the size of an array is fixed at the time of declaration and cannot be changed dynamically.  
- **Homogeneous Elements**: All elements in an array must be of the same data type.
- **Indexed Access**: Elements in an array can be accessed using their index positions, typically starting from 0.

##### Why Array Indexes Start from 0

In computer science, array indexes conventionally start from 0 rather than 1. This convention is deeply rooted in the history and design of programming languages and memory management systems. Several reasons contribute to this choice:

1. **Memory Address Calculation**: Because arrays are typically implemented as contiguous blocks of memory,starting the index from 0 simplifies memory address calculation. The memory address of the first element is the base address of the array, without any offset.
2. **Pointer Arithmetic**: Treating the first element as the base (0 offset) aligns with pointer arithmetic, where adding 0 to a pointer results in the pointer pointing to the first element.
3. **Consistency with Mathematical Notation**: In mathematics and formal logic, sequences are often represented using 0-based indexing so aligning array indexing with mathematical notation enhances consistency and ease of understanding for programmers familiar with mathematical concepts.
4. **Historical Influence**: Early programming languages like C, which heavily influenced subsequent languages, adopted 0-based indexing.

While some programming languages and systems deviate from the convention of 0-based indexing (e.g. MATLAB and R, which use 1-based indexing), the prevalence of 0-based indexing in mainstream programming languages underscores its importance and practical benefits.

#### One-dimensional Array

A linear array that stores elements in a single row or column.

```python
# Creating a one-dimensional array
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])  # Output: 1

# Modifying elements
numbers[2] = 10
print(numbers)  # Output: [1, 2, 10, 4, 5]
```

For an array of integers in Python, where each integer takes up 4 bytes (32 bits), the memory allocation can be  visualized as follows:

- The array `numbers` starts at memory address `0x1000`.
- Memory addresses are contiguous, with no gaps between them.
- Accessing `numbers[0]` corresponds to memory location `0x1000`.
- Accessing `numbers[1]` corresponds to memory location `0x1004`, and so on.

|  0x1000   |  0x1004  |  0x1008  |  0x100C  |  0x1010  |
|:---------:|:--------:|:--------:|:--------:|:--------:|
|     1     |    2     |    3     |    4     |    5     |

#### Multi-dimensional Array

Arrays that store elements in multiple rows and columns, forming a matrix-like structure.

```python
# Creating a multi-dimensional array (2D)
#  1 2 3
#  4 5 6
#  7 8 9

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0][1])  # Output: 2

# Modifying elements
matrix[1][2] = 10
print(matrix)  # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
```

- Multi-dimensional arrays are typically allocated in memory by either *row-major order* or *column-major order*.
- The choice between row-major and column-major order can impact performance depending on the access patterns of the algorithm being executed.
  - For example, row-major order may provide better performance for algorithms that iterate over rows, while column-major order may be better for algorithms that iterate over columns.

##### Row-Major Order

- For multi-dimensional arrays that are allocated in row-major order, the elements of each row are stored sequentially in memory.
- Successive rows are stored one after the other.
- C, C++, and Python (NumPy) typically use row-major order.
- The first row `[1, 2, 3]` starts at memory address `0x1000` and continues for 12 bytes (3 integers of 4 bytes each).
- The second row `[4, 5, 6]` starts immediately after the first row at memory address `0x100C` and continues for 12 bytes.
- The third row `[7, 8, 9]` follows the second row at memory address `0x1018` and continues for 12 bytes.
- Each integer takes up 4 bytes of memory, and they are stored sequentially in memory.
- Memory addresses are contiguous, with no gaps between them.

|   0x1000  |  0x1004  |  0x1008  |  0x100C  |  0x1010  |  0x1014  |  0x1018  |  0x101C  |  0x1020  |
|:---------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|     1     |     2    |     3    |     4    |     5    |     6    |     7    |     8    |     9    |

##### Column-Major Order

- For multi-dimensional arrays that are allocated in column-major order, the elements of each column are stored sequentially in memory.
- Successive columns are stored one after the other.
- Fortran and MATLAB typically use column-major order.
- In this example, the first column `[1, 4, 7]` starts at memory address `0x1000` and continues for 12 bytes (3 integers * 4 bytes each).
- The second column `[2, 5, 8]` follows the first column at memory address `0x100C` and continues for 12 bytes.
- The third column `[3, 6, 9]` follows the second column at memory address `0x1018` and continues for 12 bytes.
- Each integer takes up 4 bytes of memory, and they are stored sequentially in memory.
- Memory addresses are contiguous, with no gaps between them.

|   0x1000  |  0x1004  |  0x1008  |  0x100C  |  0x1010  |  0x1014  |  0x1018  |  0x101C  |  0x1020  |
|:---------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|:--------:|
|     1     |     4    |     7    |     2    |     5    |     8    |     3    |     6    |     9    |

#### Operations on Arrays

- **Accessing**: Retrieving elements from an array by their index position.
- **Traversal**: Iterating through all elements of the array.
- **Insertion**: Adding new elements to the array.
- **Deletion**: Removing elements from the array.

```python
# Traversal
for num in numbers:
    print(num)

# Output:
# 1
# 2
# 10
# 4
# 5

# Insertion
numbers.append(6)
print(numbers)  # Output: [1, 2, 10, 4, 5, 6]

# Deletion
del numbers[2]
print(numbers)  # Output: [1, 2, 4, 5, 6]
```

- Accessing Arrays
  - **Access Time**: Accessing elements by index is constant time $O(1)$ since the memory address can be calculated based on the index.
- Traversing Arrays
  - **Sequential Access**: Traversing arrays sequentially is $O(n)$ and efficient due to the contiguous memory allocation.
  - **Cache Locality**: Sequential access patterns exhibit good cache locality, enhancing performance.
- Inserting Items
  - **Shift Operations**: When inserting an item in the middle of an array, elements after the insertion point need to be shifted to accommodate the new item.
  - **Memory Overhead**: Shifting elements can be costly, especially for large arrays, leading to inefficient memory usage.
  - **Complexity**: Insertion in the middle of an array is $O(n)$ due to shifting, where n is the number of elements after the insertion point.
- Deleting Items
  - **Shift Operations**: Similar to insertion, deleting an item from the middle of an array requires shifting elements after the deletion point.
  - **Memory Overhead**: Shifting elements can lead to memory fragmentation and inefficient memory usage.
  - **Complexity**: Deletion in the middle of an array is $O(n)$ due to shifting, where n is the number of elements after the deletion point.
- Memory Reallocation (Dynamic Arrays)
  - **Resizing Arrays**: Dynamic arrays automatically handle memory reallocation when capacity is exceeded.
  - **Amortized Complexity**: Insertion at the end of a dynamic array is typically amortized $O(1)$ due to occasional resizing operations.
  - **Resizing Strategy**: Common strategies include doubling the capacity or increasing by a constant factor to reduce frequent reallocations.

### Linked Lists

### Hashing (Dictionaries)

#### Using Arrays

- This is $O(n)$

```python
class MyDictionary:
    def __init__(self):
        self.entries = []
    
    def add(self, key, value):
        for entry in self.entries:
            if entry[0] == key:
                entry[1] = value
                return
        self.entries.append([key, value])
    
    def get(self, key):
        for entry in self.entries:
            if entry[0] == key:
                return entry[1]
        raise KeyError("Key '{}' not found".format(key))

# Example usage:
my_dict = MyDictionary()
my_dict.add("apple", 10)
my_dict.add("banana", 20)
print(my_dict.get("apple"))  # Output: 10
```

#### Using Hashing

- This is $O(1)$

```python
class MyDictionary:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.entries = [None] * self.capacity
    
    def add(self, key, value):
        index = hash(key) % self.capacity
        if self.entries[index] is None:
            self.entries[index] = (key, value)
        else:
            raise ValueError("Key '{}' already exists".format(key))
    
    def get(self, key):
        index = hash(key) % self.capacity
        entry = self.entries[index]
        if entry is not None and entry[0] == key:
            return entry[1]
        raise KeyError("Key '{}' not found".format(key))

# Example usage:
my_dict = MyDictionary()
my_dict.add("apple", 10)
my_dict.add("banana", 20)
print(my_dict.get("apple"))  # Output: 10
```