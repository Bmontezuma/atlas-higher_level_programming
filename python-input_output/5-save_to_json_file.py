#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Parameters:
    - my_obj: The object to be written to the file.
    - filename (str): The name of the file to which the object will be saved.

    Returns:
    None

    Example:
    >>> my_list = [1, 2, 3]
    >>> save_to_json_file(my_list, "my_list.json")
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
