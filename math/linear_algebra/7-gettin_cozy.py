#!/usr/bin/env python3
"""
This module provides function that concatenates two matrices
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along the specified axis.

    Args:
        mat1 (list): The fitst matrix to concatenate
        mat2 (list): The second matrix to concatenate
        axis (list): The axis along which to concatenate the matrices.
            0 for rows, 1 for columns.
    Returns:
        The concatenated matrix.
    """
    if axis == 0:
        return [[i, j] for i, j in zip(mat1, mat2)]
    elif axis == 1:
        return [[i for i in row1 + row2] for row1, row2 in zip(mat1, mat2)]
