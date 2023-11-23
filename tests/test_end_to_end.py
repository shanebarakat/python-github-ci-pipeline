"""End-to-end tests of the whole python package"""

# standard lib imports #
import base64

# 3rd party imports #
import cryptography.fernet

# project module imports #
from diffie_hellman_merkle.user import DiffieHellmanMerkle


def test_encrypted_communication():
    r"""Verifies that 2 users can communicate a secret encrypted message,
    where the encryption key is communicated using Diffie-Hellman-Merkle
    key exchange
    """
    public_shared_modulus: int = 7_069_067_389
    public_shared_base: int = 247
    original_message: str = "the secret channel is working nicely"
    original_message_bytes: bytes = original_message.encode("utf-8")

    user1 = DiffieHellmanMerkle(
        shared_modulus=public_shared_modulus,
        shared_base=public_shared_base,
        personal_secret=80_085,
    )
    user2 = DiffieHellmanMerkle(
        shared_modulus=public_shared_modulus,
        shared_base=public_shared_base,
        personal_secret=616_673,
    )

    # user1 encrypts message #
    user1.generate_shared_secret(user2.value_to_share)
    user1_fernet = cryptography.fernet.Fernet(
        key=base64.urlsafe_b64encode(
            str(user1.shared_secret).encode("utf-8").ljust(32)[:32]
        )
    )
    encrypted_message: bytes = user1_fernet.encrypt(original_message_bytes)

    # user2 decrypts message #
    user2.generate_shared_secret(user1.value_to_share)
    user2_fernet = cryptography.fernet.Fernet(
        key=base64.urlsafe_b64encode(
            str(user2.shared_secret).encode("utf-8").ljust(32)[:32]
        )
    )
    decrypted_message_bytes: bytes = user2_fernet.decrypt(encrypted_message)
    decrypted_message: str = decrypted_message_bytes.decode("utf-8")

    # decrypted message must match original message #
    assert (
        decrypted_message == original_message
    ), f'decrypted message "{decrypted_message}" does not match original message "{original_message}"'
