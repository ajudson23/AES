from Crypto import Random
from Crypto.Cipher import AES       # this includes openSSL as a feature of the libary 
import os
import os.path

''' pad data to be appropriate block size ''' 
def pad(message):
    return message+b"\0" * (AES.block_size - len(message) % AES.block_size) 

''' this function encrypts a file, it relies on the library AES, where it can pull the particular mode aka CBC
    this library also sets the block sizes for variables such as the message and IV. 
    The AES.new function creates a new AES cipher object   '''
def encryption(plainText, key):                    
    plainText = pad(plainText)
    initializationVector = Random.new().read(AES.block_size)        # create a random IV using appropriate block size for AES
    cipher = AES.new(key, AES.MODE_CBC, initializationVector)
    return initializationVector + cipher.encrypt(plainText)         # concatenating the IV w/ the encrypted plaintext, which will be useful for when we decrypt

''' This function will read f/ a file --> call encryption() function --> then write to a file
    with encrypted message & adding ".enc" at the end of file name '''
def encryptFile(fileName, key):
    with open(fileName, 'rb') as fo:
        plaintext = fo.read()
    enc = encryption(plaintext, key)
    with open(fileName + ".enc", 'wb') as fo:
        fo.write(enc)

''' This function Decrypts an encrypted message 
    It will get the IV by using the slicing opperation with the block size
    It will create a new AES cipher object using the key, the CBC mode & IV
    lastly it will decrypt the cipher '''
def decryption(cipherText, key):
    initializationVector = cipherText[:AES.blockSize]
    cipher = AES.new(key, AES.MODE_CBC, initializationVector)
    plaintext = cipher.decrypt(cipherText[AES.blockSize:])
    return plaintext.rstrip(b"\0")                                  # rstrip gets rid of trailing zero bytes which was created to fill the block size

''' This function will read f/ a file --> call decryption() function --> then write to a file
    with new plaintext message & adding ".dec" at the end of file name '''
def decryptFile(fileName, key):
    with open(fileName, 'rb') as fo:
        cipherText = fo.read()
    dec = decryption(cipherText, key)
    with open(fileName[:-4] + ".dec", 'wb') as fo:
        fo.write(dec)
    

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
clear = lambda: os.system('clear')                                  # clear// function that will clear out the text in the terminal

while True:
    clear()
    choice = int(input(
        "1. Press '1' to encrypt a file.\n2. Press '2' to decrypt a file.\n3. Press '3' to exit.\n"))
    clear()
    if choice == 1:
        encryptFile(str(input("Enter name of file to encrypt: ")), key)
    elif choice == 2:
        decryptFile(str(input("Enter name of file to decrypt: ")), key)
    elif choice == 3:
        exit()
    else:
        print("Please select a valid option!")