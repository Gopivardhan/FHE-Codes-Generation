
import tenseal as ts

# Create CKKS context
context = ts.context(ts.LLWE, 2048, 64, 16, 32, 64)
context.generate_galois_keys()
context.generate_public_key()

# Create CKKS vectors
vec1 = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0])
vec2 = ts.ckks_vector(context, [5.0, 6.0, 7.0, 8.0])

# Encrypt CKKS vectors
enc_vec1 = vec1.encrypt()
enc_vec2 = vec2.encrypt()

# Perform CKKS addition
result = enc_vec1 + enc_vec2

# Decrypt result
dec_result = result.decrypt()

# Print result
print(dec_result)