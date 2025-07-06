```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, scale=2**30)
key_generator = ts.CryptoContext(context)
public_key = key_generator.public_key()
encryptor = ts.Encryptor(public_key, context)
decryptor = ts.Decryptor(key_generator.secret_key(), context)

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

dot_product = encrypted_vector1 * encrypted_vector2
decrypted_result = decryptor.decrypt(dot_product)

print(decrypted_result.get_value())
```