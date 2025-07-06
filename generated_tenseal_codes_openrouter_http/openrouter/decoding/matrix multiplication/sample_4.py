
import tenseal as ts
import numpy as np

# Initialize context
context = ts.context(scheme=ts.Scheme.FHE,
                     poly_modulus_degree=4096,
                     mode=ts.OperationMode.GFWT)

# Generate two random 2x2 matrices
A = np.random.rand(2, 2)
B = np.random.rand(2, 2)

# Encrypt matrices
A_ckks = ts.ckks_vector(context, A)
B_ckks = ts.ckks_vector(context, B)

# Perform matrix multiplication
C_ckks = A_ckks * B_ckks

# Decrypt result
C = C_ckks.decrypt()

# Print result
print(C)
