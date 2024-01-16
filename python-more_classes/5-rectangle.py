#!/usr/bin/python3
"""
Module for the Rectangle class
"""


class Rectangle:
    """
    Rectangle class

    Usage:
    >>> r = Rectangle(3, 4)
    >>> r.width
    3
    >>> r.height
    4
    >>> r.area()
    12
    >>> r.perimeter()
    14
    >>> print(r)
    ###
    ###
    ###
    ###
    >>> repr(r)
    'Rectangle(3, 4)'
    >>> del r
    Bye rectangle...
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width

        Returns:
            int: Width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Args:
            value (int): Value to set as width

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height

        Returns:
            int: Height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height

        Args:
            value (int): Value to set as height

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: Perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            str: String representation of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """
        Returns a string representation of the rectangle for eval()

        Returns:
            str: String representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted
        """
        print("Bye rectangle...")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
