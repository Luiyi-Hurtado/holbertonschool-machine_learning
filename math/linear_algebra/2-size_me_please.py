#!/usr/bin/env python3
def matrix_shape(matrix):
    """Return shape from a matrix

    args(matrix):
        list of lists with contend integers
    return(shape):
        list of integer with the size of the matrix
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
