#!/usr/bin/env python3
"""
This module provides function for transpose a 2D matrix.

The function in this module take a matrix as input and
return new transpose matrix.
"""


def matrix_transpose(matrix):
    """
    Transpose a 2D matrix.

    Args:
        matrix (list): Array of numbers
    Returns:
        list: transpose new matrix
    """
    transpose = [[matrix[j][i]
                  for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose
