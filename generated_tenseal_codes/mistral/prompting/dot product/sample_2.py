import tenseal as ts

context = ts.context(128, 60, 30)
encoder = ts.CKKSEncoder(context)

vector1 = ts.ckks_vector(context, encoder.encode([1.0, 2.0, 3.0, 4.0, 5.0]))
vector2 = ts.ckks_vector(context, encoder.encode([6.0, 7.0, 8.0, 9.0, 10.0]))

result = vector1 * vector2
decoded_result = encoder.decode(result.scale()[0])

print(decoded_result)