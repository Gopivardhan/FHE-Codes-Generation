
import tenseal as ts

# Initialize the context
context = ts.context(
    poly_modulus_degree=4096,
    coeff_modulus=[2**64, 2**64],
    scale=2**40,
    precision=40,
    evaluate=True,
    generate_keys=True
)

# Generate public and secret key
public_key = context.secret_key
secret_key = context.secret_key

# Create two random vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [2, 3, 4, 5, 6])

# Multiply the vectors
encrypted_result = vec1 * vec2

# Decrypt the result
decrypted_result = ts.ckks_vector.decrypt(context, encrypted_result, public_key)

# Print the result
print(decrypted_result)
