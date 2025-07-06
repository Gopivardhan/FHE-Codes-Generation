import tenseal as ts

context = ts.context(ts.SEAL_CKKS, 8192, 60, 30)
keygen = ts.CKKSEncryptor(context)
encoder = ts.CKKSEncoder(context)
decryptor = ts.CKKSDecryptor(keygen.secret_key())

vector1 = [1.0, 2.0, 3.0, 4.0, 5.0]
vector2 = [6.0, 7.0, 8.0, 9.0, 10.0]

enc_vector1 = encoder.encode(vector1, scale=2**30)
enc_vector2 = encoder.encode(vector2, scale=2**30)

ctxt_vector1 = keygen.encrypt(enc_vector1)
ctxt_vector2 = keygen.encrypt(enc_vector2)

dot_product = ctxt_vector1 * ctxt_vector2
result = decryptor.decrypt(dot_product)
decoded_result = encoder.decode(result)

print(decoded_result[0])