#!/usr/bin/env python3
"""Function for concatenate two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ 
    Return concatenates two matrices along specific axis

    Args:
        mat1 (list of list):
            the first matrix for concatenate
        mat2 (list of list):
            the second matrix for concatenate right to the mat1
        axis (int):
            specifies the axis along which to concatenate the matrices (default is 0)

    Returns:
        list of lists: concatenate matrix with different axis
    """
    cat_mat = []
    if axis == 0:
        if len(mat1[0]) == len(mat2[0]):
            cat_mat = mat1 + mat2
            return cat_mat
    elif axis == 1:
        if len(mat1) == len(mat2):
            for indx in range(len(mat1)):
                cat_mat.append(mat1[indx] + mat2[indx])
            return cat_mat
    return None
