# Turing Grille Cipher
# Consists of a matrix with holes in it
# The holes are filled with plaintext


# Implementation
import numpy as np


class TuringGrille:
    def __init__(self):
        self.holeMatrix = []
        self.pMatrix = []
        self.cMatrix = []
        self.plaintext = ""
        self.ciphertext = ""

    def encrypt(self, plaintext, dim, mode):
        # Check if plaintext or key overpassed matrix dimension
        plaintext = plaintext.replace(" ", "")
        if len(plaintext) > (dim * dim):
            return "Plaintext overpassed matrix dimension\n"
        # Fill plaintext with X
        while len(plaintext) < (dim * dim):
            plaintext += "X"
        # Recive and check holes
        n = int(input("Insert the number of holes: "))
        holes = []
        while n > 0:
            hole = int(input("Enter position of hole: "))
            if hole > (dim * dim):
                print("Invalid position, try again")
                continue
            holes.append(hole - 1)
            n -= 1
        # Put holes in matrix
        self.holeMatrix = np.full((dim, dim), "")
        for element in holes:
            self.holeMatrix[element // dim][element % dim] = "X"
        # Fill matrix with plaintext
        self.pMatrix = np.full((dim, dim), "")
        pos = 0
        for k in range(4):
            for i in range(dim):
                for j in range(dim):
                    if self.holeMatrix[i][j] == "X":
                        self.pMatrix[i][j] = plaintext[pos]
                        pos += 1
            if mode == 1:
                self.holeMatrix = self.rotLeft(self.holeMatrix, dim)
            else:
                self.holeMatrix = self.rotRight(self.holeMatrix, dim)
        # Get ciphertext
        for i in range(dim):
            for j in range(dim):
                self.ciphertext += self.pMatrix[i][j]

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext, dim, mode):
        # Check if plaintext or key overpassed matrix dimension
        ciphertext = ciphertext.replace(" ", "")
        if len(ciphertext) > (dim * dim):
            return "Ciphertext overpassed matrix dimension\n"
        # Fill plaintext with X
        while len(ciphertext) < (dim * dim):
            ciphertext += "X"
        # Recive and check holes
        n = int(input("Insert the number of holes: "))
        holes = []
        while n > 0:
            hole = int(input("Enter position of hole: "))
            if hole > (dim * dim):
                print("Invalid position, try again")
                continue
            holes.append(hole - 1)
            n -= 1
        # Put holes in matrix
        self.holeMatrix = np.full((dim, dim), "")
        for element in holes:
            self.holeMatrix[element // dim][element % dim] = "X"
        print(self.holeMatrix)
        # Fill matrix with ciphertext
        self.cMatrix = np.full((dim, dim), "")
        pos = 0
        while pos < len(ciphertext):
            for i in range(dim):
                for j in range(dim):
                    self.cMatrix[i][j] = ciphertext[pos]
                    pos += 1
        print(self.cMatrix)

        # Get plaintext
        for k in range(4):
            for i in range(dim):
                for j in range(dim):
                    if self.holeMatrix[i][j] == "X":
                        self.plaintext += self.cMatrix[i][j]
            if mode == 1:
                self.holeMatrix = self.rotLeft(self.holeMatrix, dim)
            else:
                self.holeMatrix = self.rotRight(self.holeMatrix, dim)

        return f"This is your message: {self.plaintext}\n"


def menu():
    print("xX Turing Grille Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        tgrill = TuringGrille()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            dim = int(input("Enter dimension of matrix: "))
            mode = int(
                input(
                    "Enter direction of rotation (1 for left any other number for right): "
                )
            )
            plaintext = input("Enter plaintext: ").upper()
            cipher = tgrill.encrypt(plaintext, dim, mode)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            dim = int(input("Enter dimension of matrix: "))
            mode = int(
                input(
                    "Enter direction of rotation (1 for left any other number for right): "
                )
            )
            ciphertext = input("Enter ciphertext: ").upper()
            message = tgrill.decrypt(ciphertext, dim, mode)
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
# JIM ATTACKS AT DAWN

# Holes
# 4 holes
# 1 10 12 15

# Cipher message
# JKTDSAATWIAMCNAT (Left)
# JKDTSTAAAIWMNCAT (Right)


# Example 2

# Cipher message
# TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE X

# Holes
# 21 holes
# 1 4 6 12 18 20 25 30 32 35 41 43 45 49 53 55 60 65 68 72 75

# Message
# THISISAMESSAGETHATIAMENCRYPTINGSWITHATURNINGGRILLETOSPROVIDETHXSILLUSTRATSIVEEXAMPLE
