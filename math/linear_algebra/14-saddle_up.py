#!/usr/bin/env python3
"""
Function that performs matrix multiplication
Using a numpy library
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Use two matrices and  use the dot function for
    create a innier product

    Args:
        mat1 (matrix):
            a matrix with integer for create a product
        mat2 (matrix):
            a matrix with integer for create a proudct with dot

    Return:
        matrix : dot_mat
            a matrix with the product from the dot multiplication
    """
    dot_mat = np.dot(mat1, mat2)
    return dot_mat
