```python
import tenseal as ts

# Create context with certain parameters
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40], plain_modulus=2**32)

# Generate encryption keys
encryptor = context.generate_encryptor()
decryptor = context.generate_decryptor()

# Encrypt input vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = ts.ckks_vector(context, vector1)
encrypted_vector1.encrypt(encryptor)
encrypted_vector2 = ts.ckks_vector(context, vector2)
encrypted_vector2.encrypt(encryptor)

# Perform dot product operation
result = encrypted_vector1 * encrypted_vector2

# Decrypt and print the result
decrypted_result = result.decrypt(decryptor)
print(decrypted_result)
```
Note: The code above assumes that the input vectors are of the same size and contain floating-point numbers. The plain\_modulus parameter should be set to a power of 2 that is greater than or equal to the maximum absolute value of the input vectors. The coefficients of the ciphertext polynomials will be rounded to the nearest integer during encryption, so the results may not be exact.