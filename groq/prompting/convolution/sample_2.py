import tenseal as ts

# Create CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set global scale and generate Galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define vectors
vec1 = [1, 2, 3, 4, 5]
vec2 = [6, 7, 8, 9, 10]

# Encrypt vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform convolution operation
convolution_result = encrypted_vec1.convolution(encrypted_vec2)

# Decrypt convolution result
decrypted_convolution_result = convolution_result.decrypt()

# Compute final result
final_result = sum(decrypted_convolution_result)

print(final_result)
