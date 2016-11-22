"""
Tests for ensure integer function
"""

from __future__ import (absolute_import)
from nose.tools import raises
from ensure_integer import NotPositiveIntegerError
from ensure_integer import ensure_integer


@raises(NotPositiveIntegerError)
def test_exception_for_less_than_1_part1():
    """Numbers less than 1 are not allowed as input."""

    ensure_integer(0)


@raises(NotPositiveIntegerError)
def test_exception_for_less_than_1_part2():
    """Numbers less than 1 are not allowed as input."""

    ensure_integer(-16)


@raises(NotPositiveIntegerError)
def test_exception_for_non_integer():
    """Non-integers are not allowed as input."""

    ensure_integer(155.2223)


def test_ensure_positive_integer():
    """Make sure positive integers return True"""

    assert ensure_integer(1) == True
    assert ensure_integer(2) == True
    assert ensure_integer(23) == True
    assert ensure_integer(595823) == True


def test_ensure_integer_greater_than_8_part1():
    """Make sure integers greater than 8 return True"""

    assert ensure_integer(23, greater_than=8) == True
    assert ensure_integer(9, greater_than=8) == True
    assert ensure_integer(11423, greater_than=8) == True


@raises(NotPositiveIntegerError)
def test_ensure_integer_greater_than_8_part2():
    """Make sure integers less than 8 return True"""

    assert ensure_integer(8, greater_than=8) == True
