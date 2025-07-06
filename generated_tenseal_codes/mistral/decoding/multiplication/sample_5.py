```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, plain_modulus=2**32)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector1 = ts.ckks_vector(context, np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32))
vector2 = ts.ckks_vector(context, np.array([5.0, 6.0, 7.0, 8.0], dtype=np.float32))

encrypted_result = vector1 * vector2
decrypted_result = decryptor.decrypt_batch(encrypted_result)

print(decrypted_result)
```