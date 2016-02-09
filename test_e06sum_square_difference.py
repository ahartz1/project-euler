"""
Tests for Project Euler Problem #6: Sum Square Difference
"""

from __future__ import (absolute_import)
from e06sum_square_difference import sum_square_diff


def test_sum_square_diff_3():
    '''
    Test that for n of 3, result is 22
    (1 + 2 + 3)^2 = 36
    (1^2 + 2^2 + 3^2) = 14
    36 - 14 = 22
    '''

    assert sum_square_diff(3) == 22


def test_sum_square_diff_10():
    '''Test that for n of 10, result is 2640 (given test case)'''

    assert sum_square_diff(10) == 2640
