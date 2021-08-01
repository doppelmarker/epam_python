import os

from homework1.task3.max_min.task3 import find_maximum_and_minimum


def test_max_min_positive1():
    cur_path = os.path.dirname(__file__)
    assert find_maximum_and_minimum(os.path.join(cur_path, "../max_min/some_file1.txt")) == (10, 0)


def test_max_min_positive2():
    cur_path = os.path.dirname(__file__)
    assert find_maximum_and_minimum(os.path.join(cur_path, "../max_min/some_file2.txt")) == (198, -10)
