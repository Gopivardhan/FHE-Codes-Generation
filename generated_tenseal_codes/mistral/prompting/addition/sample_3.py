import tenseal as ts

context = ts.context(128, 10, 30, ts.PACKED)

vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0])
vector2 = ts.ckks_vector(context, [4.0, 5.0, 6.0])

result = vector1 + vector2

decrypted_result = result.decrypt()