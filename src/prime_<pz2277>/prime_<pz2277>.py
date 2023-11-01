import math

def is_prime(n):
    """Check if a number is a prime number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a prime number, False otherwise.

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
