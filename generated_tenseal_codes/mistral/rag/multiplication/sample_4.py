import tenseal as ts

context = ts.context(ts.SEAL_CKKS_PACKED, 8192, 60, 30, ts.coeff_modulus_128_bits())
encryptor = ts.CKKSEncryptor(context)
decryptor = ts.CKKSDecryptor(context)

vector1 = [i for i in range(1024)]
vector2 = [j*2 for j in range(1024)]

encrypted_vector1 = encryptor.encrypt(vector1)
encrypted_vector2 = encryptor.encrypt(vector2)

result = encrypted_vector1 * encrypted_vector2
decrypted_result = decryptor.decrypt(result)

print(decrypted_result.tolist()[:10])