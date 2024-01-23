#!/usr/bin/python3


class MyList(list):
    """
    MyList inherits from list and provides additional functionality.

    Public methods:
    - print_sorted(self): Prints the list in ascending order.

    Note: This class assumes that all elements in the list are of type int.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Returns:
        - list: A new list containing elements in ascending order.
        """
        sorted_list = sorted(self)
        print("Sorted List:", sorted_list)
        return sorted_list 
