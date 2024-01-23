#!/usr/bin/python3
"""
1-my_list

This module contains the definition of the MyList class.
"""


class MyList(list):
    """
    MyList class that inherits from list.

    Public Methods:
    - print_sorted(self): Prints the list, but sorted (ascending sort).
    """

    def print_sorted(self):
        """
        Prints the list, but sorted (ascending sort).

        Example:
        >>> my_list = MyList()
        >>> my_list.append(1)
        >>> my_list.append(4)
        >>> my_list.append(2)
        >>> my_list.append(3)
        >>> my_list.append(5)
        >>> print(my_list)
        [1, 4, 2, 3, 5]
        >>> my_list.print_sorted()
        [1, 2, 3, 4, 5]
        >>> print(my_list)
        [1, 4, 2, 3, 5]
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
