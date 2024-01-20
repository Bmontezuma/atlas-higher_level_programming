#!/usr/bin/python3

def read_file(filename=""):
    """
    This function reads a file and prints its content to the standard output.
    """
    with open(filename, 'r') as file:
        print(file.read())
