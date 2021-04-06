from Utils import *


class RSAPrivateKey:

    def __init__(self, d, n):
        self.d = d
        self.n = n
        self.blocCount = get_block_count(self.n)

    # Decode using PRIVATE key
    def decode(self, val):
        print("Decoding using PRIVATE key " + str(len(val)))
        output = []

        for i in range(0, len(val), self.blocCount):
            bloc = []
            for j in range(i, i + self.blocCount):
                bloc.append(val[j])

            bloc_val = int.from_bytes(bloc, byteorder='big')
            print("[" + str(i) + "] " + str(bloc_val))
            output.append(home_mod_exponent(bloc_val, self.d, self.n))

        return bytearray(output).decode()

    # Encode using PRIVATE key
    def encode(self, src):
        print("Encoding using PRIVATE key")
        encoded_string = src.encode()
        byte_array = bytearray(encoded_string)

        output = []
        for byte in byte_array:

            val = home_mod_exponent(byte, self.d, self.n)
            array = val.to_bytes(self.blocCount, 'big')
            for v in array:
                output.append(v)

        return bytearray(output)