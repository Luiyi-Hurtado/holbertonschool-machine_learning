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
    add_mat = [[0, 0], [0, 0]]
    for row in range(len(mat1)):
        for colum in range(len(mat1[0])):
            add_mat[row][colum] = mat1[row][colum] + mat2[row][colum]
    return add_mat
