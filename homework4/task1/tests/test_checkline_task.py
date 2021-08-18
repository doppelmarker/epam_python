import os

import pytest

from homework4.task1.fileread.fileread import *

"""
If first line is a number return true if number in an interval [1, 3)*
and false otherwise.
In case of any error, a ValueError should be thrown.
"""


@pytest.fixture()
def file():
    filename = "testfile.txt"
    file = open(filename, mode="w+")
    yield file
    file.close()
    os.remove(filename)


def write_and_read(data, file):
    file.write(data)
    file.seek(0)
    line = file.readline()
    return line


def test_checkline_included_in_interval_positive_number_in_file(file):
    data = "1"

    line = write_and_read(data, file)

    expected = True
    actual = checkline(line)

    assert actual == expected


def test_checkline_not_included_in_interval_positive_number_in_file(file):
    data = "3"

    line = write_and_read(data, file)

    expected = False
    actual = checkline(line)

    assert actual == expected


def test_checkline_not_included_in_interval_negative_number_in_file(file):
    data = "-1"

    line = write_and_read(data, file)

    expected = False
    actual = checkline(line)

    assert actual == expected


def test_checkline_not_number_in_file(file):
    data = "abc"

    line = write_and_read(data, file)

    with pytest.raises(ValueError):
        checkline(line)
