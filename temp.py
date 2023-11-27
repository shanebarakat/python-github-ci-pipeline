from diffie_hellman_merkle.user import DiffieHellmanMerkle

public_shared_modulus: int = 857_083
public_shared_base: int = 2

user1 = DiffieHellmanMerkle(
    shared_modulus=public_shared_modulus,
    shared_base=public_shared_base,
    personal_secret=69_420,
)
user2 = DiffieHellmanMerkle(
    shared_modulus=public_shared_modulus,
    shared_base=public_shared_base,
    personal_secret=8_008_135,
)

user1.generate_shared_secret(user2.value_to_share)
user2.generate_shared_secret(user1.value_to_share)
print(
    f"""
Calculation result to share:
    User 1: {user1.value_to_share}  # 267_629
    User 2: {user2.value_to_share}  # 187_245
"""
)
