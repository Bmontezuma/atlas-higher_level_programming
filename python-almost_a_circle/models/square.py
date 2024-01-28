#!/usr/bin/python3
"""
Module containing the Square class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a square.

        Args:
            size (int): The size of the square.
            x (int): The x coordinate of the square.
            y (int): The y coordinate of the square.
            id (int): The ID of the square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string of the square.

        Returns:
            str: String of the square.
        """
        return "[Square]".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        Gets size of the square.

        Returns:
            int: Size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size of the square.
        """
        self.width = value
        self.height = value

    def update(self, id=None, x=None, y=None, size=None):
        """
        Updates the square's attributes.

        Args:
            id (int, optional): The new ID of the square.
            x (int, optional): The new x coordinate of the square.
            y (int, optional): The new y coordinate of the square.
            size (int, optional): The new size of the square.
        """
        if id is not None:
            self.id = id
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if size is not None:
            self.width = size
            self.height = size

    def to_dictionary(self):
        """
        Converts the square to a dictionary.

        Returns:
            dict: A dictionary representing the square.
        """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
