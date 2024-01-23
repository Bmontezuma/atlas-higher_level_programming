#!/usr/bin/python3
"""
MyList module
"""


class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
