#!/usr/bin/python3
"""
Module for Square class
"""
from '9-rectangle' import Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a Square instance
        Args:
            size (int): Size of the square, must be a positive integer
        """
        super().__init__(size, size)
