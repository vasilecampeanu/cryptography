# Probleme cu algoritmul asta. Nu functioneaza.

from typing import List

# Algoritm multiplicare matrici
def matrix_multiply(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if len(A[0]) != len(B):
        raise ValueError("Invalid matrices!")

    result = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Algoritm inversare matrice
def matrix_inverse(A: List[List[int]]) -> List[List[int]]:
    # calculam determinantul
    det = matrix_determinant(A)
    if det == 0:
        return None
    
    # Calculam matricea adjuncta
    adjoint = matrix_adjoint(A)
    
    # Determinam in final inversa
    inverse = [[adj // det for adj in row] for row in adjoint]
    
    return inverse

# Minor:
# [a, b, c]
# [d, e, f]   -->   [e, f]
# [g, h, i]         [h, i]
# Folosit in calcularea determinantului
def minor(A: List[List[int]], i: int, j: int) -> List[List[int]]:
    return [row[:j] + row[j+1:] for row in A[:i] + A[i+1:]]

# Calculam determinantul
def matrix_determinant(A: List[List[int]]) -> int:
    if len(A) != len(A[0]):
        raise ValueError("Matrix is not square!")

    if len(A) == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]
    det = 0
    for i in range(len(A)):
        det += (-1) ** i * A[0][i] * matrix_determinant(minor(A, 0, i))
    return det

# Matricea adjuncta
def matrix_adjoint(A: List[List[int]]) -> List[List[int]]:
    if len(A) != len(A[0]):
        raise ValueError("Matrix is not square!")
    
    if len(A) == 2:
        return [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]

    adjoint = []
    for i in range(len(A)):
        row = []
        for j in range(len(A)):
            minor = minor(A, i, j)
            row.append((-1) ** (i + j) * matrix_determinant(minor))
        adjoint.append(row)
    return adjoint

# Algoritmul de decriptare
def hill_cipher_decrypt(ciphertext: str, key: List[List[int]]) -> str:
    # Calculam inversa keii
    key_inverse = matrix_inverse(key)
    if not key_inverse:
        raise ValueError("Key matrix is not invertible!")
    
    # Divide the ciphertext into blocks of length equal to the key size
    ciphertext_matrix = [
        [ord(c) - ord('A') for c in ciphertext[i:i+len(key)]]
        for i in range(0, len(ciphertext), len(key))
    ]
    
    # Decriptam fiecare bloc
    plaintext = ""
    for block in ciphertext_matrix:
        block_matrix = [[c] for c in block]
        decrypted_block_matrix = matrix_multiply(key_inverse, block_matrix)
        plaintext += "".join([chr((c[0] % 26) + ord('A')) for c in decrypted_block_matrix])
    
    return plaintext

key = [[5, 8], [17, 3]]
decrypted = hill_cipher_decrypt("PBNMSE", key)
print(decrypted)
