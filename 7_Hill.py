# Hill Cipher
# Consists of a matrix with the plaintext and a key matrix
# Key matrix must be invertible
# To encrypt, multiply plaintext matrix with key matrix in modulo 26
# To decrypt, multiply ciphertext matrix with inverse key matrix in modulo 26


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
from sympy import Matrix
import numpy as np


class Hill:
    def __init__(self):
        self.pmatrix = []
        self.kmatrix = []
        self.cmatrix = []
        self.plaintext = ""
        self.ciphertext = ""

    def encrypt(self, plaintext, key, dim):
        # Check if plaintext or key overpassed matrix dimension
        plaintext = plaintext.replace(" ", "")
        key = key.replace(" ", "")
        if (len(plaintext) > (dim * dim)) or (len(key) > (dim * dim)):
            return "Plaintext or key overpassed matrix dimension\n"
        # Fill plaintext matrix
        self.pmatrix = list(plaintext)
        for i in range(len(plaintext)):
            self.pmatrix[i] = alpha[plaintext[i]]
        while len(self.pmatrix) < (dim * dim):
            self.pmatrix.append(0)
        self.pmatrix = np.array(self.pmatrix).reshape(dim, dim)
        # Fill key matrix
        self.kmatrix = list(key)
        for i in range(len(key)):
            self.kmatrix[i] = alpha[key[i]]
        while len(self.kmatrix) < (dim * dim):
            self.kmatrix.append(0)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Check if key matrix is invertible and can be used
        self.kmatrix = Matrix(self.kmatrix)
        try:
            self.kmatrix.inv_mod(26)
        except:
            return "Key matrix is not invertible, you can't use this key\n"
        self.kmatrix = list(self.kmatrix)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Multiply ciphertext matrix with inverse key matrix in modulo 26
        self.cmatrix = np.matmul(self.pmatrix, self.kmatrix)
        self.cmatrix = self.cmatrix % 26
        # Convert ciphertext matrix to ciphertext
        for i in range(dim):
            for j in range(dim):
                letter = list(alpha.keys())[
                    list(alpha.values()).index(self.cmatrix[i][j])
                ]
                self.ciphertext += letter

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext, key, dim):
        # Check if plaintext or key overpassed matrix dimension
        if (len(ciphertext) > (dim * dim)) or (len(key) > (dim * dim)):
            return "Plaintext or key overpassed matrix dimension\n"
        # Fill plaintext matrix
        ciphertext = ciphertext.replace(" ", "")
        self.cmatrix = list(ciphertext)
        for i in range(len(ciphertext)):
            self.cmatrix[i] = alpha[ciphertext[i]]
        while len(self.cmatrix) < (dim * dim):
            self.cmatrix.append(0)
        self.cmatrix = np.array(self.cmatrix).reshape(dim, dim)
        # Fill key matrix
        key = key.replace(" ", "")
        self.kmatrix = list(key)
        for i in range(len(key)):
            self.kmatrix[i] = alpha[key[i]]
        while len(self.kmatrix) < (dim * dim):
            self.kmatrix.append(0)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Calculate matrix modular inverse
        self.kmatrix = Matrix(self.kmatrix)
        try:
            self.kmatrix = self.kmatrix.inv_mod(26)
        except:
            return "Key matrix is not invertible\n"
        self.kmatrix = list(self.kmatrix)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Multiply ciphertext matrix with inverse key matrix in modulo 26
        self.pmatrix = np.matmul(self.cmatrix, self.kmatrix)
        self.pmatrix = self.pmatrix % 26
        # Convert plaintext matrix to plaintext
        for i in range(dim):
            for j in range(dim):
                letter = list(alpha.keys())[
                    list(alpha.values()).index(self.pmatrix[i][j])
                ]
                self.plaintext += letter

        return f"This is your message: {self.plaintext}\n"


def menu():
    print("xX Hill Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        hill = Hill()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            dim = int(input("Enter dimension of matrix: "))
            plaintext = input("Enter plaintext: ").upper()
            key = input("Enter key: ").upper()
            cipher = hill.encrypt(plaintext, key, dim)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            dim = int(input("Enter dimension of matrix: "))
            ciphertext = input("Enter ciphertext: ").upper()
            key = input("Enter key: ").upper()
            message = hill.decrypt(ciphertext, key, dim)
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

# Dimension
# 2

# Message
# JULY

# Key
# LIDH

# Ciphertext
# DELW


# Example 2

# Dimension
# 5

# Ciphertext
# VKFZRVWTIAZSMISGKA

# Key
# LIDH

# Message
#
