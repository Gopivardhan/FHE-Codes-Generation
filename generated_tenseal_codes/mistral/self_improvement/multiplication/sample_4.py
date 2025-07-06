```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 10, 2)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [i for i in range(1024)]
vector2 = [j*2 for j in range(1024)]

plain_vector1 = ts.ckks_vector(vector1)
plain_vector2 = ts.ckks_vector(vector2)

cipher_vector1 = encryptor.encrypt(plain_vector1)
cipher_vector2 = encryptor.encrypt(plain_vector2)

result = cipher_vector1 * cipher_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result.scale * sum(vector1[i] * vector2[i] for i in range(1024)) / decrypted_result.size)
```
Note: This code assumes that the vectors are of size 1024 and that the scaling factor used during encryption is 2^60. The result is then scaled down by the scaling factor and the size of the vector to obtain the actual result.