import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 60, 60], scale=2**30)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

convolved_vectors = ts.convolve(encrypted_vector1, encrypted_vector2)
decrypted_result = decryptor.decrypt(convolved_vectors)

print(decrypted_result)