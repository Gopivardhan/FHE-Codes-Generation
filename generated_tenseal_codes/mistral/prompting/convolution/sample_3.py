import tenseal as ts

context = ts.context(128, 60, 30, ckks=True, scale=2**30)
encoder = ts.CKKSEncoder(context)

x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [6.0, 7.0, 8.0]

x_vec = ts.ckks_vector(context, encoder.encode(x))
y_vec = ts.ckks_vector(context, encoder.encode(y))

result_vec = ts.convolve(x_vec, y_vec)

decoded_result = encoder.decode(result_vec.decrypt())