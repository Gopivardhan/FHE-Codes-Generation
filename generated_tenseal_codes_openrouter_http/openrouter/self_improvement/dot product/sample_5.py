```
import tenseal as ts

# Initialize CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096, 
    scale=2**(-25), 
    precision=11, 
    mode=ts.CKKSContext.Mode.GSW
)

# Encrypt input vectors
v1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
v2 = ts.ckks_vector(context, [2, 4, 6, 8, 10])

# Perform dot product
result = v1 * v2

# Decrypt result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
```