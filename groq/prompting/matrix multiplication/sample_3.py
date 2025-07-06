import tenseal as ts

# Create CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set global scale
context.global_scale = 2**40

# Generate galois keys
context.generate_galois_keys()

# Define vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [9, 10, 11, 12, 13, 14, 15, 16]
vec3 = [17, 18, 19, 20, 21, 22, 23, 24]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform encrypted matrix multiplication
result_encrypted = encrypted_vec1 * encrypted_vec2

# Decrypt result
result_decrypted = result_encrypted.decrypt()

# Define matrices
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

# Perform matrix multiplication
result_matrix = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]

# Multiply result matrix with vec3
result_encrypted_matrix = [ts.ckks_vector(context, row) for row in result_matrix]
result_decrypted_matrix = [vec.decrypt() for vec in result_encrypted_matrix]
result_final = [sum(a * b for a, b in zip(vec, vec3)) for vec in result_decrypted_matrix]

# Print final result
print(result_final)
