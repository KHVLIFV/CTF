from Crypto.Util.number import *
import random

flag = b"[REDACTED]"

def gen_coefficient():
    a = random.randint(0, 0x1000000001)
    b = random.randint(0, 0x1000000001)
    c = random.randint(0, 0x1000000001)
    d = random.randint(0, 0x1000000001)
    e = random.randint(0, 0x1000000001)

    return a, b, c, d, e

def get_bits():
    bits = []

    for i in range(1000):
        bits.append(random.getrandbits(32))
    
    with open("bits.txt", "w") as f:
        for b in bits:
            f.write(str(b) + '\n')


def custom_encryption(m, a, b, c, d, e):
    msg = m
    enc = []

    for val in msg:
        r = 5*a*pow(val, 4) + b*pow(val, 3) + 3*c*pow(val, 2) + 15*d*val + e
        enc.append(r)
        
    with open("encrypted.txt", "w") as f:
        for e in enc:
            f.write(str(e) + '\n')


def main():
    get_bits()

    a, b, c, d, e = gen_coefficient()

    custom_encryption(flag, a, b, c, d, e)
    


if __name__ == '__main__':
    main()