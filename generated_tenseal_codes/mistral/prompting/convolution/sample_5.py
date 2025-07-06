import tenseal as ts

context = ts.context(128, 60, 30, ts.coeff_modulus.BFVrns, c = 60)
encoder = ts.CKKSEncoder(context)

x = [1.0, 2.0, 3.0, 4.0]
y = [5.0, 6.0, 7.0]

x_vector = ts.ckks_vector(context, encoder.encode(x))
y_vector = ts.ckks_vector(context, encoder.encode(y))

result = ts.convolve(x_vector, y_vector)
decoded_result = encoder.decode(result.decrypt())

print(decoded_result)