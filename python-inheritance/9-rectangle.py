#!/usr/bin/python3
"""
Module: 9-rectangle

This module defines a class Rectangle that inherits from BaseGeometry.

Usage:
    Rectangle = __import__('9-rectangle').Rectangle

    r = Rectangle(3, 5)

    print(r)
    print(r.area())
"""


class BaseGeometry:
    """
    A class representing BaseGeometry.

    Public Methods:
    - area(self): Raises Exception with message area() is not implemented.
    - integer_validator(self, name, value): Validates the integer value.
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the integer value.

        Args:
            name (str): The name of the value.
            value: The value to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to
        """
