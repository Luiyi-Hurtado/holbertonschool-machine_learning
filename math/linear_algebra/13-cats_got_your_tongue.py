#!/usr/bin/env python3
"""
This module provide function tha concatenate two matrices.
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenate two matrices

   Args:
        mat1 (list): The fitst matrix to concatenate.
        mat2 (list): The second matrix to concatenate.
        axis (list): The axis along which to concatenate the matrices
            0 for rows, 1 for columns.
    Return:
        The concatenated matrix.
    """
    concat = np.concatenate((mat1, mat2), axis)
    return concat
