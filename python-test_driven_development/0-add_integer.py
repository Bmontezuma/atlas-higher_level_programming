#!/usr/bin/python3
"""
This module defines a function add_integer that adds two integers.

>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2, 0)  # Corrected test case
2
>>> add_integer(100.3, -2)
98
>>> add_integer(4, "School")
Traceback (most recent call last):
    ...
TypeError: b must be an integer
>>> add_integer(None, 5)  # Corrected test case
Traceback (most recent call last):
    ...
TypeError: a must be an integer
"""


def add_integer(a, b):
    """
    Adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
