import tenseal as ts

context = ts.context(ts.SCHEME_TYPE.CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40])

vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0])
vector2 = ts.ckks_vector(context, [5.0, 6.0, 7.0, 8.0])

result = vector1 * vector2
result.scale()
result.rescale_to_next_interval()

dot_product = result[0]
dot_product.decrypt()