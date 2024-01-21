#!/usr/bin/python3
"""
Module documentation

This module defines the MyList class, which inherits from the built-in list class.
It includes a public instance method print_sorted that prints the list in ascending order.

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
    Class documentation

    This class inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Method documentation

        This method prints the list in ascending order.
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
