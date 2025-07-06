import tenseal as ts
import numpy as np

# Initialize context
context = ts.context(scheme=ts.schemeCKKS, poly_mod_degree=128, coeff_mod_bit_size=60)

# Generate two random vectors
vec1 = ts.ckks_vector.from_numpy(context, np.random.rand(1000))
vec2 = ts.ckks_vector.from_numpy(context, np.random.rand(1000))

# Add the vectors
result = vec1 + vec2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)