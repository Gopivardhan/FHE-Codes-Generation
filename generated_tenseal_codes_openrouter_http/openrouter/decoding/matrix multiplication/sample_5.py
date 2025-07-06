
import tenseal as ts
import numpy as np

# Initialize context
context = ts.context(scheme=ts.Scheme.FHE,
                     poly_modulus_degree=4096,
                     coefficient_modulus=[2**16, 2**16],
                     scale=2**40)

# Set the context to the specified mode
context.global_scale = 2**40

# Create a CKKS vector
vec1 = ts.ckks_vector(context, np.random.rand(1000).astype(np.float32))
vec2 = ts.ckks_vector(context, np.random.rand(1000).astype(np.float32))

# Perform matrix multiplication
result = vec1 * vec2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)