#!/usr/bin/env python3
"""
This module provides function for that adds two arrays

The function in this module take two arrays as input and
returns a new array with the add numbers
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise

    Args:
        arr1 (list): array of numbers
        arr2 (list): array of numbers
    Returns:
        add_list: new list with add numbers
    """
    if len(arr1) != len(arr2):
        return None
    add_list = [a + b for a, b in zip(arr1, arr2)]
    return add_list
