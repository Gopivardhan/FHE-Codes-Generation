import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 0, 10)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

dot_product = encrypted_vector1 * encrypted_vector2
decrypted_result = decryptor.decrypt(dot_product)

print(decrypted_result)