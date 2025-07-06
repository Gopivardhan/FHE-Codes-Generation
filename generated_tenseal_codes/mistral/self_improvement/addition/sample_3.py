```python
import tenseal as ts

# Set the context parameters for CKKS scheme
context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 0, 10)

# Generate a keypair
key_pair = context.key_generator().create_key_pair()

# Encrypt two vectors
vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]
encrypted_vector1 = ts.ckks_vector(context, key_pair.public_key(), vector1)
encrypted_vector2 = ts.ckks_vector(context, key_pair.public_key(), vector2)

# Perform addition operation
result = encrypted_vector1 + encrypted_vector2

# Decrypt the result
decrypted_result = result.decrypt(key_pair.secret_key())

# Print the result
print(decrypted_result.get_value())
```