from Crypto.Cipher import DES

def main():

    while(True):
        userInput = raw_input("Type 'g' to generate hash of plaintext or 'm' to confirm message came from inteded sender: ")

        if(userInput.lower() == 'g'):
            key = raw_input('Enter password for hashing algorithm (must be 8 bytes): ')
            print('Hashed data is ' + generateHash(key, 'AAAABBBBCCCCD'))

        elif(userInput.lower() == 'm'):
            key = raw_input('Enter the password that was used to generate the hash (must be 8 bytes): ')
            suppliedHash = raw_input('Enter the hash that was supplied with the message: ')
            print(confirmMessageAuthenticity(key, suppliedHash, 'AAAABBBBCCCCD'))


def confirmMessageAuthenticity(key, suppliedHash, message):
    calculatedHash = generateHash(key, message)

    if(calculatedHash == suppliedHash):
        return('Success!, Message was successfully verified!')
    else:
        return('Failure!, Message could not be verified, may not have been authored by expected author!')

def generateHash(key, text):
    keyLen = len(key)

    print('Plaintext is ' + text)

    print('\nSeperating plaintext into keysize len blocks')
    textBlockList = list(seperateToBlocks(text, keyLen))

    print(textBlockList)

    print('\nPadding last block')

    if (len(textBlockList[-1]) != keyLen):
        textBlockList[-1] = pad(textBlockList[-1], keyLen)
    else:
        textBlockList.append(padEmpty(keyLen))

    print(textBlockList)

    print('\nHashing Data')

    hashedData = hashData(textBlockList, key)

    return hashedData.encode('hex')

def hashData(textBlockList, key):
    encryptedTextList = []

    encryptedTextList.append(xor(encryptText(textBlockList[0], key), key))

    for i in range(1, len(textBlockList)):
        encryptedTextList.append(xor(encryptText(textBlockList[i], encryptedTextList[i - 1]), encryptedTextList[i - 1]))

    return encryptedTextList[-1]

def xor(data, key):
    l = len(key)
    buff = []
    for i, val in enumerate(data):
        buff.append(chr(ord(val) ^ ord(key[i % l])))
    return ''.join(buff)

def seperateToBlocks(text, keyLen):
    while text:
        yield text[:keyLen]
        text = text[keyLen:]

def encryptText(key, text):
    des = DES.new(key, DES.MODE_ECB)

    return des.encrypt(text)

def padEmpty(keyLen):
    tempEmptyBlock = str(keyLen)
    numSpace = 0

    while(len(tempEmptyBlock) % keyLen != 0):
        tempEmptyBlock += ' '
        numSpace += 1

    return ' ' * numSpace + str(keyLen)


def pad(text, keyLen):
    paddingSize = (keyLen - len(text) % keyLen)
    tempText = text + str(paddingSize)
    numSpaces = 0
    while(len(tempText) % keyLen):
        tempText += ' '
        numSpaces += 1

    if(len(text) % keyLen != 0):
        text = text + ' ' * numSpaces + str(paddingSize)

    return text


if __name__ == "__main__":
    main()