#!/usr/bin/python3
"""Module to define a Rectangle."""


class Rectangle:
    """
    Class that defines a Rectangle.

    Attributes:
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.

    Methods:
        __init__(self, width, height): Initializes a new instance of the class.
        width(self): Getter method for the width attribute.
        height(self): Getter method for the height attribute.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): String representation of the rectangle.
        __repr__(self): String representation of the rectangle for debugging.
    """
    def __init__(self, width=0, height=0):
        """Initializes a new instance of the class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        String representation of the Rectangle.

        Returns:
        - str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height) + '\n'

    def __repr__(self):
        """
        String representation of the Rectangle for debugging.

        Returns:
        - str: String representation of the rectangle.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
