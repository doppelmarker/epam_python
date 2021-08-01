"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file1.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    all_numbers = []
    with open(file_name) as file:
        for line in file:
            line_numbers = [int(num) for num in line.split(" ")]
            all_numbers += line_numbers
    return max(all_numbers), min(all_numbers)
