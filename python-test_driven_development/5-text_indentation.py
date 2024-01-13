#!/usr/bin/python3


def text_indentation(text):
    """
    Print a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char

        if char in separators:
            print(current_line.strip())
            print()  # Print an empty line after the separator
            current_line = ""

    if current_line:
        print(current_line.strip())
