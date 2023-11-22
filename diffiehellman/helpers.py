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
