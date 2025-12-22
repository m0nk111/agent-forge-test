import pytest
from string_utils import reverse, capitalize_words


@pytest.mark.parametrize("input_text, expected", [
    ("hello", "olleh"),
    ("", ""),
    ("123", "321"),
    ("ab12", "21ba"),
    ("Hello World", "dlroW olleH"),
])
def test_reverse(input_text, expected):
    assert reverse(input_text) == expected


def test_reverse_non_string_raises_type_error():
    with pytest.raises(TypeError, match="Input must be a string."):
        reverse(123)


@pytest.mark.parametrize("input_text, expected", [
    ("hello world", "Hello World"),
    ("   test   case   ", "Test Case"),
    ("", ""),
    ("multiple   spaces", "Multiple Spaces"),
    ("single", "Single"),
    ("123 abc", "123 Abc"),
    ("camelCase", "Camelcase"),
])
def test_capitalize_words(input_text, expected):
    assert capitalize_words(input_text) == expected


def test_capitalize_words_non_string_raises_type_error():
    with pytest.raises(TypeError, match="Input must be a string."):
        capitalize_words(123)