```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, plain_modulus=2**32)
encoder = ts.CKKSEncoder(context)
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
relin_keys = [key_generator.create_relin_keys() for _ in range(10)]
encryptor = ts.CKKSEncryptor(public_key, encoder)
decryptor = ts.CKKSDecryptor(key_generator.secret_key(), encoder)

matrix_a = np.random.rand(1024, 1024).astype(np.float32)
matrix_b = np.random.rand(1024, 1024).astype(np.float32)

matrix_a_encrypted = ts.ckks_matrix(encryptor, matrix_a)
matrix_b_encrypted = ts.ckks_matrix(encryptor, matrix_b)

product = matrix_a_encrypted @ matrix_b_encrypted
product_decrypted = decryptor.decrypt_batch(product, relin_keys)

print(product_decrypted)
```