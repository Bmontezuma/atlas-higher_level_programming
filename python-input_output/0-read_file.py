#!/usr/bin/python3
"""
Defines function to read content of file and print it to the standard output.
"""


def read_file(filename=""):
    """
    A module for reading content of file and print it to the standard output.

    Parameters:
    - filename (str): The name of the file to be read. Default is empty string.

    Returns:
    None

    Examples:
    >>> read_file("example.txt")
    This function reads a file and prints its content to the standard output.
    """
    with open(filename, 'r') as file:
        print(file.read())
