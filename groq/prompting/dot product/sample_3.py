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
vec1 = [1, 2, 3, 4, 5]
vec2 = [6, 7, 8, 9, 10]

# Encrypt the vectors
enc_vec1 = ts.ckks_vector(context, vec1)
enc_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted dot product operation
dot_product = ts.dot_product(enc_vec1, enc_vec2)

# Decrypt the dot product result
dec_dot_product = dot_product.decrypt()

# Compute the final result
result = sum(dec_dot_product)
print(result)
