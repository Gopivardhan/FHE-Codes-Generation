import tenseal as ts

# Initialize the context
context = ts.context(
    poly_modulus_degree=4096,
    coeff_modulus=[2**21, 2**21],
    scale=2**(-51),
    security_level=128
)

# Set the context to the specified parameters
context.set_party_vector(0)

# Create two encrypted vectors
vec1 = ts.ckks_vector(context, [1, 2, 3])
vec2 = ts.ckks_vector(context, [4, 5, 6])

# Perform the addition operation
result = vec1 + vec2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the decrypted result
print(decrypted_result)