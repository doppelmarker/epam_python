from homework1.task4.sum_of_4.task4 import check_sum_of_four


def test_4_sum_positive1():
    assert check_sum_of_four([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
