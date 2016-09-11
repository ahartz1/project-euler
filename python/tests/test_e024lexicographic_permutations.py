"""
Tests for Project Euler #24: Lexicographic Permutations
"""

from __future__ import (absolute_import)
from nose.tools import raises
from e024lexicographic_permutations import NumberOutOfRangeError
from e024lexicographic_permutations import lexicographic_permutations
from e024lexicographic_permutations import check_num_digits_moved


@raises(NumberOutOfRangeError)
def test_number_exceeds_permutations_error():
    '''With two digits, there are only 2 permutations; expect error'''

    lexicographic_permutations(1, 3)


@raises(NumberOutOfRangeError)
def test_check_num_digits_moved_true():
    '''As above, with two digits, there are only 2 permutations, expect error'''

    check_num_digits_moved(1, 3)


def test_check_num_digits_moved_false():
    '''There are 6 permutations of 3 digits; all three digits are involved'''

    assert check_num_digits_moved(2, 6) == (3, 6)


def test_lexicographic_permutations_1():
    '''With 3 digits, we expect the 3rd permutation to be 102'''

    assert lexicographic_permutations(2, 3) == '102'


def test_lexicographic_permutations_2():
    '''With 3 digits, we expect the 6th permutation to be 210'''

    assert lexicographic_permutations(2, 6) == '210'


def test_lexicographic_permutations_3():
    '''With 5 digits, we expect the 16th permutation to be 03241'''

    assert lexicographic_permutations(4, 16) == '03241'
