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
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted convolution operation
encrypted_conv = encrypted_vec1.convolve(encrypted_vec2)

# Decrypt the result
decrypted_conv = encrypted_conv.decrypt()

# Print the final output
print(decrypted_conv)
