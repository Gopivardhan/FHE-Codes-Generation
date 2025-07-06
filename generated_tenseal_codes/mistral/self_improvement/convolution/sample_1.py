```python
import tenseal as ts

# Set the parameters for the CKKS scheme
context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 0, 20)

# Create encryption parameters using the context
encryptor = ts.CKKSEncryptor(context)

# Encrypt input vectors
vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]
encrypted_vector1 = ts.ckks_vector(encryptor, vector1)
encrypted_vector2 = ts.ckks_vector(encryptor, vector2)

# Perform convolution operation
result = encrypted_vector1 * encrypted_vector2

# Decrypt the result
decryptor = ts.CKKSDecryptor(context)
decryptor.set_secret_key(encryptor.secret_key())
decrypted_result = decryptor.decrypt_batch(result)[0]

# Print the result
print(decrypted_result)
```
Note: This code assumes that the input vectors are of length 5 and that the convolution operation is performed element-wise. In practice, the length of the vectors and the type of convolution operation (e.g., circular or linear) may vary depending on the specific use case.