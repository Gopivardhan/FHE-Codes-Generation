```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40])
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

matrix_a = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]
matrix_b = [[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]]

matrix_a_encrypted = [encryptor.encrypt(vector) for vector in [matrix_a[i] for i in range(len(matrix_a))]]
matrix_b_encrypted = [encryptor.encrypt(vector) for vector in [matrix_b[i] for i in range(len(matrix_b))]]

result = ts.ckks_matrix_multiply(matrix_a_encrypted, matrix_b_encrypted)
result_decrypted = [decryptor.decrypt(vector) for vector in result]

print(result_decrypted)
```