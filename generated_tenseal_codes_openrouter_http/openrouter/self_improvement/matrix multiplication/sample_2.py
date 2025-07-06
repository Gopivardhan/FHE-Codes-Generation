```
import tenseal as ts

# Initialize CKKS context
context = ts.context(ts.DKKT, 12, 64, 1 << 10)
context.set_poly_mod_coeffs([1] * 64)
context.generate_galois_keys()

# Generate random vectors
A = ts.ckks_vector(context, [10] * 64)
B = ts.ckks_vector(context, [10] * 64)

# Perform matrix multiplication
C = A * B

# Decrypt and print the result
print(C.decrypt())
```