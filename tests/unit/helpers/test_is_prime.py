
"""Unit tests for the function diffie_hellman_merkle.helpers.is_prime"""

import unittest
from diffie_hellman_merkle.helpers import is_prime


def test_is_prime():
    """Verify output on some known cases"""
    # Create a dummy TestCase instance to use its assertion methods
    tester = unittest.TestCase()
    for case in (
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (4_257_452_468_388, False),
        (4_257_452_468_389, True),
        (4_257_452_468_390, False),
    ):
        func_output = is_prime(case[0])
        expected_output: bool = case[1]
        tester.assertEqual(
            func_output, expected_output,
            f"is_prime({case[0]}) returned {func_output} but expected {case[1]}"
        )

