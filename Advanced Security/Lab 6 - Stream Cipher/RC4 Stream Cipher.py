

def main():

    while(True):
        print('\nAre you encrypting or decrypting? (Enter "e" or "d")')

        if(raw_input() == 'e'):
            encrypt()
        else:
            decrypt()

def encrypt():
    print('Enter your key: ')
    key = raw_input()
    print('Enter your plaintext:')
    userInput = raw_input()

    key = toOrdinal(key)

    S = generateKSA(key)

    cipherText = generatePRGA(S, userInput)

    print('Ciphertext encoded in hex is: ' + cipherText.encode('hex'))


def decrypt():
    print('Enter your key: ')
    key = raw_input()
    print('Enter your cipher:')
    userInput = raw_input()

    key = toOrdinal(key)
    userInput = userInput.decode('hex')

    S = generateKSA(key)

    cipherText = generatePRGA(S, userInput)

    print('Decrypted plaintext is: ' + cipherText)

def generateKSA(key):

    S = []

    for i in range(0, 256):
        S.append(i)

    j = 0

    for i in range(0, 256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return(S)

def generatePRGA(S, userInput):

    cipherText = []
    i = 0
    j = 0

    for c in userInput:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        cipherText.append(chr(ord(c) ^ S[(S[i] + S[j]) % 256]))
    return ''.join(cipherText)
    #return codecs.encode(bytes(str.encode(''.join(cipherText))), 'hex_codec')

def toOrdinal(key):
    ordKeyList = []

    for i in key:
        ordKeyList.append(ord(i))

    return ordKeyList

if __name__ == "__main__":
    main()