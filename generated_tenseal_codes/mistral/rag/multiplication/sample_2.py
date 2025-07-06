import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, ts.coeff_modulus_builder(2**60))
context.global_scale = 2**60
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [i+1j*j for i in range(1024) for j in range(8)]
vector2 = [i+1j*j for i in range(1024) for j in range(8)]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

product = encrypted_vector1 * encrypted_vector2
decrypted_product = decryptor.decrypt(product)

print(decrypted_product)