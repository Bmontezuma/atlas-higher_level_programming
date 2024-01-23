#!/usr/bin/python3
"""
Module defines a class `MyList` that inherits from built-in `list` class.
It adds a method `print_sorted()` which prints the list in ascending order.

# Test appending elements and printing sorted
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
    This class inherits from built-in `list` class in Python.
    It overrides the `__str__` method to return string representation of list.
    It also adds method `print_sorted()` which prints list in ascending order.
    """

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print("Sorted List:", sorted_list)

    def __str__(self):
        """Return a string representation of the list."""
        return super().__str__()
