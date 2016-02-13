"""
Project Euler #9: Special Pythagorean Triplet

Find a * b * c such that:
    1) a < b < c
    2) a + b + c = n
    3) a^2 + b^2 = c^2

"""

from __future__ import (print_function)


def special_pythagorean_triplet(n):
    '''
    Return a * b * c such that the above conditions are met, else return None
    '''

    for a in range(1, n):
        for b in range(a + 1, n):
            # Condition 1) requires that c is minimally equal to b + 1.
            # Substituting into condition 2: if a + b + (b + 1) > n, we are
            # beyond the largest value of 'b' for a fixed 'a'. Factoring the
            # above, a + 2 * b + 1 > n represents an end-of-loop condition.
            if a + 2 * b + 1 > n:
                break

            # Satisfy condition 2
            c = n - (a + b)

            # Satisfy condition 3
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

            # Check to see if there is no way of satisfying condition 3
            if a ** 2 + b ** 2 > c ** 2:
                break
    return None


if __name__ == '__main__':
    spt_n = 1000
    print('Special Pythagorean Triplet adding up to {}: {}'.format(
        spt_n, special_pythagorean_triplet(spt_n)))
