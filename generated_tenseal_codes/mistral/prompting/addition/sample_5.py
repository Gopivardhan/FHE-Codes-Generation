import tenseal as ts

context = ts.context(128, 10, 30, ts.SEAL_PLAINTEXT_MODULUS_BIT_COUNT_128)
encoder = ts.CKKSEncoder(context)

vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0])
vector2 = ts.ckks_vector(context, [4.0, 5.0, 6.0])

vector1.encrypt(encoder)
vector2.encrypt(encoder)

result = vector1 + vector2

result.decrypt(encoder)

print(result.scale)
print(result.get_plain_text())