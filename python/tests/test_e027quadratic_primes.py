"""
Tests for Project Euler #27: Quadratic Primes
"""

from __future__ import (absolute_import)
from e027quadratic_primes import consecutive_primes


def test_consecutive_primes_1():
    """From project description, n^2 + n + 41 has 40 consecutive primes."""

    assert consecutive_primes(1, 41) == 40


def test_consecutive_primes_2():
    """From project description, n^2 - 79n + 1601 has 80 consecutive primes."""

    assert consecutive_primes(-79, 1601) == 80


def test_consecutive_primes_3():
    """Discovered max."""

    assert consecutive_primes(-999, 61) == 1011
