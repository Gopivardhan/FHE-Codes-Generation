import tenseal as ts

# Create a CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set global scale and generate keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [9, 10, 11, 12, 13, 14, 15, 16]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform encrypted convolution operation
convolution = encrypted_vec1.convolution(encrypted_vec2)

# Decrypt the result
decrypted_convolution = convolution.decrypt()

# Compute the final result
result = sum(decrypted_convolution)
print(result)
