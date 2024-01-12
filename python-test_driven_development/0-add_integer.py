#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a (int or float): The first integer or float.
        b (int or float): The second integer or float

    Returns:
        int: Addition of a and b

    Raises:
        TypeError: If not integer or float
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
