
"""# User-facing functions and classes"""

from diffie_hellman_merkle import helpers


class DiffieHellmanMerkle:
    """For secure key exchange across an unsecure (public) channel using Finite Field Diffie-Hellman-Merkle Key Exchange (RFC 7919)

    Refer to:
        https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange#Cryptographic_explanation

    Attributes:
        shared_modulus (int): Publicly-shared modulus number (must be a prime number), 'p' in DH.
        shared_base (int): Publicly-shared base number, 'g' in DH.
        personal_secret (int): Secret (non-public) number unique to this user, 'a' or 'b' in DH.
        value_to_share (int): Publicly-shared result of algorithmic calculation for this user (function of `shared_modulus`,`shared_base` and `personal_secret`), 'A' or 'B' in DH.
        shared_secret (int | None): Secure secret (non-public) number to use for encrypted communication, 'K' in DH.
    """

    def __init__(
        self,
        shared_modulus: int,
        shared_base: int,
        personal_secret: int,
    ) -> None:
        """Initializes a DiffieHellmanMerkle object with public and private parameters.

        This constructor performs validation of the shared modulus and shared base,
        and calculates the initial public key to share.

        Args:
            shared_modulus (int): A large prime number, publicly known. This is 'p' in DH.
            shared_base (int): A primitive root modulo `shared_modulus`, publicly known. This is 'g' in DH.
            personal_secret (int): A secret integer, unique to this participant. This is 'a' or 'b' in DH.

        Raises:
            ValueError: If `shared_modulus` is not prime or `shared_base` is not a primitive root modulo `shared_modulus`.
        """
        self._validate_parameters(shared_modulus, shared_base)

        self.shared_modulus: int = shared_modulus
        self.shared_base: int = shared_base
        self.personal_secret: int = personal_secret
        self.value_to_share: int = helpers.modulo_exp(
            base=self.shared_base, exp=self.personal_secret, mod=self.shared_modulus
        )
        self.shared_secret: int | None = None

    def _validate_parameters(self, shared_modulus: int, shared_base: int) -> None:
        """Validates the shared modulus and shared base parameters.

        Ensures that the shared modulus is a prime number and the shared base
        is a primitive root modulo the shared modulus.

        Args:
            shared_modulus (int): The modulus to validate ('p' in DH).
            shared_base (int): The base to validate against the modulus ('g' in DH).

        Raises:
            ValueError: If `shared_modulus` is not prime or `shared_base` is not a primitive root modulo `shared_modulus`.
        """
        if not helpers.is_prime(shared_modulus):
            raise ValueError(
                f"shared_modulus must be a prime number ({shared_modulus} is not prime)"
            )
        if not helpers.g_is_primitive_root_modulo_p(g=shared_base, p=shared_modulus):
            raise ValueError(
                f"`shared_base` must be a primitive root modulo `shared_modulus`. Received shared_base={shared_base}, shared_modulus={shared_modulus}"
            )

    def generate_shared_secret(
        self,
        received_value_to_share: int,
    ) -> None:
        """Computes the shared secret using the received public key from the other party.

        This method calculates the final shared secret (K) using the other party's
        public key (B or A) and this instance's private key (a or b).
        The result is stored in the `shared_secret` attribute.

        Args:
            received_value_to_share (int): The public key received from the other participant
                                    (e.g., B = g^b mod p, if this instance is Alice).

        Returns:
            None: The shared secret is stored internally in `self.shared_secret`.
        """

        self.shared_secret = helpers.modulo_exp(
            base=received_value_to_share,
            exp=self.personal_secret,
            mod=self.shared_modulus,
        )
