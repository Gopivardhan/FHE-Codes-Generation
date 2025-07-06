import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale and generate the Galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [8, 7, 6, 5, 4, 3, 2, 1]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted dot product operation
dot_product = encrypted_vec1.dot(encrypted_vec2)

# Decrypt the dot product result
decrypted_dot_product = dot_product.decrypt()

# Compute the final result using plaintext operations
final_result = sum(decrypted_dot_product)

# Print the final result
print(final_result)
