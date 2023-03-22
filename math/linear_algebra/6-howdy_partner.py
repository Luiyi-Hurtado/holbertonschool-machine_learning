#!/usr/bin/env python3
"""Function for concatenate two arrays"""


def cat_arrays(arr1, arr2):
    """
    Return new list with concatenate two arrays

    Parameters
    ----------
    arr1 : list
        list of the integers
    arr2 : list
        list of the integers
    Return
    ------
    list : new list
        list with concatenate arrays
    """
    concat_list = arr1 + arr2
    return concat_list
