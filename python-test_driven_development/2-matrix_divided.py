#!/usr/bin/python3
"""
This module defines a function matrix_divided to divide all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix.
        div (int or float): The divisor.

    Returns:
        list of lists: The matrix with all elements divided by the divisor.

    Raises:
        TypeError: If the matrix is not a list of lists or if div is not an int or float.
        ZeroDivisionError: If div is 0.

    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [
        [round(elem / div, 2) for elem in row]
        for row in matrix
    ]
    return new_matrix

