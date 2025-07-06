```
import tenseal as ts

# Create CKKS context
context = ts.context(
    scale=2**15,
    poly_modulus_degree=4096,
    coeff_mod_bit_sizes=[30, 30, 30, 30, 30, 30]
)

# Create CKKS vectors
a = ts.ckks_vector.from_float(context, [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
b = ts.ckks_vector.from_float(context, [7.0, 8.0, 9.0, 10.0, 11.0, 12.0])

# Encrypt CKKS vectors
a_enc = a.encrypt()
b_enc = b.encrypt()

# Perform CKKS dot product
result_enc = a_enc.dot(b_enc)

# Decrypt the result
result_dec = result_enc.decrypt()

# Print the result
print(result_dec)