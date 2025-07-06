```
import tenseal as ts
import numpy as np

# Initialize CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096, 
    scale=2**(-15), 
    precision=11
)

# Load the context
context.global_scale = 2**15
context.create_context()

# Define the matrices
A = np.random.rand(2, 2).astype(np.float32)
B = np.random.rand(2, 2).astype(np.float32)

# Encrypt the matrices
A_enc = ts.ckks_vector(context, A)
B_enc = ts.ckks_vector(context, B)

# Perform matrix multiplication
C_enc = A_enc @ B_enc

# Decrypt the result
C_dec = C_enc.decrypt()

# Print the result
print(C_dec)
```