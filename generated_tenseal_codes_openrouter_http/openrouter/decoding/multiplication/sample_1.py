import tenseal as ts

context = ts.context(scheme=ts.scheme_ckks, poly_mod_degree=256, scale=2**23, precision=30)
context.generate_galois_keys()
context.generate_gaussian_parameters()

vector1 = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vector2 = ts.ckks_vector(context, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

encrypted_result = vector1 * vector2

decrypted_result = encrypted_result.decrypt()

print(decrypted_result)