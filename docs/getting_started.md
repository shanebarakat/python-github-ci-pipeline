
Suppose that 2 users want to share secret information but that their communication must be performed across a public (unsecure) channel (e.g. over the internet).

If both users have access to the same shared secret key, then they can use this key in order to send encrypted messages across the public channel. 

```python 
>>> from some_cool_cryptography_package import encrypt_message, decrypt_message
>>> shared_secret_key: int = 46_290 

>>> # user 1 encrypts a message #
>>> encrypted_message: str = encrypt_message(
...     message="attack at midnight tonight", 
...     secret_key=shared_secret_key
... )

>>> # user 2 decrypts the message #
>>> decrypted_message: str = decrypt_message(
...     encrypted_message, 
...     secret_key=shared_secret_key
... )
>>> print(decrypted_message)
'attack at midnight tonight'
```

But how can both users share the same secure secret key (known only to the 2 of them) if the key must be communicated across a public (unsecure) channel?

The [Diffie-Hellman-Merkle](https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange) algorithm provides an elegant solution, which works as follows:

1. The users decide on 2 shared numbers (integers) to use. These numbers can be shared across a public (unsecure) channel:

    * A shared modulus number `p` (which must be a prime number, and for security should be larger than 2048 bits)

    * A shared base number `g` (which need not be big, but which needs to be a [primitive root modulo *p*](https://en.wikipedia.org/wiki/Primitive_root_modulo_n))

2. Each user chooses their own private secret (integer) key, and does not share this with anyone. 

3. Each user combines their private secret key with the 2 shared public numbers using a simple arithmetic formula ([detail here](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#Cryptographic_explanation)), and they then share the result of that communication with the other user across the public (unsecure) channel.

4. Both users then combine the (now 4) public numbers with their own private secret key in order to generate a secure shared secret key (i.e. the users' private calculations both give the same result). This calculation also uses a very simple arithmetic formula - you can find the precise details [here](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#Cryptographic_explanation).

Here is how this can be achieved using this python module:

```python
>>> from diffie_hellman_merkle.user import DiffieHellmanMerkle

>>> public_shared_modulus: int = 857_083
>>> public_shared_base: int = 2

>>> user1 = DiffieHellmanMerkle(
...         shared_modulus=public_shared_modulus,
...         shared_base=public_shared_base,
...         personal_secret=69_420,
... )
>>> user2 = DiffieHellmanMerkle(
...         shared_modulus=public_shared_modulus,
...         shared_base=public_shared_base,
...         personal_secret=8_008_135,
... )

>>> print(
... "Calculation result to share:\n",
... "    User 1: ", user1.value_to_share, "\n",
... "    User 2: ", user2.value_to_share, "\n",
... )
Calculation result to share:
    User 1:  267629 
    User 2:  187245
```

In the case of the 4 numbers used in this example (857083, 2, 267629, 187245), the shared secret key could be discovered using brute force, but if `p` were at least 2048 bits, then this would be infeasible for modern computers.

```python
>>> user1.generate_shared_secret(received_value_to_share=user2.value_to_share)
>>> user2.generate_shared_secret(received_value_to_share=user1.value_to_share)
>>> print( user1.shared_secret == user2.shared_secret )
True
```