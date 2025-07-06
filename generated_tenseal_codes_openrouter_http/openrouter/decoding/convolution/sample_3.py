
import tenseal as ts

# Initialize context
context = ts.context(
    scale=2**15,
    poly_modulus_degree=4096,
    modulus=2**61-1,
    coeff_modulus=[2**61-1]*3,
    security_level=3
)
context.generate_galois_keys()
context.generate_gaussian_noise(stddev=1.0)

# Encrypt input vectors
x = ts.ckks_vector(context, [1, 2, 3, 4, 5])
y = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform convolution
result = ts.convolve(x, y)

# Decrypt result
decrypted_result = result.decrypt()

# Print result
print(decrypted_result)
