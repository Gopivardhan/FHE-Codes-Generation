import tenseal as ts

context = ts.context(ts.scheme_type.CKKS, poly_modulus_degree=8192, coeff_modulus_bits=60, scale=2**30, scale_factor=2**10)
key_generator = ts.key_generator(context)
encryptor = ts.encryptor(context, key_generator.public_key())
decryptor = ts.decryptor(context, key_generator.secret_key())

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

dot_product = encrypted_vector1 * encrypted_vector2
decrypted_dot_product = decryptor.decrypt(dot_product)

print(decrypted_dot_product)