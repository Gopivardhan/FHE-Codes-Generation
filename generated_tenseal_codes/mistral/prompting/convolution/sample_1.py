import tenseal as ts

context = ts.context(seal_level=50, poly_modulus_degree=8192, coeff_modulus_bits=60)

input1 = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0, 5.0])
input2 = ts.ckks_vector(context, [6.0, 7.0, 8.0, 9.0, 10.0])

result = ts.convolve(input1, input2)

output = result.scale() \
    .rescale_to_nearest_int() \
    .decode()

print(output)