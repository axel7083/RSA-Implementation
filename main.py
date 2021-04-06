from scripts.Utils import *
from scripts.RSA import RSA


def bob_actions(private_bob, public_alice):
    # Bob use alice's public key to encode the message
    enc = public_alice.encode(msg)
    # Bob use his private key to generate a signature
    sig_enc = private_bob.encode(generate_signature(msg))

    return enc, sig_enc


def alice_actions(private_alice, public_bob, enc, sig_enc):
    # Alice use her private key to decode the message
    dec = private_alice.decode(enc)

    sig = generate_signature(dec)
    sig_dec = public_bob.decode(sig_enc)

    if sig != sig_dec:
        print("Wrong message")
        return
    else:
        print("Signature matching")
        print(dec)
        return


if __name__ == "__main__":
    alice = RSA(2010942103422233250095259520183, 3503815992030544427564583819137, 17)
    bob = RSA(9434659759111223227678316435911, 8842546075387759637728590482297, 23)

    public_alice = alice.get_public_key()
    private_alice = alice.get_private_key()

    public_bob = bob.get_public_key()
    private_bob = bob.get_private_key()

    msg = "Hello world, I can make a message as long as I want because I am cutting it in small part"

    enc, sig_enc = bob_actions(private_bob, public_alice)

    alice_actions(private_alice, public_bob, enc, sig_enc)
