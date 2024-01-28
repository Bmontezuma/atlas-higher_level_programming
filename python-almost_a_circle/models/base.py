#!/usr/bin/python3
"""
This module defines the Base class.
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: The JSON string representation of list_dictionaries.

        Examples:
            >>> Base.to_json_string([{'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}])
            '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'

            >>> Base.to_json_string([])
            '[]'

            >>> Base.to_json_string(None)
            '[]'
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
