"""
Tests for Project Euler #9: Special Pythagorean Triplet
"""


from __future__ import (absolute_import)
from e09special_pythagorean_triplet import special_pythagorean_triplet


def test_known_special_pythagorean_triplet():
    '''a = 3, b = 4, c = 5 should result in 60'''

    assert special_pythagorean_triplet(12) == 60
