```python
import tenseal as ts

# Context setup
context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])
context.generate_galois_keys()
context.generate_inverse_keys()

# Encrypted vectors
vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]
encryptor = ts.Encryptor(context, ts.SEAL_ENCRYPTION_SCHEME.CKKS)
encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

# CKKS convolution
convolution_poly_size = len(vector1) + len(vector2) - 1
result = ts.CkksConvolution(context, encrypted_vector1, encrypted_vector2, convolution_poly_size)

# Decrypt and print the result
decryptor = ts.Decryptor(context)
decrypted_result = decryptor.decrypt(result)
print(decrypted_result)
```