```python
import tenseal as ts

# Create context with required parameters
context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 10, ts.coeff_modulus.BFV)

# Generate encryption keys
encryptor = context.encryptor()
decryptor = context.decryptor()

# Encrypt input vectors
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
This code will perform CKKS multiplication of two encrypted vectors using TenSEAL library in Python. Note that the result might not be accurate due to the noise introduced during the encryption and multiplication processes. To obtain an accurate result, the vectors should be scaled down appropriately before encryption.