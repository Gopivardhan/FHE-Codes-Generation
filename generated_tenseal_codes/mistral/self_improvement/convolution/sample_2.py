```python
import tenseal as ts

# Create context with specified parameters
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 60, 60], scale=2**30)

# Create encryption keys
encryptor = context.encryptor()
decryptor = context.decryptor()

# Encrypt input vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector2 = ts.ckks_vector(context, vector2)

# Perform convolution operation
result = encrypted_vector1 * encrypted_vector2

# Decrypt and print the result
decrypted_result = decryptor.decrypt_batch(result)[0]
print(decrypted_result)
```
Note: This code assumes that the vectors have the same length and that the result of the convolution can be represented within the scale and precision of the CKKS scheme. You may need to adjust the parameters of the context and the scale of the inputs depending on your specific use case.