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
        return {attr: getattr(self, attr) for attr in attrs or dir(self) if isinstance(attr, str) and hasattr(self, attr)}

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance
        Args:
            json (dict): Dictionary with attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
