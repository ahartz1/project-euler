"""
Project Euler #31: Coin Sums

From the description:
    In England the currency is made up of pound, £, and pence, p, and there are
    eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

    How many different ways can £2 be made using any number of coins?
"""

from __future__ import (absolute_import, print_function)
from ensure_integer import ensure_integer
from itertools import combinations


def coin_sums(pounds=2, pence=0, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
    """
    The number of English coin combinations summing to the given amount.

    Args:
        pounds (int): The number of pounds in the sum.
        pence (int): The number of pence in the sum.
        coins (tuple): (optional) The coins to use.
    Return:
        The number of combinations of English coins that sum to the given amount.
    """

    ensure_integer(pounds, greater_than=-1, var_name='pounds')
    ensure_integer(pence, greater_than=-1, var_name='pence')
    target_pence = (100 * pounds) + pence

    num_combinations = 0
    # We need to cycle through the different combinations. Because these aren't
    # permutations, we need to make sure not to double count.
    # We could make a function that calculates the number of combinations for a
    # particular set of coins, then feed each potential combination into it.
    for i in range(1, len(coins) + 1):
        for combo in list(combinations(coins, i)):
            num_combinations += num_coin_combos(list(combo), target_pence)

    return num_combinations


def num_coin_combos(coins, target_pence):
    """
    The number of combinations of specific `coins` to make `target_pence`.

    Uses a recursive approach, starting with the largest number of the biggest
    coin first.

    Args:
        coins (array): The coin values (in pence) that must be used in
            combination to make up `target_pence`.
        target_pence (int): The number of pence to add up to.
    Return:
        The number of combinations possible using each of the specified coins at
        least once.
    """

    if sum(coins) > target_pence:
        # If the sum of the coins is too big, then no possible combinations.
        return 0

    if len(coins) == 1:
        # Recursion base case
        if target_pence % coins[0] == 0:
            # If this coin can make target_pence evenly, then combo is valid
            return 1
        return 0

    # Make sure the biggest coin is at the end of the list
    coins = sorted(coins)

    num_combos = 0
    num_biggest_coin = (target_pence - sum(coins[:-1])) // coins[-1]
    while num_biggest_coin > 0:
        num_combos += num_coin_combos(
            coins[:-1],
            target_pence - (num_biggest_coin * coins[-1]))

        num_biggest_coin -= 1

    return num_combos


if __name__ == '__main__':
    pounds = 2
    pence = 0
    print('The number of combinations in English coins to make up £{} {}p: '
          '{}'.format(pounds, pence, coin_sums(pounds, pence)))
