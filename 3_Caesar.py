# Caesar's Cipher
# The key is a number from 1 to 25
# Each letter in the message is shifted upper as many positions in the alphabet as the key


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
class Caesar:
    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""

    def encrypt(self, plaintext, key):
        for i in range(len(plaintext)):
            # Ignore spaces
            if plaintext[i] == " ":
                continue
            # Shift letter
            code = (alpha[plaintext[i]] + key) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.ciphertext += letter

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext, key):
        for i in range(len(ciphertext)):
            # Ignore spaces
            if ciphertext[i] == " ":
                continue
            # Shift letter
            code = (alpha[ciphertext[i]] - key) % 26
            letter = list(alpha.keys())[list(alpha.values()).index(code)]
            self.plaintext += letter

        return f"This is your message: {self.plaintext}\n"


def menu():
    print("--------------------------")
    print("xX Caesar's Cipher Xx")
    print("--------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("--------------------------")


def main():
    while True:
        menu()
        caesar = Caesar()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            key = int(input("Enter key: "))
            cipher = caesar.encrypt(plaintext, key)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            key = int(input("Enter key: "))
            message = caesar.decrypt(ciphertext, key)
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


# Example 1

# Message
# RETURN TO ROME

# Key
# 3

# Cipher message
# UHWXU QWRUR PH


# Example 2

# Cipher message
# WKLVL VHAWU HPHOB LQVHF XUHHQ FUBSW LRQGR QRWXV HLWWR SURWH FWYDO XDEOH LQIRU PDWLR Q

# Key
# 3

# Message
# THISISEXTREMELYINSECUREENCRYPTIONDONOTUSEITTOPROTECTVALUABLEINFORMATION


# Example 3
# LWLVF ODLPH GWKHH DUOLH VWNQR ZQUHI HUHQF HWRWK LVWBS HRIFL SKHUL VLQWK HNDPD VXWUD ZKLFK VDBVZ RPHQV KRXOG OHDUQ WKHDU WRIVH FUHWZ ULWLQ JWRFR QFHDO WKHLU OLDVR QV

# Key
# 3

# Message
# ITISCLAIMEDTHEEARLIESTKNOWNREFERENCETOTHISTYPEOFCIPHERISINTHEKAMASUTRAWHICHSAYSWOMENSHOULDLEARNTHEARTOFSECRETWRITINGTOCONCEALTHEIRLIASONS


# Example 4

# Message
# we will attack at dawn through the left flank

# Key
# 3

# Cipher message
# ZHZLOODWWDFNDWGDZQWKURXJKWKHOHIWIODQN
