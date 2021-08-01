from homework1.task5.k_max.task5 import find_maximal_subarray_sum


def test_max_sum_positive1():
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3) == 18
