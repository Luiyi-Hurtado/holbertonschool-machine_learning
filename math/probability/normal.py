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
