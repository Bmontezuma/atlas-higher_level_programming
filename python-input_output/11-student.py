#!/usr/bin/python3
""" Module for Student class
"""


class Student:
    """ Student class
    """

    def __init__(self, first_name, last_name, age):
        """ Initializes a Student instance
        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): List of strings specifying attribute names
        Returns:
            dict: Dictionary representation of the Student instance
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance
        Args:
            json (dict): Dictionary with attribute names and values
        """
        self.__dict__.update(json)
