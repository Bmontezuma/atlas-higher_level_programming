#!/usr/bin/python3
"""
Module that defines the Student class
"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize Student instance with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of Student instance.

        Args:
            attrs (list): List specifying attribute names to retrieve.

        Returns:
            dict: Dictionary of the Student instance.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
