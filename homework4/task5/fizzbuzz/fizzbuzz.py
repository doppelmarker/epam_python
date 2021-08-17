from typing import Generator

fizzes = [""] + ([""] * 2 + ["Fizz"]) * 33 + [""]
buzzes = [""] + ([""] * 4 + ["Buzz"]) * 20


def fizzbuzz(n: int) -> Generator[str, None, None]:
    for i in range(1, n + 1):
        yield fizzes[i] + buzzes[i] or i


for element in fizzbuzz(100):
    print(element)
