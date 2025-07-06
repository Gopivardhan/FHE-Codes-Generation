import tenseal as ts

context = ts.context(ts.SEAL_CKKS_SCHEME, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40])

encryptor = ts.Encryptor(context)
decryptor = ts.Decryptor(context)

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

product = encrypted_vector1 * encrypted_vector2
decrypted_product = decryptor.decrypt(product)

print(decrypted_product.scale)
print(decrypted_product.value)