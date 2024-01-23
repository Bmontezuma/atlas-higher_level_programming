#!/usr/bin/python3
"""
Module defines a Square class that inherits from Rectangle (9-rectangle.py).

Example:
>>> s = Square(13)
>>> print(s)
[Square] 13/13
>>> s.area()
169
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Example:
    >>> s = Square(13)
    >>> print(s)
    [Square] 13/13
    >>> s.area()
    169
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Parameters:
        - size (int): The size of the square.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than or equal to 0.
        """
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the Square.

        Returns:
        - str: [Square] size/size
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)

    def area(self):
        """
        Computes the area of the Square.

        Returns:
        - int: The area of the square.
        """
        return self._Rectangle__width * self._Rectangle__height
