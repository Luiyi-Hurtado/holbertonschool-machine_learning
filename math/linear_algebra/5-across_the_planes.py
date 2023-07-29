#!/usr/bin/env python3
"""
This module provides function for that adds two matrices element-wise.

The function in this module take two matrices as input and returns a new matrices with the add numbers.
"""


def add_matrices2D(mat1, mat2):
    """
    Add matrices2D

    Args:
        mat1 (list): list of integers.
    """
    pass
    if len(mat1[0]) != len(mat2[0]):
        return None
    add_matrices = [[mat1[i][j] + mat2[i][j]
                     for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return add_matrices
