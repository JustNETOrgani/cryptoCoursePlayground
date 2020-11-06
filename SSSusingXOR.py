# A simple implementation of Secret Sharing Scheme using XOR and Random number generation.
# Three executives out of which any two can reconstruct the secret. 
import secrets 

# Helper functions
def prng():
    print('Generating randomness...')
    rand_1 = bin(secrets.randbits(128))
    rand_2 = bin(secrets.randbits(128))
    return rand_1[2:], rand_2[2:]

def secretTransform(mySecret):
    print('Secret transformation...')
    secretToAscii = [ord(letter) for letter in mySecret]
    # print('Ascii form is: ', messageToAscii)
    secretToBin = list()
    for msg in secretToAscii:
        secretToBin.append(f'{msg:08b}')
    # print('Message as bin is: ', messageToBin)
    secret_in_BinFormat = ''.join(secretToBin)
    return secret_in_BinFormat

def creatingXors(rand_1, rand_2, secTransformed):
    print('Xor operations...')
    k_one_prime = int(rand_1,2) ^ int(secTransformed,2)
    k_two_prime = int(rand_2,2) ^ int(secTransformed,2)
    check_secret_from_k1_k1P = '0'+bin(int(rand_1,2) ^ k_one_prime)[2:]
    check_secret_from_k2_k2P = '0'+bin(int(rand_2,2) ^ k_two_prime)[2:]
    if (secTransformed == check_secret_from_k1_k1P) and (secTransformed == check_secret_from_k2_k2P):
        print('Xoring checks completed.')
    else:
        print('Xoring checks did not succeed.')
    return k_one_prime, k_two_prime  

def distrbuteShares(k_one, k_one_prime, k_two, k_two_prime):
    print('Distributing shares...')
    # Shares.
    share_1 = list()
    share_2 = list()
    share_3 = list()
    share_1.extend((int(k_one,2), int(k_two,2)))
    share_2.extend((k_one_prime, int(k_two,2)))
    share_3.append(k_two_prime)
    return share_1, share_2, share_3

def reconstructSecret(share_1, share_2, share_3):
    secReconFor1n2 = share_1[0] ^ share_2[0]
    secReconFor1n3 = share_1[1] ^ share_3[0]
    secReconFor2n3 = share_2[1] ^ share_3[0]
    sec_binToIntStringFromS1n2 = bin(secReconFor1n2)
    sec_binToIntStringFromS1n3 = bin(secReconFor1n3)
    sec_binToIntStringFromS2n3 = bin(secReconFor2n3)
    print('Getting reconstructed secret. Standby...')
    reconstructions = list()
    reconstructions.extend(('0'+ sec_binToIntStringFromS1n2[2:],'0'+ sec_binToIntStringFromS1n3[2:],'0'+ sec_binToIntStringFromS2n3[2:]))
    return reconstructions

# Main function
def mainFunc():
    print('Setting up system...')
    # The secret.
    topSecret =  "This is top secret"
    secret_in_Bin_format = secretTransform(topSecret)
    # Generate random number.
    k_one, k_two = prng()
    # Create k-primes via Xor.
    k_one_prime, k_two_prime  = creatingXors(k_one, k_two, secret_in_Bin_format)
    # Distribute shares.
    share_1, share_2, share_3 = distrbuteShares(k_one, k_one_prime, k_two, k_two_prime)
    print('*********************************************************************************************')
    print('Share_1 for disbribution:', share_1)
    print('Share_2 for disbribution:', share_2)
    print('Share_3 for disbribution:', share_3)
    print('*********************************************************************************************')
    # Secret reconstruction.
    secretReconstructed = reconstructSecret(share_1, share_2, share_3)
    print('Actual secret: ', secret_in_Bin_format)
    #print('Reconstructed secret: ', secretReconstructed[0])
    for i in secretReconstructed:
        if (secret_in_Bin_format != i):
            print('Oops! Reconstructed secret DOES NOT match actual secret.')
        else:
            print('Great! Reconstructed secret MATCHES the actual secret.')
    print('End of system execution.')

# Call main function to begin system execution. 
mainFunc()