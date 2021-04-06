from scripts.Utils import *


class RSAPublicKey:

    def __init__(self, e, n):
        self.e = e
        self.n = n
        self.blocCount = get_block_count(self.n)
        print("Block size: " + str(self.blocCount))

    # Encode using PUBLIC key
    def encode(self, src):
        print("Encoding using PUBLIC key")
        encoded_string = src.encode()
        byte_array = bytearray(encoded_string)

        output = []
        for byte in byte_array:

            val = home_mod_exponent(byte, self.e, self.n)
            # print(str(byte) + " -> " + str(val))
            array = val.to_bytes(self.blocCount, 'big')
            for v in array:
                output.append(v)

        return bytearray(output)

    # Decode using PUBLIC key
    def decode(self, val):
        print("Decoding using PUBLIC key")
        output = []

        for i in range(0, len(val), self.blocCount):
            bloc = []
            for j in range(i, i + self.blocCount):
                bloc.append(val[j])

            bloc_val = int.from_bytes(bloc, byteorder='big')
            # print(bloc_val)
            output.append(home_mod_exponent(bloc_val, self.e, self.n))

        return bytearray(output).decode()