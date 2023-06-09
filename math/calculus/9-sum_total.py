#!/usr/bin/env python3
"""
Function for sum a square notation
"""


def summation_i_squared(n):
    """
    Use n like a stopping condition for calculate
    the value for i

    Args:
        n (int):
            is the stopping condition

    Returns:
        int:
            value for all squared numbers
    """
    if not isinstance(n, int) or n < 1:
        return None

    return (n * (n + 1) * (2 * n + 1)) // 6
