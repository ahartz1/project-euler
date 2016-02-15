"""
Tests for prime number evaluation function
"""

from __future__ import (absolute_import)
from is_prime import is_prime


def test_is_prime():
    '''Make sure we are only getting primes'''

    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(4) == False
    assert is_prime(23) == True
    assert is_prime(102) == False
