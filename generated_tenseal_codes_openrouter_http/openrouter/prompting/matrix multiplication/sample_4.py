import tenseal as ts

# Context setup
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    security_level=ts.SecurityLevel.SECURITY_DEFAULT,
    max_degree=12
)

# Key generation
context.generate_galois_keys()

# Encryption
plain_A = ts.ckks_vector(context, [1, 2, 3])
plain_B = ts.ckks_vector(context, [4, 5, 6])

# Encryption
encrypted_A = plain_A.encrypt()
encrypted_B = plain_B.encrypt()

# CKKS operation
encrypted_C = encrypted_A * encrypted_B

# Decryption
decrypted_C = encrypted_C.decrypt()

# Print the result
print(decrypted_C)
