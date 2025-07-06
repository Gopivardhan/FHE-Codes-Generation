import tenseal as ts

# Set up the context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale and generate Galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Encrypt the vectors
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform matrix multiplication on the encrypted vectors
result = encrypted_vector1 @ encrypted_vector2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the decrypted result
print(decrypted_result)
