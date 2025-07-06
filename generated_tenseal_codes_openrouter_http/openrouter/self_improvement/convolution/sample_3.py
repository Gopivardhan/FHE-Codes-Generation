```python
import tenseal as ts

# Initialize the CKKS context
context = ts_ckks_context(
    poly_modulus_degree=4096,
    security_level=128,
    scheme=ts.SCHEME_BFV,
    mode=ts.MODE_GALois,
    precision=60
)

# Encrypt a vector
encrypted_vector = context.encrypt([1, 2, 3])

# Perform convolution operation
encrypted_result = encrypted_vector * encrypted_vector

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the result
print(decrypted_result)
```