
import tenseal as ts

context = ts.context(
    scale_bits=70,
    poly_modulus_degree=4096,
    mode=ts.ContextMode.GPU_FPGA_OIL
)

context.generate_galois_keys()
context.generate_powers_of_two()

# Create two CKKS vectors
vector1 = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vector2 = ts.ckks_vector(context, [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# Encrypt vectors
encrypted_vector1 = vector1.encrypt()
encrypted_vector2 = vector2.encrypt()

# Perform dot product
dot_product = encrypted_vector1 * encrypted_vector2

# Decrypt result
decrypted_result = dot_product.decrypt()

print(decrypted_result)
