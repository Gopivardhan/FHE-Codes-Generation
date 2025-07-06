import tenseal as ts

context = ts.context(ts.scheme_type.CKKS, 8192, 60, 30, 10, 2, 0, 10)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector1 = [i + 0.5 for i in range(10)]
vector2 = [i - 0.5 for i in range(10)]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

result = encrypted_vector1 + encrypted_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result)