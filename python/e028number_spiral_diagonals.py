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
from ensure_integer import ensure_integer


class NonOddInputError(Exception):
    pass


def spiral_diagonals_sum(edge_length=1001):
    """
    Return sum of spiral diagonals

    Args:
        edge_length (int): The length of the outside edge of the spiral (odd).

    Returns:
        Sum of spiral diagonals.
    """

    ensure_integer(edge_length, var_name='edge_length')
    if edge_length % 2 == 0:
        raise NonOddInputError('edge_length must be odd')

    spiral_edge = 1
    spiral_corners = [1, ]
    while spiral_edge < edge_length:
        # Next odd edge length
        spiral_edge += 2

        # Top right corner is square of spiral_edge
        temp_corner = spiral_edge ** 2
        spiral_corners.append(temp_corner)
        for _ in range(3):
            # Other corners can be calculated by subtracting spiral_edge - 1
            # from the previous corner value
            temp_corner -= (spiral_edge - 1)
            spiral_corners.append(temp_corner)

    return sum(spiral_corners)


if __name__ == '__main__':
    edge_length = 1001
    print('Spiral Diagonal Sum for spiral of edge length'
          ' {}: {}'.format(edge_length, spiral_diagonals_sum(edge_length)))
