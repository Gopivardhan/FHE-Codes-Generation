import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])

encryptor = ts.CKKSEncryptor(context)

vector1 = [1, 2, 3, 4] * 1024
vector2 = [5, 6, 7, 8] * 1024

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

convolved_vectors = encrypted_vector1 * encrypted_vector2

decryptor = ts.CKKSDecryptor(context)
decryptor.decrypt_and_decompress(convolved_vectors)

print(decryptor.get_plain_text())