#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Parameters:
    - my_obj: The object to be converted to a JSON string.

    Returns:
    str: JSON representation of the object.

    Example:
    >>> my_list = [1, 2, 3]
    >>> to_json_string(my_list)
    '[1, 2, 3]'
    """
    return json.dumps(my_obj)
