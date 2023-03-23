#!/usr/bin/env python3
"""Function perfomrs matrix multiplication"""


def mat_mul(mat1, mat2):
    """
    Return a matrix multiplication

    Args:
        mat1 (list of lists):
            first matrix for multiplicate with mat2
        mat2 (list od lists):
            second matrix for multiplacete

    Returns:
        list : mul_mat
            this list have a required shape for the result
            of multiplicatino
    """
    if not (len(mat1[0]) == len(mat2)):
        return None
    mul_mat = [[0 for _ in range(len(mat2[0]))] for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mul_mat[i][j] = mat1[i][k] * mat2[k][j]

    return mul_mat
