"""Unit tests for the function diffiehellman.helpers.is_prime"""

from diffie_hellman_merkle.helpers import is_prime


def test_is_prime():
    """Check output on some known cases"""
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
        assert (
            func_output == expected_output
        ), f"is_prime({case[0]}) returned {func_output} but expected {case[1]}"
