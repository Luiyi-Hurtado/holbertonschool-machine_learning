#!/usr/bin/env python3
"""
This module provide function that perfoms matrix multiplication.
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Multiplocate two matrices

    Args:
        mat1 (list): first matriz to multiplicate.
        mat2 (list): second matriz to multiplicate.
    Return:
        Multiplication two matrices.
    """
    mul = np.dot(mat1, mat2)
    return mul
