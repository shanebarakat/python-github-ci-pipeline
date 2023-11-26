"""Unit tests of the class diffiehellmann.user.DiffieHellmann"""

from diffie_hellman_merkle.user import DiffieHellmanMerkle


def test_generate_shared_secret():
    """docstring TODO"""
    user1 = DiffieHellmanMerkle(
        shared_modulus=89_067_389,
        shared_base=2,
        personal_secret=1_234,
    )
    user2 = DiffieHellmanMerkle(
        shared_modulus=7_069_067_389,
        shared_base=69_420,
        personal_secret=4_321,
    )
    user1.generate_shared_secret(user2.value_to_share)
    user2.generate_shared_secret(user1.value_to_share)
    assert (
        user1.shared_secret == user2.shared_secret
    ), "both users must generate the same shared secret"
