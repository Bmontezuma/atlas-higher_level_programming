#!/usr/bin/python3
"""
Module defines custom list class, MyList, that inherits from built-in list class in Python.
It includes a method, print_sorted, that prints the list in ascending order.
"""


class MyList(list):
    """
    Custom list class that includes a method for printing the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
