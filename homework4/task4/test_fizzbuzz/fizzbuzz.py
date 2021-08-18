"""
This is the "fizzbuzz" module.
The fizzbuzz module supplies one function, fizzbuzz(n). For example,
>>> list(fizzbuzz(5))
[1, 2, 'Fizz', 4, 'Buzz']
"""


def fizzbuzz(n):
    """
    Return a generator, which yields
    elements of fizzbuzz sequence in the interval [1; n].
    >>> list(fizzbuzz(15))
    [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
    >>> list(fizzbuzz(-1))
    Traceback (most recent call last):
       ...
    ValueError: n must be >= 1
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    fizzes = [""] + ([""] * 2 + ["Fizz"]) * 33 + [""]
    buzzes = [""] + ([""] * 4 + ["Buzz"]) * 20
    for i in range(1, n + 1):
        yield fizzes[i] + buzzes[i] or i


if __name__ == "__main__":
    import doctest

    doctest.testmod()
