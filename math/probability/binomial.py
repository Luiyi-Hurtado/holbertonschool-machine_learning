#!/usr/bin/env python3
"""
Module name: binomial.py
Author: Luiyi-Hurado
Date created: 5/4/2022
Last updated: 5/4/2022
Version: 1.0v

Description: This module contains the Binomial class, which represents
a Binomial distribution.
"""


class Binomial:
    """
    A class representing a Binomial distribution.

    Parameters
    ----------
        data : list or None
            A list of the data to be used to estimate the distribution.
            If None, the distribution will be initialized with the given
            `n` and `p`.
            Default None
        n : int
            The number of trials.
            Default 1.
        p : float
            The probability of success for each trial.
            Default 0.5.

    Attributes
    ----------
        n : int
            The number of trials.
        p : float
            The probability of success for each trial.

    Raises
    ------
        ValueError
            If n is not a positive integer.
            If p is not a probability value between 0 and 1 (inclusive).
            If data is given but not a list.
            If data is given but does not contain at least two data points.
    """

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize a Binomial distribution with the given parameters.

        If data is None, the distribution will be initialized with the
            given number of trials and probability of success.
        If data is given, the number of trials and probability of success
            will be calculated from the data.
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = n
            self.p = p
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data msut contain multiple values")
            self.n = round(sum(data) / len(data))
            self.p = sum(data) / (self.n*1.0)
            # self.n = int(self.n)

    def fact(self, n):
        """
        Give a factorial value from a specified integer.

        Parameters:
        -----------
            n (int)
                A value for any function.

        Returns:
        --------
            If n is equal to 0, return 1.
            If n is greater to 0, calculate the factorial of the value.
        """
        return 1 if n == 0 else n * self.fact(n-1)

    def pmf(self, k):
        """
        Calculate the probability mass function (PMF)
        of the Binomial distribution for a given number of successes `k`.

        Parameters
        ----------
            k : int
                The number of successes.

        Returns
        -------
            float
                The probability of getting `k` successes in `n`
                trials with probability of success `p`.
        """
        pass

    def cdf(self, k):
        """
        Calculate the cumulative distribution function (CDF)
        of the Binomial distribution for a given number of successes `k`.

        Parameters
        ----------
            k : int
                The number of successes.

        Returns
        -------
            float
                The probability of getting up to `k` successes in `n` trials
                with probability of success `p`.
        """
        pass
