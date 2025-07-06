import tenseal as ts

# Create CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Define vectors
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform encrypted matrix multiplication
encrypted_result = encrypted_vec1.dot(encrypted_vec2)

# Decrypt result
decrypted_result = encrypted_result.decrypt()

# Compute final result
final_result = sum(decrypted_result)

print(final_result)
