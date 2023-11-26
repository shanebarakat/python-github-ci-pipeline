"""# User-facing functions and classes"""

from diffie_hellman_merkle import helpers


class DiffieHellmanMerkle:
    """For secure key exchange across an unsecure (public) channel using Finite Field Diffie-Hellman-Merkle Key Exchange (RFC 7919)

    Refer to:
        https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange#Cryptographic_explanation

    Attributes:
        shared_modulus (int): Publicly-shared modulus number (must be a prime number)
        shared_base (int): Publicly-shared base number
        personal_secret (int): Secret (non-public) number unique to this user
        value_to_share (int): Publicly-shared result of algorithmic calculation for this user (function of `shared_modulus`,`shared_base` and `presonal_secret`)
        shared_secret (int): Secure secret (non-public) number to use for encrypted communication
    """

    def __init__(
        self,
        shared_modulus: int,
        shared_base: int,
        personal_secret: int,
    ):
        if not helpers.is_prime(shared_modulus):
            raise ValueError(
                f"shared_modulus must be a prime number ({shared_modulus} is not prime)"
            )
        if not helpers.g_is_primitive_root_modulo_p(g=shared_base, p=shared_modulus):
            raise ValueError(
                f"`shared_base` must be a primitive root modulo `shared_modulus`. Received shared_base={shared_base}, shared_modulus={shared_modulus}"
            )
        self.shared_modulus = shared_modulus
        self.shared_base = shared_base
        self.personal_secret = personal_secret
        self.value_to_share: int = helpers.modulo_exp(
            base=self.shared_base, exp=self.personal_secret, mod=self.shared_modulus
        )
        self.shared_secret: int | None = None

    def generate_shared_secret(
        self,
        received_value_to_share: int,
    ) -> None:
        """Computes a secret shared secret key

        Args:
            received_value_to_share (int): `value_to_share` received from the user that we wish to securely communicate with.

        Returns:
            None (does not return anything)
        """

        self.shared_secret = helpers.modulo_exp(
            base=received_value_to_share,
            exp=self.personal_secret,
            mod=self.shared_modulus,
        )
