"""
Tests for Project Euler #10: Summation of Primes
"""

from __future__ import (absolute_import)
from e10summation_of_primes import sum_of_primes


def test_sum_of_primes_below_10():
    '''2 + 3 + 5 + 7 = 17'''

    assert sum_of_primes(10) == 17
