#!/usr/bin/env python3
"""
This module provides function that multiplicate two matrices
"""


def mat_mul(mat1, mat2):
    """
    Matrix multiplication

    Args:
        mat1 (list): The first matrix to multiplicate
        mat2 (list): The second matrix to multiplicate
    Return:
        Multiplicate matrix
    """
    rows1, cols1 = len(mat1), len(mat1[0])
    rows2, cols2 = len(mat2), len(mat2[0])

    if cols1 != rows2:
        return None

    mul_mat = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            mul_mat[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(cols1))
    return mul_mat
