"""Units tests of the function diffie_hellman_merkle.helpers.is_primitive_root_modulo_p"""

from diffie_hellman_merkle.helpers import g_is_primitive_root_modulo_p


def test_is_primitive_root_modulo_p():
    """Checks a few hand-picked known cases (positive and negative cases)"""
    for g, p, true_state in (
        (7, 42_071, True),
        (6, 42_071, False),
        (2, 1_000_003, True),
        (27, 1_000_003, False),
        (986, 54_319, True),
        (985, 54_319, False),
    ):
        func_output = g_is_primitive_root_modulo_p(g, p)
        assert (
            func_output == true_state
        ), f"expected result '{true_state}' but received is_primitive_root_modulo_p(g={g}, p={p})='{func_output}'"
