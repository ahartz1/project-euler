"""Project Euler Problem #4: Largest Palindrome Product"""


def lgst_pal(n):
    """
    This function is meant to determine the largest palindrome number created
    from the product of 2 n-digit-long numbers.
    """

    # Start by finding the largest and smallest n-digit num products
    largest = int('9' * n) ** 2
    smallest = int(str('1' + ('0' * (n - 1)))) ** 2

    # Go through possible range, test for palindrome, then test for divisiblity
    for i in range(largest, smallest - 1, -1):
        if is_palindrome(i):
            ret = check_n_digit_div(i, n)
            if ret[1] is not None:
                return ret


def is_palindrome(num):
    '''Test whether given number is a palindrome or not'''

    str_num = str(num)
    if str_num == str_num[::-1]:
        return True
    return False


def check_n_digit_div(num, n):
    '''See if num is divisible by two n-digit numbers'''

    # Start of range should be the largest n-digit number
    largest = int('9' * n)

    # End of range should be the smallest n-digit number
    smallest = int('1' + ('0' * (n - 1)))

    for i in range(largest, smallest - 1, -1):
        if len(str(num // i)) > n:
            return [num, None, None]
        if num % i == 0 and len(str(i)) == len(str(num // i)) == n:
            return [num, i, num // i]
    return [num, None, None]


if __name__ == '__main__':
    print(lgst_pal(3))
