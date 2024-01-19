#!/usr/bin/python3
"""
Module: 1-my_list

This module defines class MyList that inherits from list and provides a method
to print the list in sorted order.

Usage:
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
"""


class MyList(list):
    """
    MyList class inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        Example:
        >>> my_list = MyList()
        >>> my_list.append(1)
        >>> my_list.append(4)
        >>> my_list.append(2)
        >>> my_list.append(3)
        >>> my_list.append(5)
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        """
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
