# DES Cipher
# Data Encryption Standard (DES) is a symmetric-key algorithm for the encryption of digital data
# DES is a block cipher that encrypts data in 64-bit blocks, doing 16 rounds of encryption
# DES uses a 64-bit key, of which 8 bits are used for parity checking
# As it uses a short key length is considered insecure by today's standards
# DES uses a Feistel network, a symmetric structure used in the construction of block ciphers
# For this implementation, we will use the pyDes library and the pillow library to work with images, to encrypt and decrypt an image using its pixels


# Implementation
import pyDes
import base64
from PIL import Image


class Des:
    def encrypt(self, imgBytes, key):
        # Check if key is 8 bytes long
        if len(key) != 8:
            return "Key must be 8 bytes long\n"
        # Make padding if necessary
        while (len(imgBytes) % 8) != 0:
            imgBytes += b"\x00"
        # Create a DES object with pyDes and encrypt image
        intDes = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
        encBytes = intDes.encrypt(imgBytes)
        b64Bytes = base64.b64encode(encBytes)
        return b64Bytes

    def decrypt(self, encBytes, key):
        # Check if key is 8 bytes long
        if len(key) != 8:
            return "Key must be 8 bytes long\n"
        # Create a DES object with pyDes and decrypt image
        intDes = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
        imgBytes = intDes.decrypt(encBytes)
        return imgBytes


def menu():
    print("---------------------------------------------------")
    print("xX DES Cipher Xx")
    print("---------------------------------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("--------------------------------------------------")


def main():
    while True:
        menu()
        des = Des()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            print("Enter the image name, remember this must")
            imgName = input("be in the same folder than the program: ")
            img = Image.open(imgName)
            print("The original size of the image is:", img.size, "wxh")
            img = img.convert("RGB")
            imgBytes = img.tobytes()
            key = input("Enter 8 bytes key: ").upper().encode()
            encBytes = des.encrypt(imgBytes, key)
            with open("11_DES_enc.txt", "wb") as f:
                f.write(encBytes)
            print("Encrypted bytes from image saved in the 11_DES_enc.txt file\n")
            continue
        # Decrypt
        if choice == "2":
            print("Enter the image name, remember this must")
            imgName = input("be in the same folder than the program: ")
            img = Image.open(imgName)
            print("The original size of the image is:", img.size, "wxh")
            key = input("Enter 8 bytes key: ").upper().encode()
            with open("11_DES_enc.txt", "rb") as f:
                b64Bytes = f.read()
            encBytes = base64.b64decode(b64Bytes)
            imgBytes = des.decrypt(encBytes, key)
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
