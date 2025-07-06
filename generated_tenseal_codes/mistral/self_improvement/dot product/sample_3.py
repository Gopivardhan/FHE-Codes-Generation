```python
import tenseal as ts

# Create context with required parameters
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])

# Generate keys
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
secret_key = key_generator.secret_key()

# Encrypt vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = ts.ckks_vector(context, public_key, vector1)
encrypted_vector2 = ts.ckks_vector(context, public_key, vector2)

# Perform dot product
dot_product = encrypted_vector1 * encrypted_vector2

# Decrypt and print result
decrypted_result = dot_product.decrypt(secret_key)
print(decrypted_result)
```