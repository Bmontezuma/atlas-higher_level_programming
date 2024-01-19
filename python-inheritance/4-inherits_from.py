#!/usr/bin/python3
"""
Module: 4-inherits_from

This module defines a function inherits_from that checks if an object is an
instance of a class that inherited (directly or indirectly) from the specified class.

Usage:
    inherits_from = __import__('4-inherits_from').inherits_from

    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited (directly or indirectly)
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The specified class.

    Returns:
        True if obj is an instance of a class that inherited from a_class, otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
