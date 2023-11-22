"""User-facing functions"""

import helpers


class DiffieHellman:
    """docstring TODO
    Finite Field Diffie-Hellman (RFC 7919)
    https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange#Cryptographic_explanation
    """

    def __init__(
        self,
        shared_modulus: int,
        shared_base: int,
    ):
        """docstring TODO"""
        self.shared_modulus = shared_modulus
        self.shared_base = shared_base
