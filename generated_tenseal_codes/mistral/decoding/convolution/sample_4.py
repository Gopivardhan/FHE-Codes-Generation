```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, plain_modulus=2**32)
encryptor = ts.Encryptor(context)
decryptor = ts.Decryptor(context)

vector1 = ts.ckks_vector(context, np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float32))
vector2 = ts.ckks_vector(context, np.array([6.0, 7.0, 8.0, 9.0, 10.0], dtype=np.float32))

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

result = encrypted_vector1 * encrypted_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result.get_value())
```