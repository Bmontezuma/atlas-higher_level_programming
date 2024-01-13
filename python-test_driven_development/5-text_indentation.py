#!/usr/bin/python3
"""
This module has function to print text with 2 new lines after each: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

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
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
