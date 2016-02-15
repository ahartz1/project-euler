"""
Project Euler #10: Summation of Primes
"""

from __future__ import (absolute_import, print_function)
from is_prime import is_prime


def sum_of_primes(n):
    '''Return the sum of all primes less than or equal to n'''

    ret = 0
    for i in range(2, n + 1):
        if is_prime(i):
            ret += i
    return ret

if __name__ == '__main__':
    our_n = 2000000
    print('Sum of primes <= {}: {}'.format(our_n, sum_of_primes(our_n)))
