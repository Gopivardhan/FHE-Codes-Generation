```python
import tenseal as ts

# Create a CKKS context
context = ts.context(
    scheme=ts.scheme.CKKS,
    poly_mods=[ts.MPPolynomialModulusSetting(
        degree=256,
        modulus_bits=4096,
        precision=30,
        base=257,
        coefficient_modulus=1 << 20,
        quotient_degree=16,
        embedding_degree=1024,
        min_poly_modulus_degree=256,
        max_poly_modulus_degree=65536,
    )
),
    plaintext_modulus=257,
    num_gallop_steps=10,
    relin_keys=2,
    security_level=ts.SecurityLevel.tiny,
)

# Create a CKKS encoder
encoder = context.encoder()

# Create a plaintext
plaintext = [1, 2, 3, 4]

# Encrypt the plaintext
encrypted = ts.ckks_vector(context, plaintext)

# Perform CKKS operation
encrypted = encrypted * encrypted

# Decrypt the result
decrypted = encrypted.decrypt()

# Print the result
print(decrypted)
```