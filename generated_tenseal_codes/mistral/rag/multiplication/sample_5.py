import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 20)
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector_1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector_2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector_1 = encryptor.encrypt(vector_1)
encrypted_vector_2 = encryptor.encrypt(vector_2)

result = encrypted_vector_1 * encrypted_vector_2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result.scale)
print(decrypted_result.get_value())