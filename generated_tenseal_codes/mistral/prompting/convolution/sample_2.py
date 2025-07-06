import tenseal as ts

context = ts.context(scheme='CKKS', poly_modulus_degree=8192, coeff_modulus_bit_sizes=[60, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40, 40], scale=2**20)

input_vector = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0])
kernel = ts.ckks_vector(context, [0.5, 0.5])

input_vector.rescale()
kernel.rescale()

output_vector = ts.convolve(input_vector, kernel)
output_vector.rescale()

result = output_vector.decrypt()