```python
import tenseal as ts

# Create context with desired parameters
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 60])

# Create encryption parameters
encryptor = ts.CKKSEncryptor(context)

# Generate random vectors for matrix multiplication
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
matrix_a_encrypted = [encryptor.encrypt(i) for sublist in matrix_a for i in sublist]
matrix_b_encrypted = [encryptor.encrypt(i) for sublist in matrix_b for i in sublist]

# Perform matrix multiplication using CKKS
matrix_a_ckks = ts.CKKSMatrix(context, matrix_a_encrypted)
matrix_b_ckks = ts.CKKSMatrix(context, matrix_b_encrypted)
result_ckks = matrix_a_ckks @ matrix_b_ckks

# Decrypt the result and print it
decryptor = ts.CKKSDecryptor(context)
result_decrypted = [decryptor.decrypt(i) for i in result_ckks.get_vector()]
print(result_decrypted)
```