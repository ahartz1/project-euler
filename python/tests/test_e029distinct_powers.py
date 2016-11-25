"""
Tests for Project Euler #29: Distinct Powers
"""

from __future__ import (absolute_import)
from e029distinct_powers import distinct_powers


def test_distinct_powers_small():
    """Test known value of distinct powers for a=5 and b=5"""

    assert distinct_powers(2, 5) == 4


def test_distinct_powers_another_small():
    """Test known value of distinct powers for a=5 and b=5"""

    assert distinct_powers(5, 5) == 15
