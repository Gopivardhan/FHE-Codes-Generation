import tenseal as ts

context = ts.context(128, 10, 30, ts.coeff_modulus.POW2_128_BYTE, False)
vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0])
vector2 = ts.ckks_vector(context, [5.0, 6.0, 7.0, 8.0])
result = vector1 + vector2
result.scale()
decrypted_result = result.decrypt()