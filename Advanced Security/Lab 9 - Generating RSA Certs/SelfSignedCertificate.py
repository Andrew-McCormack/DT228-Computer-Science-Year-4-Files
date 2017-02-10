import OpenSSL
from OpenSSL import crypto, SSL

def main():
    userInput  = 's'
    while(True):
        userInput = input("\nEnter r to create x509 root certificateor (Part 1 of lab), enter e to create an end user certificate (Part 2 of lab),\n"
                          "enter v to validate chain of certificates (Part 3 of lab): ")

        if(userInput.lower() == 'r'):
            CERT_FILE = 'x509Certificate.crt'
            KEY_FILE = 'private.key'
            REQ_FILE = 'service.req'

            k = generatePrivateKeyPair(2048)
            print("Successfully generated private key pair!")

            req = create_and_sign_request(k)
            print("Sucessfully created cert signing request!")

            cert = create_and_sign_certificate(req, k)

            print("Successfully created cert!")

            #Files need to be created before they can be opened in binary read mode
            open(CERT_FILE, "w+").close()
            open(KEY_FILE, "w+").close()
            open(REQ_FILE, "w+").close()

            open(CERT_FILE, "br+").write(
                crypto.dump_certificate(crypto.FILETYPE_PEM, cert))
            open(KEY_FILE, "br+").write(
                crypto.dump_privatekey(crypto.FILETYPE_PEM, k))
            open(REQ_FILE, "br+").write(
                crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))

            print("Cert file and key file successfully created, saved as: " + CERT_FILE + " and " + KEY_FILE)


        elif(userInput.lower() == 'e'):
            END_USER_CERT_FILE ='EndUserCertificate.crt'

            key = generatePrivateKeyPair(1024)
            endUserRequest = create_and_sign_request(key)
            endUserCert = create_end_user_cert(endUserRequest)

            # File must be created before it can be opened in binary write
            open(END_USER_CERT_FILE, "w+").close()

            open(END_USER_CERT_FILE, "br+").write(
                crypto.dump_certificate(crypto.FILETYPE_PEM, endUserCert))

            print("End user cert file successfully created, saved as: " + END_USER_CERT_FILE)

        elif (userInput.lower() == 'v'):
            # Pass in end user cert i.e. 'EndUserCertificate.crt'
            if(verifyCert(input('Enter name of cert: ')) == True):
                print('Cert successfully validated!')
            else:
                print('Cert validation failed!')

def create_end_user_cert(endUserRequest):
    PRIVATE_KEY = 'private.key'
    ROOT_CERTIFICATE = 'x509Certificate.crt'

    st_cert = open(ROOT_CERTIFICATE, 'rt').read()

    c = OpenSSL.crypto
    cert = c.load_certificate(c.FILETYPE_PEM, st_cert)

    k = open(PRIVATE_KEY, 'rt').read()
    privateKey = c.load_privatekey(c.FILETYPE_PEM, k)

    endUserCert = crypto.X509()
    endUserCert.set_serial_number(2)
    endUserCert.gmtime_adj_notBefore(0)
    endUserCert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    endUserCert.set_issuer(cert.get_subject())
    endUserCert.set_subject(endUserRequest.get_subject())
    endUserCert.set_pubkey(endUserRequest.get_pubkey())
    endUserCert.sign(privateKey, 'md5')
    return endUserCert


def generatePrivateKeyPair(n):
    k = crypto.PKey()
    k.generate_key(crypto.TYPE_RSA, n)

    return k

def create_and_sign_request(k):

    req = crypto.X509Req()
    subject = req.get_subject()
    subject.C = input("Enter country: ")
    subject.ST = input("Enter state: ")
    subject.L = input("Enter location: ")
    subject.O = input("Enter organization: ")
    subject.OU = input("Enter organization unit: ")
    subject.CN = input("Enter common name: ")
    req.set_pubkey(k)
    req.sign(k, "md5")

    return req

def create_and_sign_certificate(req, k):
    cert = crypto.X509()
    cert.set_serial_number(1)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(10 * 365 * 24 * 60 * 60)
    cert.set_issuer(req.get_subject())
    cert.set_subject(req.get_subject())
    cert.set_pubkey(req.get_pubkey())
    cert.sign(k, 'md5')

    return cert


def verifyCert(CERT_NAME):
    ROOT_CERTIFICATE = 'x509Certificate.crt'

    c = OpenSSL.crypto

    root_cert = open(ROOT_CERTIFICATE, 'rt').read()
    rootCert = c.load_certificate(c.FILETYPE_PEM, root_cert)

    certBeingChecked = open(CERT_NAME, 'rt').read()
    certBeingChecked = c.load_certificate(c.FILETYPE_PEM, certBeingChecked)

    try:
        store = crypto.X509Store()
        store.add_cert(rootCert)

        store_ctx = crypto.X509StoreContext(store, certBeingChecked)

        store_ctx.verify_certificate()

        return True

    except Exception as e:
        print('Could not verify cert!')
        print(e)
        return False


if __name__ == "__main__":
    main()