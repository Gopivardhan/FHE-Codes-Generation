
import tenseal as ts

# Initialize the context
context = ts.context(scheme=ts.scheme.FHE,
                     poly_modulus_degree=4096,
                     mode=ts.mode.GSW)

# Generate the public and secret keys
context.generate_galois_keys()
context.generate_secret_keys()

# Create two vectors
vector1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vector2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform matrix multiplication
result = vector1 * vector2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
