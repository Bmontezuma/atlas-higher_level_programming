#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int or float): An integer or float.

    Returns:
        list: A new matrix divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix of integers/floats.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 2)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 0)
        Traceback (most recent call last):
        ZeroDivisionError: division by zero
    """
    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must matrix of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
