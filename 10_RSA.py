# RSA (Rivest-Shamir-Adleman) Cipher
# Is an example of asymmetic or public key cryptography
# Public keys can be given to anyone
# Private key must remain secret
# The algorithm is based on prime factorization
# The security of RSA relies on the fact that it is easy to multiply large numbers, but it is extremely difficult to factor their product

# The algorithm is the following:
# Choose two distinct prime numbers p and q
# Compute n = pq
# Compute the totient of n, phi(n) = (p - 1)(q - 1)
# Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
# Compute d such that de = 1 (mod phi(n))
# The public key is (n, e) and the private key is (n, d)
# Encryption: c = m^e (mod n)
# Decryption: m = c^d (mod n)
# Where m is the plaintext message and c is the ciphertext message


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
import random
import math


class RSA:
    def __init__(self, bits=64):
        self.bits = bits
        self.public_key, self.private_key = self.generate_keys(bits)

    def generate_keys(self, bits):
        p = self.generate_prime(bits)
        q = self.generate_prime(bits)
        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = self.choose_public_key(phi_n)
        d = self.calculate_private_key(e, phi_n)
        public_key = (n, e)
        private_key = (n, d)
        return public_key, private_key

    def generate_prime(self, bits):
        while True:
            num = random.getrandbits(bits)
            if self.is_prime(num):
                return num

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    def choose_public_key(self, phi_n):
        e = random.randint(2, phi_n - 1)
        while math.gcd(e, phi_n) != 1:
            e = random.randint(2, phi_n - 1)
        return e

    def calculate_private_key(self, e, phi_n):
        d = self.modular_inverse(e, phi_n)
        return d

    def modular_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1

    def encrypt(self, plaintext):
        n, e = self.public_key
        ciphertext = [pow(ord(char), e, n) for char in plaintext]
        return ciphertext

    def decrypt(self, ciphertext):
        n, d = self.private_key
        decrypted_text = "".join([chr(pow(char, d, n)) for char in ciphertext])
        return decrypted_text


def menu():
    print("xX RSA Cipher Xx")
    print("------------------------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    print("------------------------")


def main():
    while True:
        menu()
        rsa = RSA()
        choice = input("Enter your choice: ")
        # Encrypt
        if choice == "1":
            plaintext = input("Enter plaintext: ").upper()
            cipher = rsa.encrypt(plaintext)
            print("Encrypted Message:", cipher)

            message = rsa.decrypt(cipher)
            print("Decrypted Message:", message)

            continue
        # Decrypt
        if choice == "2":
            ciphertext = input("Enter ciphertext: ").upper()
            message = rsa.decrypt(ciphertext)
            print("Decrypted Message:", message)
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
# hola

# Key
#

# Cipher message
# 326552601299438552565696261982604313796304008265332355237858209930907745
