#!/usr/bin/python3
"""
This module reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    This function reads a file and prints its content to the standard output.
    """
    with open(filename, 'r') as file:
        print(file.read())
