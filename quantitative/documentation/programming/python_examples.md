# Python Examples

- [Python Examples](#python-examples)
  - [Simple Function Timer](#simple-function-timer)

## Simple Function Timer

```python
import time

def time_it(func, *args, rep=1, **kwargs):
        start = time.perf_counter()
        for i in range(rep):
            func(*args, **kwargs)
        end = time.perf_counter()
        return (end - start) / rep

def compute_powers_1(n, *, start=1, end):
    # Using a for loop
    result = []
    for i in range(start, end):
        result.append(n**i)
    return result

def compute_powers_2(n, *, start=1, end):
    # Using list comprehension
    return [n**i for i in range(start, end)]

def compute_powers_3(n, *, start=1, end): 
    # Using generator expression (doesn't actually compute the powers)
    return (n**i for i in range(start, end))

def compute_powers_3_list(n, *, start=1, end): 
    # Compute the powers by returning a list
    return list(compute_powers_3(n, start=start, end=end))

print(time_it(compute_powers_1, 2, start=0, end=20000, rep=5)) # 0.6105392131999906
print(time_it(compute_powers_2, 2, start=0, end=20000, rep=5)) # 0.5973786137999924

print(time_it(compute_powers_3, 2, start=0, end=20000, rep=5)) # 1.508999957877677e-06
print(time_it(compute_powers_3_list, 2, start=0, end=20000, rep=5)) # 0.5008902788000341
```
