#!/usr/bin/python3
"""
Module to find the max integer in a list

Example:
    >>> max_integer([1, 2, 3, 4])
    4
    >>> max_integer([1, 3, 4, 2])
    4
    >>> max_integer([])
    None
    >>> max_integer([-5, -2, -8, -1])
    -1
    >>> max_integer([1, 4, 4, 3])
    4
"""


def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None

    Args:
        lst (list): List of integers.

    Returns:
        int or None: The maximum integer in the list, or None if the list is empty.
    """
    if not lst:
        return None
    result = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > result:
            result = lst[i]
        i += 1
    return result
