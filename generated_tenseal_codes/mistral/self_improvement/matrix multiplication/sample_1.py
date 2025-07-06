```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 60])
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matrix_a_encrypted = [encryptor.encrypt(vector) for vector in [matrix_a[i] for i in range(len(matrix_a))]]
matrix_b_encrypted = [encryptor.encrypt(vector) for vector in [matrix_b[i] for i in range(len(matrix_b))]]

result = ts.ckks_matrix_multiply(matrix_a_encrypted, matrix_b_encrypted)
result_decrypted = [decryptor.decrypt(vector) for vector in result]

print(result_decrypted)
```
Note: This code assumes that the input matrices `matrix_a` and `matrix_b` have the same number of rows and that the number of columns of `matrix_a` is equal to the number of rows of `matrix_b`. The code also assumes that the entries of the matrices are integers that can be encrypted using the specified modulus bit sizes. If the entries are floating-point numbers, they will need to be scaled and rounded to integers before encryption.