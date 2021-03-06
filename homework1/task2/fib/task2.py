"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""
from typing import Sequence


def check_sum_of_neighbors(x: int, y: int, z: int) -> bool:
    return (x + y) == z


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        raise ValueError("Invalid data!")
    while len(data) >= 3:
        a, b, c = data[0], data[1], data[2]
        if not check_sum_of_neighbors(a, b, c):
            return False
        data = data[1:]
    return True
