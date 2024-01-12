#!/usr/bin/python3
"""
This is a module defining a square class.
"""


class Square:
    """
    This is a class representing a square.

    Attributes:
        __size (int): Attribute representing the size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with optional size parameter.

        Args:
            size (int, optional): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
