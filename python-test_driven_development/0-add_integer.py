#!/usr/bin/python3
"""
This module defines the add_integer function.

The function adds two integers.

"""


def add_integer(a, b=98):
    """
    Add two integers.

    Arguments:
    a (int or float): The first number.
    b (int or float, default: 98): The second number.

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    return int(a) + int(b)
