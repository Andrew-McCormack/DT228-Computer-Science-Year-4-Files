from collections import Counter
import string

def main():
    while(True):

        selection = raw_input(
            '\nAre you encrypting or decrypting the message? (Enter e for encrypt, d for decrypt)\n')

        if (selection == 'e'):
            message = raw_input('Enter your message: ')

            key = raw_input('What is the password? ')

            print('The encrypted message is: ' + encrypt(message, key))

        elif (selection == 'd'):
            cipher = raw_input('Enter your encrypted message: ')

            key = raw_input('What is the password? ')

            print('The decrypted message is: ' + decrypt(cipher, key))


def findDecimalValue(character, characterOrdValue):

    if(characterOrdValue >= 65 and characterOrdValue <= 90):
        return characterOrdValue - 65
    elif (characterOrdValue >= 97 and characterOrdValue <= 122):
        return characterOrdValue - 97
    return 0

def caesar(s, k, decrypt=False):
    if decrypt:
        k = 26 - k
    r = ""


    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90):
            r += chr((ord(i) - 65 + k) % 26 + 65)
        elif (ord(i) >= 97 and ord(i) <= 122):
            r += chr((ord(i) - 97 + k) % 26 + 97)
        else:
            r += i
    return r

def encrypt(message, key):
    encryptedMessage = []
    paddedKey = makeKeySameLengthAsMessage(message, key)

    for i in range(0, len(message)):
        passCharacterOrdValue = ord(paddedKey[i])
        decimalPassCharValue = findDecimalValue(paddedKey[i], passCharacterOrdValue)

        encryptedMessage.append(caesar(message[i], decimalPassCharValue))

    return ''.join(encryptedMessage)

def decrypt(cipher, key):
    decryptedMessage = []
    paddedKey = makeKeySameLengthAsMessage(cipher, key)

    for i in range(0, len(cipher)):
        passCharacterOrdValue = ord(paddedKey[i])

        decimalPassCharValue = findDecimalValue(paddedKey[i], passCharacterOrdValue)
        decryptedMessage.append(caesar(cipher[i], decimalPassCharValue, True))

    return ''.join(decryptedMessage)

def makeKeySameLengthAsMessage(message, key):
    keyList = []
    key = list(key)
    counter = 0

    for i, value in enumerate(message):
        if (not (value.isspace()) and value.isalpha()):
            keyList.append(key[counter % len(key)])
            counter += 1
        else:
            keyList.append(' ')
    return keyList

def findSameSizeSubStrings(message, n):
    m = list(message)
    word = ''
    potentialSubStringMatches = []

    for c in message:
        if (c.isalpha()):
            word = word + c
        else:
            if len(word) == n:
                potentialSubStringMatches.append(word)
                word = ''
            else:
                word = ''

    return potentialSubStringMatches

if __name__ == "__main__":
    main()

