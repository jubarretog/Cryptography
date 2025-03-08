# AES Cipher
# Advanced Encryption Standard (AES) is a symmetric encryption algorithm that encrypts and decrypts data in blocks of 128 bits
# It is a secure and efficient algorithm that is used by the U.S. government to protect classified information
# Compared to the DES algorithm, the AES algorithm is more secure and efficient
# Uses a block size of 128 bits and supports key sizes of 128, 192, and 256 bits
# Uses a substitution-permutation network, which is a series of mathematical operations that are applied to the data
# This method do 10 rounds for 128-bit keys, 12 rounds for 192-bit keys, and 14 rounds for 256-bit keys

# In this implementation AES will be used to encrypt and decrypt images using its pixels, using the PyAES library and the Pillow library to work with images


# Implementation
import pyaes
import base64
from PIL import Image


class Aes:
    def encrypt(self, imgBytes, key, keySize):
        # Check if key is has the correct bytes long
        if len(key) != keySize:
            return "Key must has the correct bytes long\n"
        # Make padding if necessary
        key = key.ljust(keySize, b"\0")
        # Create a AES object with pyaes and encrypt image
        intAes = pyaes.AESModeOfOperationCTR(key)
        encBytes = intAes.encrypt(imgBytes)
        # Encode the encrypted bytes in base64
        b64Bytes = base64.b64encode(encBytes)
        return b64Bytes

    def decrypt(self, encBytes, key, keySize):
        # Check if key is has the correct bytes long
        if len(key) != keySize:
            return "Key must has the correct bytes long\n"
        # Create a DES object with pyDes and decrypt image
        intAes = pyaes.AESModeOfOperationCTR(key)
        imgBytes = intAes.decrypt(encBytes)
        return imgBytes


def menu():
    print("---------------------------------------------------")
    print("xX AES Cipher Xx")
    print("---------------------------------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("--------------------------------------------------")


def main():
    while True:
        menu()
        aes = Aes()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            print("Enter the image name, remember this must")
            imgRoute = input("be in the same folder than the program: ")
            img = Image.open(imgRoute)
            print("The original size of the image is:", img.size, "wxh")
            img = img.convert("RGB")
            imgBytes = img.tobytes()
            keySize = int(input("Enter the key size (16, 24 or 32 bytes): "))
            if keySize not in [16, 24, 32]:
                print("Invalid key size. Please try again\n")
                continue
            key = input("Enter key bytes: ").upper().encode()
            encBytes = aes.encrypt(imgBytes, key, keySize)
            with open("9_AES_enc.txt", "wb") as f:
                f.write(encBytes)
            print("Encrypted bytes from image saved in the 9_AES_enc.txt file\n")
            continue
        # Decrypt
        if choice == "2":
            print("Enter the image name, remember this must")
            imgRoute = input("be in the same folder than the program: ")
            img = Image.open(imgRoute)
            print("The original size of the image is:", img.size, "wxh")
            keySize = int(input("Enter the key size (16, 24 or 32 bytes): "))
            if keySize not in [16, 24, 32]:
                print("Invalid key size. Please try again\n")
                continue
            key = input("Enter key bytes: ").upper().encode()
            with open("9_AES_enc.txt", "rb") as f:
                b64Bytes = f.read()
            encBytes = base64.b64decode(b64Bytes)
            imgBytes = aes.decrypt(encBytes, key, keySize)
            img = Image.frombytes("RGB", img.size, imgBytes)
            print("The decrypted image will be displayed\n")
            img.show()
            continue
        # Exit
        if choice == "3":
            print("Thank you for using this program")
            exit()

        print("Invalid choice. Please try again\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
        exit()
