"""
Project Euler #26: Reciprocal Cycles

Find the integer x which has the longest repeating pattern in the decimals of
1/x for x < 1000.
"""

from __future__ import (absolute_import, print_function)
from decimal import Decimal
from decimal import getcontext


class NumberOutOfRangeError(Exception):
    pass


def reciprocal_cycles(max_num, precision=6000):
    """
    Return x below `max_num` where 1/x has the longest repeating pattern.

    Args:
        max_num (int): The non-inclusive number below which to look.
        precision (int): The number of decimal digits to use when calculating.

    Returns:
        The number whose repeating pattern is longest. If no repeating patterns
        exist, return None.

    Raises:
        NumberOutOfRangeError: Input number was not an integer greater than
        zero.
    """

    if max_num < 1 or max_num % 1 != 0:
        raise NumberOutOfRangeError('max_num must be a positive integer')

    getcontext().prec = precision
    longest_pattern = 0
    ret = None
    for i in range(2, max_num):
        unit_decimal = Decimal(1) / Decimal(i)
        decimal_list = list(str(unit_decimal))
        # Only bother to continue if we have enough digits for potential repeat
        if len(decimal_list) < precision:
            continue
        # Remove leading zero, decimal point, and last (likely rounded) digit
        decimal_list = decimal_list[2:-1]
        pattern_length = find_pattern(decimal_list)
        if pattern_length > longest_pattern:
            longest_pattern = pattern_length
            ret = i

    return ret


def find_pattern(in_list):
    """
    Return the length of a repeating pattern in `in_list`, if one exists.

    Args:
        in_list (list): List of single characters.

    Returns:
        The integer length of the pattern, 0 if no pattern found.
    """

    # Pattern sets are stored as: [pattern_list, offset]
    pattern_sets = list()
    for i, curr_char in enumerate(in_list):
        if i == 0:
            pattern_sets.append([[curr_char], i])
            continue
        for pattern_set in pattern_sets:
            # If the first character of the pattern matches, investigate further
            if pattern_set[0][0] == curr_char:
                if pattern_is_repeated(pattern_set[0], pattern_set[1], in_list):
                    # We have a winner
                    return len(pattern_set[0])
            # Otherwise, add the current character to this pattern set
            pattern_set[0].append(curr_char)
        # Make a new pattern set that starts with this character
        pattern_sets.append([[curr_char], i])
    return 0


def pattern_is_repeated(pattern, offset, in_list):
    """
    Checks if `pattern` at `offset` repeats in `in_list`.

    Args:
        pattern (list): List of single characters.
        offset (int): The offset at which to start the comparison in `in_list`.
        in_list (list): List of single characters against which to compare the
            pattern.

    Returns:
        A Boolean indicating whether the specified pattern repeats in `in_list`.
    """
    p_len = len(pattern)
    n = 1
    match = False
    # If the `in_list` subset length does not match the `pattern` length, we
    # can't make an accurate comparison
    while len(in_list[offset + (p_len * (n - 1)):offset + (p_len * n)]) \
            == len(pattern):
        if in_list[offset + (p_len * (n - 1)):offset + (p_len * n)] \
                == pattern:
            match = True
        else:
            match = False
            break
        n += 1
    return match


if __name__ == '__main__':
    max_digit = 1000
    print('The number with the longest repeating decimal below {}: {}'.format(
        max_digit, reciprocal_cycles(max_digit)))
