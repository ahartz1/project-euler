""""
Project Euler Problem #7: 10,001st Prime
"""

from __future__ import (absolute_import, print_function)
from is_prime import is_prime


def nth_prime(n):
    '''Return the nth prime number'''

    primes_found = 0
    i = 2
    while primes_found < n:
        if is_prime(i):
            primes_found += 1
        i += 1

    # We return i - 1 here because 1 is added to i at the end of each loop
    return i - 1


if __name__ == '__main__':
    '''Answer: 104743'''
    print(nth_prime(10001))
