import enchant
# PyEnchant is a package which uses dictionaries to check whether a string is a specific language
# it is used for brute forcing caesar cipher solutions where the key is unknown

def main():

    while(True):
        selection = raw_input('\nAre you encrypting or decrypting the message? (Enter e for encrypt, d for decrypt)\n')

        if (selection.lower() == 'e'):
            message = raw_input('Enter your message: ')

            key = int(raw_input('What key are you shifting the message by? '))

            print('\nThe encrypted message is: ' + encrypt(message, key))

        elif (selection.lower() == 'd'):
            message = raw_input('Enter your encrypted message: ')

            key = int(raw_input('What key was the message shifted by: '))

            print('\nThe decrypted message is: ' + decrypt(message, key))

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


if __name__ == "__main__":
    main()