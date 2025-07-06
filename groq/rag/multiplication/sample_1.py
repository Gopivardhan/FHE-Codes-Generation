import tenseal as ts

# Set up context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Define vectors to encrypt
vec1 = [1, 2, 3, 4]
vec2 = [5, 6, 7, 8]

# Encrypt vectors
enc_vec1 = ts.ckks_vector(context, vec1)
enc_vec2 = ts.ckks_vector(context, vec2)

# Multiply encrypted vectors
result = enc_vec1 * enc_vec2

# Decrypt result
dec_result = result.decrypt()

# Print result
print(dec_result)
