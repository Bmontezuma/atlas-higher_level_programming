#!/usr/bin/python3
"""
Module provides function for looking up attributes and methods of an object.
"""


def lookup(obj):
    """
    Function takes object as input and returns a list of attributes and methods.

    :param obj: The input object.
    :return: A list containing attributes and methods of the input object.
    """
    return dir(obj)

# Additional test cases
result_int = lookup(int)
result_float = lookup(float)
result_object = lookup(object)
result_list = lookup(list)

class MyClassWithDirMethod:
    """
    A class with a custom dir method.
    """
    def dir(self):
        """
        Custom dir method returning a list.
        """
        return ["my_class", "is", "empty"]

class MyClassEmpty:
    """
    An empty class.
    """
    pass

class MyClassWithAttribute:
    """
    A class with one attribute.
    """
    one_attribute = 89

class MyClassWithMethod:
    """
    A class with one method.
    """
    def one_method(self):
        """
        An example method.
        """
        pass
