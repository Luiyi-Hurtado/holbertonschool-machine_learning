#!/usr/bin/env python3
"""function for transpose of a 2D matrix"""


def matrix_transpose(matrix):
    """Return transposed matrix in a new matrix

    Parameters
    ----------
    matrix : List of lists
        list of list with integers

    Return
    ------
    list : new matrix
        a list of lists with the content transposed
    """
    nrows = len(matrix)
    ncolums = len(matrix[0])
    matrix_T = []
    for indx1 in range(ncolums):
        row = []
        for indx2 in range(nrows):
            row.append(matrix[indx2][indx1])
        matrix_T.append(row)
    return matrix_T
