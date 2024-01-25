#!/usr/bin/python3
"""This is my Base module"""


class Base:
    """The Base class for managing IDs"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
