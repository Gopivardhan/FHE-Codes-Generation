import tenseal as ts

# Set up the context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Adjust the global scale
context.global_scale = 2**40

# Generate Galois keys
context.generate_galois_keys()

# Define two vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Encrypt the vectors
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform convolution operation on encrypted vectors
encrypted_convolution = encrypted_vector1.convolution(encrypted_vector2)

# Decrypt the result
decrypted_convolution = encrypted_convolution.decrypt()

# Perform vector multiplication to get the actual convolution result
convolution_result = [a * b for a, b in zip(decrypted_convolution, decrypted_convolution)]

# Print the output
print(convolution_result)
