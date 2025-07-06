```
import tenseal as ts

# Create a CKKS context
context = ts CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-40),
    precision=30,
    mode=ts.BaseContext.CKKS
)

# Create two vectors
v1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
v2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Encrypt the vectors
encrypted_v1 = v1.encrypt()
encrypted_v2 = v2.encrypt()

# Perform CKKS matrix multiplication
result = encrypted_v1 * encrypted_v2

# Decrypt the result
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)
```