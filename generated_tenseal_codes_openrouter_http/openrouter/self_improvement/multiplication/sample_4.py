```
import tenseal as ts

# Initialize CKKS context
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=4096, scale=2**40)
context.set_relaxation_values(15, 15, 8)
context.generate_public_key()
context.generate_secret_key()

# Create CKKS vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Encrypt vectors
enc_vec1 = vec1.encrypt()
enc_vec2 = vec2.encrypt()

# Perform multiplication
mul_result = enc_vec1 * enc_vec2

# Decrypt result
dec_result = mul_result.decrypt()

# Print result
print(dec_result)
```