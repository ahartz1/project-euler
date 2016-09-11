"""
Project Euler #24: Lexicographic Permutations

From the description:
    "A permutation is an ordered arrangement of objects. . . . If all of the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order.

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4,
    5, 6, 7, 8 and 9?"
"""

from __future__ import (absolute_import, print_function)
from math import ceil


class NumberOutOfRangeError(Exception):
    pass


def lexicographic_permutations(m, target_p_num):
    '''Return the target_p_num'th lexicographic permuatation of the
    numbers 0 though m'''

    # Make a list of the digit characters we are working with
    digits = [str(i) for i in range(0, m + 1)]

    # Determine how many digits are involved in reaching the target permutation
    num_digits_moved, permutations = check_num_digits_moved(m, target_p_num)

    curr_index = m + 1 - num_digits_moved
    while num_digits_moved > 1:
        # The number of permutations represented by the next digit's position
        digit_scale = permutations / num_digits_moved

        # target_p_num of 0 represents the maximum number of permutations for
        # the remaining digits (i.e., reverse this and all digits after)
        if target_p_num == 0:
            digits = digits[0:curr_index] + digits[len(digits):curr_index - 1:-1]
            break

        # Only perform calculations if digit_scale is not too large
        if target_p_num / digit_scale >= 1:
            # Determine the next digit by figuring out how many cycles of the
            # subsequent digits were needed to make it
            cycles_needed = ceil(target_p_num / digit_scale)

            # Rearrange the digits to reflect the number of cycles needed
            temp = digits.pop(curr_index + cycles_needed - 1)
            digits.insert(curr_index, temp)

            # Update target_p_num to be the remainder
            target_p_num = target_p_num % digit_scale

        # Prep for the next loop
        permutations = digit_scale
        num_digits_moved -= 1
        curr_index += 1

    return ('').join(digits)


def check_num_digits_moved(m, target_p_num):
    '''If target_p_num is less than 1 or exceeds the number of permutations
    of the numbers 0 though m, raise exception, otherwise return a tuple
    containing the number of permuted digits it takes to reach the
    target_p_num and the total permutations represented by that many
    digits'''

    if target_p_num < 1:
        raise NumberOutOfRangeError

    # Determine how many digits are involved (the final value of i) and the
    # number of permutations that they represent
    permutations = 1
    for i in range(1, m + 2):
        permutations *= i
        if permutations >= target_p_num:
            break

    # If the desired permutation number is greater than the total number of
    # permutations, raise error
    if permutations < target_p_num:
        raise NumberOutOfRangeError

    return (i, permutations)


if __name__ == '__main__':
    target_p_num = 1000000
    m = 9
    print('Permutation {:2} of the numbers 0–{}: {}'.format(
        target_p_num, m, lexicographic_permutations(m, target_p_num)))
