
import tenseal as ts
import numpy as np

# Initialize context
context = ts.context(
    scale=2**14,
    poly_mod_degree=4096,
    precision=64,
    noise_stddev=1.5,
    mode=ts.ContextMode.GPU
)

# Generate two random vectors
vector1 = np.random.rand(100).astype(np.float32)
vector2 = np.random.rand(100).astype(np.float32)

# Encrypt vectors
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform dot product
encrypted_result = encrypted_vector1 * encrypted_vector2

# Decrypt result
decrypted_result = encrypted_result.decrypt()

# Print result
print(decrypted_result)
