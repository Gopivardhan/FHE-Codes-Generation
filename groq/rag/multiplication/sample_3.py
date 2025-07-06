import tenseal as ts

# Set up the context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale
context.global_scale = 2**40

# Generate the Galois keys
context.generate_galois_keys()

# Create two vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [8, 7, 6, 5, 4, 3, 2, 1]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted multiplication operation
encrypted_result = encrypted_vec1 * encrypted_vec2

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the output
print(decrypted_result)
