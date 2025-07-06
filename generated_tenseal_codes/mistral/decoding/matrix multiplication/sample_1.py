```python
import tenseal as ts
import numpy as np

context = ts.context(ts.SEAL_CPU, 3, 100)
context.global_scale = pow(2, 60)
context.generate_galois_keys()
context.generate_encryption_keys()

encryptor = ts.Encryptor(context, context.public_key)
evaluator = ts.Evaluator(context)
decryptor = ts.Decryptor(context, context.secret_key)

matrix_a = np.random.rand(10, 10).astype(np.float64)
matrix_b = np.random.rand(10, 10).astype(np.float64)

matrix_a_encrypted = [encryptor.encrypt(val) for val in matrix_a.flatten()]
matrix_b_encrypted = [encryptor.encrypt(val) for val in matrix_b.flatten()]

matrix_a_vector = ts.ckks_vector(context, matrix_a_encrypted)
matrix_b_vector = ts.ckks_vector(context, matrix_b_encrypted)

matrix_a_multiplier = ts.Plaintext(context, matrix_a)
matrix_b_multiplier = ts.Plaintext(context, matrix_b)

matrix_c_vector = matrix_a_vector * matrix_b_multiplier
matrix_c_vector = matrix_c_vector * matrix_b_vector

matrix_c_decrypted = np.array([decryptor.decrypt(ctxt) for ctxt in matrix_c_vector.get_value()])
matrix_c_decrypted = matrix_c_decrypted.reshape(10, 10)

print(matrix_c_decrypted)
```