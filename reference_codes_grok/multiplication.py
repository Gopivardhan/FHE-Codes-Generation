import tenseal as ts

# Setup TenSEAL context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2**40

# Input vectors
v1 = [0, 1, 2, 3, 4]
v2 = [4, 3, 2, 1, 0]

# Encrypt vectors
enc_v1 = ts.ckks_vector(context, v1)
enc_v2 = ts.ckks_vector(context, v2)

# Element-wise multiplication
result = enc_v1 * enc_v2
print("Element-wise Multiplication Result:", result.decrypt())  # ~ [0, 3, 4, 3, 0]
