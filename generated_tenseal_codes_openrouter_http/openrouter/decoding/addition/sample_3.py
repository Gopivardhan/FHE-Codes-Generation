import tenseal as ts

context = ts.context(scheme=ts.Scheme.CKKS, poly_modulus_degree=4096, coeff_mod_bit_sizes=[30, 30, 30, 30, 30])
context.generate_galois_keys()
context.generate_polynomial_modulus()

a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [2, 3, 4, 5, 6])

a += b
a.decrypt()

print(a)