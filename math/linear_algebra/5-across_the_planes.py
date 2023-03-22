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
    len_mat1 = len(mat1)
    len_mat2 = len(mat2[0])
    add_mat = []
    if not (len_mat1 == len_mat2):
        return None
    for rows in range(len_mat1):
        row = []
        for colum in range(len_mat2):
            row.append(mat1[rows][colum] + mat2[rows][colum])
        add_mat.append(row)
    return add_mat
