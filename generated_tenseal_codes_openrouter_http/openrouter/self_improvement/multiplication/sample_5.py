```python
import tenseal as ts

# Generate key pair
context = ts_ckks_context(
    scheme=ts.scheme_type.CKKS,
    poly_modulus_degree=4096,
    poly_mod_count=6,
    plain_mod_count=6,
    scaling_mod_count=6,
    precision=30
)

keygen = context.keygen()
public_key = keygen.public_key
secret_key = keygen.secret_key

# Encrypt plaintext
plaintext = ts.ckks_vector(context, [1, 2, 3, 4, 5])
encrypted = public_key.encrypt(plaintext)

# Perform operation (in this case, multiplication)
encrypted_result = encrypted * encrypted

# Decrypt result
decrypted_result = secret_key.decrypt(encrypted_result)

# Print result
print(decrypted_result)
```