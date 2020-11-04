# A simple implementation of Secret Sharing Scheme using XOR and Random number generation. 
import secrets 

def prng():
    rand = bin(secrets.randbits(128))
    return rand[2:]

myRand = prng()
print('Random number is: ', myRand)