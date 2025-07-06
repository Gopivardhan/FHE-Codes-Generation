```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])
context.global_scale = pow(2, 60)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

matrix_a = np.random.rand(1024, 1024).astype(np.float32)
matrix_b = np.random.rand(1024, 1024).astype(np.float32)

matrix_a_encrypted = ts.ckks_matrix(matrix_a, encryptor)
matrix_b_encrypted = ts.ckks_matrix(matrix_b, encryptor)

product = matrix_a_encrypted @ matrix_b_encrypted
decrypted_result = decryptor.decrypt_batch(product)

print(decrypted_result)
```
This code creates a CKKS context with the specified parameters, generates encryption and decryption keys, encrypts two randomly generated matrices, performs matrix multiplication using the CKKS scheme, decrypts the result, and prints it. Note that the resulting decrypted matrix is a list of float32 values.