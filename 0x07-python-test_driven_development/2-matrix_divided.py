#!/usr/bin/python3
"""This module defines the function 'matrix_divided
which returns a new matrix
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div
    Args:
        matrix - list of lists containing integers or floats
        div - (int) the divisor
    Raises:
        TypeError - if matrix contains any form of data aside ints or floats
        TypeError - if size of each rows of the matrix are different
        TypeError - if div value does not contain int or float
        ZeroDivisionError - if div is equal to zero
    Return:
        a new matrix rounded up to 2 decimal places
    """

    for lst in matrix:
        for val in lst:
            if type(val) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")

        if len(list) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(y/div, 2) for y in x] for x in matrix]
    return new_matrix
