import hashlib
import binascii


def home_pgcd(a,b): #recherche du pgcd
    if a == 0:
        return (b, 0, 1)
    g, y, x = home_pgcd(b % a, a)
    return g, x - (b // a) * y, y


def home_ext_euclid(a, m):
    g, x, y = home_pgcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x % m


# pour transformer un string en int
def home_string_to_int(x):
    z = 0
    for i in reversed(range(len(x))):
        z = int(ord(x[i]))*pow(2, (8*i))+z
    return z


# pour transformer un int en string
def home_int_to_string(x):
    txt = ''
    res1 = x
    while res1 > 0:
        res= res1 % (pow(2,8))
        res1 = (res1-res)//(pow(2, 8))
        txt = txt+chr(res)
    return txt


def home_mod_exponent(x, p, n):
    """
    :return: y = x^p mod n
    """
    result = 1
    while p > 0:
        if p & 1 > 0:
            result = (result*x) % n
        p >>= 1
        x = (x*x) % n
    return result


def get_block_count(n):
    """
    This function allow us to count the number of byte needed to store n

    :param n: The n value used
    :return: The number of byte needed to store the value n
    """
    count = 1
    while n > pow(2, count*8):
        count += 1

    return count


# Generate signature using PRIVATE key
def generate_signature(val, mode="sha256"):
    hashlib.sha256()
    if mode == "sha256":
        signature = hashlib.sha256(val.encode()).digest()
    elif mode == "md5":
        signature = hashlib.md5(val.encode(encoding='UTF-8', errors='strict')).digest()  # MD5 du message
    else:
        raise Exception("Wrong signature mode")

    signature = binascii.b2a_uu(signature)
    signature = signature.decode()  # en string

    return signature
