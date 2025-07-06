import tenseal as ts

# Initialize CKKS context
context = ts.context(
    scheme=ts.scheme.CKKS,
    poly_modulus_degree=4096,
    scale=2**(-24),
    precision=11,
    mode=ts.contextMode.GF2^2
)

# Initialize CKKS context
context.generate_galois_keys()
context.generate_ring_elements()

# Define two integers to be encrypted
a = 123
b = 456

# Encrypt the integers
a_enc = ts.ckks_vector.from_py(context, [a])
b_enc = ts.ckks_vector.from_py(context, [b])

# Perform multiplication
result_enc = a_enc * b_enc

# Decrypt the result
result = result_enc.get_plain()

print(result)