
Suppose that 2 users want to share secret information but that their communication must be performed across a public (unsecure) channel (e.g. over the internet).

If both users have access to the same shared secret key, then they can use this key in order to send encrypted messages across the public channel. 

```python 
>>> from some_cool_cryptography_package import encrypt_message, decrypt_message
>>> shared_secret_key: int = 46290 

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