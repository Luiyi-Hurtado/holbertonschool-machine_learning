#!/usr/bin/env python3
"""
Module name: normal.py
Author: Luiyi-Hurado
Date created: 5/4/2022
Last updated: 5/4/2022
Version: 1.0v

Description: This module contains the normal class, which represents
a Normal distribution.
"""


class Normal:
    """
    A class representing a Normal distribution.

    Parameters
    -----------
        data (list):
            A list of the data to be used to estimate the distribution.
        mean (float):
            The mean (average) value of the distribution.
        stddev (float):
            The standard deviation (spread) of the distribution.

    Attributes
    ----------
        mean (float):
            The mean (average) value of the distribution.
        stddev (float):
            The standard deviation (spread) of the distribution.

    Raises
    ------
        If the standard derivation is less or equal to 0.
        If the data is not a list.
        If the lenght of data is less than 2 values.
    """

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize a Poisson distrubucion with the given paramters.

        Parameters
        ----------
            data (list):
                A list of data to be used to estimate the distribution.
                Default is None.
            mean (float):
                The mean (average) value of the distribution.
                Default is 0.0
            stddev (float):
                The standard deviation (spread) of the distribution.
                Default is 1.0
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = sum(data) / len(data)
            self.stddev = (sum([(x - self.mean)**2 for x in data])
                           / (len(data)))**0.5

    def z_score(self, x):
        """
        Use a normal probability to find the value of a normal random
        variable X.

        Parameters
        ----------
            x (int)
                Individual value.

        Returns
        -------
            Calculate the z_score.
        """
        z_value = (x - self.mean) / self.stddev
        return z_value

    def x_value(self, z):
        """
        Use a normal probability to find the value of a normal random
        variable X.

        Parameters
        ----------
            z (int)
                z-score can be placed on a normal distribution curve.

        Re
        """
        x_value = self.mean + (z*self.stddev)
        return x_value

    def pdf(self, x):
        """
        """
        term1 = 1 / (self.stddev * ((2 * 3.1415926536) ** 0.5))
        term2 = ((x - self.mean) ** 2) / (2 * (self.stddev ** 2))
        pdf_value = term1 * (2.7182818285 ** (-term2))
        return pdf_value
