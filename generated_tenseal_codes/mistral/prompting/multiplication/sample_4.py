import tenseal as ts

context = ts.context(128, 60, [30, 40, 50], 10)

vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0, 5.0])
vector2 = ts.ckks_vector(context, [6.0, 7.0, 8.0, 9.0, 10.0])

result = vector1 * vector2
result.scale()
result.decompose()
result.rescale()

decrypted_result = result.decrypt()