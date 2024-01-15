#!/usr/bin/python3
"""
Module for Rectangle class.
"""


class Rectangle:
    """
    Class that defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
        - width (int): Width of the rectangle.
        - height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
        - int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
        - value (int): Value to set for width.

        Raises:
        - ValueError: If value is not an integer or if it's less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
        - int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
        - value (int): Value to set for height.

        Raises:
        - ValueError: If value is not an integer or if it's less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle.

        Returns:
        - int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle.

        Returns:
        - int: Perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        String representation of the Rectangle.

        Returns:
        - str: String representation of the rectangle.
        """
        return '\n'.join(['#' * self.__width] * self.__height) + '\n'
