import tenseal as ts

context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-25),
    precision=25
)

context.global_scale = 2**25

# Initialize plaintext
a = ts.ckks_vector(context, [1, 2, 3, 4])
b = ts.ckks_vector(context, [5, 6, 7, 8])

# Encrypt
a_enc = a.encrypt()
b_enc = b.encrypt()

# Perform multiplication
c_enc = a_enc * b_enc

# Decrypt
c = c_enc.decrypt()

print(c)