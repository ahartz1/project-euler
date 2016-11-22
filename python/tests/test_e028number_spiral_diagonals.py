"""
Tests for Project Euler #28: Number Spiral Diagonals
"""

from __future__ import (absolute_import)
from e028number_spiral_diagonals import spiral_diagonals_sum


def test_spiral_diagonals_sum_edge_3():
    """Test known value of edge length 3"""

    assert spiral_diagonals_sum(3) == 25


def test_spiral_diagonals_sum_edge_5():
    """Test known value of edge length 5"""

    assert spiral_diagonals_sum(5) == 101
