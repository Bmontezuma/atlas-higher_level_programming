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

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
