#!/usr/bin/python3


def class_to_json(obj):
    """
    Returns a dictionary for JSON serialization of an object.

    Parameters:
    - obj: Instance of a class with serializable attributes.

    Returns:
    dict: Dictionary for JSON serialization.

    Example:
    >>> class_to_json(MyClass("John"))
    {'name': 'John', 'number': 0}
    """
    json_dict = {}
    for key, value in obj.__dict__.items():
        if not key.startswith("_") and not callable(value):
            json_dict[key] = value if isinstance(value, (list, dict, str, int, bool)) \
                else class_to_json(value)
    return json_dict
