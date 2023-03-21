#!/usr/bin/env python3
"""Fucntion for adds twi arrays element-wise"""


def add_arrays(arr1, arr2):
    """Return new list with the integers adding

    Paramaters
    ----------
    arr1 : list
        list of integers
    arr2: list
        list of integers

    Return
    ------
    list: new array
        list with the result of the add
    """
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)
    add_arr = []
    if not (len_arr1 == len_arr2):
        return None
    for indx in range(len_arr1):
        add_arr.append(arr1[indx]+arr2[indx])
    return add_arr
