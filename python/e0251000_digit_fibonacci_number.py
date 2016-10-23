"""
Project Euler #25: 1000-digit Fibonacci number

Find the index of the first 1000-digit number in the Fibonacci sequence.
"""

from __future__ import (absolute_import, print_function)


class NumberOutOfRangeError(Exception):
    pass


def fibonacci_x_digits_index(num_digits):
    """Return the index of the first Fibonacci number with `num_digits`"""
    if num_digits < 1:
        raise NumberOutOfRangeError('Must specify number larger than 1')

    lastnum = 1
    currnum = 1
    index = 2
    while len(str(currnum)) < num_digits:
        swap = lastnum
        lastnum = currnum
        currnum = swap + lastnum
        index += 1

    return index


if __name__ == '__main__':
    fibonacci_length = 1000
    print('First Fibonacci number of length {}: {}'.format(
        fibonacci_length, fibonacci_x_digits_index(fibonacci_length)))
