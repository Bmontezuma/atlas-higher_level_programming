#!/usr/bin/python3
"""
Module: 6-base_geometry

This module defines a class BaseGeometry.

Usage:
    BaseGeometry = __import__('6-base_geometry').BaseGeometry

    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
"""


class BaseGeometry:
    """
    A class representing BaseGeometry.

    Public Methods:
    - area(self): Raises Exception with message area() is not implemented.
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")
