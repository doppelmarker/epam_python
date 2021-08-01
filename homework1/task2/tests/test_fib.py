from homework1.task2.fib.task2 import check_fibonacci


def test_fib_positive1():
    """Testing that the sequence of elements is a fibonacci sequence"""
    assert check_fibonacci([0, 1, 1])


def test_fib_positive2():
    assert check_fibonacci((0, 1, 1, 2, 3, 5, 8))


def test_fib_negative1():
    assert not check_fibonacci([0, 1, 1, 21, 124])
