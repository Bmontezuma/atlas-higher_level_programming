#!/usr/bin/python3
"""
Module for Square class
"""
from __import__('10-square').Square


class Square(Square):
    """
    Square class, inherits from Square (10-square)
    """
    def __str__(self):
        """
        Returns a string representation of the square
        """
        return "[Square] {}/{}".format(self.width, self.height)
