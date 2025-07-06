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
vec1 = [1.0, 2.0, 3.0, 4.0]
vec2 = [5.0, 6.0, 7.0, 8.0]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform encrypted addition
encrypted_result = encrypted_vec1 + encrypted_vec2

# Decrypt result
decrypted_result = encrypted_result.decrypt()

# Print result
print(decrypted_result)
