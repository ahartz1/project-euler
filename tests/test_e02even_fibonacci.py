"""
Tests for Project Euler #2: Even Fibonacci Numbers
"""

from __future__ import (absolute_import,)
from e02even_fibonacci import even_fibonacci_sum


def test_even_fibonacci_sum():
    '''Test on the small cases that we can confirm'''

    '1, 1, 2, 3, 5, 8, 13; 2 + 8 = 10'
    assert even_fibonacci_sum(8) == 10

    '21, 34'
    assert even_fibonacci_sum(34) == 44
