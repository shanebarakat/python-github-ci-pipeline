
"""Unit tests of the class diffie_hellman_merkle.user.DiffieHellmanMerkle"""

# 3rd party imports #
import pytest

# project module imports #
from diffie_hellman_merkle.user import DiffieHellmanMerkle


def test_invalid_user_input():
    """Verify that invalid user input is identified and raises appropriate errors"""
    with pytest.raises(ValueError) as excinfo:
        DiffieHellmanMerkle(
            shared_modulus=25,  # not a prime number
            shared_base=420,
            personal_secret=69,
        )
    if "shared_modulus must be a prime number" not in str(excinfo.value):
        pytest.fail("Expected 'shared_modulus must be a prime number' in exception message")

    with pytest.raises(ValueError) as excinfo:
        DiffieHellmanMerkle(
            shared_modulus=907,
            shared_base=888,  # not a primitive root of `shared_modulus`
            personal_secret=420,
        )
    if "`shared_base` must be a primitive root modulo `shared_modulus`" not in str(excinfo.value):
        pytest.fail("Expected '`shared_base` must be a primitive root modulo `shared_modulus`' in exception message")


def test_generate_shared_secret():
    """Verify that a generated shared key matches for both users"""
    public_shared_modulus: int = 543_287
    public_shared_base: int = 170
    user1 = DiffieHellmanMerkle(
        shared_modulus=public_shared_modulus,
        shared_base=public_shared_base,
        personal_secret=1_234,
    )
    user2 = DiffieHellmanMerkle(
        shared_modulus=public_shared_modulus,
        shared_base=public_shared_base,
        personal_secret=4_321,
    )
    user1.generate_shared_secret(user2.value_to_share)
    user2.generate_shared_secret(user1.value_to_share)
    if user1.shared_secret != user2.shared_secret:
        pytest.fail("both users must generate the same shared secret")

