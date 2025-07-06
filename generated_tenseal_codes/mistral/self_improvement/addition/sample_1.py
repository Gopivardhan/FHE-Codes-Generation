```python
import tenseal as ts

# Create context with certain parameters
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])

# Create key generator and generate keys
key_generator = ts.CKKSKeyGenerator(context)
key_generator.create_public_key()
key_generator.create_secret_key()
relin_keys = [key_generator.create_relin_keys() for _ in range(5)]
key_generator.create_galois_keys()

# Encrypt vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector1.encrypt(key_generator.public_key)
encrypted_vector2 = ts.ckks_vector(context, vector2)
encrypted_vector2.encrypt(key_generator.public_key)

# Perform addition
encrypted_result = encrypted_vector1 + encrypted_vector2

# Decrypt and print the result
decrypted_result = encrypted_result.decrypt(key_generator.secret_key)
print(decrypted_result.get_plain_text())
```