#!/usr/bin/python3


def append_write(filename="", text=""):
    """
    Appends text to a file and returns the added character count.

    Parameters:
    - filename (str): Target file. Default is an empty string.
    - text (str): String to append. Default is an empty string.

    Returns:
    int: Number of characters added.

    Example:
    >>> append_write("file_append.txt", "This School is so cool!\n")
    24
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
        return len(text)
