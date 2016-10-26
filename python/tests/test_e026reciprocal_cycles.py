"""
Tests for Project Euler #26: Reciprocal Cycles
"""

from __future__ import (absolute_import)
from nose.tools import raises
from e026reciprocal_cycles import NumberOutOfRangeError
from e026reciprocal_cycles import find_pattern
from e026reciprocal_cycles import pattern_is_repeated
from e026reciprocal_cycles import reciprocal_cycles


@raises(NumberOutOfRangeError)
def test_exception_for_less_than_1():
    """Numbers less than 1 are not allowed as input."""

    reciprocal_cycles(0)


@raises(NumberOutOfRangeError)
def test_exception_for_non_integer():
    """Non-integers are not allowed as input."""

    reciprocal_cycles(155.2223)


def test_find_pattern_no_repeat():
    """Confirm that if no pattern exists, we get 0."""

    no_repeat = ['1', '2', '5']
    assert find_pattern(no_repeat) == 0


def test_find_pattern_has_repeat():
    """Confirm that if pattern exists, we detect it."""

    has_repeat = ['1', '2', '1', '2', '1', '2']
    assert find_pattern(has_repeat) == 2


def test_find_pattern_has_repeat_after_filler():
    """Confirm that if pattern exists, we detect it."""

    has_repeat = ['0', '1', '2', '1', '2', '1', '2']
    assert find_pattern(has_repeat) == 2


def test_pattern_is_repeated_false():
    """Confirm that if pattern does not exist, we get False."""

    pattern = ['1', '2']
    offset = 0
    in_list = ['1', '2', '4', '2', '4', '2', '4']
    assert pattern_is_repeated(pattern, offset, in_list) == False


def test_pattern_is_repeated_true():
    """Confirm that if pattern exists, we get True."""

    pattern = ['2', '4']
    offset = 1
    in_list = ['1', '2', '4', '2', '4', '2', '4', '2']
    assert pattern_is_repeated(pattern, offset, in_list) == True


def test_reciprocal_cycles_none():
    """Confirm that if no patterns exist, we get None."""

    assert reciprocal_cycles(3) == None


def test_reciprocal_cycles_one():
    """1/3 has longest under 4: 1-digit-long repeat, 0.(3)."""

    assert reciprocal_cycles(4) == 3


def test_reciprocal_cycles_six():
    """1/7 has longest under 8: 6-digit-long repeat, 0.(142857)."""

    assert reciprocal_cycles(8) == 7
