# Hill Cipher
# Consists of a matrix with the plaintext and a key matrix
# Key matrix must be invertible
# To encrypt, multiply plaintext matrix with key matrix in modulo 26
# To decrypt, multiply ciphertext matrix with inverse key matrix in modulo 26
# In this implementation the matrices are filled by rows
# It works with any dimension of the key matrix

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

    def modular_inverse(a, mod):
        a = a % mod
        for x in range(1, mod):
            if (a * x) % mod == 1:
                return x
        raise ValueError(f"No modular inverse exists for {a} under modulo {mod}")

    def matrix_modular_inverse(matrix, mod):
        # Compute the determinant modulus
        det = int(round(np.linalg.det(matrix)))
        det_mod = det % mod
        # Compute modular inverse of the determinant
        try:
            det_inv = Hill.modular_inverse(det_mod, mod)
        except ValueError:
            raise ValueError(
                "Matrix determinant has no modular inverse, so the matrix is not invertible under this modulus."
            )
        # Compute the adjugate matrix (transpose of cofactor matrix)
        n = len(matrix)
        cofactor_matrix = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                minor = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
                cofactor = int(round(np.linalg.det(minor)))
                cofactor_matrix[i, j] = ((-1) ** (i + j)) * cofactor
        # Transpose of the cofactor matrix
        adjugate_matrix = cofactor_matrix.T
        # Multiply adjugate by determinant's modular inverse make module operation
        inv_matrix = (det_inv * adjugate_matrix) % mod
        return inv_matrix

    def encrypt(self, plaintext, key, dim):
        # Check if key overpass matrix dimension
        key = key.replace(" ", "")
        if len(key) > (dim * dim):
            return "Key overpass matrix dimension\n"
        # Separate plaintext in n-grams
        plaintext = plaintext.replace(" ", "")
        if len(plaintext) % dim != 0:
            plaintext += "X" * (dim - (len(plaintext) % dim))
        for i in range(0, len(plaintext), dim):
            self.pmatrix.append(plaintext[i : i + dim])
        # Fill key matrix
        self.kmatrix = list(key)
        for i in range(len(key)):
            self.kmatrix[i] = alpha[key[i]]
        while len(self.kmatrix) < (dim * dim):
            self.kmatrix.append(0)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Check if key matrix is invertible and can be used
        try:
            Hill.matrix_modular_inverse(self.kmatrix, 26)
        except:
            return "Key matrix is not invertible, you can't use this key\n"
        self.kmatrix = list(self.kmatrix)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Multiply n-grams with key matrix in modulo 26
        for row in self.pmatrix:
            row = np.array([alpha[letter] for letter in row])
            row = np.matmul(row, self.kmatrix)
            row = row % 26
            for element in row:
                self.cmatrix.append(element)
        # Convert ciphertext matrix to ciphertext
        for letter in self.cmatrix:
            letter = list(alpha.keys())[list(alpha.values()).index(letter)]
            self.ciphertext += letter

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext, key, dim):
        # Check if key overpass matrix dimension
        key = key.replace(" ", "")
        if len(key) > (dim * dim):
            return "Key overpass matrix dimension\n"
        # Separate plaintext in n-grams
        ciphertext = ciphertext.replace(" ", "")
        if len(ciphertext) % dim != 0:
            ciphertext += "X" * (dim - (len(ciphertext) % dim))
        for i in range(0, len(ciphertext), dim):
            self.cmatrix.append(ciphertext[i : i + dim])
        # Fill key matrix
        self.kmatrix = list(key)
        for i in range(len(key)):
            self.kmatrix[i] = alpha[key[i]]
        while len(self.kmatrix) < (dim * dim):
            self.kmatrix.append(0)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Check if key matrix is invertible and can be used
        try:
            self.kmatrix = Hill.matrix_modular_inverse(self.kmatrix, 26)
        except:
            return "Key matrix is not invertible, you can't use this key\n"
        self.kmatrix = list(self.kmatrix)
        self.kmatrix = np.array(self.kmatrix).reshape(dim, dim)
        # Multiply n-grams with key matrix in modulo 26
        for row in self.cmatrix:
            row = np.array([alpha[letter] for letter in row])
            row = np.matmul(row, self.kmatrix)
            row = row % 26
            for element in row:
                self.pmatrix.append(element)
        # Convert ciphertext matrix to ciphertext
        for letter in self.pmatrix:
            letter = list(alpha.keys())[list(alpha.values()).index(letter)]
            self.plaintext += letter

        return f"This is your message: {self.plaintext}\n"


def menu():
    print("--------------------------")
    print("xX Hill Cipher Xx")
    print("--------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("--------------------------")


def main():
    while True:
        menu()
        hill = Hill()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            dim = int(input("Enter dimension of the key matrix: "))
            plaintext = input("Enter plaintext: ").upper()
            key = input("Enter key: ").upper()
            cipher = hill.encrypt(plaintext, key, dim)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            dim = int(input("Enter dimension of the key matrix: "))
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
# 2

# Ciphertext
# VKFZRVWTIAZSMISGKA

# Key
# LIDH

# Message
# NUMBERTHEORYISEASY


# Example 3

# Dimension
# 3

# Ciphertext
# BCBAIECPSSYNRNAMACDSMEIIPVDBPL

# Key
# GYBNQKURP

# Message
# THISISHILLWITHBIGGERKEYMATRIXX
