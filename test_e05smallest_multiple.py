"""
Tests for Project Euler Problem #5: Smallest Multiple
"""

from __future__ import (absolute_import)
from e05smallest_multiple import smallest_multiple, is_prime


def test_is_prime():
    '''Make sure we are only getting primes'''

    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(23) == True
    assert is_prime(102) == False


def test_1_to_2_smallest_multiple():
    '''Test the 1–2 case'''

    assert smallest_multiple(2) == 2


def test_1_to_6_smallest_multiple():
    '''Test the 1–6 case (2 * 2 * 3 * 5)'''

    assert smallest_multiple(6) == 60


def test_1_to_10_smallest_multiple():
    '''Test the known 1–10 case'''

    assert smallest_multiple(10) == 2520
