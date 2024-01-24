#!/usr/bin/python3
"""
My List module
"""


class MyList(list):
    """A custom list class that can print its elements in sorted order.

    Public instance method:
        def print_sorted(self): Prints the list, but sorted in ascending order.
    """

    def print_sorted(self):
        """Prints the elements of the list in ascending sorted order."""
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt", verbose=True,
                     optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
