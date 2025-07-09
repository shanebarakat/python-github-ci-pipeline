"""A python implementation of the original
[Diffie-Hellman-Merkle Key Exchange](https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange#Cryptographic_explanation)
algorithm.

This algorithm allows users to generate a (secure) shared secret key where all communication is across a public (unsecure) network.
It provides the necessary components to perform the key exchange, including prime number generation, base generation, private key generation, public key calculation, and shared secret derivation.
"""