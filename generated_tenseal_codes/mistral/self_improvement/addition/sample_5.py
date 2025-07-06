```python
import tenseal as ts

# Set the context parameters for CKKS scheme
context = ts.context(ts.SEALContext(scheme_type=ts.scheme_type.CKKS))

# Create encryption parameters and a secret key
encryptor = ts.CKKSEncryptor(context)
secret_key = ts.CKKSKeyGenerator(context).secret_key()

# Encrypt input vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = ts.ckks_vector(context, encryptor, vector1)
encrypted_vector2 = ts.ckks_vector(context, encryptor, vector2)

# Perform addition operation
encrypted_result = encrypted_vector1 + encrypted_vector2

# Decrypt the result
decryptor = ts.CKKSDecryptor(secret_key)
result = decryptor.decrypt_batch(encrypted_result)

# Print the result
print(result)
```