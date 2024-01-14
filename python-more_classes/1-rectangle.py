#!/usr/bin/python3
"""
This module contains a class Rectangle.
"""


class Rectangle:
    """
    This class defines a rectangle with attributes width and height.

    Examples:
    >>> r = Rectangle(2, 4)
    >>> r.width
    2
    >>> r.height
    4
    >>> r.width = 10
    >>> r.height = 3
    >>> r.__dict__
    {'_Rectangle__width': 10, '_Rectangle__height': 3}

    Additional error cases:
    >>> try:
    ...     myrectangle = Rectangle(2, -3)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    # Expecting: [ValueError] Height must be >= 0

    >>> try:
    ...     myrectangle = Rectangle(-2, 3)
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    # Expecting: [ValueError] Width must be >= 0

    >>> try:
    ...     myrectangle = Rectangle(2, 3)
    ...     myrectangle.width = -4
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    # Expecting: [ValueError] Width must be >= 0

    >>> try:
    ...     myrectangle = Rectangle(2, 3)
    ...     myrectangle.width = "4"
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    # Expecting: [TypeError] Width must be an integer!

    >>> try:
    ...     myrectangle = Rectangle(2, 3)
    ...     myrectangle.height = -4
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    # Expecting: [ValueError] Height must be >= 0

    >>> try:
    ...     myrectangle = Rectangle(2, 3)
    ...     myrectangle.height = "4"
    ... except Exception as e:
    ...     print("[{}] {}".format(e.__class__.__name__, e))
    # Expecting: [TypeError] Height must be an integer!
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method for width.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width.

        Args:
            value (int): Value to set width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer!")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height.

        Args:
            value (int): Value to set height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer!")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value
