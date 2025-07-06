```
import tenseal as ts

# Initialize the CKKS context
context = ts.context(ts.LWEParameters(
    poly_modulus_degree=4096,
    coefficient_modulus=[8192],
    scale=1.0,
    security_level=128
))
context.generate_galois_keys()
context.generate_psycho_keys()

# Create two vectors to perform convolution
v1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
v2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Perform convolution
v3 = v1 * v2

# Decrypt and print the result
print(v3.decrypt())
```