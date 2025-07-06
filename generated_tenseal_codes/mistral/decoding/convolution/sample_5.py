```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40])
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
encryptor = ts.CKKSEncryptor(context, public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key())

input_vector1 = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float32)
input_vector2 = np.array([5.0, 6.0, 7.0, 8.0], dtype=np.float32)

encrypted_vector1 = encryptor.encrypt(input_vector1)
encrypted_vector2 = encryptor.encrypt(input_vector2)

convolution_result = encrypted_vector1 * encrypted_vector2

decrypted_result = decryptor.decrypt(convolution_result)
print(decrypted_result.tolist()[0])
```
Note: The above code performs element-wise multiplication between two encrypted vectors, which is not exactly the same as convolution. To perform convolution using TenSEAL, you would need to pad and flip one of the vectors before performing the element-wise multiplication. Additionally, you may need to adjust the parameters of the `context` object based on your specific use case.