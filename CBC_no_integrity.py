intercepted_CT = '20814804c1767293b99f1d9cab3bc3e7ac1e37bfb15599e5f40eef805488281d'
orig_PT = "Pay Bob 100$" # (excluding the quotes)
# Underlying Cipher: CBC with random IV.

# Attacker can change to  "Pay Bob 500$". 
# Get new Ciphertext.

def PTManipulation(plainText):
    messageToAscii = [ord(letter) for letter in plainText]
    # print('Ascii form is: ', messageToAscii)
    messageToBin = list()
    for msg in messageToAscii:
        messageToBin.append(f'{msg:08b}')
    # print('Message as bin is: ', messageToBin)
    PT_Bin = ''.join(messageToBin)
    print('PT is: ', PT_Bin)
    return hex(int(PT_Bin,2))[2:]

PT_in_Hex = PTManipulation(orig_PT)
print('PT in Hex form: ', PT_in_Hex)