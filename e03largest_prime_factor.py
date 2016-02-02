"""
Project Euler problem #3: Largest Prime Factor
"""

from __future__ import (print_function,)


def lpf(n):
    '''Returns the largest prime factor of n for n > 1'''

    # Idea: Build up list of primes, if a factor is found, reset the range
    # e.g.: 100 / 2 = 50, 50 / 2 = 25, 25 / 5 = 5 done; 5 iterations total

    primes_lt_n = [2]
    largest_prime = 1
    loop_n = n

    while True:
        # Try to reduce n by dividing by primes until largest prime factor is
        # found
        for loop_count, i in enumerate(primes_lt_n):

            # if loop_n divisible by i, update loop_n value to loop_n / i
            if loop_n % i == 0:
                loop_n = loop_n / i

                # check if i is the largest prime found, if so, update
                # largest_prime
                if i > largest_prime:
                    largest_prime = i

                # Restart the for loop
                break

            # End of current loop processing
            if loop_count == len(primes_lt_n) - 1:

                # Check for end condition where last prime is greater than
                # loop_n.  If the last prime tried is larger than loop_n, then
                # our largest factor is known.
                if primes_lt_n[-1] > loop_n:
                    return largest_prime

                # If we got this far, none of the primes tried are factors, so
                # remove them all and restart the for loop with just the next
                # prime
                test_prime = next_prime(primes_lt_n[-1])
                primes_lt_n = [test_prime]
                break


def next_prime(m):
    '''Generate next prime'''
    while True:
        m += 1
        if is_prime(m):
            return m


def is_prime(m):
    '''determine if m is prime'''
    for i in range(m - 1, 1, -1):
        if m % i == 0:
            return False
    return True

if __name__ == '__main__':
    print('Largest common factor of 600851475143: {}'.format(lpf(600851475143)))
