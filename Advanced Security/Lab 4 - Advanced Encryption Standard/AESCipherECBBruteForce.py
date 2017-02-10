from Crypto.Cipher import AES

def main():
    # My cipher is different to the one given as my padding technique is different
    myCipherText = '43d3215c92a75a1478fcf9cb950d20db34457979266106e7cec72d63d1535d39'
    labCipherText = '43D3215C92A75A1478FCF9CB950D20DB502A485FD5735486D57AEA9AA809E3DD'.lower()

    print('Trying with my cipher text (my cipher text works with my unpadding algorithm, so padding will be removed) \n')
    BruteForceKey(myCipherText)

    print('\nTrying with lab cipher text (the decrypted lab cipher will not work with my unpadding algorithm, so padding will remain) \n')
    BruteForceKey(labCipherText)

def BruteForceKey(cipherText):

    possibleValidDecryptions = []
    possibleValidKeys = []

    print('Beginning brute force on ' + cipherText)
    with open('rockyou.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            if(len(line)  == 16 or len(line) == 24 or len(line) == 32):
                if(isascii(line)):
                    if (len(line) == len(line.encode())):
                        possibleDecryption = AttemptDecryption(line, cipherText)
                        if (possibleDecryption != ''):
                            possibleValidDecryptions.append(possibleDecryption)
                            possibleValidKeys.append(line)

    print('\nFinished brute force')
    print('Potential decryptions are: ')

    for i in range(len(possibleValidDecryptions)):
        print('"' + possibleValidDecryptions[i] + '"'  + ', found using key ' + '"' + possibleValidKeys[i] + '"\n')


def AttemptDecryption(key, cipherText):
    aes = AES.new(key, AES.MODE_ECB)

    decrypted = aes.decrypt(cipherText.decode('hex'))

    if(isascii(decrypted) == True):
        print('Found a possible decryption!')
        return Unpad(decrypted)
    return ''

def isascii(text):

    try:
        if(len(text) == len(text.encode())):
            return True
    except UnicodeDecodeError:
        return False
    else:
        return False

def Unpad(text):
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

    print('Could not remove padding or padding not present')
    return text

def Pad(text):
    paddingSize = (16 - len(text) % 16)
    tempText = text + str(paddingSize)
    numSpaces = 0
    while(len(tempText) % 16):
        tempText += ' '
        numSpaces += 1

    if(len(text) % 16 != 0):
        text = text + ' ' * numSpaces + str(paddingSize)

    return text

def Unpad(text):
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