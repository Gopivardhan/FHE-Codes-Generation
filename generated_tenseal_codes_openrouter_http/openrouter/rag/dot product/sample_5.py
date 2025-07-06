```
import tenseal as ts

# Create a CKKS context
context = ts CKKSContext(
    poly_modulus_degree=[4096, 4096],
    coeff_modulus=[8192, 8192, 8192],
    scale=2**40,
    precision_bits=60,
    mode='CKKS'
)

# Generate two vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6])
vec2 = ts.ckks_vector(context, [4, 3, 2, 1, 0, 1])

# Perform CKKS dot product
result = ts.dot(vec1, vec2)

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
```