# Stream Cipher using One Time Pad (OTP) ---- Simple Example.
plainText =  "attack at dawn"
CipherText = "6c73d5240a948c86981bc294814d"
def PTManipulation(plainText):
    messageToAscii = [ord(letter) for letter in plainText]
    # print('Ascii form is: ', messageToAscii)
    messageToBin = list()
    for msg in messageToAscii:
        messageToBin.append(f'{msg:08b}')
    # print('Message as bin is: ', messageToBin)
    PT = ''.join(messageToBin)
    print('PT is: ', PT)
    return PT

def ctManipulation(CT):
    # Convert CT to bin.
    CTtoBin = bin(int(CT, base=16))
    print('CT is: ', CTtoBin[2:])
    return CTtoBin

def getOTP(PT, CTtoBin):
    # XOR operation.
    XORing =  int(PT,2) ^ int(CTtoBin,2)
    OTP = '{0:b}'.format(XORing)
    print('OTP used was: ', OTP)
    return OTP

def OTPencryption(plaintxt,optKey):
    PT = PTManipulation(plainText)
    # Perform Xor
    xoringPTandKey = int(optKey,2) ^ int(PT,2)
    # Convert to hex
    encryptedTex = hex(xoringPTandKey)[2:]
    return encryptedTex

def getOrigPT(OTP, CTtoBin):
    # Trying Reverse procedure.
    deducedMsgAsInt = int(OTP,2) ^ int(CTtoBin,2)
    binString = '0'+'{0:b}'.format(deducedMsgAsInt)
    #print('PT is: ', deducedMessageBin)
    binToIntString = int(binString, 2)
    print('Getting orignla plaintext...')
    return binToIntString.to_bytes((binToIntString.bit_length() + 7) // 8, 'big').decode()

# Main run.
PT = PTManipulation(plainText)
CTtoBin = ctManipulation(CipherText)
OTP = getOTP(PT, CTtoBin)
originalPT = getOrigPT(OTP, CTtoBin)
print('****************************************')
print('First Original Plaintext was: ', originalPT)
print('****************************************')
# Testing Stream cipher encryption.
encryptedTxtInHex = OTPencryption(plainText,OTP)
print('The Ciphertext in Hex form is: ', encryptedTxtInHex)
if encryptedTxtInHex == CipherText:
    print('Encrypted text matches Ciphertext.')
else: 
    print('Encrypted text does not match Ciphertext.')

# Assigning new PT.
plainText =  "attacks at python"
encryptedTxtInHex = OTPencryption(plainText,OTP)
print('The Ciphertext in Hex form is: ', encryptedTxtInHex)
# Check if PT can be deduced from CT and OTP.
CTtoBin = ctManipulation(encryptedTxtInHex)
originalPT = getOrigPT(OTP, CTtoBin)
print('****************************************')
print('Second Original Plaintext was: ', originalPT)
print('****************************************')
