```
import tenseal as ts

# Create CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**(-40),
    precision=11,
    coeff_mod_bits=40
)

# Generate public and secret keys
public_key, secret_key = context.key_gen()

# Create CKKS vectors
a = ts.ckks_vector(context, [1, 2, 3, 4])
b = ts.ckks_vector(context, [5, 6, 7, 8])

# Encrypt vectors
a_enc = a.encrypt(public_key)
b_enc = b.encrypt(public_key)

# Perform CKKS matrix multiplication
c_enc = a_enc * b_enc

# Decrypt result
c_dec = c_enc.decrypt(secret_key)

# Print result
print(c_dec)
```