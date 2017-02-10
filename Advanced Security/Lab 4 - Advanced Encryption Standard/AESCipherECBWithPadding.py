from Crypto.Cipher import AES

def main():

    key = '1234567812345678'

    text = 'AAAABBBBCCCCDDDDAA'

    print('Plaintext is ' + text)
    cipherText = encryptText(key, text)

    print('Encrypted text in hex is ' + cipherText)
    unencryptedText = decryptText(key, cipherText)

    print('Unencrypted text is ' + unencryptedText)

def encryptText(key, text):
    aes = AES.new(key, AES.MODE_ECB)

    return aes.encrypt(pad(text)).encode('hex')

def decryptText(key, cipherText):
    aes = AES.new(key, AES.MODE_ECB)

    return unPad(aes.decrypt(cipherText.decode('hex')))

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

    print('Could not detect padding in text')
    return text

if __name__ == "__main__":
    main()