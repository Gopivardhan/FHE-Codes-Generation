```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, coeff_mod_bit_sizes=[60, 40, 40])
context.global_scale = 2**30
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector1 = ts.ckks_vector(context, np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32))
vector2 = ts.ckks_vector(context, np.array([5.0, 6.0, 7.0, 8.0], dtype=np.float32))

encrypted_sum = vector1 + vector2
decrypted_sum = decryptor.decrypt_batch(encrypted_sum)

print(np.array(decrypted_sum, dtype=np.float32))
```