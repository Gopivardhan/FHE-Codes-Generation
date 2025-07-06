import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, ts.coeff_modulus_t(64, 120, 50, 40))
context.global_scale = 2**30
context.generate_galois_keys()
context.generate_inverse_keys()

encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

matrix_a_encrypted = [encryptor.encrypt(vector) for vector in [matrix_a[i] for i in range(len(matrix_a))] ]
matrix_b_encrypted = [encryptor.encrypt(vector) for vector in [matrix_b[i] for i in range(len(matrix_b))] ]

matrix_c_encrypted = [ts.ckks_matrix_multiply(matrix_a_encrypted[i], matrix_b_encrypted) for i in range(len(matrix_a))]

matrix_c_decrypted = [decryptor.decrypt(matrix_c_encrypted[i]) for i in range(len(matrix_c_encrypted))]

print(matrix_c_decrypted)