import pytest
from calculator import add


def test_empty_string_returns_zero():
    assert add("") == 0


def test_single_number_returns_value():
    assert add("1") == 1


def test_two_numbers_return_sum():
    assert add("1,2") == 3


def test_multiple_numbers_and_newlines():
    assert add("1,2\n3") == 6


def test_trailing_separator_should_raise_error():
    with pytest.raises(ValueError):
        add("1,2,")
