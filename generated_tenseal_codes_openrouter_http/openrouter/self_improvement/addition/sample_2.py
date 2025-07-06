import tenseal as ts

# Initialize CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**23,
    precision=23,
    coeff_modulus=[
        ts.Modulus(2**64),
        ts.Modulus(2**64)
    ]
)

# Create CKKS context
context.generate_galois_keys()
context.generate_noise_budget()

# Encrypt the vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform addition
result = vec1 + vec2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)