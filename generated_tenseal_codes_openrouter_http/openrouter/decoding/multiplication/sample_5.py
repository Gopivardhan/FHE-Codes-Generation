
import tenseal as ts

# Initialize context
context = ts.context(scheme=ts.Scheme.FHE,
                     poly_modulus_degree=4096,
                     mode=ts.ContextMode.GPU)
context.generate_public_key()
context.generate_secret_key()

# Generate two random vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform multiplication
result = vec1 * vec2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
