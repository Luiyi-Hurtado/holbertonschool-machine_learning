#!/usr/bin/env python3
"""Function for create a matrix with the add of two matrices"""


def add_matrices2D(mat1, mat2):
    """
    Return list the add matrix if the matrices are
    the same shape

    Parameters
    ----------
    mat1 : list
        list of the lists with integers
    mat2 : list
        list of the lists with integers

    Return
    ------
    List : new array
        a list content the add result from the two matrices
    None : Boolean
        if the shape of matrices are not the same
    """
    nrows_mat1 = len(mat1)
    nrows_mat2 = len(mat2)
    ncolums_mat1 = len(mat1[0])
    ncolums_mat2 = len(mat2[0])

    if nrows_mat1 != nrows_mat2 or \
            ncolums_mat1 != ncolums_mat2:
        return None
    add_mat = []
    for row in range(nrows_mat1):
        add_row = []
        for colum in range(ncolums_mat1):
            add_row.append(mat1[row][colum] + mat2[row][colum])
        add_mat.append(add_row)
    return add_mat
