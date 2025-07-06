import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, 8192, 60, 30, 10, 2, 0, False)
key_generator = ts.CKKSKeyGenerator(context)
encryptor = ts.CKKSEncryptor(context, key_generator.public_key)
decryptor = ts.CKKSDecryptor(context, key_generator.secret_key)

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

ctxt1 = encryptor.encrypt(vector1)
ctxt2 = encryptor.encrypt(vector2)

ctxt_sum = ctxt1 + ctxt2

decrypted_sum = decryptor.decrypt(ctxt_sum)

print(decrypted_sum)