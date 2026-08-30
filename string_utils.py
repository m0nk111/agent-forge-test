"""String utility functions for reversing and capitalizing words."""

def reverse(text: str) -> str:
    """Reverse the input string.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return text[::-1]


def capitalize_words(text: str) -> str:
    """Capitalize each word in the input string.

    Args:
        text (str): The input string containing words to be capitalized.

    Returns:
        str: The input string with each word capitalized.

    Raises:
        TypeError: If input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    return ' '.join(word.capitalize() for word in text.split())