```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])
context.global_scale = pow(2, 60)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector1 = np.random.rand(1024).astype(np.float32)
vector2 = np.random.rand(1024).astype(np.float32)

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

dot_product = encrypted_vector1 * encrypted_vector2
result = decryptor.decrypt(dot_product)

print(result.item())
```