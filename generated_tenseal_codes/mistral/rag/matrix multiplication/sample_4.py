import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])

encryptor = ts.CKKSEncryptor(context)

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matrix_a_encrypted = [encryptor.encrypt(vector) for vector in [ts.ckks_vector(a_row) for a_row in matrix_a]]
matrix_b_encrypted = [encryptor.encrypt(vector) for vector in [ts.ckks_vector(b_row) for b_row in matrix_b]]

result = [ts.ckks_matrix(context) for _ in range(3)]

for i in range(3):
    for j in range(3):
        tmp_vector = ts.ckks_vector(context, [0]*context.slot_count)
        for k in range(3):
            tmp_vector += matrix_a_encrypted[i] * matrix_b_encrypted[k]
        result[i].scale_and_add_inplace(tmp_vector, [float(j)]*context.slot_count)

decryptor = ts.CKKSDecryptor(context)

decrypted_result = [[decryptor.decrypt(row)[0] for row in result[i]] for i in range(3)]

print(decrypted_result)