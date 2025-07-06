
import tenseal as ts

# Create a CKKS context
context = ts.CKKS(
    poly_mod_count=4096,
    poly_mod_degree=8192,
    scheme=ts.SCHEME.FH,
    security=3
)

# Create a CKKS encoder
encoder = ts.CKKSVectorEncoder(context)

# Create a plaintext array
plaintext = [1, 2, 3, 4]

# Encrypt the plaintext array
encrypted = ts.ckks_vector(context, plaintext)

# Perform a convolution operation on the encrypted data
encrypted_convolution = ts.convolution(context, encrypted)

# Decrypt the convolution result
decrypted_convolution = ts.decrypt(context, encrypted_convolution)

# Print the decrypted result
print(decrypted_convolution)
