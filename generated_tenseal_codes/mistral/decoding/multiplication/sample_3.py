```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 2, 0, 40)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.SealEncryptor(context, key_generator.public_key())
decryptor = ts.SealDecryptor(context, key_generator.secret_key())

vector1 = [i + 1j * j for i, j in enumerate(range(10))]
plain_text1 = ts.Plaintext(vector1)
cipher_text1 = encryptor.encrypt(plain_text1)

vector2 = [i + 1j * (10 - j) for i, j in enumerate(range(10))]
plain_text2 = ts.Plaintext(vector2)
cipher_text2 = encryptor.encrypt(plain_text2)

cipher_text_product = cipher_text1 * cipher_text2
decrypted_result = decryptor.decrypt(cipher_text_product)
result = decrypted_result.get_vector()
print(result)
```