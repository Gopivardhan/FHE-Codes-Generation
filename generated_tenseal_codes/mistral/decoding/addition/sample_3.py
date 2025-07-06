```python
import tenseal as ts

context = ts.context(ts.SEAL_CPU, ts.CKKS_Scheme)
context.generate_galois_keys()
context.generate_inplace_encoding_context(poly_modulus_degree=8192, coeff_modulus_bits=60)

encryptor = ts.Encryptor(context)
decryptor = ts.Decryptor(context)

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = ts.ckks_vector(context, encryptor, vector1)
encrypted_vector2 = ts.ckks_vector(context, encryptor, vector2)

encrypted_vector_sum = encrypted_vector1 + encrypted_vector2

decrypted_vector_sum = decryptor.decrypt_batch(encrypted_vector_sum)

print(decrypted_vector_sum)
```