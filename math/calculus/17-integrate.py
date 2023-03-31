#!/usr/bin/env python3
"""
Fucntion that calculates the integral
of a polynomial
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Args:
        poly: list of coefficients representing a polynomial.
        C: integer representing the integration constant.

    Returns:
        A new list of coefficients representing the integral of the polynomial.
    """

    if type(C) != int or type(poly) != list or  \
            not all(isinstance(i, (int, float)) for i in poly):
        return None

    result = [C]

    for i in range(len(poly)):
        coef = poly[i] / (i+1)
        if coef.is_integer():
            coef = int(coef)
        result.append(coef)

    return result
