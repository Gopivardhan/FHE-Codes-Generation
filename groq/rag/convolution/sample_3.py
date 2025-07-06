import tenseal as ts

# Set up the context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set the global scale and generate the Galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define the vectors
vec1 = [1, 2, 3, 4, 5]
vec2 = [6, 7, 8, 9, 10]

# Encrypt the vectors
encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

# Perform the convolution operation
convolution = encrypted_vec1.convolute(encrypted_vec2)

# Decrypt the result
decrypted_convolution = convolution.decrypt()

# Print the output
print(decrypted_convolution)
