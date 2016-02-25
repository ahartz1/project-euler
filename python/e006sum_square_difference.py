"""
Project Euler Problem #6: Sum Sqaure Difference
"""

from __future__ import (print_function,)


def sum_square_diff(n):
    '''Return the difference of the sum of squares from 1-n and the square of
    the sum 1-n'''

    # Aggregate as we go
    sum_of_squares = 0
    sum_of_n = 0
    for i in range(1, n + 1):
        sum_of_squares += (i * i)
        sum_of_n += i

    return (sum_of_n * sum_of_n) - sum_of_squares

if __name__ == '__main__':
    print(sum_square_diff(100))
