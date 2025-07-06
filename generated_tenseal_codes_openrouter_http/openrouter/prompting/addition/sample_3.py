
import tenseal as ts

# Set up context with default parameters
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    number_bits=64,
    security_level=128,
    mode=ts.MODE.GALOIS
)

# Generate keys
context.generate_galois_keys()

# Create CKKS vector with secret data
plain_data = ts.ckks_vector(context, [1, 2, 3, 4, 5])

# Encrypt the vector
encrypted_data = plain_data.encrypt(context)

# Perform CKKS addition
encrypted_data += encrypted_data

# Decrypt the result
decrypted_result = encrypted_data.decrypt(context)

# Print the result
print(decrypted_result)