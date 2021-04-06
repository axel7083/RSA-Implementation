from scripts.Utils import *
from scripts.RSAPrivateKey import RSAPrivateKey
from scripts.RSAPublicKey import RSAPublicKey


class RSA:

    def __init__(self, p, q, e):
        self.p = p  # must be prime
        self.q = q  # must be prime
        self.n = p * q

        self.phi = ((self.p - 1) * (self.q - 1))
        self.e = e
        self.d = home_ext_euclid(self.e, self.phi)

    def get_public_key(self):
        return RSAPublicKey(self.e, self.n)

    def get_private_key(self):
        return RSAPrivateKey(self.d, self.n)
