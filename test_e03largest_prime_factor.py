"""
Tests for Project Euler #3: Largest Prime Factor
"""


from __future__ import (absolute_import,)
from e03largest_prime_factor import is_prime, lpf


def test_is_prime():
    '''Test that prime test is correct'''

    assert is_prime(2) == True


def test_largest_prime_factor():
    '''Simple tests of small numbers'''

    assert lpf(2) == 2
    assert lpf(4) == 2
    assert lpf(6) == 3
    assert lpf(13195) == 29
