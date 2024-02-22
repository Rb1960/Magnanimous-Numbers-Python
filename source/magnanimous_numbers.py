"""
Implement a predicate to determine if a number is a Magnanimous Number


Note:
    Magnanimous Numbers are based on a sequence of integers therefore
    all non-integer objects are NOT magnannimous, and the predicate should return False
    
    Negative integers are also NOT Magnanimous.
    
"""
from sympy import isprime


def _reject_non_candidates(candidate):
    """
    Reject non-integer values  and negative integers
    """
    if not isinstance(candidate, int):
        return True

    return candidate < 0


def is_magnanimous(candidate):
    """
    checks if the candidate is a magnanimous_number

    :return:
    True if magnanimous otherwise False
    """
    as_str = str(candidate)
    if _reject_non_candidates(candidate):
        return False

    result = True
    for index in range(1, len(as_str)):
        lhs = int(as_str[0:index])
        rhs = int(as_str[index:])
        if not isprime(lhs + rhs):
            result = False
            break

    return result
