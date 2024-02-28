NAME OF PROJECT:
================
Encrypting & Decrypting in AES mode CBC

NAME OF PROGRAMMER:
===================
Ashley J
Michal L

STATEMENT:
==========
I have neither given nor received unauthorized assistance on this work.
However, Sully allowed for Michal L. and Ashley J. to work together on this assignment 

SPECIAL INSTRUCTIONS:
=====================
Describe where the files can be found.
    They can be found on canvas. I recommend downloading File 1 ('AES_encrypt_decrypt.py') & File 2 ('plaintext1.txt'). 
    When you run File 1 you will be asked to input a file to encrypt. Here you will type in File2 ('plaintext1.txt').
    File 3 & 4 just show my output. You will actually generate this on your own by following the instructions below -- So no 
    need to download them your self!

    File 1: AES_encrypt_decrypt.py
    File 2: plaintext1.txt
    File 3: plaintext1.txt.enc
    File 4: plaintext1.txt.dec

Provide any special instructions to access or run your program.
    To run this program you will need the files AES_encrypt_decrypt.py & plaintext1.txt in a directory
    1. Start the program via command line: Type: python3 AES_encrypt_decrypt.py or just run the program manually
    2. A menu option will be listed w/ options to encrypt/decrypt/exit -- press '1' for encrypt
    3. You will need to enter in a file name, you can use the file "plaintext1.txt" or any file in your director 
    4. Now a new file will be created with the new encryption. This file should be called 'plaintext1.txt.enc' unless you chose a different file name
    5. The menu option should show on the command line. Press '2' to decrypt. 
    6. Type the file that was just created called 'plaintext1.txt.enc'
    7. Now a new file should've been created called 'plaintext1.txt.dec' -- you should be able to see the plaintext again
    8. exit the program by pressing '3' whenever you feel

PROBLEM DESCRIPTION AND REMEDIATION:
====================================
We had some experimental issues learning what libaries would work best & how to implement openSSL. 
We learned that openSSL is included in the libaries that we were using already. 
Most of the issues arised from trial and error & bug fixing, but nothing too major.
It is most appreciated that we didn't have to code out the entire AES cipher w/out using libraries, 
because this cipher is insanely intense from what I learned! <-- but as it should be though

RESOURCES: 
==========
https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.197-upd1.pdf
https://onboardbase.com/blog/aes-encryption-decryption/
https://www.javainuse.com/aesgenerator
