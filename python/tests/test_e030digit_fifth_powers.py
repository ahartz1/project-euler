"""
Tests for Project Euler #30: Digit Fifth Powers
"""

from __future__ import (absolute_import)
from e030digit_fifth_powers import is_digit_powers
from e030digit_fifth_powers import digit_powers_sum


def test_digit_powers_sum_forth():
    """Test known value for 4th powers"""

    assert digit_powers_sum(4) == 19316


def test_is_digit_powers():
    """Test is_digit_powers for known values"""

    assert is_digit_powers(1634, 4) is True
    assert is_digit_powers(1633, 4) is False
    assert is_digit_powers(153, 3) is True
    assert is_digit_powers(84, 2) is False
