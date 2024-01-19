#!/usr/bin/python3
"""
Module: 3-is_kind_of_class

This module defines a function is_kind_of_class that checks if an object is an
instance of, or if the object is an instance of a class that inherited from,
the specified class.

Usage:
    is_kind_of_class = __import__('3-is_kind_of_class').is_kind_of_class

    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of
    a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if obj is an instance of a_class or its subclass, otherwise False.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
