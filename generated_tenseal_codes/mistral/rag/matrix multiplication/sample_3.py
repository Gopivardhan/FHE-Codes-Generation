import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 2, device="cpu")
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matrix1_encrypted = [encryptor.encrypt(vector) for vector in map(ts.ckks_vector, matrix1)]
matrix2_encrypted = [encryptor.encrypt(vector) for vector in map(ts.ckks_vector, matrix2)]

result = ts.ckks_matrix_mul(matrix1_encrypted, matrix2_encrypted)

result_decrypted = [decryptor.decrypt(vector) for vector in result]
print([vector.get_value() for vector in result_decrypted])