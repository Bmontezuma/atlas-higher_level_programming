#!/usr/bin/python3
"""
Custom List Module

Example Usage:
    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]
    >>> my_list.print_sorted()
    Sorted List: [1, 2, 3, 4, 5]
    >>> print(my_list)
    [1, 4, 2, 3, 5]
"""


class MyList(list):
    """
    A custom list class that provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(f"Sorted List: {sorted_list}")
