

"""Unit tests of the function diffie_hellman_merkle.helpers.modulo_exp"""

import secrets
import unittest
from diffie_hellman_merkle.helpers import modulo_exp


class TestModuloExp(unittest.TestCase):
    """
    Comprehensive unit tests for the modulo_exp function.

    This test suite verifies the correctness, robustness, and performance
    of the modulo_exp function by comparing its output against
    expected results for a wide range of randomly generated inputs.
    """

    def test_expected_output(self) -> None:
        """
        Confirm that the modulo_exp function works as expected for a variety of random test cases.

        Generates 1000 random sets of base, exponent, and modulus,
        then asserts that the function's output matches the
        mathematically expected result ((base ** exponent) % modulus).
        This test helps ensure the function's accuracy across different input ranges.
        """
        for _ in range(1000):
            base: int = secrets.SystemRandom().randint(2, 999_999)
            exponent: int = secrets.SystemRandom().randint(2, 69)
            modulus: int = secrets.SystemRandom().randint(2, 999)

            func_output: int = modulo_exp(base, exponent, modulus)
            expected_output: int = (base ** exponent) % modulus

            self.assertEqual(
                func_output,
                expected_output,
                f"""
                Case: ({base}^{exponent})mod{modulus}
                Expected result {expected_output} ...
                ...but received result modulo_exp({base}, {exponent}, {modulus}) = {func_output}"""
            )

