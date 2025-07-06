import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, [30, 40, 50], 2, device='cpu')

vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0])
vector2 = ts.ckks_vector(context, [4.0, 5.0, 6.0])

result = vector1 * vector2
result.scale()
result.decompose()

output = result.get_value()

print(output)