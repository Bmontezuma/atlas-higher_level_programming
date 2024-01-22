#!/usr/bin/python3
"""
Module for appending text to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends given text to text file and returns number of characters.

    Args:
        filename (str): The name of the text file.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
