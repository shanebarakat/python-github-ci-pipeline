

"""# Internal (non-user-facing) helper functions and classes

- `modulo_exp(base: int, exp: int, mod: int) -> int` - Memory-efficient calculation of the modulo of an exponentiated number (e.g. the value of 123^456)mod7
- `is_prime(n: int) -> bool` - Returns `True` if integer `n` is prime, otherwise `False`
- `_is_prime_small_checks(n: int) -> bool | None` - Internal helper for `is_prime` to perform initial quick checks.
- `g_is_primitive_root_modulo_p(g: int, p: int) -> bool` - Returns `True` if `g` is primitive root modulo prime number `p`, otherwise `False`
"""


def modulo_exp(base: int, exp: int, mod: int) -> int:
    r"""Memory-efficient calculation of the modulo of an exponentiated number.

    For example, calculates the value of (123^456)mod7.

    This algorithm is based on the method described in the Wikipedia article:
    https://en.wikipedia.org/wiki/Modular_exponentiation#Memory-efficient_method

    Examples:
        >>> modulo_exp(base=6, exp=9, mod=420)
        216
        >>> modulo_exp(base=2, exp=10, mod=5)
        4

    Args:
        base (int): The base number to be exponentiated.
        exp (int): The exponent.
        mod (int): The modulus (divisor) in the modulo calculation.

    Returns:
        int: The final result of the modulo calculation.
    """
    moving_solution: int = 1
    moving_exp: int = 0
    while moving_exp < exp:
        moving_exp += 1
        moving_solution = (base * moving_solution) % mod
    return moving_solution


def _is_prime_small_checks(n: int) -> bool | None:
    """Performs initial quick checks for primality for small numbers and divisibility by 2 and 3.

    This is an internal helper function for `is_prime`.

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool | None:
            - True if `n` is definitively prime (i.e., 2 or 3).
            - False if `n` is definitively not prime (e.g., less than 2, even, or divisible by 3).
            - None if further checks are required (i.e., `n` > 3 and not divisible by 2 or 3).
    """
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    return None


def is_prime(n: int) -> bool:
    """Checks if an integer `n` is a prime number.

    This function uses an optimized trial division algorithm.
    It first performs quick checks for small primes (2, 3) and divisibility by 2 and 3.
    Then, it proceeds with a wheel factorization optimization for larger numbers,
    checking only divisors of the form 6k ± 1.

    Examples:
        >>> is_prime(69)
        False
        >>> is_prime(440_817_757)
        True
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True
        >>> is_prime(7)
        True

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool: `True` if `n` is prime, otherwise `False`.
    """
    result = _is_prime_small_checks(n)
    if result is not None:
        return result

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        # Optimized trial division: checks numbers of the form 6k ± 1
        # Alternates adding 2 and 4 to 'i' (e.g., 5, 7, 11, 13, 17, 19...)
        i += w
        w = 6 - w

    return True


def g_is_primitive_root_modulo_p(g: int, p: int) -> bool:
    """Checks if `g` is a primitive root modulo a prime number `p`.

    A number `g` is a primitive root modulo a prime `p` if the smallest positive integer `k`
    for which `g^k ≡ 1 (mod p)` is `p-1`. This is equivalent to checking that `g^m ≢ 1 (mod p)`
    for all `m` that are proper divisors of `p-1`.

    This function iterates through all possible proper divisors `m` of `p-1` and checks the condition.

    Examples:
        >>> g_is_primitive_root_modulo_p(g=69, p=251)
        False
        >>> g_is_primitive_root_modulo_p(g=6, p=251)
        True
        >>> g_is_primitive_root_modulo_p(g=2, p=7)
        True
        >>> g_is_primitive_root_modulo_p(g=4, p=7)
        False
        >>> g_is_primitive_root_modulo_p(g=3, p=5)
        True

    Args:
        g (int): The potential primitive root number.
        p (int): The prime modulus.

    Returns:
        bool: `True` if `g` is a primitive root modulo `p`, otherwise `False`.
    """
    # According to the definition, g is a primitive root modulo p if for every
    # proper divisor m of (p-1), g^m % p is not equal to 1.
    # We iterate through all numbers from 1 to p-2. If m is a divisor of (p-1)
    # and g^m % p == 1, then g is not a primitive root.
    for m in range(1, p - 1):
        if (p - 1) % m == 0 and modulo_exp(base=g, exp=m, mod=p) == 1:
            return False
    return True
