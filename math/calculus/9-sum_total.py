#!/usr/bin/env python3
"""
Function for sum a square notation
"""


def summation_i_squared(n):
    """
    """
    sum = 0
    if isinstance(n, int):
        for i in range(1, n + 1):
            sum += (i*i)
        return sum
        # print(sum)
