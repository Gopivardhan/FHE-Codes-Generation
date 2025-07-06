```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 20)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector_1 = [i+1j*i for i in range(1024)]
vector_2 = [i-1j*i for i in range(1024)]

encrypted_vector_1 = encryptor.encrypt(vector_1)
encrypted_vector_2 = encryptor.encrypt(vector_2)

product = encrypted_vector_1 * encrypted_vector_2
decrypted_product = decryptor.decrypt(product)

print(decrypted_product)
```