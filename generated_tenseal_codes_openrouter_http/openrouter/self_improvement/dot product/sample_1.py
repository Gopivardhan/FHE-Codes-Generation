```python
import tenseal as ts

# Initialize CKKS context
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_mod_count=128,
    poly_mod_degree=8192,
    plaintext_modulus=256,
    evaluation_key_modulus=256,
    relin_key_modulus=256,
    min_polynomial_degree=512,
    max_poly_memory=1024,
    security_level=128,
    deallocate_on_exit=True
)

# Create a CKKS key pair
public_key, secret_key = context.generate_pairing_keypair()

# Encrypt the inputs
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
x_enc = context.encrypt(x, secret_key)
y_enc = context.encrypt(y, secret_key)

# Perform the operation
result_enc = context.dot_product(x_enc, y_enc)

# Decrypt the result
result = context.decrypt(result_enc)

# Print the result
print(result)
```