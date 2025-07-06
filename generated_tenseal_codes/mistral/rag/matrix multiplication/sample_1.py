import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, ts.COEFF_MOD_MAX)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matrix1_encrypted = [encryptor.encrypt(vector) for vector in [ts.ckks_vector(row) for row in matrix1]]
matrix2_encrypted = [encryptor.encrypt(vector) for vector in [ts.ckks_vector(row) for row in matrix2]]

result = [ts.ckks_vector([0] * context.dimension) for _ in range(len(matrix1))]

for i, row1 in enumerate(matrix1_encrypted):
    for j, row2 in enumerate(matrix2_encrypted):
        result[i] += row1 * row2

result_decrypted = [decryptor.decrypt(vector) for vector in result]

print([[float(i) for i in vector] for vector in result_decrypted])