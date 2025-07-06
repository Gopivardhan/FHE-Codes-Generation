import tenseal as ts

# Set up the context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set global scale and generate galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define the vectors
vector1 = [1, 2, 3, 4, 5]
vector2 = [6, 7, 8, 9, 10]

# Encrypt the vectors
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform convolution
encrypted_convolution = encrypted_vector1 * encrypted_vector2

# Decrypt the convolution
decrypted_convolution = encrypted_convolution.decrypt()

# Perform element-wise multiplication to get the actual convolution result
convolution_result = [x * y for x, y in zip(decrypted_convolution, decrypted_convolution)]

# Print the result
print(convolution_result)
