
import tenseal as ts

# Set up the context
context = ts.context(scheme=ts.Scheme.CKKS, poly_mod_degree=4096, scale=2**40)
context.generate_galois_keys()
context.generate_public_key()

# Create a vector
plaintext = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Encrypt the vector
encrypted = ts.ckks_vector(context, plaintext)

# Create a convolutional kernel
kernel = [1, 2, 3]

# Perform the convolution
encrypted_result = encrypted.convolve(kernel)

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the result
print(decrypted_result)
