
"""Unit tests for the function diffie_hellman_merkle.helpers.is_prime"""

import unittest
from typing import List, Tuple
from diffie_hellman_merkle.helpers import is_prime


def test_is_prime() -> None:
    """Verify output on some known cases."""
    # Create a dummy TestCase instance to use its assertion methods
    tester: unittest.TestCase = unittest.TestCase()

    test_cases: List[Tuple[int, bool]] = [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (4_257_452_468_388, False),
        (4_257_452_468_389, True),
        (4_257_452_468_390, False),
    ]

    for number, expected_output in test_cases:
        func_output: bool = is_prime(number)
        tester.assertEqual(
            func_output,
            expected_output,
            f"is_prime({number}) returned {func_output} but expected {expected_output}"
        )
