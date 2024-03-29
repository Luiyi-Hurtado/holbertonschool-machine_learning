#!/usr/bin/env python3
"""
This module calculate the shape of a matrix
"""


def matrix_shape(matrix):
    """
    calculate the shape of the matrix
    """
    shape = []
    while (isinstance(matrix, list)):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
