```
import tenseal as ts

# Initialize CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096, 
    scale=2**(-25), 
    precision=11, 
    coeff_modulus=[2**31 - 1] * 4, 
    sec_level=True, 
    relin_type='auto', 
    mode='gsw'
)

# Generate and encrypt two vectors
v1 = ts.ckks_vector(context, [1, 2, 3])
v2 = ts.ckks_vector(context, [4, 5, 6])

# Perform addition
v3 = v1 + v2

# Decrypt the result
v3_plain = v3.decrypt()

# Print the result
print(v3_plain)
```