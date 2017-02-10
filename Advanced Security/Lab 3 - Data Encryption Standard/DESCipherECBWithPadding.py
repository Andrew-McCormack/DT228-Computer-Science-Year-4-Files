from Crypto.Cipher import DES
import binascii
import array
import re
import base64

def main():
    key = '12345678'
    text = 'AAAABBBBCCCC'

    print('Plaintext is ' + text)

    encryptedText = encryptText(key, text)
    print('Encrypted text in hex is ' + encryptedText)

    decryptedText = decryptText(key, encryptedText)
    print('Unencrypted text is ' + decryptedText)


def encryptText(key, text):
    des = DES.new(key, DES.MODE_ECB)

    return des.encrypt(pad(text)).encode('hex')

def decryptText(key, cipherText):
    des = DES.new(key, DES.MODE_ECB)

    return unPad(des.decrypt(cipherText.decode('hex')))

def pad(text):
    paddingSize = (16 - len(text) % 16)
    tempText = text + str(paddingSize)
    numSpaces = 0
    while(len(tempText) % 16):
        tempText += ' '
        numSpaces += 1

    if(len(text) % 16 != 0):
        text = text + ' ' * numSpaces + str(paddingSize)

    return text

def unPad(text):
    textList = list(text)
    paddingNum = ''

    ensureBreakOccured = False

    for i in reversed(textList):
        if( i != ' '):
            paddingNum = paddingNum + i
        else:
            ensureBreakOccured = True
            break

    if(ensureBreakOccured == True):
        paddingNum = ''.join(reversed(paddingNum))

        newTextList = []

        for i in range(len(textList) - int(paddingNum)):
            newTextList.append(textList[i])

        return ''.join(newTextList)

    print('No padding found in text')
    return text

if __name__ == "__main__":
    main()