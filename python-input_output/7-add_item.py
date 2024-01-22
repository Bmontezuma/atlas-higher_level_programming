#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a JSON file.
"""

import sys
import os.path
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


def add_item(args):
    """
    Adds all arguments to a Python list and saves them to a JSON file.

    Args:
        args (list): List of arguments.

    Returns:
        None.
    """
    filename = "add_item.json"
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    add_item(sys.argv[1:])
