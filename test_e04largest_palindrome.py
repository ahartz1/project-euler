"""
Tests for Project Euler Problem #4: Largest Palindrome Product
"""


from e04largest_palindrome import check_n_digit_div, is_palindrome, lgst_pal


def test_check_n_digit_div():
    '''Test that given number is divisible by 2 n-digit numbers'''
    assert check_n_digit_div(9009, 2) == [9009, 99, 91]
    assert not check_n_digit_div(9009, 2) == [9009, 99, 92]


def test_is_palindrome():
    '''Test that palindromes are correctly recognized'''
    assert is_palindrome(333)
    assert not is_palindrome(321)
    assert is_palindrome(323)
    assert not is_palindrome(233)


def test_known():
    '''Test that 9009 = 99 * 91'''

    assert lgst_pal(2) == [9009, 99, 91]


def test_div_palindrome_are_of_n_digits():
    '''Test that factors are both of n digits'''

    assert not lgst_pal(2) == [9779, 127, 77]
