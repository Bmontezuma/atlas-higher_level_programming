#!/usr/bin/python3
"""
Module: 7-base_geometry

This module defines a class BaseGeometry.

Usage:
    BaseGeometry = __import__('7-base_geometry').BaseGeometry

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
    - integer_validator(self, name, value): Validates the value.
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value.

        Args:
            name (str): The name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
