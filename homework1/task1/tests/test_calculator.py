from homework1.task1.calculator.calc import check_power_of_2


def test_positive_case1():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_positive_case2():
    assert check_power_of_2(1)


def test_negative_case1():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)


def test_negative_case2():
    assert not check_power_of_2(0)
