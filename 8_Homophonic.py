# Homophonic Cipher
# Consists of mapping each symbol of the plaintext alphabet to several symbols of the ciphertext alphabet
# Usually the cypher alphabet is larger than the plaintext alphabet


# Alphabet
alpha = {
    "A": [9, 12, 33, 47, 53, 67, 78, 92],
    "B": [48, 81],
    "C": [13, 41, 62],
    "D": [1, 3, 45, 79],
    "E": [14, 16, 24, 44, 46, 55, 57, 64, 74, 82, 87, 98],
    "F": [10, 31],
    "G": [6, 25],
    "H": [23, 39, 50, 56, 65, 68],
    "I": [32, 70, 73, 83, 88, 93],
    "J": [15],
    "K": [4],
    "L": [26, 37, 51, 84],
    "M": [22, 27],
    "N": [18, 58, 59, 66, 71, 91],
    "O": [0, 5, 7, 54, 72, 90, 99],
    "P": [38, 95],
    "Q": [94],
    "R": [29, 35, 40, 42, 77, 80],
    "S": [11, 19, 36, 76, 86, 96],
    "T": [17, 20, 30, 43, 49, 69, 75, 85, 97],
    "U": [8, 61, 63],
    "V": [34],
    "W": [60, 89],
    "X": [28],
    "Y": [21, 52],
    "Z": [2],
}


# Implementation
import random


class Homophonic:
    def __init__(self):
        self.plaintext = []
        self.ciphertext = []

    def encrypt(self, plaintext):
        plaintext = plaintext.replace(" ", "")
        for i in range(len(plaintext)):
            self.ciphertext.append(random.choice(alpha[plaintext[i]]))
        result = " ".join(str(x) for x in self.ciphertext)

        return f"This is your encrypted message: {result}\n"

    def decrypt(self, ciphertext):
        values = ciphertext.split(" ")
        for element in values:
            for key, value in alpha.items():
                if int(element) in value:
                    self.plaintext.append(key)
        result = "".join(self.plaintext)

        return f"This is your message: {result}\n"


def menu():
    print("--------------------------")
    print("xX Homophonic Cipher Xx")
    print("--------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("--------------------------")


def main():
    while True:
        menu()
        homo = Homophonic()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            cipher = homo.encrypt(plaintext)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            message = homo.decrypt(ciphertext)
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

# Message
# Crypto is fun

# Key
# Alphabet defined at beginning

# Ciphertext
# 62 35 21 38 20 72 32 76 10 61 91 (Won't be the same every time)


# Example 2

# Ciphertext
# 13 5 26 0 22 81 88 47

# Key
# Alphabet defined at beginning

# Message
# COLOMBIA
