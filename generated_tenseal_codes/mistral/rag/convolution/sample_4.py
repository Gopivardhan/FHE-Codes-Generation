import tenseal as ts

context = ts.context(ts.scheme_type.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, scale=2**30, batch_size=1024)
key_generator = ts.CryptoContext(context).generate_keys()
encryptor = ts.Encryptor(context, key_generator.public_key)
decryptor = ts.Decryptor(context, key_generator.secret_key)

vector_a = [1.0, 2.0, 3.0, 4.0] * (1024 // 4)
vector_b = [5.0, 6.0, 7.0, 8.0] * (1024 // 4)

encrypted_a = encryptor.encrypt(ts.ckks_vector(vector_a))
encrypted_b = encryptor.encrypt(ts.ckks_vector(vector_b))

convolution = encrypted_a * encrypted_b
result = decryptor.decrypt(convolution)

print(result.scale() * result.get_value()[:4])