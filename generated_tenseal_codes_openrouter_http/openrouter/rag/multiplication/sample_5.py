```
import tenseal as ts

# Create CKKS context
context = ts.ckks_context(scheme='bfv', poly_modulus_degree=4096, coeff_mod_bit_sizes=[30, 30, 30, 30, 30])

# Create CKKS vectors
vec1 = ts.ckks_vector.from_float_vector([1, 2, 3, 4, 5], context)
vec2 = ts.ckks_vector.from_float_vector([6, 7, 8, 9, 10], context)

# Encrypt vectors
enc_vec1 = vec1.encrypt()
enc_vec2 = vec2.encrypt()

# Perform CKKS multiplication
mul_enc_vec = enc_vec1 * enc_vec2

# Decrypt result
dec_mul_vec = mul_enc_vec.decrypt()

# Print result
print(dec_mul_vec.get_float_data())
```