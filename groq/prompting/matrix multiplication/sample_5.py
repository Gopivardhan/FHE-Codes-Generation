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

# Define vectors
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]
vec3 = [7, 8, 9]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)
encrypted_vec3 = ts.ckks_vector(context, vec3)

# Create encrypted matrices
encrypted_matrix1 = encrypted_vec1 * encrypted_vec2
encrypted_matrix2 = encrypted_vec2 * encrypted_vec3

# Perform encrypted matrix multiplication
encrypted_result = encrypted_matrix1 * encrypted_matrix2

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Compute the final result
final_result = sum(sum(row) for row in decrypted_result)
