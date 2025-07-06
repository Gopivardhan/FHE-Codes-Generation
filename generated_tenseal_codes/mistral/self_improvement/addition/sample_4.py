```python
import tenseal as ts

context = ts.context(ts.SEAL_CPU, 3, 60)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key())
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key())

vector1 = [1.2, 2.3, 3.4, 4.5, 5.6]
vector2 = [6.7, 7.8, 8.9, 9.10, 10.11]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

encrypted_sum = encrypted_vector1 + encrypted_vector2

decrypted_sum = decryptor.decrypt(encrypted_sum)

print(decrypted_sum)
```