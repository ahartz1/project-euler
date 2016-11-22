"""
Project Euler problems often require positive integer inputs. This is an error
class and test for positive integers by default, with the option to get an
integer greater than a given value.
"""


class NotPositiveIntegerError(Exception):
    pass


def ensure_integer(n, greater_than=0, var_name="Input"):
    """
    Return True if n is a positive integer, else raise NotPositiveIntegerError

        Args:
            n (int): The input in question.
            greater_than (int): (optional) The number which n must be greater
                than.
            n_name (string): (optional) The name of the input variable for use
                in the error message.

        Returns:
            True if n is integer and meets greater_than criteria, error
            otherwise.
    """

    if n % 1 != 0 or n <= greater_than:
        raise NotPositiveIntegerError(
            var_name + ' must be an integer greater than ' +
            str(greater_than))
    return True
