# AES Cipher
#


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
        # Create a DES object with pyDes and encrypt image
        intAes = pyaes.AESModesOfOperation()
        encBytes = intAes.encrypt(imgBytes)
        b64Bytes = base64.b64encode(encBytes)
        return b64Bytes

    def decrypt(self, encBytes, key, keySize):
        # Check if key is has the correct bytes long
        if len(key) != keySize:
            return "Key must has the correct bytes long\n"
        # Create a DES object with pyDes and decrypt image
        intAes = pyaes.AESModeOfOperation()
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
            key = input("Enter key bytes: ").upper().encode()
            encBytes = aes.encrypt(imgBytes, key, keySize)
            with open("12_AES_enc.txt", "w") as f:
                f.write(encBytes)
            print("Encrypted bytes from image saved in the 12_AES_enc.txt file\n")
            continue
        # Decrypt
        if choice == "2":
            print("Enter the image name, remember this must")
            imgRoute = input("be in the same folder than the program: ")
            img = Image.open(imgRoute)
            print("The original size of the image is:", img.size, "wxh")
            keySize = int(input("Enter the key size (16, 24 or 32 bytes): "))
            key = input("Enter key bytes: ").upper().encode()
            with open("12_AES_enc.txt", "rb") as f:
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
