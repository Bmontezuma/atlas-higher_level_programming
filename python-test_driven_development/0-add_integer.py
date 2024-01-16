def add_integer(a, b=98):
    """
    Add two integers.

    Prototype: def add_integer(a, b=98):
    a and b must be integers or floats, raise a TypeError exception message
    a must be an integer or b must be an integer
    a and b must be first casted to integers if they are float
    Returns an integer: the addition of a and b
    You are not allowed to import any module
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer or float")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
