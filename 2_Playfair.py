# Playfair Cipher
# The key is put into a 5x5 matrix without repeating any letters.
# The matrix is filled with the remaining letters of the alphabet.
# The letters of the plaintext are put into pairs.
# If a pair has the same letter, an X is inserted between them.
# If the plaintext has an odd number of letters, an X is added at the end.
# For each pair, the letters are encrypted using the following rules:
# If the letters are in the same column, replace each letter with the letter below it.
# If the letters are in the same row, replace each letter with the letter to its right.
# Else replace each letter with the letter in the same row but in the other column of the pair.
# The ciphertext is formed by joining the encrypted pairs.


# Implementation
class Playfair:
    def __init__(self):
        self.plaintext = ""
        self.ciphertext = ""

    def encrypt(self, plaintext, key):
        # Create key matrix
        matrix = self.matrix(key)
        # Separe plaintext into pairs
        plaintext = plaintext.replace("J", "I").replace(" ", "")
        text = list(plaintext)
        pairs = []
        for i in range(0, len(text), 2):
            if i < len(text) - 1 and text[i] == text[i + 1]:
                text.insert(i + 1, "X")
        result = "".join(text)

        if len(result) % 2 != 0:
            result += "X"
        # Create pairs
        for i in range(0, len(result), 2):
            pairs.append(result[i] + result[i + 1])
        # Encrypt
        for pair in pairs:
            # Get coordinates of each letter
            coor = self.get_coordinates(pair, matrix)
            # Check if letters are in the same column
            if coor[1] == coor[3]:
                self.ciphertext += matrix[(coor[0] + 1) % 5][coor[1]]
                self.ciphertext += matrix[(coor[2] + 1) % 5][coor[3]]
            # Check if letters are in the same row
            elif coor[0] == coor[2]:
                self.ciphertext += matrix[coor[0]][(coor[1] + 1) % 5]
                self.ciphertext += matrix[coor[2]][(coor[3] + 1) % 5]
            # If not, form a rectangle
            else:
                self.ciphertext += matrix[coor[0]][coor[3]]
                self.ciphertext += matrix[coor[2]][coor[1]]

        return f"This is your encrypted message: {self.ciphertext}\n"

    def decrypt(self, ciphertext, key):
        matrix = self.matrix(key)
        ciphertext = ciphertext.replace("J", "I").replace(" ", "")
        text = list(ciphertext)
        # Create pairs
        pairs = []
        for i in range(0, len(text), 2):
            pairs.append(text[i] + text[i + 1])
        # Decrypt
        for pair in pairs:
            # Get coordinates of each letter
            coor = self.get_coordinates(pair, matrix)
            # Check if letters are in the same column
            if coor[1] == coor[3]:
                self.ciphertext += matrix[(coor[0] - 1) % 5][coor[1]]
                self.ciphertext += matrix[(coor[2] - 1) % 5][coor[3]]
            # Check if letters are in the same row
            elif coor[0] == coor[2]:
                self.ciphertext += matrix[coor[0]][(coor[1] - 1) % 5]
                self.ciphertext += matrix[coor[2]][(coor[3] - 1) % 5]
            # If not, form a rectangle
            else:
                self.ciphertext += matrix[coor[0]][coor[3]]
                self.ciphertext += matrix[coor[2]][coor[1]]

        return f"This is your message: {self.ciphertext}\n"

    def matrix(self, key):
        # Eliminate duplicate letters
        key = key.upper().replace("J", "I").replace(" ", "")
        new_key = ""
        for letter in key:
            if letter not in new_key:
                new_key += letter
        # Complete key with alphabet
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        for letter in alphabet:
            if letter not in new_key:
                new_key += letter
        # Fill matrix with key
        k = 0
        matrix = [[0 for x in range(5)] for y in range(5)]
        for i in range(5):
            for j in range(5):
                matrix[i][j] = new_key[k]
                k += 1

        return matrix

    def get_coordinates(self, pair, matrix):
        coor = []
        for i in range(5):
            for j in range(5):
                if pair[0] == matrix[i][j]:
                    coor.append(i)
                    coor.append(j)
        for i in range(5):
            for j in range(5):
                if pair[1] == matrix[i][j]:
                    coor.append(i)
                    coor.append(j)

        return coor


def menu():
    print("--------------------------")
    print("xX Playfair Cipher Xx")
    print("--------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("--------------------------")


def main():
    while True:
        menu()
        pfair = Playfair()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            key = input("Enter key: ")
            cipher = pfair.encrypt(plaintext, key)
            print(cipher)
            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            key = input("Enter key: ")
            message = pfair.decrypt(ciphertext, key)
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
# this secret message is encrypted

# Key
# yoanpiz

# Cipher message
# WE DL LK HW LY LF XP QP HF DL HY HW OY YL KP


# Example 2

# Cipher message
# ZO MH LC HY ZK MN SO NQ DL KT OQ CY KI EC LK SO YI EQ PQ RX EY KR WM NS DL GY LD GF AB YA QN YE AP GN IX PG HY YS NB HT EC TL KF VN RP YT PU PF CY EB YA WM KI MP LF UZ LH TC YH NP CK KL LY YT KI GB DH CY EC RD GN CL GO IH YE TY KI XO UY VN SC LX KF MX PW

# Key
# yoanpiz

# Message
# OUR FRIEND FROM PARIS EXAMINED HIS EMPTY GLASS WITH SURPRISE AS IF EVAPORATION HAD TAKEN PLACE WHILE HE WASNT LOXOKING I POURED SOME MORE WINE AND HE SETTLED BACK IN HIS CHAIR FACE TILTED UP TOWARDS THE SUNX
