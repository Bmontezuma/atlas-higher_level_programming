#!/usr/bin/python3
"""
This module provides functionality for working with cities and states.
"""

class City:
    """
    Represents a city with its name and state.
    """

    def __init__(self, name, state):
        """
        Initialize a new City instance with the given name and state.
        """
        self.name = name
        self.state = state

    def display(self):
        """
        Display the city's name and state.
        """
        print(f"{self.name}, {self.state}")
