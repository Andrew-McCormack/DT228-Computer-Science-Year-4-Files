from Crypto.Cipher import DES
import base64
import binascii

def main():
    key = '12345678'
    text = 'AAAABBBBAAAABBBB'

    print('Plaintext is ' + text)

    encryptedText = encryptText(key, text)

    print('Encrypted text in hex is ' + encryptedText)

    decryptedText = decryptText(key, encryptedText)

    print('Decrypted text is ' + decryptedText)

def encryptText(key, text):
    des = DES.new(key, DES.MODE_ECB)

    return des.encrypt(text).encode('hex')

def decryptText(key, encryptedText):
    des = DES.new(key, DES.MODE_ECB)

    return des.decrypt(encryptedText.decode('hex'))

if __name__ == "__main__":
    main()