import math

def is_prime(n):

    """
    Determine whether a number is a prime number.
    
    :param n: The number to be checked.
    :type n: int
    :return: True if n is a prime number, False otherwise.
    :rtype: bool
    
    Example:
    >>> is_prime(5)
    True
    
    >>> is_prime(4)
    False
    
    """
    
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
