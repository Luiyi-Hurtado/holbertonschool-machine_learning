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
        if len(mat1[0]) != len(mat2[0]):
            return None
        return [row for row in mat1] + [row for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [mat1[idx] + mat2[idx] for idx in range(len(mat1))]
