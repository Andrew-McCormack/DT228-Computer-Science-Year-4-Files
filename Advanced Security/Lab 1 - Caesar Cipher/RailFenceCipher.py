def main():
    while (True):
        selection = raw_input('\nAre you encrypting or decrypting the message? (Enter e for encrypt, d for decrypt)\n')

        if (selection.lower() == 'e'):
            message = raw_input('Enter your message: ')

            key = int(raw_input('What key are you shifting the message by? '))

            print('The encrypted message is: ' + encrypt(message, key))

        elif (selection.lower() == 'd'):
            encryptedMessage = raw_input('Enter your encrypted message: ')
            key = int(raw_input('What key was the message shifted by? '))

            print('The decrypted message is: ' + decrypt(encryptedMessage, key))


def fence(p, k):
    fence = [[None] * len(p) for n in range(k)]
    rails = range(k - 1) + range(k - 1, 0, -1)

    for n, x in enumerate(p):
        fence[rails[n % len(rails)]][n] = x

    return [c for rail in fence for c in rail if c is not None]

def encrypt(p, k):
    return ''.join(fence(p, k))

def decrypt(c, k):
    rng = range(len(c))
    pos = fence(rng, k)

    return ''.join(c[pos.index(k)] for k in rng)

if __name__ == "__main__":
    main()