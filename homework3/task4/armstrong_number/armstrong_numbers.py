"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number
Examples:
- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions
### Example function signature and call
"""

from math import pow
from typing import List


def get_digits(number: int) -> List[int]:
    return [int(digit) for digit in str(number)]


def is_armstrong(number: int) -> bool:
    digits = get_digits(number)
    return number == sum([pow(digit, len(digits)) for digit in digits])
    # return number == sum(map(pow, digits, [len(digits)]*len(digits)))


print(is_armstrong(4679307774))

assert is_armstrong(153) is True, "Is Armstrong number"
assert is_armstrong(10) is False, "Is not Armstrong number"
