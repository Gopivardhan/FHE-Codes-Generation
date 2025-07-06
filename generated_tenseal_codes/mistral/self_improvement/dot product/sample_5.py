```python
import tenseal as ts

# Create context with desired parameters
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])

# Create key generator and generate keys
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
secret_key = key_generator.secret_key()

# Encrypt input vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = ts.ckks_vector(context, public_key, vector1)
encrypted_vector2 = ts.ckks_vector(context, public_key, vector2)

# Perform dot product operation
result = encrypted_vector1 * encrypted_vector2

# Decrypt and print the result
decrypted_result = result.decrypt(secret_key)
print(decrypted_result)
```
Note: The poly\_modulus\_degree and coeff\_modulus\_bit\_sizes parameters should be chosen according to the desired level of security and precision for your specific use case. The example above uses parameters that are suitable for demonstration purposes but may not be sufficient for production use.