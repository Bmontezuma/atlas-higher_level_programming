#!/usr/bin/python3


def read_file(filename=""):
    """
    A simple module for reading the content of a file and printing it to the standard output.

    Parameters:
    - filename (str): The name of the file to be read. Default is an empty string.

    Returns:
    None

    Examples:
    >>> read_file("example.txt")
    This function reads a file and prints its content to the standard output.
    """
    with open(filename, 'r') as file:
        print(file.read())
