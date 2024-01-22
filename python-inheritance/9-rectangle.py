#!/usr/bin/python3
"""
Module: 8-rectangle

This module defines a class Rectangle that inherits from BaseGeometry.

Usage:
    Rectangle = __import__('8-rectangle').Rectangle

    # Example Usage
    r = Rectangle(4, 5)
    print(r)
    print(r.area())

    try:
        r = Rectangle(2, "hello")
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


class Rectangle(BaseGeometry):
    """
    A class representing Rectangle, inheriting from BaseGeometry.

    Public Methods:
    - __init__(self, width, height): Initializes Rectangle width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
