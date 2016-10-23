"""
Tests for Project Euler #25: 1000-digit Fibonacci number
"""

from __future__ import (absolute_import)
from nose.tools import raises
from e0251000_digit_fibonacci_number import NumberOutOfRangeError
from e0251000_digit_fibonacci_number import fibonacci_x_digits_index


@raises(NumberOutOfRangeError)
def test_exception_for_less_than_1():
    '''The index of the first 3-digit Fibonacci number is 12'''

    fibonacci_x_digits_index(0)


def test_fibonacci_2_digits():
    '''The index of the first 2-digit Fibonacci number is 7'''

    assert fibonacci_x_digits_index(2) == (7)


def test_fibonacci_3_digits():
    '''The index of the first 3-digit Fibonacci number is 12'''

    assert fibonacci_x_digits_index(3) == (12)
