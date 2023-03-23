#!/usr/bin/env python3
"""
Function that concatenate two matrices along
a specific axis, using the numpy library
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Use the two matrices and concatenates based
    on the axis

    Args:
        mat1 (numpy.ndarray):
            a first array for concatenate
        mat2 (numpy.ndarray):
            a array for concatenate with the first
        axis (int):
            a integer respresenting a concatenate axis

    Return:
        numpy.ndarray : cat_mat
            an array with the concatenate result
    """
    cat_mat = np.concatenate((mat1, mat2), axis)
    return cat_mat
