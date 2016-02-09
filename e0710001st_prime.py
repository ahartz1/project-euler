""""
Project Euler Problem #7: 10,001st Prime
"""

from __future__ import (print_function)


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


def is_prime(n):
    '''Return True if n is prime, False otherwise
    Slightly different implementation to avoid wasting cycles where no multiple
    is able to be found'''

    i = 2
    while i < n:
        if n % i == 0:
            return False
        if n / i < 0.5:
            i = n - 1
        i += 1

    return True


if __name__ == '__main__':
    '''Answer: 104743'''
    print(nth_prime(10001))
