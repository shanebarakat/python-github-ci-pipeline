"""Unit tests of the function diffiehellman.helpers.modulo_exp"""

from diffie_hellman_merkle.helpers import modulo_exp


def test_expected_output_modulo_exp():
    """Confirm that the function works as expected for some hard-coded test cases"""
    for pair in ((5, 9, 4), (2, 12, 7), (2, 50, 12)):
        func_output = modulo_exp(pair[0], pair[1], pair[2])
        expected_output: int = (pair[0] ** pair[1]) % pair[2]
        assert func_output == expected_output, f"""
        Case: ({pair[0]}^{pair[1]})mod{pair[2]}
        Expected result {expected_output} ...
        ...but received result modulo_exp({pair[0]}, {pair[1]}, {pair[2]}) = {func_output}"""
