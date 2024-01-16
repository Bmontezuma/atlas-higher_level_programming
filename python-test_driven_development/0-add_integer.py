#!/usr/bin/python3
"""
This module provides a function to add two integers.

Usage:
    from 0-add_integer import add_integer
    result = add_integer(a, b)

Args:
    a (int or float): The first integer.
    b (int or float): The second integer. Defaults to 98.

Returns:
    int: The sum of a and b.

Raises:
    TypeError: If a or b is not an integer or float.

Example:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer("School")
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or float
    >>> add_integer(None)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer or float
"""


def add_integer(a, b=98):
    """Adds two integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)


if __name__ == "__main__":
    # Example usage
    result = add_integer(3, 4)
    print(result)
