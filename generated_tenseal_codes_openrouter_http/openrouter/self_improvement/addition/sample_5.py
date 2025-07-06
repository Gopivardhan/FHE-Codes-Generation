```python
import tenseal as ts

# Initialize the CKKS context
context = ts_ckks(
    scheme=ts.scheme.ckks,
    poly_modulus_degree=8192,
    poly_modulus=ts.poly_modulus.ckks_baseprime_4096,
    coeff_modulus=[ts.coeff_modulus.ckks_baseprime(20, 3)],
    precision=30,
    security_level=ts.SecurityLevel.SECURITY_LEVEL_TYPE.STANDARD
)

# Generate a random vector
plain = [1, 2, 3, 4, 5]

# Encrypt the vector
encrypted = context.encrypt(plain)

# Add two encrypted vectors
encrypted_add = encrypted + encrypted

# Decrypt the result
decrypted = encrypted_add.decrypt()

# Print the result
print(decrypted)
```