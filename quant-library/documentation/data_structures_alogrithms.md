# Data Structures and Algorithms

## Introduction

### Big O Notation

Big O notation is a mathematical tool used in computer science to describe the efficiency of algorithms. It focuses on the upper bound of an algorithm's runtime as the input size increases. In simpler terms, it tells us how long an algorithm will take to execute for larger datasets.

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
