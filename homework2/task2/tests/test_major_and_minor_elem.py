from homework2.task2.most_least_common.most_least_common import major_and_minor_elem


def test_major_and_minor_elem01():
    assert major_and_minor_elem([1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 2, 2, 2]) == (6, 3)


def test_major_and_minor_elem02():
    assert major_and_minor_elem([3, 1, 1, 2, 2]) == (2, 1)
