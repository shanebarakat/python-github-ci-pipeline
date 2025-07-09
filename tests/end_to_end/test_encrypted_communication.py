

"""End-to-end tests of the whole system"""

# standard lib imports #
import base64

# 3rd party imports #
import cryptography.fernet
import pytest

# project module imports #
from diffie_hellman_merkle.user import DiffieHellmanMerkle


def test_encrypted_communication():
    """
    Tests end-to-end encrypted communication between two users.

    This test verifies that:
    1. Two users can establish a shared secret key using Diffie-Hellman-Merkle
       (DHM) key exchange.
    2. A message encrypted by one user using the shared key can be
       successfully decrypted by the other user using the same shared key.
    """
    public_shared_modulus: int = 855_467
    public_shared_base: int = 101
    original_message: str = "the secret channel is working nicely"
    original_message_bytes: bytes = original_message.encode("utf-8")

    user1: DiffieHellmanMerkle = DiffieHellmanMerkle(
        shared_modulus=public_shared_modulus,
        shared_base=public_shared_base,
        personal_secret=80_085,
    )
    user2: DiffieHellmanMerkle = DiffieHellmanMerkle(
        shared_modulus=public_shared_modulus,
        shared_base=public_shared_base,
        personal_secret=616_673,
    )

    # user1 encrypts message #
    user1.generate_shared_secret(user2.value_to_share)
    user1_fernet: cryptography.fernet.Fernet = cryptography.fernet.Fernet(
        key=base64.urlsafe_b64encode(
            str(user1.shared_secret).encode("utf-8").ljust(32)[:32]
        )
    )
    encrypted_message: bytes = user1_fernet.encrypt(original_message_bytes)

    # user2 decrypts message #
    user2.generate_shared_secret(user1.value_to_share)
    user2_fernet: cryptography.fernet.Fernet = cryptography.fernet.Fernet(
        key=base64.urlsafe_b64encode(
            str(user2.shared_secret).encode("utf-8").ljust(32)[:32]
        )
    )
    decrypted_message_bytes: bytes = user2_fernet.decrypt(encrypted_message)
    decrypted_message: str = decrypted_message_bytes.decode("utf-8")

    # decrypted message must match original message #
    if decrypted_message != original_message:
        pytest.fail(
            f'decrypted message "{decrypted_message}" does not match '
            f'original message "{original_message}"'
        )

