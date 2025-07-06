import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, ts.coeff_modulus_builder(2**60))
encoder = ts.CKKSEncoder(context)
key_generator = ts.CKKSKeyGenerator(context)
public_key = key_generator.public_key()
secret_key = key_generator.secret_key()
encryptor = ts.CKKSEncryptor(context, public_key)
decryptor = ts.CKKSDecryptor(context, secret_key)

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = encryptor.encrypt(encoder.encode(vector1))
encrypted_vector2 = encryptor.encrypt(encoder.encode(vector2))

product = encrypted_vector1 * encrypted_vector2
decrypted_product = decryptor.decrypt(encoder.decode(product))

print(decrypted_product.tolist()[:4])