import tenseal as ts

context = ts.context(ts.SEAL_CPU, 8192, 60)
keygen = ts.CKKSKeyGenerator(context)
encoder = ts.CKKSEncoder(context)

public_key = keygen.public_key()
secret_key = keygen.secret_key()
relin_keys = [keygen.create_relin_keys()]

vector1 = [1.0, 2.0, 3.0, 4.0]
vector2 = [5.0, 6.0, 7.0, 8.0]

encrypted_vector1 = encoder.encode(vector1, public_key)
encrypted_vector2 = encoder.encode(vector2, public_key)

encrypted_vector1 = ts.ckks_vector(encrypted_vector1, public_key)
encrypted_vector2 = ts.ckks_vector(encrypted_vector2, public_key)

encrypted_sum = encrypted_vector1 + encrypted_vector2

decrypted_sum = encoder.decode(encrypted_sum, secret_key)

print(decrypted_sum)