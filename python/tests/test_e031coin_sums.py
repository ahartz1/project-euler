"""
Tests for Project Euler #31: Coin Sums
"""

from __future__ import (absolute_import)
from e031coin_sums import num_coin_combos
from e031coin_sums import coin_sums


def test_num_coin_combos():
    """Test for combinations of specific coins"""

    assert num_coin_combos([1, 5], 5) == 0
    assert num_coin_combos([1, 5], 6) == 1
    assert num_coin_combos([1, 2, 5], 10) == 2
    assert num_coin_combos([1, 2, 5, 10], 30) == 15


def test_coin_sums_small():
    """Test known values"""

    assert coin_sums(pounds=0, pence=1, coins=(1, )) == 1
    assert coin_sums(pounds=0, pence=2, coins=(1, 2)) == 2
    assert coin_sums(pounds=0, pence=3, coins=(1, 2)) == 2
    assert coin_sums(pounds=0, pence=4, coins=(1, 2)) == 3
    assert coin_sums(pounds=0, pence=5, coins=(1, 2, 5)) == 4
    assert coin_sums(pounds=0, pence=10, coins=(1, 2, 5, 10)) == 11
