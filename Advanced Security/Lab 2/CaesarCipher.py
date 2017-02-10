import enchant
import re
# PyEnchant is a package which uses dictionaries to check whether a string is a specific language
# it is used for brute forcing caesar cipher solutions where the key is unknown

def main():

    selection = raw_input('Are you encrypting or decrypting the message? (Enter e for encrypt, d for decrypt, e to exit)\n')

    while(selection.lower != 'f'):

        if (selection.lower() == 'e'):
            message = raw_input('Enter your message:')

            key = int(raw_input('What key are you shifting the message by? '))

            print('\nThe encrypted message is: ' + encrypt(message, key))

        elif (selection.lower() == 'd'):
            message = raw_input('Enter your encrypted message: ')

            knowKey = raw_input('Do you have the key the message was shifted by? (Enter y or n) ')

            if(knowKey.lower() == 'y'):
                key = int(raw_input('What key was the message shifted by: '))

                print('\nThe decrypted message is: ' + decrypt(message, key))

            else:
                result = findKey(message)
                print(result)

        selection = raw_input('\nAre you encrypting or decrypting the message? (Enter e for encrypt, d for decrypt, e to exit)\n')



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

def encrypt(p, k):
    return caesar(p, k)

def decrypt(c, k):
    return caesar(c, k, True)

def findKey(message):

    dictionary = enchant.Dict("en_US")
    subStringCounter = 0
    realWordCounter = 0
    shift = None
    foundValidSentence = False


    for key in range(1, 26):
        decryptedSentence = decrypt(message, key)

        # Remove all non alpha-numeric characters from decrypted string using regular expression then convert to list of substrings
        wordList = re.sub("[^\w]", " ", decryptedSentence).split()
        for word in wordList:
            subStringCounter += 1

            #Check if substring is valid English
            if(dictionary.check(word)):
                realWordCounter += 1

        # If the real word count is the same amount as the number of sub strings in the decrypted string we know that all of the words are valid
        if(realWordCounter == subStringCounter):
            shift = key
            foundValidSentence = True
            break
        else:
            subStringCounter = 0
            realWordCounter = 0

    if(foundValidSentence):
        return ('\nThe message was encrypted using a key shift of: ' + str(shift) + ' and decrypted to: ' + decryptedSentence)

    return 'Could not find a valid decryption!'

if __name__ == "__main__":
    main()