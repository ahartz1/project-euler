"""
Project Euler problem #3: Largest Prime Factor
"""

from __future__ import (print_function,)


def lpf(n):
    '''Returns the largest prime factor of n for n > 1'''

    if is_prime(n):
        return n

    # Start at large end of range, working toward 1
    for i in range(n - 1, 0, -1):

        # if our number is divisible by i, check to see if i is prime
        if n % i == 0:
            if is_prime(i):
                return i
        if i == 1:
            return 1


def is_prime(m):
    '''determine if m is prime'''
    for i in range(m - 1, 1, -1):
        if m % i == 0:
            return False
    return True

if __name__ == '__main__':
    print('Largest common factor of 600851475143: {}'.format(lpf(600851475143)))
    # print('Largest common factor of 13195: {}'.format(lpf(13195)))
