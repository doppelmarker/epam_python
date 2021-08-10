from functools import lru_cache
from timeit import default_timer as timer
from typing import Callable


def memoize(f, k):
    mem_f = lru_cache(maxsize=k)(f)
    return mem_f


def cache(f: Callable) -> Callable:
    return memoize(f, 2)


def func(a, b):
    return (a ** b) ** 2


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main():
    values = 50, 400
    cache_func = cache(func)

    res1 = cache_func(*values)
    start = timer()
    res2 = cache_func(*values)
    end = timer()
    print(res1 is res2, end - start)

    res3 = func(*values)
    start = timer()
    res4 = func(*values)
    end = timer()
    print(res3 is res4, end - start)

    cache_func = cache(fib)
    n = 30
    res1 = cache_func(n)
    start = timer()
    res2 = cache_func(n)
    end = timer()
    print(res1 is res2, end - start)

    res3 = fib(n)
    start = timer()
    res4 = fib(n)
    end = timer()
    print(res3 is res4, end - start)

    print(res1, res2)
    print(res1 == res2)


if __name__ == "__main__":
    main()
