from PIL import Image, ImageOps
import bitarray

def main():

    while(True):
        choice = raw_input('\nEnter g to convert colour image to grayscale, c to copy grayscale image pixel by pixel into new image,\n'
                           'e to hide a message within a grayscale image or d to decode a hidden message from an image\n')

        if(choice.lower() == 'g'):
            fileName = raw_input('Enter the name of the image: ')
            print(convertToGrayscale(fileName))
        elif(choice.lower() == 'c'):
            fileName = raw_input('Enter the name of the image: ')
            print(iterateThroughPixelsAndWriteToNew(fileName))
        elif(choice.lower() == 'e'):
            fileName = raw_input('Enter the name of the image: ')
            message = raw_input('Enter the message you wish to hide: ')
            print(encodeMessageIntoImage(fileName, message))
        elif(choice.lower() == 'd'):
            fileName = raw_input('Enter the name of the image: ')
            print(decodeMessageFromImage(fileName))

def binaryStringToAsciiString(messageBitString):
    return "".join([chr(int(messageBitString[i:i + 8], 2)) for i in range(0, len(messageBitString), 8)])

def changeLeastSignificantBitAndConvertToInt(bitField, bit):
    bitFieldList = list(bitField)
    bitFieldList[-1] = bit
    out = 0

    # Convert bitfield to int representation
    for bit in bitFieldList:
        out = (out << 1) | int(bit)

    return out


def encodeMessageIntoImage(fileName, message):
    messageBitArray = bitarray.bitarray()
    messageBitArray.fromstring(message)

    #Append 15 ones followed by a single zero as a trailer id so program will know when to stop looking for hidden info when decoding message from images
    messageBitArray += "1111111111111110"
    try:
        img = Image.open(fileName, 'r')

        if (img.mode == 'L'):
            encodedSecretImage = Image.new('L', img.size)

            x, y = img.size
            count = 0
            print '\nBeginning encoding\n'
            for xPix in range(x):
                for yPix in range(y):
                    print '.',
                    coordinate = xPix, yPix
                    value = img.getpixel(coordinate)
                    if(count != len(messageBitArray)):
                        bitfield = ''.join(list(bin(value))[2:])
                        modifiedBitField = changeLeastSignificantBitAndConvertToInt(bitfield, messageBitArray[count])
                        encodedSecretImage.putpixel(coordinate, modifiedBitField)
                        count += 1
                    else:
                        encodedSecretImage.putpixel(coordinate, value)

            if(count == len(messageBitArray)):
                newFileName = fileName.split(".")[0] + "EncodedMessageVersion.png"
                encodedSecretImage.save(newFileName)
                return 'Message successfully encoded into ' + newFileName
            else:
                return 'Unable to encode message into ' + fileName
        return 'Image must be in grayscale, run grayscale command (g) to create grayscale version!'

    except:
        return 'Unable to open file, ensure correct file name was given!'

def decodeMessageFromImage(fileName):
    messageBitString = ''

    try:
        img = Image.open(fileName, 'r')

        if (img.mode == 'L'):
            x, y = img.size

            print('\nBeginning decoding\n')
            for xPix in range(x):
                for yPix in range(y):
                    print '.',
                    coordinate = xPix, yPix
                    value = img.getpixel(coordinate)

                    bitfield = ''.join(list(bin(value))[2:])
                    messageBitString += bitfield[-1]

                    # End of message is marked by trailer id = 1111111111111110
                    if (messageBitString[-16:] == '1111111111111110'):
                        messageBitString = messageBitString[:-16]
                        return "\nMessage is: " + binaryStringToAsciiString(messageBitString)

            return "Could not find hidden message!"
        return 'Image must be in grayscale, run grayscale command (g) to create grayscale version!'

    except:
        return 'Unable to open file, ensure correct file name was given!'

def convertToGrayscale(fileName):
    try:
        img = Image.open(fileName, 'r')
        grayScaleVersionImage = Image.new('L', img.size)

        x, y = img.size

        print('\nBeginning conversion\n')
        for xPix in range(x):
            for yPix in range(y):
                print '.',
                coordinate = xPix, yPix
                r,g,b,a = img.getpixel(coordinate)
                average = (r + g + a) / 3
                grayScaleVersionImage.putpixel(coordinate, average)

        newFileName = fileName.split(".")[0] + "-Grayscale.png"
        grayScaleVersionImage.save(newFileName)
        return("Finished converting image to grayscale, saved as " + newFileName)

    except:
        return 'Unable to open file, ensure correct file name was given!'

def iterateThroughPixelsAndWriteToNew(fileName):

    try:
        img = Image.open(fileName, 'r')
        x, y = img.size

        if(img.mode == 'L'):
            newImg = Image.new("L", img.size)

            print('Beginning copy process\n')
            for xPixel in range(x):
                for yPixel in range(y):
                    print '.',
                    coordinate = xPixel, yPixel
                    value = img.getpixel(coordinate)
                    newImg.putpixel(coordinate, value)

            newFileName = fileName.split(".")[0] + "Copy.png"
            newImg.save(newFileName)

            return("Successfully copied image pixel by pixel into " + newFileName)

        return("Image must be in grayscale, run grayscale command (g) to create grayscale version!")

    except:
        return 'Unable to open file, ensure correct file name was given!'

def pixValueToHex(pixValue):
    return '#{:02x}'.format(pixValue)

if __name__ == '__main__':
    main()