#!/usr/bin/env python3
"""
Function for return a transposes matrix
Using the transpose function
"""


def np_transpose(matrix):
    """
    Return a transpose matrices

    Args:
        matrix (list of list):
            list with differents shapes

    Return:
        list : mat_t
            a transpose matrix
    """
    mat_t = matrix.transpose()

    return mat_t
