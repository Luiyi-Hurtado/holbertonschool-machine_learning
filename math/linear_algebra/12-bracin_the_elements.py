#!/usr/bin/env python3
"""
This module provide function tha calculate add, sub, mul, div.
"""


def np_elementwise(mat1, mat2):
    """
    Calculate add, sub, mul and div using two matrices.

    Args:
        mat1 (list): first matrix for calculate.
        mat2 (list): second matrix for calculate.
    Return:
        Addition, subtraction, multiplication and division.
    """
    add_mat = (mat1 + mat2)
    sub_mat = (mat1 - mat2)
    mul_mat = (mat1 * mat2)
    div_mat = (mat1 / mat2)
    return add_mat, sub_mat, mul_mat, div_mat
