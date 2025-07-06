```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 0, 10)
encryptor = ts.SealEncryptor(context)
decryptor = ts.SealDecryptor(context)

vector1 = [i + 1j * i for i in range(1024)]
vector2 = [i + 1j * (i + 1) for i in range(1024)]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

product = encrypted_vector1 * encrypted_vector2
decrypted_product = decryptor.decrypt(product)

print(decrypted_product)
```