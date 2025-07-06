
import tenseal as ts

# Initialize context
context = ts.context(scheme=ts.scheme.FHE, poly_modulus_degree=8192, mode=ts.mode.GFW)

# Set the scale for the context
context.set_scale(2**22)

# Generate the public key and secret key
public_key = context.global_public_key
secret_key = context.secret_key

# Create two CKKS vectors
v1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
v2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Encrypt the vectors
encrypted_v1 = v1.encrypt(public_key)
encrypted_v2 = v2.encrypt(public_key)

# Perform the dot product
result = encrypted_v1.dot(encrypted_v2)

# Decrypt the result
decrypted_result = result.decrypt(secret_key)

# Print the result
print(decrypted_result)