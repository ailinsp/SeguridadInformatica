import pyAesCrypt

from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "#Training"
encFileSize = stat("ejemplo.txt.aes").st_size
with open("ejemplo.txt.aes", "rb") as fIn:
    with open("ejemploOut.txt", "wb") as fOut:
        try:
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError:
            remove("ejemploOut.txt")