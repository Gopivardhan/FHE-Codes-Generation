import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 60, 60])
input1 = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0])
input2 = ts.ckks_vector(context, [5.0, 6.0, 7.0, 8.0])
result = ts.convolve(input1, input2)
result.scale()
result.store()
print(result.get_value())