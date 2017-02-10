import bitarray
import random
import re

def main():
    userInput  = 's'
    while(True):
        ba = bitarray.bitarray()
        userInput = raw_input("Enter G to generate public-private key pair, E to encrypt, D to decrypt\n")

        if (userInput.lower() == 'g'):
            keys = generateKeys()
            d = keys[0]
            e = keys[1]
            n = keys[2]

            print("Private key (d,n) is: (" + str(d) + ", " +  str(n) + ")")
            print("Public key (e,n) is: (" + str(e) + ", " + str(n) + ")\n")

        elif (userInput.lower() == 'e'):
            message = raw_input("\nEnter your message: \n")
            e = int(raw_input("Enter value for e:\n"))
            n = int(raw_input("Enter value for n:\n"))

            cipher = encryptMessage(message, e, n)

            print("Public key encrypted message is:\n" + cipher +"\n")

        elif (userInput.lower() == 'd'):
            cipher = raw_input("\nEnter your cipher text\n")
            d = int(raw_input("Enter value for d\n"))
            n = int(raw_input("Enter value for n\n"))

            message = decryptMessage(cipher, d, n)

            print("Private key decrypted message is: " + message + "\n")

def generateKeys():

    primeList = list(primes_sieve2(1000))

    e = 65537

    p = random.choice(primeList)
    q = random.choice(primeList)
    n = p * q
    totient = (p - 1) * (q - 1)

    while(p == q or findGCD(e, totient) != 1):
        p = random.choice(primeList)
        q = random.choice(primeList)
        n = p * q
        totient = (p - 1) * (q - 1)

    d = xgcd(e, totient)

    if(d < 0):
        d = d + totient

    keys = []
    keys.append(d)
    keys.append(e)
    keys.append(n)

    return(keys)

def encryptMessage(message, e, n):
    """
        Encryption involves merely converting the character value of each element in the message String to its ordinal value,
        applying the RSA encryption algorithm to this value and then finally applying a padding of length 8 to the encrypted value.
        Each of the encrypted values are concatenated to the encrypted string.
    """

    M = ''
    encrypted = ''
    print("\nBeginning encryption\n")
    for i in message:
        print ".",
        M = str(ord(i))
        encrypted += (Pad(str((int(M) ** e) % n)))

    print("Finished encryption!\n")
    return encrypted

def decryptMessage(cipher, d, n):
    """
        Decryption involves separating the large number cipher value into a list of smaller values by splitting on every 8 numbers
        from the large cipher value. Each of these 8 number values are then unpadded using the unpadding function to find the real
        encrypted value and then the RSA unencryption algoritm is applied to this value. The unencrypted value is then converted into
        its characted representation and concatenated onto the decrypted string.
    """

    valueList = re.findall('........', cipher)

    deCrypted = ''
    print("\nBeginning decryption\n")
    for i in valueList:
        print ".",
        number = int(Unpad(i))
        deCryptedNumber = number ** d % n
        deCrypted += chr(deCryptedNumber)

    print("Finished decrypting!\n")
    return deCrypted


def primes_sieve2(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def findGCD(x, y):

    while(y):
        x, y = y, x % y

    return x

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    """return  b, x0, y0"""
    return x0

def Pad(text):
    paddingSize = (8 - len(text) % 8)
    tempText = text + str(paddingSize)
    numSpaces = 0
    while(len(tempText) % 8):
        tempText += ' '
        numSpaces += 1

    if(len(text) % 8 != 0):
        text = text + '0' * numSpaces + str(paddingSize)

    return text

def Unpad(text):
    textList = list(text)
    paddingNum = ''

    ensureBreakOccured = False

    for i in reversed(textList):
        if( i != '0'):
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

def split_by_n( seq, n ):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]

if __name__ == "__main__":
    main()