import tenseal as ts

context = ts.context(scheme=ts.scheme_ckks, poly_mod_degree=4096, scale=2**30, precision=30)
context.generate_galois_keys()
context.generate_sk()

# Set the plaintext values
a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [2, 3, 4, 5, 6])

# Encrypt the plaintext values
a_enc = a.encrypt()
b_enc = b.encrypt()

# Perform the dot product
result_enc = a_enc.dot(b_enc)

# Decrypt the result
result_dec = result_enc.decrypt()

print(result_dec)