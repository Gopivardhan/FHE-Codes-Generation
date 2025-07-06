
import tenseal as ts
import numpy as np

# Set up the context
context = ts.context(ts.SCHEME_TYPE.CKKS, 12, 351)
context.global_scale = 2**20
context.generate_galois_keys()

# Create two 2x2 matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Convert the matrices to CKKS vectors
encrypted_matrix1 = ts.ckks_vector(context, matrix1.flatten())
encrypted_matrix2 = ts.ckks_vector(context, matrix2.flatten())

# Perform the matrix multiplication
encrypted_result = encrypted_matrix1 * encrypted_matrix2

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the result
print(decrypted_result)
