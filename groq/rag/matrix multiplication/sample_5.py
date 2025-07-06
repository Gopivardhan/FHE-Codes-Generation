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
vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

# Encrypt the vectors
enc_vec1 = ts.ckks_vector(context, vec1)
enc_vec2 = ts.ckks_vector(context, vec2)

# Define the matrix
matrix = [[7, 8], [9, 10]]

# Encrypt the matrix
enc_matrix = ts.ckks_matrix(context, matrix)

# Perform matrix multiplication
result = enc_matrix * enc_vec1 * enc_vec2

# Decrypt the result
dec_result = result.decrypt()

# Print the output
print(dec_result)
