import hashlib
import random
import struct
import time
from concurrent.futures import ProcessPoolExecutor
from timeit import default_timer as timer


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def benchmark(f):
    def wrapper(*args):
        start = timer()
        result = f(*args)
        end = timer()
        print(f"It took {end - start} seconds!")
        return result

    return wrapper


def get_values():
    return [i for i in range(0, 501)]


@benchmark
def evaluate():
    values = get_values()

    with ProcessPoolExecutor(max_workers=50) as executor:
        results = executor.map(slow_calculate, values)
        print(list(results))


if __name__ == "__main__":
    evaluate()
