import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale and generate galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vec1 = [1, 2, 3, 4]
vec2 = [5, 6, 7, 8]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted matrix multiplication operation
encrypted_result = encrypted_vec1 * encrypted_vec2

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Compute the final result using plaintext operations
final_result = sum(decrypted_result)

# Print the final result
print(final_result)
