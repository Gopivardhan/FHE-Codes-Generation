```python
import tenseal as ts

# Set the polynomial degree and other parameters for the CKKS scheme
context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, coeff_modulus=[ts.CoeffModulus(60, 40) for _ in range(10)], plain_modulus=128)

# Create encryptor and decryptor objects
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

# Encrypt input vectors
vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]
encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

# Perform matrix multiplication
result = encrypted_vector1 * encrypted_vector2

# Decrypt the result and print it
decrypted_result = decryptor.decrypt(result)
print(decrypted_result)
```
Note: The above code assumes that the vectors are of the same length and that the matrix multiplication is performed element-wise. If you want to perform a standard matrix multiplication between two matrices, you will need to modify the code accordingly.