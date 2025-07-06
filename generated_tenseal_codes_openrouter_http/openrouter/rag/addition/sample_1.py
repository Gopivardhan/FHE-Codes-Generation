
import tenseal as ts

# Create CKKS context
context = ts.context(ts.SCHEME_TYPE.CKKS, 12, 64)
context.generate_galois_keys()
context.global_scale = 2**20

# Create CKKS vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
vec2 = ts.ckks_vector(context, [5, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6])

# Perform CKKS addition
result = vec1 + vec2

# Decrypt result
decrypted_result = result.decrypt()

# Print result
print(decrypted_result)
