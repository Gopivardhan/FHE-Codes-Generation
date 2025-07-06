import tenseal as ts

# Set up the context
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

# Encrypt the vectors
enc_vec1 = ts.ckks_vector(context, vec1)
enc_vec2 = ts.ckks_vector(context, vec2)

# Perform the dot product operation
dot_product = enc_vec1.dot(enc_vec2)

# Decrypt the result
dec_dot_product = dot_product.decrypt()

# Print the output
print(dec_dot_product)
