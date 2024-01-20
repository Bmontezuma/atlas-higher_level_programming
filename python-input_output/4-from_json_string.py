#!/usr/bin/python3
import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.

    Parameters:
    - my_str (str): JSON string to be converted.

    Returns:
    object: Python data structure.

    Example:
    >>> s_my_list = "[1, 2, 3]"
    >>> from_json_string(s_my_list)
    [1, 2, 3]
    """
    return json.loads(my_str)
