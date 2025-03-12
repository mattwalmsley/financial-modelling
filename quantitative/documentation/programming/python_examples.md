# Python Examples

- [Python Examples](#python-examples)
  - [Simple Function Timer](#simple-function-timer)
  - [Function Timer Decorator](#function-timer-decorator)
  - [Logging Decorator](#logging-decorator)

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

## Function Timer Decorator

```python
def timed(func):
    from time import perf_counter
    from functools import wraps

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = [f"{k}={v}" for k, v in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ', '.join(all_args)
        print(f"{func.__name__}({args_str}) took {elapsed:.6f}s to run.")

        return result

    return wrapper

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(fib_loop(100))
# output:
# fib_loop(100) took 0.000004s to run.
# 354224848179261915075


from functools import reduce

@timed
def fib_reduce(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-1), [0, 1])[-1]

print(fib_reduce(100))
# output:
# fib_reduce(100) took 0.000053s to run.
# 354224848179261915075
```

## Logging Decorator

```python
def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def wrapper(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{run_dt}: called {fn.__name__}')
        return result

    return wrapper

@logged
def add(x, y):
    return x + y

print(add(1, 2))
# output:
# 2021-08-02 14:00:00.000000+00:00: called add
```