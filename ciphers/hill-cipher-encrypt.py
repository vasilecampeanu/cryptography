# Am verificat daca criptarea este corecta folosind:
# https://www.dcode.fr/hill-cipher

from typing import List

# Algoritm de multiplicare a matricilor.
def matrix_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A[0]) != len(B):
        raise ValueError("Invalid matrices!")

    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# List[List[int]] -> Este un tip in python folosit pentru a semnala o lista de liste de integrale.
def hill_cipher(plaintext: str, key: List[List[int]]) -> str:
    
    # Calculam ASCII
    plaintext_matrix = [
        [ord(c) - ord('A') for c in plaintext[i:i+len(key)]]
        for i in range(0, len(plaintext), len(key))
    ]

    if len(plaintext_matrix[-1]) < len(key):
        plaintext_matrix[-1] += [0] * (len(key) - len(plaintext_matrix[-1]))

    # Varaibila asta stocheaza textul criptat
    ciphertext = ""

    # Criptam fiecare block
    for block in plaintext_matrix:
        block_matrix = [[c] for c in block]
        encrypted_block_matrix = matrix_multiply(key, block_matrix)
        ciphertext += "".join([chr((c[0] % 26) + ord('A')) for c in encrypted_block_matrix])

    return ciphertext

key = [[5, 8], [17, 3]]
ciphertext = hill_cipher("HELLO", key)
print(ciphertext)
