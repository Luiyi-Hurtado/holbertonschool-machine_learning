#!/usr/bin/env python3
"""
Module name: exponential.py
Author: Luiyi-Hurado
Date created: 4/4/2022
Last updated: 4/4/2022
Version: 1.1v

Description: This module contains the Exponential class, which represents
a Exponential distribution.
"""


class Exponential:
    """
    Class representing a Poisson distribution.

    Parameters:
    -----------
        data (list)
            A list the date to be used to estimate the distribution.
        lambths (float)
            The expected number of occurrences in a given time frame.

    Attributes:
    -----------
        lambtha (float)
            The expected number of occurrences in a given time frame.

    Raises:
    -------
        ValueError:
            If lambtha is not a positive value or equals to 0.
            If data is given but it´s not a list.
            If data is given but doesn´t at least two data points.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize a Poisson distrubucion with the given paramters.

        If data is not given, set lambtha to the given value.
        If data is given, calculate the lambtha of data.

        Parameters:
        -----------
            data (list)
                A list of data to be used to estimate the distribution.
                Default is None.
            lambtha (float)
                The expected number of occurrences in a given time frame.
                Default is 1.0.
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = 1 / (sum(data)/len(data))

    def pdf(self, x):
        """
        Calculate the Probability Density Function(PDF), with the lambtha value
        and the x value.

        Parameters:
        -----------
            x (int):
                Is the time period.

        Returns:
        --------
            If x is less than 0, return zero.
            Otherwise, calculate the Probability Density Function(PDF).
        """
        if x < 0:
            return 0
        pdf_value = (self.lambtha * 2.7182818285**(-self.lambtha * x))
        return pdf_value

    def cdf(self, x):
        """
        Calculate the Cumulative Distribution Function(CDF), with the lambtha value
        and the x value.

        Parameters:
        -----------
            x (int):
                Is the time period.

        Returns:
        --------
            If x is less than 0, return zero.
            Otherwise, calculate the Cumulative Distribution Function(CDF).
        """
        if x < 0:
            return 0
        cdf_value = (1 - 2.7182818285**(-self.lambtha * x))
        return cdf_value
