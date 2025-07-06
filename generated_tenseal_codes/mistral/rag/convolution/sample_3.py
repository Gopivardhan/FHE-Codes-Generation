import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, ts.coeff_modulus_builder(2**60))
context.global_scale = 2**30
context.generate_galois_keys()
context.generate_inverse_keys()
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context, context.get_inverse_keys())

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

x_encrypted = encryptor.encrypt(x)
y_encrypted = encryptor.encrypt(y)

result = ts.convolve(x_encrypted, y_encrypted)
result_decrypted = decryptor.decrypt(result)

print(result_decrypted)