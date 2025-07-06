import tenseal as ts

# Create a CKKS context
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    degree=256,
    precision=30,
    security_level=128
)

# Generate a random plaintext vector
plaintext = ts.ckks_vector.random(context, 4)

# Encrypt the plaintext
encrypted = context.encrypt(plaintext)

# Create a convolution matrix
convolution_matrix = ts.ckks_matrix.random(context, (4, 4))

# Perform CKKS convolution
result = context.convolution(convolution_matrix, encrypted)

# Decrypt the result
decrypted = context.decrypt(result)

# Print the result
print(decrypted)