```python
import tenseal as ts

# Generate keys
context = ts.CKKS(
    poly_mod_count=8192,
    poly_mod_degree=8192,
    sec_param=10,
    scheme=ts.SCHEME_BFV,
    noise_stddev=1.5,
    deallocation=true
)
context.global_scale = 4096
context.keygen()
public_key = context.public_key
secret_key = context.secret_key

# Encrypting
x = ts.ckks_vector(context, [1, 2, 3, 4])
y = ts.ckks_vector(context, [5, 6, 7, 8])

# Perform operation
result = ts.ckks_vector(context)
result += x * y

# Decrypting
decrypted_result = secret_key.decrypt(result)

print(decrypted_result)
```