import pyAesCrypt

from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "#Training"
with open("ejemplo.txt", "rb") as fIn:
    with open("ejemplo.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)
        # get encrypted file size
        encFileSize = stat("ejemplo.txt.aes").st_size