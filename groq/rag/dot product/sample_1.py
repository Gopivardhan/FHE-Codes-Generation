import tenseal as ts

# Set up context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vec1 = [1, 2, 3, 4]
vec2 = [5, 6, 7, 8]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform dot product operation
encrypted_dot_product = encrypted_vec1 * encrypted_vec2

# Decrypt result
decrypted_dot_product = encrypted_dot_product.decrypt()

# Print output
print(decrypted_dot_product)
