# Stream Cipher using One Time Pad (OTP) to encrypt plaintext using OOP technique.
# OTP can be Unicode, Hex, BIN. 
class encryption:
    def __init__(self, plainText, otpKey):
        self.plainText = plainText
        self.otpKey = otpKey
    def charToBinConvertor(self):
        ptToAscii = [ord(letter) for letter in self.plainText]
        ptCharToBin = list()
        for item in ptToAscii:
            ptCharToBin.append(f'{item:08b}')
        # print('Message as bin is: ', messageToBin)
        pt_Char_In_Bin_Format = ''.join(ptCharToBin)
        # print('PT is: ', char_In_Bin_Format)
        # Check otpKey is in binary format or not.
        for i in str(self.otpKey):
            if (i in '10'):
                otpBinState = True
            else:
                otpBinState = False
        if otpBinState == False:
            otp_Char_In_Bin_Format = processOTP(self.otpKey)
        else:
            otp_Char_In_Bin_Format = ''
        return pt_Char_In_Bin_Format, otp_Char_In_Bin_Format
            
    def OTPencryption(self):
        PT_Bin, OTP_BIN = self.charToBinConvertor()
        if (len(OTP_BIN) == 0):
            # Perform Xor
            xoringPTandKey = int(self.otpKey,2) ^ int(PT_Bin,2)
        else:
            xoringPTandKey = int(OTP_BIN,2) ^ int(PT_Bin,2)
            # Convert to hex
        encryptedTex = hex(xoringPTandKey)[2:]
        return encryptedTex

def processOTP(otpKey):
    # Check string type before conversion.
    if (otpKey.isalpha() == True):
        # Convert to Alphabet to ASCII.
        otpToAscii = [ord(letter) for letter in otpKey]
        otpCharToBin = list()
        for item in otpToAscii:
            otpCharToBin.append(f'{item:08b}')
        otp_Char_In_Bin_Format = ''.join(otpCharToBin)
    else:
        # Convert Hex to Bin.
        try:
            otp_Char_In_Bin_Format = bin(int(otpKey, base=16))
        except ValueError:
            print('OTP is not in hex.')
    return otp_Char_In_Bin_Format
    
class decryption:
    def __init__(self, cipherText, otpKey):
        self.cipherText = cipherText
        self.otpKey = otpKey
    def convertHexToBin(self):
        # Convert hex to bin.
        CTtoBin = bin(int(self.cipherText, base=16))
        # print('CT is: ', CTtoBin[2:])
        return CTtoBin
    def decryptCipher(self):
        CTtoBin = self.convertHexToBin()
        print('Getting original plaintext...')
        for i in str(self.otpKey):
            if (i in '10'):
                binStateOfotpForDecryption = True
            else:
                binStateOfotpForDecryption = False
        if binStateOfotpForDecryption == True:
            deducedMsgAsInt = int(self.otpKey,2) ^ int(CTtoBin,2)
            decryptedMsg = self.getDecryptedData(deducedMsgAsInt)
            return decryptedMsg
        else:
            processedOptKey = processOTP(self.otpKey)
            deducedMsgAsInt = int(processedOptKey,2) ^ int(CTtoBin,2)
            decryptedMsg = self.getDecryptedData(deducedMsgAsInt)
            return decryptedMsg
        
    def getDecryptedData(self, deducedMsgAsInt):
        binString = '0'+'{0:b}'.format(deducedMsgAsInt)
        #print('PT is: ', deducedMessageBin)
        binToIntString = int(binString, 2)
        return binToIntString.to_bytes((binToIntString.bit_length() + 7) // 8, 'big').decode()

if __name__ == "__main__":
    OTP = "ffa2ae"
    #OTP = '110100000111101000010100010101101001111111111010110011100111111011000011101110100110111101011111011000100011'
    PT =  "attack at dawn"
    print('Initializing...')
    print('Plaintext: ', PT)
    # Instantiate encryption class.
    encrypt = encryption(PT, OTP)
    encryptedText = encrypt.OTPencryption()
    print('Ciphertext: ', encryptedText)
    # Instantiate decryption class.
    decrypt = decryption(encryptedText, OTP)
    recoveredText = decrypt.decryptCipher()
    print('Original text: ', recoveredText)
