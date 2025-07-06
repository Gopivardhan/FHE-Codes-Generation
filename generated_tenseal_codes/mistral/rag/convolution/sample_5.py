import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 0, 10, 2)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [1, 2, 3, 4, 5]
vector2 = [6, 7, 8, 9, 10]

enc_vector1 = encryptor.encrypt(vector1)
enc_vector2 = encryptor.encrypt(vector2)

result = enc_vector1 * enc_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result)