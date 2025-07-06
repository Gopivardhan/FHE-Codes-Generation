import tenseal as ts

# Set up the context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Configure the global scale
context.global_scale = 2**40

# Generate Galois keys
context.generate_galois_keys()

# Define two vectors to encrypt
vector1 = [1, 2, 3, 4]
vector2 = [5, 6, 7, 8]

# Encrypt the vectors
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform the multiplication operation
encrypted_product = encrypted_vector1 * encrypted_vector2

# Decrypt the result
decrypted_product = encrypted_product.decrypt()

# Print the output
print(decrypted_product)
