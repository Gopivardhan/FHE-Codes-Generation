import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale
context.global_scale = 2**40

# Generate the galois keys
context.generate_galois_keys()

# Define two vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [9, 10, 11, 12, 13, 14, 15, 16]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Create a matrix by repeating the vectors
matrix = [[encrypted_vec1[i * 4 + j] for j in range(4)] for i in range(2)]
vector = [[encrypted_vec2[i]] for i in range(8)]

# Perform the encrypted matrix multiplication
result = ts.ckks_matrix_multiply(context, matrix, vector)

# Decrypt the result
decrypted_result = result.decrypt()

# Compute the final result
final_result = sum(sum(row) for row in decrypted_result)

# Print the final result
print(final_result)
