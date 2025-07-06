import tenseal as ts

context = ts.context(128, 60, [30, 40, 50], ckks=True)

matrix_a = ts.ckks_matrix(3, 4, context)
matrix_b = ts.ckks_matrix(4, 5, context)

result = ts.ckks_matrix(3, 5, context)

matrix_a.fill_uniform(context)
matrix_b.fill_uniform(context)

ts.matrix_mul(result, matrix_a, matrix_b)

result.scale(2**-100)

result.round()

result.flush_cache()