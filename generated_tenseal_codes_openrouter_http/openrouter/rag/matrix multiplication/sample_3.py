```
import tenseal as ts

# Create CKKS context
context = ts.ckks_context(
    poly_modulus_degree=4096,
    coeff_modulus=[8, 8],
    scale=2**23
)

# Create CKKS vector
a = ts.ckks_vector.from_py([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], context)
b = ts.ckks_vector.from_py([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], context)

# Encrypt vectors
a_enc = a.encrypted_vector(context)
b_enc = b.encrypted_vector(context)

# Perform CKKS matrix multiplication
c_enc = a_enc * b_enc

# Decrypt result
c = c_enc.decrypt()

# Print result
print(c)
```