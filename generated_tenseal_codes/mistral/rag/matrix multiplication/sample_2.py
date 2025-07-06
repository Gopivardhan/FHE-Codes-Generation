import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 0, 4, [16, 14, 13, 13])
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

encrypted_matrix_a = [encryptor.encrypt(vector) for vector in [ts.ckks_vector(row) for row in matrix_a]]
encrypted_matrix_b = [encryptor.encrypt(vector) for vector in [ts.ckks_vector(row) for row in matrix_b]]

result = ts.ckks_matrix_multiplication(encrypted_matrix_a, encrypted_matrix_b)
decrypted_result = [decryptor.decrypt(vector) for vector in result]

print([[float(i) for i in vector] for vector in decrypted_result])