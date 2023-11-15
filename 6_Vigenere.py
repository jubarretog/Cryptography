# Vigenere Cipher
#


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
        self.plaintext = ""
        self.ciphertext = ""

    def encrypt(self, plaintext):
        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext):
        return f"This is your message: {self.plaintext}\n"


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
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            cipher = vige.encrypt(plaintext)
            print(cipher)
            continue
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            message = vige.decrypt(ciphertext)
            print(message)
            continue
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
#
