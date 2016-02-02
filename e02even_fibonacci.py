"""
Project Euler #2: Even Fibonacci Numbers

The Fibonacci sequence is 1 1 2 3 5 8 etc., where the next number of the
sequence is the sum of the previous two. Here, we find the sum of just the even
numbers in this sequence where the Fibonacci number is less than max.
"""

from __future__ import (print_function,)


def even_fibonacci_sum(max):
    '''Uses Python 3 print function'''
    lastnum = 1
    currnum = 1
    sum = 0
    while currnum < max:
        swap = lastnum
        lastnum = currnum
        currnum = swap + lastnum
        if currnum % 2 == 0:
            sum += currnum
    return sum

if __name__ == '__main__':
    print('The sum of even Fibonacci numbers up to {} is: {}'.format(
        4000000, even_fibonacci_sum(4000000)))
