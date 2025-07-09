

"""Units tests of the function diffie_hellman_merkle.helpers.is_primitive_root_modulo_p"""

import unittest
from diffie_hellman_merkle.helpers import g_is_primitive_root_modulo_p


def test_is_primitive_root_modulo_p() -> None:
    """
    Checks a few hand-picked known cases (positive and negative cases) for `g_is_primitive_root_modulo_p`.

    Tests various combinations of `g` and `p` to ensure the function correctly identifies
    primitive roots modulo `p`.
    """
    tester = unittest.TestCase()
    for g, p, true_state in (
        (7, 42_071, True),
        (6, 42_071, False),
        (2, 1_000_003, True),
        (27, 1_000_003, False),
        (986, 54_319, True),
        (985, 54_319, False),
    ):
        func_output = g_is_primitive_root_modulo_p(g, p)
        tester.assertEqual(
            func_output, true_state,
            f"expected result '{true_state}' but received "
            f"is_primitive_root_modulo_p(g={g}, p={p})='{func_output}'"
        )

