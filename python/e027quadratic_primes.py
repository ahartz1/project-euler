"""
Project Euler #27: Quadratic Primes

From the description:

    Considering quadratics of the form:

        n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

        where |n| is the modulus/absolute value of n
        e.g., |11| = 11 and |−4| = 4

    Find the product of the coefficients, a and b, for the quadratic
    expression that produces the maximum number of primes for consecutive values
    of n, starting with n = 0.
"""

from __future__ import (absolute_import, print_function)
from is_prime import is_prime


class NotPositiveIntegerError(Exception):
    pass


def quadratic_primes(max_coefficient=1000):
    """
    Return a * b where n^2 + an + b produces the most consecutive primes

    Args:
        max_coefficient (int): The maximum value of b (and a + 1); positive.

    Returns:
        The product of a and b; a; b; and the number of consecutive primes they
        produce.

    Note: This takes a long time to run!
    """

    if max_coefficient % 1 != 0 or max_coefficient < 0:
        raise NotPositiveIntegerError(
            'max_coefficient must be a positive integer')

    consecutive_primes_max = 0
    a_value = None
    b_value = None
    for a in range(-max_coefficient + 1, max_coefficient):
        for b in range(-max_coefficient, max_coefficient + 1):
            c_p = consecutive_primes(a, b)
            if c_p > consecutive_primes_max:
                consecutive_primes_max = c_p
                a_value = a
                b_value = b

    return a_value * b_value, a_value, b_value, consecutive_primes_max


def consecutive_primes(a, b):
    """
    Return the number of consecutive primes produced by n^2 + an + b

    Args:
        a (int): The 'a' coefficient.
        b (int): The 'b' coefficient.

    Returns:
        The number of consecutive primes; zero if the first number is not prime
    """

    count = 0
    n = 0
    while is_prime(n**2 + a*n + b):
        count += 1
        n += 1

    return count


if __name__ == '__main__':
    max_digit = 1000
    product, a, b, c_p_max = quadratic_primes(max_digit)
    print('a * b for n^2 + an + b with most consecutive primes:'
          '{} (a:{}, b:{}, consecutive primes: {})'.format(
              product, a, b, c_p_max))
