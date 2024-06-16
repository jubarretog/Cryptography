# Vigenere Cipher
# Consists of several Caesar ciphers in sequence with different shift values
# The shift value for each letter is determined by a key
# The key is form by repeating a keyword until it matches the length of the plaintext
# Then a XOR operation is performed between the plaintext and the key
# The result is sliced into groups of characters with the same length


# Alphabet
alpha = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}


# Implementation
class Vigenere:
    def __init__(self):
        self.plaintext = []
        self.ciphertext = []

    def encrypt(self, plaintext, key):
        # Complete plaintext with X if necessary to make it divisible by t
        plaintext = plaintext.replace(" ", "")
        t = int(input("Enter length of slices: "))
        while (len(plaintext) % t) != 0:
            plaintext += "X"
        # Make key as long as plaintext
        key = key.replace(" ", "")
        for i in range(len(plaintext)):
            if len(key) < len(plaintext):
                key += key[i]
        # Make XOR operation
        for i in range(len(plaintext)):
            code = (alpha[plaintext[i]] + alpha[key[i]]) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.ciphertext.append(letter)
        # Cut ciphertext into groups t of characters
        result = ""
        for i in range(0, len(self.ciphertext), t):
            result = result + "".join(self.ciphertext[i : i + t]) + " "

        return f"This is your encrypted message: {result.strip()}\n"

    def decrypt(self, ciphertext, key):
        # Make key as long as ciphertext
        ciphertext = ciphertext.replace(" ", "")
        key = key.replace(" ", "")
        for i in range(len(ciphertext)):
            if len(key) < len(ciphertext):
                key += key[i]
        # Make XOR operation
        for i in range(len(ciphertext)):
            code = (alpha[ciphertext[i]] - alpha[key[i]]) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.plaintext.append(letter)
        result = "".join(self.plaintext)

        return f"This is your message: {result}\n"


def menu():
    print("xX Vigenere Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        vige = Vigenere()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            key = input("Enter key: ").upper()
            cipher = vige.encrypt(plaintext, key)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            key = input("Enter key: ").upper()
            message = vige.decrypt(ciphertext, key)
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
# TO BE OR NOT TO BE THAT IS THE QUESTION

# Key
# RELATIONS

# Slice's length
# 5

# Ciphertext
# KSMEH ZBBLK SMEMP OGAJX SEJCS FLZSY


# Example 2

# Message
# THERE IS A SECRET PASSAGE BEHIND THE PICTURE FRAME

# Key
# CRYPTO

# Slice length
# 3

# Ciphertext
# VYC GXW URQ TVF GKN PLG CXC QXV KEB IAS RZA INF GWP PFS
