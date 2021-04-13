from scripts.RSAKey import RSAKey
from scripts.Utils import *


class RSAPrivateKey(RSAKey):

    def __init__(self, d, n):
        self.d = d
        self.n = n
        self.bloc_size = get_block_size(self.n)
        super().__init__(self.bloc_size)

    # Encode using PRIVATE key
    def encode(self, src):
        return super()._encode(src, self.d, self.n)

    # Decode using PRIVATE key
    def decode(self, val):
        return super()._decode(val, self.d, self.n)
