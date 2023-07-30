#!/usr/bin/env python3
"""
This module provide function that transpose a matrix.
"""


def np_transpose(matrix):
    """
    Transpose matrix.

    Args:
        matrix (list): matrix to transpose
    Return:
        a transpose matrix
    """
    tp_matrix = matrix.copy()
    return tp_matrix.transpose()
