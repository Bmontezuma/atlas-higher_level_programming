#!/usr/bin/python3
"""This module defines the Base class."""
import json


class Base:
    """Base class for managing id attribute and JSON."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance with id."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string of list_objs to a file."""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)  # Dummy instance
        elif cls.__name__ == "Square":
            dummy = cls(1)  # Dummy instance
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                return [cls.create(**d) for d in cls.from_json_string(file.read())]
        except FileNotFoundError:
            return []
