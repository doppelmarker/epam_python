import hashlib
import random
import struct
import time
from multiprocessing import Pool
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
    pool = Pool(processes=30)
    results = pool.map(slow_calculate, values)
    print(results)


if __name__ == "__main__":
    evaluate()
