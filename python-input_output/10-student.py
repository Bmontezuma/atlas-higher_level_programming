#!/usr/bin/python3

class Student:
    """
    Defines a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.

        Parameters:
        - first_name (str): First name of the student.
        - last_name (str): Last name of the student.
        - age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Parameters:
        - attrs (list): List of strings representing attribute names to retrieve.

        Returns:
        dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return {'first_name': self.first_name, 'last_name': self.last_name, 'age': self.age}
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
