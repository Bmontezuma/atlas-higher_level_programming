#!/usr/bin/python3
"""
Defines custom list class, MyList, that inherits from built-in list class.
It includes a method, print_sorted, that prints the list in ascending order.
"""


class MyList(list):
    """
    Custom list class provides a method to print the list in ascending order.

    >>> my_list = MyList([1, 4, 2, 3, 5])
    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]
    >>> my_list
    [1, 4, 2, 3, 5]
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        >>> my_list = MyList([1, 4, 2, 3, 5])
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        """
        print(sorted(self))
