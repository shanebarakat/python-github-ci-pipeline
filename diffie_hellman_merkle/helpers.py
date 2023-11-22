"""Internal (non-user-facing) helper functions"""


def modulo_exp(base: int, exp: int, mod: int) -> int:
    r"""docstring TODO
    This algorithm taken from the wikipedia article
    https://en.wikipedia.org/wiki/Modular_exponentiation#Memory-efficient_method
    """
    moving_solution: int = 1
    moving_exp: int = 0
    while moving_exp < exp:
        moving_exp += 1
        moving_solution = (base * moving_solution) % mod
    return moving_solution


def is_prime(n: int) -> bool:
    """Returns True if n is prime.
    Code from: https://stackoverflow.com/questions/1801391/how-to-create-the-most-compact-mapping-n-→-isprimen-up-to-a-limit-n
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
