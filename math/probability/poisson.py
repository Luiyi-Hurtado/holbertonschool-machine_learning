#!/usr/bin/env python3
"""
This module contains the Poisson class,
which represents a Poisson distribution.
"""


class Poisson:
    """
    Class representing a Poisson distribution.

    Parameters:
        data (list)
            A list the date to be used to estimate the distribution.
        lambths (float)
            The expected number of occurrences in a given time frame.

    Attributes:
        lambtha (float)
            The expected number of occurrences in a given time frame.

    Raises:
        ValueError:
            If lambtha is not a positive value or equals to 0.
            If data is given but it´s not a list.
            If data is given but doesn´t at least two data points.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize a Poisson distrubucion with the fiven paramters.

        If data is not given, set lambtha to the given value.
        If data is given, calculate the lambtha of data
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            if lambtha > 0:
                self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise ValueError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            if isinstance(data, list):
                self.lambtha = sum(data) / len(data)

    def fact(self, n):
        """
        """
        return 1 if n == 0 else n * self.fact(n-1)

    def pmf(self, k):
        """
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        pmf = ((self.lambtha**k)*(2.7182818285**-self.lambtha))/self.fact(k)
        return pmf

    def cdf(self, k):
        """
        """
        if not isinstance(k, int):
            k = int(k)
        if k < 0:
            return 0

        cdf = 0.0
        for i in range(k+1):
            cdf += (self.lambtha**i / self.fact(i))
        cdf *= (2.7182818285**-self.lambtha)
        return cdf
