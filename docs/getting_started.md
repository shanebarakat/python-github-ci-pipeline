
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

But how can both users share a secure secret key (known only to the 2 of them) if the key must be communicated across a public (unsecure) channel?

The [Diffie-Hellman-Merkle](https://en.wikipedia.org/wiki/Diffie-Hellman_key_exchange) algorithm provides an elegant solution, which works as follows:

1. The users decide on 2 shared (integer) numbers to use. These numbers can be shared across a public (unsecure) channel:

    * A shared modulus number *p* (which must be a prime number, and for security should be larger than 2048 bits)

    * A shared base number *g* (which need not be big, but which needs to be a [primitive root modulo *p*](https://en.wikipedia.org/wiki/Primitive_root_modulo_n))

2. Each user chooses their own secret (integer) key, and does not share this with anyone. 

3. Each user combines their private secret with the 2 shared public numbers using a simple arithmetic formula ([detail here](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#Cryptographic_explanation)), and then can share the result of that communication with the other user across the unsecure (public) channel.

4. Both users can then combine the 3 numbers shared across the public channel with their own secret key in order to generate a secure shared secret key (i.e. each user's private calculation results in the same number). This is, again, a very simple arithmetic operation, and you can find the precise formula [here](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#Cryptographic_explanation).

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

Using these 3 shared public numbers (857083, 2, 267629, 187245), can you work out what their shared secret key is? (helpful hint: you cannot)

```python
>>> user1.generate_shared_secret(received_value_to_share=user2.value_to_share)
>>> user2.generate_shared_secret(received_value_to_share=user1.value_to_share)
>>> print( user1.shared_secret == user2.shared_secret )
True
```