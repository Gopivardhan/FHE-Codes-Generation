
import tenseal as ts

context = ts.context(scheme=ts.schemeCKKS, poly_mod_degree=4096, scale=2**23)
context.generate_galois_keys()
context.generate_powers_of_two()

vector1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vector2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

result = vector1 + vector2

decrypted_result = result.decrypt()
print(decrypted_result)
