import pytest
import random
from scripts.Utils import *


def pgcd(n1, n2):

    for i in range(max(n1, n2), 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            return i

    return -1


# Thanks https://www.codabrainy.com/inverse-modulaire/
def mod_inverse(x, m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
        elif n == m - 1:
            return -1
        else:
            continue


def test_home_pgcd():

    n1 = random.randint(1, pow(2, 16))
    n2 = random.randint(1, pow(2, 16))
    assert pgcd(n1, n2) == home_pgcd(n1, n2)[0]


def test_home_ext_euclid():

    n1 = random.randint(1, pow(2, 16))
    n2 = random.randint(1, pow(2, 16))
    assert mod_inverse(n1, n2) == home_ext_euclid(n1, n2)


def test_home_mod_exponent():

    n1 = random.randint(1, pow(2, 16))
    n2 = random.randint(1, pow(2, 16))
    n3 = random.randint(1, pow(2, 16))

    assert home_mod_exponent(n1, n2, n3) == pow(n1, n2, n3)
