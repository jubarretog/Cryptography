# Rot13 Cipher
# Each letter in the message is shifted by 13 many positions in the alphabet


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
class Rot13:
    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""

    def encrypt(self, plaintext):
        for i in range(len(plaintext)):
            # Ignore spaces
            if plaintext[i] == " ":
                self.ciphertext += " "
                continue
            # Shift letter
            code = (alpha[plaintext[i]] + 13) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.ciphertext += letter

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext):
        for i in range(len(ciphertext)):
            # Ignore spaces
            if ciphertext[i] == " ":
                self.plaintext += " "
                continue
            # Shift letter
            code = (alpha[ciphertext[i]] - 13) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.plaintext += letter

        return f"This is your message: {self.plaintext}\n"


def menu():
    print("xX Rot13 Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        rot13 = Rot13()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            cipher = rot13.encrypt(plaintext)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            message = rot13.decrypt(ciphertext)
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
# VSGUR AFNUN FGVZR GBERN QZLRZ NVYVJ VFUGU RLFRA QZRNO YBBQL

# Key
# 3

# Message
# IFTHE NSAHA STIME TOREA DMYEM AILIW ISHTH EYSEN DMEAB LOODY
