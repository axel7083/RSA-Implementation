from scripts.RSAKey import RSAKey
from scripts.Utils import *


class RSAPublicKey(RSAKey):

    def __init__(self, e, n):
        self.e = e
        self.n = n
        self.bloc_size = get_block_size(self.n)
        super().__init__(self.bloc_size)

    # Encode using PUBLIC key
    def encode(self, src):
        return super()._encode(src, self.e, self.n)

    # Decode using PUBLIC key
    def decode(self, val):
        return super()._decode(val, self.e, self.n)