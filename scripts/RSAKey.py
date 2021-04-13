from scripts.Utils import home_mod_exponent


class RSAKey:

    def __init__(self, bloc_size):
        self.bloc_size = bloc_size

    def _encode(self, _str, a, b):
        encoded_string = _str.encode()
        byte_array = bytearray(encoded_string)

        output = []
        for byte in byte_array:

            val = home_mod_exponent(byte, a, b)
            array = val.to_bytes(self.bloc_size, 'big')
            for v in array:
                output.append(v)

        return bytearray(output)

    def _decode(self, _str, a, b):
        output = []

        for i in range(0, len(_str), self.bloc_size):
            bloc = []
            for j in range(i, i + self.bloc_size):
                bloc.append(_str[j])

            bloc_val = int.from_bytes(bloc, byteorder='big')
            output.append(home_mod_exponent(bloc_val, a, b))

        return bytearray(output).decode()
