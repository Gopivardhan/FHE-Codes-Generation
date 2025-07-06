import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 60])

matrix_a = ts.ckks_matrix(context, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = ts.ckks_matrix(context, [[10, 11, 12], [13, 14, 15], [16, 17, 18]])

result = matrix_a @ matrix_b
result.scale()
result.round()

output = result.decrypt()