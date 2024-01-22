#!/usr/bin/python3
"""
Module for writing content to a text file.
"""


def write_file(filename="", text=""):
    """
    Writes given text to text file and returns number of characters.

    Args:
        filename (str): The name of the text file.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    write_file("my_first_file.txt", "This School is so cool!\n")
