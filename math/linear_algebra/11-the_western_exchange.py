#!/usr/bin/env python3
"""
Function for return a transposes matrix
Using numpy dependeces and the transpose function
"""
import numpy as np


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
    mat_t = np.transpose(matrix)

    return mat_t
