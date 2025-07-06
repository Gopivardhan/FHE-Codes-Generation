```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, plain_modulus=2**32)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

matrix1 = np.random.rand(1024, 1024).astype(np.float32)
matrix2 = np.random.rand(1024, 1024).astype(np.float32)

enc_matrix1 = ts.ckks_matrix(matrix1, encryptor)
enc_matrix2 = ts.ckks_matrix(matrix2, encryptor)

product = enc_matrix1 @ enc_matrix2
decrypted_product = decryptor.decrypt_batch(product)

print(np.array(decrypted_product))
```
Note: This code snippet assumes that the matrices are square and have a size of 1024x1024. You may need to adjust the parameters according to your specific requirements. Additionally, the CKKS scheme supports approximate arithmetic, so the decrypted result may not be exactly equal to the plaintext product due to the noise growth during homomorphic operations.