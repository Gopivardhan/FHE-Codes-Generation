import tenseal as ts

# Setup TenSEAL context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2**40

# Input vector and matrix
v1 = [0, 1, 2, 3, 4]
matrix = [
    [73, 0.5, 8],
    [81, -5, 66],
    [-100, -78, -2],
    [0, 9, 17],
    [69, 11, 10]
]

# Encrypt the vector
enc_v1 = ts.ckks_vector(context, v1)

# Matrix multiplication
result = enc_v1.matmul(matrix)
print("Matrix Multiplication Result:", result.decrypt())  # ~ [157, -90, 153]
