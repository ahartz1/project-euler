"""
Tests for Project Euler Problem #7: 10,001st Prime
"""

from __future__ import (absolute_import)
from e00710001st_prime import nth_prime, is_prime


def test_is_prime():
    '''Make sure we are only getting primes'''

    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(23) == True
    assert is_prime(102) == False


def test_nth_prime_6():
    '''Test that for n of 6, we get 13'''

    assert nth_prime(6) == 13
