import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale and generate Galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vec1 = [1, 2, 3, 4]
vec2 = [5, 6, 7, 8]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Define the encrypted matrix
encrypted_matrix = [[ts.ckks_vector(context, [1, 2]) for _ in range(2)] for _ in range(2)]

# Perform the encrypted matrix multiplication
encrypted_result = ts.ckks_matrix_multiply(context, encrypted_matrix, encrypted_vec1, encrypted_vec2)

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Compute the final result
final_result = sum(sum(row) for row in decrypted_result)

print(final_result)
