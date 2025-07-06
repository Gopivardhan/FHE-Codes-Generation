```python
import tenseal as ts

# Set the parameters for the context
context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 0, 10, 1, 2)

# Generate encryption keys
encryptor = context.encryptor()
decryptor = context.decryptor()

# Encrypt vectors
vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]
encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

# Perform multiplication
product = encrypted_vector1 * encrypted_vector2

# Decrypt and print the result
result = decryptor.decrypt(product)
print(result)
```
Note: The result will be a vector of length 5, where each element is the product of the corresponding elements in the input vectors. The decryption process may result in some noise due to the homomorphic encryption scheme, so the output values may not be exactly equal to the expected results.