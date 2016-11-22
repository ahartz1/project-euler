"""
Project Euler #28: Number Spiral Diagonals

From the description:

    Starting with the number 1 and moving to the right in a clockwise direction
    a 5 by 5 spiral is formed as follows:

                             21 22 23 24 25
                             20  7  8  9 10
                             19  6  1  2 11
                             18  5  4  3 12
                             17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
"""

from __future__ import (absolute_import, print_function)
#  from ensure_integer import ensure_integer


def spiral_diagonal_sum(edge_length=1001):
    """
    Return sum of spiral diagonals

    Arg:
        edge_length (int): The length of the outside edge of the spiral (odd).

    Returns:
        Sum of spiral diagonals.

    Note: This takes a long time to run!
    """

    pass


if __name__ == '__main__':
    edge_length = 1001
    print('Spiral Diagonal Sum for spiral of edge length'
          ' {}: {}'.format(edge_length, spiral_diagonal_sum(edge_length)))
