#!/usr/bin/env python3
"""
Function that calculates the derivative
of a plynomial
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Args:
        poly (list):
            a list of coefficients representing a polynomial,
            where the index of the list representsthe power
            of x that the coefficient belongs to

    Returns:
        list:
            A new list of coefficients representing the
            derivative of the polynomial

    If poly is not a valid list of coefficients, returns None.
    If the derivative is 0, returns [0].
    """
    if not isinstance(poly, list) or not all(isinstance(c, (int, float)) for c in poly):
        return None

    derivative = []
    n = len(poly)
    for i in range(1, n):
        coefficient = i * poly[i]
        derivative.append(coefficient)

    if not derivative:
        return [0]

    return derivative
