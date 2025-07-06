```python
import tenseal as ts

# Initialize the CKKS context
context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_mods=[ts.PolyModulus.BFV(2048, 256, 257),
              ts.PolyModulus.BFV(2048, 256, 257)],
    sec_level=ts.SCHEME_TYPE.SC128,
    scheme_type=ts.SCHEME_TYPE.CKKS
)

# Generate keys
context.generate_galois_keys()
public_key = context.public_key
secret_key = context.secret_key

# Encrypt vectors
vector1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
vector2 = [4, 3, 2, 1, 6, 5, 4, 3, 2, 1, 8, 7, 6, 5, 4, 3]
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform operation
result = ts.ckks_vector(context, [i * j for i, j in zip(encrypted_vector1, encrypted_vector2)])

# Decrypt
decrypted_result = ts.ckks_vector(context, result).decrypt(secret_key)

# Print result
print(decrypted_result)
```