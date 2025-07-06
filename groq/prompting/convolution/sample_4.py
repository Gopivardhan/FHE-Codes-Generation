import tenseal as ts

# Create CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)

# Set global scale and generate galois keys
context.global_scale = 2**40
context.generate_galois_keys()

# Define vectors
vec1 = [1, 2, 3, 4, 5, 6, 7, 8]
vec2 = [8, 7, 6, 5, 4, 3, 2, 1]

# Encrypt vectors
enc_vec1 = ts.ckks_vector(context, vec1)
enc_vec2 = ts.ckks_vector(context, vec2)

# Perform convolution
convolution = ts.ckks_vector(context, [0] * 8)
for i in range(8):
    for j in range(8):
        convolution[i] += enc_vec1[i] * enc_vec2[j]

# Decrypt and compute final result
dec_convolution = convolution.decrypt()
final_result = sum(dec_convolution)
