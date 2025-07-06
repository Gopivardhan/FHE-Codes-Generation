import tenseal as ts

context = ts.context(ts.scheme_type.CKKS, 8192, 60, 30, 10, 0, 20)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

encrypted_sum = encrypted_vector1 + encrypted_vector2

decrypted_sum = decryptor.decrypt(encrypted_sum)

print(decrypted_sum)