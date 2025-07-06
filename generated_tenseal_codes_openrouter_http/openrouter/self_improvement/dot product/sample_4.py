```
import tenseal as ts

# Initialize CKKS context
context = ts.context(
    scale=2**14,
    poly_mod_degree=256,
    mode=ts.ContextMode.GPU_FLEXIBLE
)

# Initialize CKKS context
context.generate_galois_keys()
context.generate_polynomial_modulus()

# Encrypt vectors
a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform dot product
c = a * b

# Decrypt result
decrypted_result = c.decrypt()

print(decrypted_result)
```