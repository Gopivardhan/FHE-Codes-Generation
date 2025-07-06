import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2 ** 40

v1 = [2.0, 3.0, 4.0]
v2 = [5.0, 6.0, 7.0]

enc1 = ts.ckks_vector(context, v1)
enc2 = ts.ckks_vector(context, v2)

result = enc1 * enc2
print(result.decrypt())
