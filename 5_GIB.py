# Garbage-in-between (GIB) Cipher
# The message is hidden in between a bunch of garbage characters
# To decrypt, you need to know the position of the real characters


# Alphabet
alpha = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    " ",
]


# Implementation
import random


class GarbageInBetween:
    def __init__(self):
        self.ciphertext = ""
        self.plaintext = ""

    def encrypt(self, plaintext):
        # Check length of ciphertext
        while True:
            long = int(input("Enter length of ciphertext: "))
            if long >= len(plaintext):
                break
            print("Invalid length, try again")
        # Get position of real characters
        pos = self.real_char(plaintext, long)
        # Fill ciphertext with garbage characters
        count = 0
        for i in range(long):
            if (i + 1) in pos:
                self.ciphertext += plaintext[count]
                count += 1
            else:
                self.ciphertext += random.choice(alpha)

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext):
        # Get position of real characters
        pos = self.real_char(ciphertext, "d")
        # Extract plaintext from ciphertext
        for i in range(len(ciphertext)):
            if (i + 1) in pos:
                self.plaintext += ciphertext[i]

        return f"This is your message: {self.plaintext}\n"

    def real_char(self, text, mode):
        pos = []
        # Encrypt
        if type(mode) is int:
            n = len(text)
            while n > 0:
                key = int(input("Enter position of real character: "))
                if key > mode:
                    print("Invalid position, try again")
                    continue
                pos.append(key)
                n -= 1
        # Decrypt
        else:
            n = int(input("Enter number of real characters: "))
            while n > 0:
                key = int(input("Enter position of real character: "))
                if key > len(text):
                    print("Invalid position, try again")
                    continue
                pos.append(key)
                n -= 1

        return pos


def menu():
    print("xX Garbage-in-between Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        gib = GarbageInBetween()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            cipher = gib.encrypt(plaintext)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            message = gib.decrypt(ciphertext)
            print(message)
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


# Example

# Cipher message
# I LOVE YOUI HAVE YOUDEEP UNDERMY SKIN MYLOVE LASTSFOREVER INHYPERSPACE

# Real characters
# 8 19 26 35 36 41 46 47 49 52 60 69 70

# Message
# YOUKILLATONCE
