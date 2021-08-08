import os
from functools import reduce, wraps
from timeit import default_timer as timer


def save(filename):
    def wrapper(f):
        @wraps(f)
        def substitute(*args):
            result = f(*args)
            with open(filename, mode="a") as file:
                if os.stat(filename).st_size != 0:
                    file.write("\n")
                file.write(str(result))
            return result

        return substitute

    return wrapper


def custom_cache(f):
    cache = dict()

    @wraps(f)
    def wrapper(*args):
        if args in cache:
            print("Restored from cache")
            return cache[args]
        else:
            result = f(*args)
            print("Evaluated")
            cache[args] = result
            return result

    return wrapper


def benchmark(f):
    def wrapper(*args):
        start = timer()
        result = f(*args)
        end = timer()
        print(f"It took {end - start} seconds!")
        return result

    return wrapper


@custom_cache
@save(filename="results.txt")
def sum_numbers(*args):
    """Summarize numbers"""
    return sum(args)


@custom_cache
@save(filename="results.txt")
def multiply_numbers(*args):
    """Multiply numbers"""
    return reduce(lambda a, b: a * b, args)


@benchmark
@custom_cache
@save(filename="fib.txt")
def fib(n):
    """Find n-th fibonacci number"""
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


print(fib(300))
