#!/usr/bin/python3
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """
    This class represents a rectangle. It inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object with width and height.
        Both width and height must be positive integers.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
