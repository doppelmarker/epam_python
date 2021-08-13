from homework4.task5.fizzbuzz.fizzbuzz import fizzbuzz


def test_fizzbuzz_positive_case01():
    # Arrange
    args = 5
    # Act
    generator = fizzbuzz(args)
    # Assert
    assert list(generator) == [1, 2, "Fizz", 4, "Buzz"]


def test_fizzbuzz_positive_case02():
    # Arrange
    args = 15
    # Act
    generator = fizzbuzz(args)
    # Assert
    assert list(generator) == [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]


def test_fizzbuzz_negative_case01():
    # Arrange
    args = 5
    # Act
    generator = fizzbuzz(args)
    # Assert
    assert list(generator) != [1, 2, "Buzz", 4, "Fizz"]


def test_fizzbuzz_negative_case02():
    # Arrange
    args = 15
    # Act
    generator = fizzbuzz(args)
    # Assert
    assert list(generator) != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
