"""# Internal (non-user-facing) helper functions and classes

- `is_prime(n: int) -> bool` - Returns `True` if integer `n` is prime, otherwise `False`
- `g_is_primitive_root_modulo_p(g: int, p: int) -> bool` - Returns `True` if `g` is primitive root modulo prime number `p`, otherwise `False`
- `modulo_exp(base: int, exp: int, mod: int) -> int` - Memory-efficient calculation of the modulo of an exponentiated number (e.g. the value of 123^456)mod7
"""


def modulo_exp(base: int, exp: int, mod: int) -> int:
    r"""Memory-efficient calculation of the modulo of an exponentiated number
    e.g. the value of (123^456)mod7

    This algorithm taken from the wikipedia article:
        https://en.wikipedia.org/wiki/Modular_exponentiation#Memory-efficient_method

    Examples:
        >>> modulo_exp(base=6, exp=9, mod=420) 
        216 

    Args: 
        base (int): The base number to be exponentiated
        exp (int): The number in the exponent
        mod (int): The modulus (divisor) in the modulo calculation

    Returns:
        (int): The final result of the modulo calculation
    """
    moving_solution: int = 1
    moving_exp: int = 0
    while moving_exp < exp:
        moving_exp += 1
        moving_solution = (base * moving_solution) % mod
    return moving_solution

 
def is_prime(n: int) -> bool:
    """Returns `True` if integer `n` is prime, otherwise `False`

    This code is taken from a stack overflow answer:
        https://stackoverflow.com/questions/1801391/how-to-create-the-most-compact-mapping-n-→-isprimen-up-to-a-limit-n

    Examples:
        >>> is_prime(69)
        False
        >>> is_prime(440_817_757)
        True

    Args:
        n (int): The integer to check (whether it is prime or not)

    Returns:
        (bool): `True` if `n` is prime, otherwise `False`
    """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def g_is_primitive_root_modulo_p(g: int, p: int) -> bool:
    """Returns `True` if `g` is primitive root modulo prime number `p`, otherwise `False`

    Examples:
        >>> g_is_primitive_root_modulo_p(g=69, p=251)
        False
        >>> g_is_primitive_root_modulo_p(g=6, p=251)
        True

    Args:
        g (int): The potential primitive root number
        p (int): The modulo prime number

    Returns:
        (bool): `True` if `g` is primitive root modulo prime number `p`, otherwise `False`
    """
    for m in range(1, p - 1):
        if (p - 1) % m == 0 and modulo_exp(base=g, exp=m, mod=p) == 1:
            return False
    return True

    # alternative method: #
    # if g <= 1 or g >= p:
    #     return False
    # mods_already_seen: set[int] = set()
    # for e in range(1, p):
    #     result: int = modulo_exp(base=g, exp=e, mod=p)
    #     if result in mods_already_seen:
    #         return False
    #     mods_already_seen.add(result)
    # return True
