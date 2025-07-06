```python
import tenseal as ts

# Context setup
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40])
context.global_scale = 2**30
context.generate_galois_keys()
context.generate_evaluation_keys()

# Encrypted vectors
encryptor = ts.Encryptor(context, context.public_key)
vector1 = [i for i in range(1024)]
vector2 = [j for j in range(1, 1025)]
enc_vector1 = ts.ckks_vector(context, vector1)
enc_vector1.encrypt(encryptor)
enc_vector2 = ts.ckks_vector(context, vector2)
enc_vector2.encrypt(encryptor)

# Matrix multiplication
matrix1 = ts.CkksMatrix(context, [enc_vector1 for _ in range(1024)])
matrix2 = ts.CkksMatrix(context, [enc_vector2 for _ in range(1024)])
product = matrix1 * matrix2

# Decrypt and print the result
decryptor = ts.Decryptor(context, context.secret_key)
decrypted_result = product.decrypt(decryptor)
print(decrypted_result.scaled_down(context.global_scale))
```