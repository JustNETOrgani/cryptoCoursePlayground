# A simple implementation of Secret Sharing Scheme using XOR and Random number generation. 
import secrets 

# Shares.
share_1 = list()
share_2 = list()
share_3 = list()

# The secret.
topSecret =  "This is top secret"

# Helper functions
def prng():
    rand_1 = bin(secrets.randbits(128))
    rand_2 = bin(secrets.randbits(128))
    return rand_1[2:], rand_2[2:]

def secretTransform(mySecret):
    secretToAscii = [ord(letter) for letter in mySecret]
    # print('Ascii form is: ', messageToAscii)
    secretToBin = list()
    for msg in secretToAscii:
        secretToBin.append(f'{msg:08b}')
    # print('Message as bin is: ', messageToBin)
    secret_in_BinFormat = ''.join(secretToBin)
    return secret_in_BinFormat

def creatingXors(rand_1, rand_2, secTransformed):
    k_one_prime = int(rand_1,2) ^ int(secTransformed,2)
    k_two_prime = int(rand_2,2) ^ int(secTransformed,2)
    k_one_prime_binString = '0'+'{0:b}'.format(k_one_prime)
    k_two_prime_binString = '0'+'{0:b}'.format(k_two_prime)
    k_one_prime_binString_binToIntString = int(k_one_prime_binString, 2)
    k_two_prime_binString_binToIntString = int(k_two_prime_binString, 2)
    print('Converting prime shares to human readable...')
    k_one_prime_Hreadable = k_one_prime_binString_binToIntString.to_bytes((k_one_prime_binString_binToIntString.bit_length() + 7) // 8, 'big').decode()
    k_two_prime_Hreadable = k_two_prime_binString_binToIntString.to_bytes((k_two_prime_binString_binToIntString.bit_length() + 7) // 8, 'big').decode()
    return k_one_prime_Hreadable, k_two_prime_Hreadable, k_one_prime, k_two_prime  

def distrbuteShares(k_one_prime, k_two_prime):
    k_one, k_two = prng()
    share_1.append(k_one, k_two)
    share_2.append(k_one_prime, k_two)
    share_3.append(k_two_prime)
    return share_1, share_2, share_3

# Main function
def mainFunc():
    pass
