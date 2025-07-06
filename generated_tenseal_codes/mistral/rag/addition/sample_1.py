import tenseal as ts

context = ts.context(ts.SEAL_CKKS_SCHEME, 8192, 60, 30)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key())
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key())

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

encrypted_sum = encrypted_vector1 + encrypted_vector2

decrypted_sum = decryptor.decrypt(encrypted_sum)

print(decrypted_sum)