import tenseal as ts

context = ts.context(scheme=ts.Scheme.fhe,
                    poly_modulus_degree=[4096, 4096],
                    mode=ts.ContextMode.gauss_beaver,
                    precision=30)

context.generate_galois_keys()
context.generate_powers_of_two()

a = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0])
b = ts.ckks_vector(context, [5.0, 6.0, 7.0, 8.0])

a.encrypt()
b.encrypt()

result = a + b
result.decrypt()

print(result)