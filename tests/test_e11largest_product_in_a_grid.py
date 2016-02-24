"""
Tests for Project Euler #11: Largest Product in a Grid
"""

from __future__ import (absolute_import)
from nose.tools import raises
from e11largest_product_in_a_grid import InsufficientGridSizeError
from e11largest_product_in_a_grid import InconsistentGridError
from e11largest_product_in_a_grid import set_grid
from e11largest_product_in_a_grid import largest_grid_product
from e11largest_product_in_a_grid import largest_row_product
from e11largest_product_in_a_grid import largest_column_product
from e11largest_product_in_a_grid import largest_left_diag_product
from e11largest_product_in_a_grid import largest_right_diag_product


TEST_GRID = """
02 01 02 02 01
02 02 01 05 01
02 01 01 05 01
03 01 02 05 01
01 12 01 01 01
"""


FAIL_GRID = """
02 01 02 02 01
02 02 01 05 01
02 01 01 05 01
03 01 02 05
01 12 01 01 01
"""


@raises(InsufficientGridSizeError)
def test_exception_raised_if_grid_smaller_than_n():
    '''Should raise the InsufficientGridSizeError exception'''

    largest_grid_product(TEST_GRID, 6)


@raises(InconsistentGridError)
def test_exception_raised_if_grid_rows_different_lengths():
    '''Should raise the InconsistentGridError exception'''

    largest_grid_product(FAIL_GRID, 2)


def test_largest_row_product():
    '''TEST_GRID with n of 2; should = 12'''

    assert largest_row_product(set_grid(TEST_GRID), 2) == 12


def test_largest_column_product():
    '''TEST_GRID with n of 2; should = 25'''

    assert largest_column_product(set_grid(TEST_GRID), 2) == 25


def test_largest_left_diag_product():
    '''TEST_GRID with n of 2; should = 36'''

    assert largest_left_diag_product(set_grid(TEST_GRID), 2) == 36


def test_largest_right_diag_product():
    '''TEST_GRID with n of 2; should = 24'''

    assert largest_right_diag_product(set_grid(TEST_GRID), 2) == 24


def test_largest_grid_product_mine():
    '''Expect 2 * 5 * 5 * 5 = 250'''

    assert largest_grid_product(TEST_GRID, 4) == 250
