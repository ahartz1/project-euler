"""
Project Euler problems often require checking for prime numbers; here is the
best implementation that I've come up with.
"""


def is_prime(n):
    """
    Return True if n is prime, False otherwise

    Avoids wasting cycles where no multiple is able to be found
    """

    i = 2
    while i < n:
        if n % i == 0:
            return False
        if i > n / i:
            break
        i += 1

    return True
