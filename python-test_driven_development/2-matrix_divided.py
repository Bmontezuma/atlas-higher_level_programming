#!/usr/bin/python3
"""
This module is a function to divide all elements of matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of matrix by the given number.

    Parameters:
    matrix (list of lists): The matrix to divide.
    div (int or float): The number to divide the matrix elements by.

    Returns:
    list of lists of float: The matrix after division.

    Raises:
    TypeError: If matrix is not a matrix (list of lists) of integers/floats,
               or if each row of the matrix does not have the same size,
               or if div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
            all(isinstance(num, (int, float)) for num in row) for row in matrix
    ):
        raise TypeError("matrix must be (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(float(num) / div, 2) for num in row] for row in matrix]
