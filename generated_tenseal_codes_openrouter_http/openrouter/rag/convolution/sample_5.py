
import tenseal as ts

# Create CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-24),
    precision=25,
    coeff_mod_bit_sizes=[30, 30]
)

# Create CKKS context
ckks_context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-24),
    precision=25,
    coeff_mod_bit_sizes=[30, 30]
)

# Create two vectors to perform convolution
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [5, 4, 3, 2, 1])

# Perform convolution
conv = ts.ckks_vector(context)
conv = ts.convolution(conv, vec1, vec2)

# Decrypt and print result
decrypted = conv.decrypt()
print(decrypted)
