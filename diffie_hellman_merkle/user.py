"""User-facing functions"""

from diffie_hellman_merkle import helpers


class DiffieHellmanMerkle:
    """docstring TODO
    Finite Field Diffie-Hellman (RFC 7919)
    https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange#Cryptographic_explanation
    """

    def __init__(
        self,
        shared_modulus: int,
        shared_base: int,
        personal_secret: int,
    ):
        """docstring TODO"""
        if not helpers.is_prime(shared_modulus):
            raise ValueError(
                f"shared_modulus must be a prime number ({shared_modulus} is not prime)"
            )
        self.shared_modulus = shared_modulus
        self.shared_base = shared_base
        self.personal_secret = personal_secret
        self.value_to_share: int = helpers.modulo_exp(
            base=self.shared_base, exp=self.personal_secret, mod=self.shared_modulus
        )
        self.shared_secret = None

    def generate_shared_secret(
        self,
        received_value_to_share: int,
    ):
        """docstring TODO"""
        self.shared_secret = helpers.modulo_exp(
            base=received_value_to_share,
            exp=self.personal_secret,
            mod=self.shared_modulus,
        )
