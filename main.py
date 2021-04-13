from scripts.Utils import *
from scripts.RSABuilder import RSABuilder


def bob_actions(_private_bob, _public_alice):
    # Bob use alice's public key to encode the message
    _enc = _public_alice.encode(msg)
    # Bob use his private key to generate a signature
    _sig_enc = _private_bob.encode(generate_signature(msg))

    return _enc, _sig_enc


def alice_actions(_private_alice, _public_bob, _enc, _sig_enc):
    # Alice use her private key to decode the message
    _dec = _private_alice.decode(_enc)

    _sig = generate_signature(_dec)
    _sig_dec = _public_bob.decode(_sig_enc)

    if _sig != _sig_dec:
        print("Wrong message")
        return
    else:
        print("Signature matching")
        print(_dec)
        return


if __name__ == "__main__":
    alice = RSABuilder(2010942103422233250095259520183, 3503815992030544427564583819137, 17)
    bob = RSABuilder(9434659759111223227678316435911, 8842546075387759637728590482297, 23)

    public_alice = alice.get_public_key()
    private_alice = alice.get_private_key()

    public_bob = bob.get_public_key()
    private_bob = bob.get_private_key()

    msg = "Hello world, I can make a message as long as I want because I am cut it in small part"

    enc, sig_enc = bob_actions(private_bob, public_alice)

    alice_actions(private_alice, public_bob, enc, sig_enc)
