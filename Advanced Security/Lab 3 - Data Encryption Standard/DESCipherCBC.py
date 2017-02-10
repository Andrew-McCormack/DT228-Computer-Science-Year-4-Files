from Crypto.Cipher import DES
import binascii
import base64

def main():
    key = '12345678'
    iv = '00000000'
    text = 'AAAABBBBAAAABBBB'

    print('Plaintext is ' + text)

    encryptedText = encryptText(key, iv, text)

    print('Encrypted text in hex is ' + encryptedText)

    decryptedText = decryptText(key, iv, encryptedText)

    print ('Unencrypted text is ' + decryptedText)

def encryptText(key, iv, text):
    des_encrypt = DES.new(key, DES.MODE_CBC, iv)

    return des_encrypt.encrypt(text).encode('hex')

def decryptText(key, iv, text):
    des_decrypt = DES.new(key, DES.MODE_CBC, iv)

    return(des_decrypt.decrypt(text.decode('hex')))

if __name__ == "__main__":
    main()