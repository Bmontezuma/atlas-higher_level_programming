#!/usr/bin/python3
"""Module that defines a class MyList"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))


if __name__ == "__main__":
    # Test the MyList class
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
