import tenseal as ts

# Initialize the CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-25),
    precision=11,
    mode=ts.CKKSMode.GALILEO
)

# Initialize the CKKS context for encryption
ckks_context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-25),
    precision=11,
    mode=ts.CKKSMode.GALILEO
)

# Encrypting the input matrix
A = ts.ckks_vector(ckks_context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
B = ts.ckks_vector(ckks_context, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

# Encrypting the input matrix for the second matrix
C = ts.ckks_vector(ckks_context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
D = ts.ckks_vector(ckks_context, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])

# Matrix multiplication
E = A * B
F = C * D

# Decrypting the result
result1 = E.decrypt()
result2 = F.decrypt()

# Printing the result
print(result1)
print(result2)