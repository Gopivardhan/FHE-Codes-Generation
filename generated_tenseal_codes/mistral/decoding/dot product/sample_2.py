```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SEAL_DEFAULT_PARAMETERS)
encoder = ts.CKKSEncoder(context)
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
encryptor = ts.CKKSEncryptor(public_key)
decryptor = ts.CKKSDecryptor(key_generator.secret_key())
scale = pow(2, 30)

vector1 = np.random.rand(1000).astype(np.float32)
vector2 = np.random.rand(1000).astype(np.float32)

encrypted_vector1 = encoder.encode(vector1, scale)
encrypted_vector1 = encryptor.encrypt(encrypted_vector1)

encrypted_vector2 = encoder.encode(vector2, scale)
encrypted_vector2 = encryptor.encrypt(encrypted_vector2)

dot_product = ts.ckks_vector.dot(encrypted_vector1, encrypted_vector2)
decrypted_dot_product = decryptor.decrypt(dot_product)
decrypted_dot_product = decrypted_dot_product[0] / scale

print(decrypted_dot_product)
```