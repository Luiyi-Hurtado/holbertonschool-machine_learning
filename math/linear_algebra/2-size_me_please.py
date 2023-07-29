#!/usr/bin/env python3
"""
This module calculate the shape of a matrix
"""


def matrix_shape(matrix):
    """
    calculate the shape of the matrix
    """
    shape = []
    for i in range(len(matrix)):
        shape.append(len(matrix[i]))
    return shape
