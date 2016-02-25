"""
Project Euler Problem #5: Smallest Multiple
"""

from __future__ import (print_function, absolute_import)
from functools import reduce


def smallest_multiple(n):
    '''Return the smallest positive number that is evenly divisible by all of the
    numbers from 1 to n'''

    # Each number has prime factors. We need to keep track of _how many times_
    # any given factor is used. First, generate a list of prime numbers up to
    # and including n. Second, divide the current number by each smaller prime,
    # repeating any successful prime and recording how many times it divided.
    # Multiply each key multiplied by its value to get the smallest multiple.
    prime_list = list()
    factor_list = list()
    for i in range(2, n + 1):
        if is_prime(i):
            prime_list.append(i)
        for index, prime in enumerate(prime_list):
            prime_count = 0
            temp_i = i
            while temp_i % prime == 0:
                prime_count += 1
                temp_i //= prime
            try:
                if factor_list[index] < prime_count:
                    factor_list[index] = prime_count
            except IndexError:
                factor_list.append(1)

    # Now that we have the prime list and the number of times each has appeared,
    # we need to raise each prime to that power.
    primes_to_power = list(map(pow, prime_list, factor_list))

    # The final step is to multiply each of these together
    return reduce(mult, primes_to_power)


def is_prime(n):
    '''Returns boolean indicating whether n is prime or not'''

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def pow(a, b):
    '''Helper function for map in smallest_multiple'''
    return a ** b


def mult(a, b):
    '''Helper function for reduce in smallest_multiple'''
    return a * b


if __name__ == '__main__':
    print(smallest_multiple(20))
