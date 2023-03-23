#!/usr/bin/env python3
"""
Function that performs element-wise addition, subtraction
multiplication and the division
"""


def np_elementwise(mat1, mat2):
    """
    Use a two matrices and retrn a tuple
    wiith the basics opeations

    Args:
        mat1 (list of list):
            a list with containt integers for the operation
        mat2 (list of list):
            a list with containt integers for the operation

    Return:
        tuple : operations
            a tuple with all result of the four operations
    """
    add_mat = mat1 + mat2
    sub_mat = mat1 - mat2
    mul_mat = mat1 * mat2
    div_mat = mat1 / mat2
    return (add_mat, sub_mat, mul_mat, div_mat)
