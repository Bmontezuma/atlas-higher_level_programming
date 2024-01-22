#!/usr/bin/python3

"""
This module defines a custom list class called MyList.
"""


class MyList:
    """
    Custom List Class

    Class represents list with methods to append items and print sorted list.
    """

    def __init__(self):
        """
        Initialize MyList with an empty list.

        >>> ml = MyList()
        >>> assert ml._list == []
        """
        self._list = []

    def append(self, item):
        """
        Append an item to the list.

        Args:
            item (int): Item to append to the list.

        >>> ml = MyList()
        >>> ml.append(1)
        >>> assert ml._list == [1]
        """
        self._list.append(item)

    def print_sorted(self):
        """
        Sort the list and print it.

        >>> ml = MyList()
        >>> ml.append(1)
        >>> ml.append(4)
        >>> ml.append(2)
        >>> ml.append(3)
        >>> ml.append(5)
        >>> ml.print_sorted()
        [1, 2, 3, 4, 5]
        """
        sorted_list = sorted(self._list)
        print(sorted_list)

    def __str__(self):
        """
        Return the string representation of the list.

        >>> ml = MyList()
        >>> ml.append(1)
        >>> ml.append(4)
        >>> ml.append(2)
        >>> ml.append(3)
        >>> ml.append(5)
        >>> print(ml)
        [1, 4, 2, 3, 5]
        """
        return str(self._list)
