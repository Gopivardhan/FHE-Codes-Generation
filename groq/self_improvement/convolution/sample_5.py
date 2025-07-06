import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [8, 7, 6, 5, 4, 3, 2, 1]

# Encrypt the vectors
enc_vec1 = ts.ckks_vector(context, vec1)
enc_vec2 = ts.ckks_vector(context, vec2)

# Perform the encrypted convolution operation
result = enc_vec1.convolve(enc_vec2)

# Decrypt the result
dec_result = result.decrypt().values

# Print the final output
print(dec_result)
