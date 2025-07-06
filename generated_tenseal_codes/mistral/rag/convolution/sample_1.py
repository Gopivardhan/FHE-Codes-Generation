import tenseal as ts

context = ts.context(ts.SCHEME_CKKS, 8192, 60, 30, 10, 0, [16, 32, 64, 128])
encoder = ts.CKKSEncoder(context)

x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]

x_vec = ts.ckks_vector(context, encoder.encode(x))
y_vec = ts.ckks_vector(context, encoder.encode(y))

convolution = x_vec * y_vec
decrypted = convolution.decrypt()

print(encoder.decode(decrypted))