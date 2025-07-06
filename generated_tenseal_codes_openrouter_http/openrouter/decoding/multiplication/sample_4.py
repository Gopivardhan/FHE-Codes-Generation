
import tenseal as ts

context = ts.context(scheme=ts.scheme.CKKS, poly_mod_degree=4096, coeff_mod_bit_sizes=[30, 30, 30, 30, 30])
context.generate_galois_keys()
context.generate_public_key()

a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [6, 7, 8, 9, 10])

result = a * b

decrypted_result = result.decrypt()

print(decrypted_result)