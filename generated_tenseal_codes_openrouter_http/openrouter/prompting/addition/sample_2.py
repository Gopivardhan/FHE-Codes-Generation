import tenseal as ts

# Setup context
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    number_of_bits=256,
    precision=30
)

# Generate keys
public_key = context.generate_public_key()
private_key = context.generate_secret_key()

# Create CKKS vector
plaintext = ts.ckks_vector(context, [1, 2, 3])

# Encrypt the vector
encrypted = public_key.encrypt(plaintext)

# Perform CKKS addition
encrypted_add = encrypted + encrypted

# Decrypt the result
decrypted = private_key.decrypt(encrypted_add)

# Print the result
print(decrypted)