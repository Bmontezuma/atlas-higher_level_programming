#!/usr/bin/python3
"""This module contains a function to print a formatted name."""


def say_my_name(first_name, last_name=""):
    """
    Print the formatted name: My name is <first name> <last name>.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    error_msg = "first_name must be a string or last_name must be a string"
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError(error_msg)

    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
