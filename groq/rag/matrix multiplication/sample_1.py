import tenseal as ts
import numpy as np

# Set up context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

# Define two vectors
vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Encrypt the vectors
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Define the matrix
matrix = np.array([[7, 8], [9, 10]])

# Encrypt the matrix
encrypted_matrix = ts.ckks_matrix(context, matrix)

# Perform matrix multiplication
encrypted_result = encrypted_matrix * encrypted_vector1

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Perform additional operations (e.g., vector-matrix multiplication)
result = decrypted_result + ts.ckks_vector(context, vector2)

# Print the output
print(result.decrypt())
