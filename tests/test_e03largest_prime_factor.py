"""
Tests for Project Euler #3: Largest Prime Factor
"""


from __future__ import (absolute_import,)
from e03largest_prime_factor import next_prime, is_prime, lpf


def test_next_prime():
    '''Test that next prime is correct'''

    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert not next_prime(3) == 4


def test_is_prime():
    '''Test that prime test is correct'''

    assert is_prime(2) == True
    assert is_prime(4) == False
    assert is_prime(13) == True
    assert is_prime(9) == False


def test_largest_prime_factor():
    '''Simple tests of small numbers'''

    assert lpf(2) == 2
    assert lpf(4) == 2
    assert lpf(6) == 3
    assert lpf(13195) == 29
