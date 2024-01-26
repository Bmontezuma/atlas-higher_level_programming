#!/usr/bin/python3
"""
This module defines the Base class.
"""


class Base:
    """
    Represents the base class.

    Attributes:
        __nb_objects (int): Represents the number of objects instantiated.
        id (int): The identifier of the instance.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The identifier of the instance.

        Examples:
            >>> b1 = Base()
            >>> b1.id
            1

            >>> b2 = Base()
            >>> b2.id
            2

            >>> b3 = Base()
            >>> b3.id
            3

            >>> b4 = Base(12)
            >>> b4.id
            12
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
