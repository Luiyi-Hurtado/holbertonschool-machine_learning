#!/usr/bin/env python3
def matrix_shape(matrix):
    """Return shape from a matrix

    Parameters
    -----------
    matrix : list of list
        with integers

    Return
    -------
    list
        a list of integer with the size of the matrix
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
