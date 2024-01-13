#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    This function divides all elements of matrix by the given number.

    Parameters:
    matrix (list of lists): The matrix to divide.
    div (int or float): The number to divide the matrix elements by.

    Returns:
    list of lists of float: The matrix after division.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
            isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError("matrix must be a matrix of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
