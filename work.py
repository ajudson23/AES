from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join

class Encryptor:
    def __init__(self, key):
        self.key=key

    # pad data to be appropriate block size    
    def pad(self, s):
        return s+b"\0" * (AES.block_size - len(s) % AES.block_size)
    
    def encrypt(self, message, key, key_size = 256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
    
    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
    
    def decrypt(self, cipherText, key):
        iv = cipherText[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(cipherText[AES.block_size:])
        return plaintext.rstrip(b"\0")
    
    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            cipherText = fo.read()
        dec = self.decrypt(cipherText, self.key)
        with open(file_name[:-4] + ".dec", 'wb') as fo:
            fo.write(dec)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('clear')


while True:
    clear()
    choice = int(input(
        "1. Press '1' to encrypt file.\n2. Press '2' to decrypt file.\n3. Press '3' to exit.\n"))
    clear()
    if choice == 1:
        enc.encrypt_file(str(input("Enter name of file to encrypt: ")))
    elif choice == 2:
        enc.decrypt_file(str(input("Enter name of file to decrypt: ")))
    elif choice == 3:
        exit()
    else:
        print("Please select a valid option!")
