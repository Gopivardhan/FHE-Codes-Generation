import tenseal as ts

context = ts.context(128, 10, 30, ts.coeff_modulus.CoeffModulus_BFVrns(60))
encoder = ts.CKKSEncoder(context)

vector_1 = ts.ckks_vector(context, encoder.encode([1.0, 2.0, 3.0, 4.0]))
vector_2 = ts.ckks_vector(context, encoder.encode([5.0, 6.0, 7.0, 8.0]))

result = vector_1 * vector_2
decoded_result = result.decrypt()[0]

print(decoded_result)