```python
import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40])
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
secret_key = key_generator.secret_key()
encryptor = ts.CKKSEncryptor(context, public_key)
decryptor = ts.CKKSDecryptor(context, secret_key)

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

product = encrypted_vector1 * encrypted_vector2
decrypted_product = decryptor.decrypt(product)

print(decrypted_product)
```