"""
Project Euler Problem #8: Largest Product in a Series
"""

from __future__ import (print_function)


euler_series = '''
73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450
'''


def largest_product_in_a_series(n, series):
    '''Return the n adjacent digits in SERIES with the largest product'''

    # Start by removing the newlines that came with the copied series
    SERIES = series.replace('\n', '')

    # Substrings to investigate cannot include 0; break SERIES into list of
    # substrings not containing 0
    sub_series = SERIES.split('0')

    # Eliminate any substrings that are not at least n characters long
    working_list = list()
    for substr in sub_series:
        if len(substr) >= n:
            working_list.append(substr)
    print(working_list)

    if len(working_list) == 0:
        return 'No {}-number subsets without a zero'.format(n)

    largest_product = 1
    largest_substring = ''
    for s in working_list:
        # We add 1 below; think of the case where len(s) == n
        for i in range(len(s) - n + 1):
            sub_s_prod = 1
            for j in range(n):
                sub_s_prod *= int(s[i + j])
            if sub_s_prod > largest_product:
                largest_product = sub_s_prod
                largest_substring = s[i:i + n]

    print(largest_substring)
    return largest_product


if __name__ == '__main__':
    '''Answer: 23514624000; String: 5576689664895'''
    print(largest_product_in_a_series(13, euler_series))
