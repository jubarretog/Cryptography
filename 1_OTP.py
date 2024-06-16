# One-Time Pad (OTP) Cipher
# Consists of making a XOR operation between the plaintext and the key
# The key must be at least as long as the plaintext message
# The key must be random and never reused

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
class OneTimePad:
    def __init__(self):
        self.plaintext = []
        self.ciphertext = []

    def encrypt(self, plaintext, key):
        # Check key length
        if len(key) < len(plaintext):
            return "Key must be at least as long as the plaintext message\n"
        # Make XOR operation
        for i in range(len(plaintext)):
            code = (alpha[plaintext[i]] + alpha[key[i]]) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.ciphertext.append(letter)
        result = "".join(self.ciphertext)

        return f"This is your encrypted message: {result}\n"

    def decrypt(self, ciphertext, key):
        # Check key length
        if len(key) < len(ciphertext):
            return "Key must be at least as long as the cyphertext message\n"
        # Make XOR operation
        for i in range(len(ciphertext)):
            code = (alpha[ciphertext[i]] - alpha[key[i]]) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.plaintext.append(letter)
        result = "".join(self.plaintext)

        return f"This is your message: {result}\n"


def menu():
    print("xX One-Time Pad Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        otp = OneTimePad()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            key = input("Enter key: ").upper()
            cipher = otp.encrypt(plaintext, key)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            key = input("Enter key: ").upper()
            message = otp.decrypt(ciphertext, key)
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
# hello

# Key
# eoxjf

# Cipher message
# lsiut
