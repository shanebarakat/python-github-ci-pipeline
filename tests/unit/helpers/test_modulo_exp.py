
"""Unit tests of the function diffie_hellman_merkle.helpers.modulo_exp"""

import secrets
from diffie_hellman_merkle.helpers import modulo_exp


def test_expected_output_modulo_exp():
    """Confirm that the function works as expected for some hard-coded test cases"""
    for _ in range(100):
        pair = (
            secrets.SystemRandom().randint(2, 999_999),
            secrets.SystemRandom().randint(2, 69),
            secrets.SystemRandom().randint(2, 999),
        )
        func_output = modulo_exp(pair[0], pair[1], pair[2])
        expected_output: int = (pair[0] ** pair[1]) % pair[2]
        assert (
            func_output == expected_output
        ), f"""
        Case: ({pair[0]}^{pair[1]})mod{pair[2]}
        Expected result {expected_output} ...
        ...but received result modulo_exp({pair[0]}, {pair[1]}, {pair[2]}) = {func_output}"""

