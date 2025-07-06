```python
import tenseal as ts

# Set the parameters for the context
context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 0, 10, 10)

# Create encryption keys
encryptor = context.encryptor()
decryptor = context.decryptor()

# Encrypt input vectors
input_vector_1 = [1.0, 2.0, 3.0, 4.0, 5.0]
input_vector_2 = [6.0, 7.0, 8.0, 9.0, 10.0]
encrypted_vector_1 = ts.ckks_vector(context, input_vector_1)
encrypted_vector_2 = ts.ckks_vector(context, input_vector_2)
encryptor.encrypt(encrypted_vector_1)
encryptor.encrypt(encrypted_vector_2)

# Perform convolution operation
result = encrypted_vector_1 * encrypted_vector_2
context.convolve(result, len(input_vector_1), len(input_vector_2))

# Decrypt and print the result
decryptor.decrypt(result)
print(result.get_value())
```
Note: The above code assumes that the input vectors are of the same length and that the result of the convolution operation fits within the size of the CKKS plaintext modulus. You may need to adjust the parameters of the context and/or the input vectors to ensure that this is the case.