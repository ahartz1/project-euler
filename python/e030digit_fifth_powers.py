"""
Project Euler #30: Digit Fifth Powers

From the description:
    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
"""

from __future__ import (absolute_import, print_function)
from ensure_integer import ensure_integer


def digit_powers_sum(power=5):
    """
    Return the sum of all numbers equal to the sum of their digits raised to `power`.

    Args:
        power (int): The power to which a numbers digits must be raised before
            summing them.
    Return:
        The sum of all numbers whose sum of digits raised to `power` are equal
        to that number.
    """

    ensure_integer(power)

    power_sums = []
    # Because 1 is not a sum, skip it
    i = 2
    # If each individual digit were the maximum value (9), then we should keep
    # going until it is not possible to sum the digits to meet that value.
    while i < (9 ** power) * len(str(i)):
        if is_digit_powers(i, power):
            power_sums.append(i)
        i += 1

    return sum(power_sums)


def is_digit_powers(n, power=5):
    """
    Return True if n equals the sum of its digits raised to `power`.

    Args:
        n (int): The number to check.
        power (int): The power to raise each digit to before summing.

    Return:
        Boolean indication of whether the digits raised to the given power sum
        to n.
    """

    power_sum = 0
    terms = list(str(n))
    for term in terms:
        power_sum += int(term) ** power

    return power_sum == n


if __name__ == '__main__':
    print('The sum of the numbers that can be written as the sum of the 5th '
          'powers of their digits:\n{}'.format(digit_powers_sum(power=5)))
