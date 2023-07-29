#!/usr/bin/env python3
"""
This module provides function for concatenates two arrays.

The function in this module take two arrays and
returns a new list with conacatenates integers
"""


def cat_arrays(arr1, arr2):
    """
    Cocatenates two arrays

    Args:
        arr1 (list): list of integers
        arr2 (list): list of integers
    return:
        concat_list: new list with concatenate integers
    """
    concat_list = arr1 + arr2
    return concat_list
