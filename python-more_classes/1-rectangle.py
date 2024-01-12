#!/usr/bin/python3
"""
Module contains a class Rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle.
    """

    def __init__(self, width=0, height=0):
        """Initialize Rectangle

        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer!")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

        @property
        def height(self):
            """Get or set height of Rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(self, value):
                raise TypeError("Height must be integer!")
            if value < 0:
                raise ValueError("Height must be >= 0")
            self.__height = value
