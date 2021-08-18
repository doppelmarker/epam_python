import os

import pytest

from homework4.task2.openurl.openurl import *


@pytest.fixture(scope="module")
def content():
    # Correct reading of file!!!
    file = open(os.path.join(os.path.dirname(__file__), "mocked_content.txt"), "r")
    yield file.read()
    file.close()


def test_count_i_occurrences_positive_mocked(mocker, content):
    mocker.patch("homework4.task2.openurl.openurl.request_url", return_value=content)
    url = "https://example.com/"

    expected_occurrences = 59
    actual_occurrences = count_i_occurrences(url)

    assert expected_occurrences == actual_occurrences


def test_count_i_occurrences_negative_mocked(mocker, content):
    mocker.patch("homework4.task2.openurl.openurl.request_url", return_value=content)
    url = "https://example.com/"

    expected_occurrences = 200
    actual_occurrences = count_i_occurrences(url)

    assert expected_occurrences != actual_occurrences


def test_count_i_occurrences_positive_not_mocked():
    url = "https://example.com/"

    expected_occurrences = 59
    actual_occurrences = count_i_occurrences(url)

    assert expected_occurrences == actual_occurrences


def test_count_i_occurrences_should_raise_value_error_when_unreachable_url():
    url = "fgdadasdagrggdthadsfsdf"

    with pytest.raises(ValueError):
        count_i_occurrences(url)
