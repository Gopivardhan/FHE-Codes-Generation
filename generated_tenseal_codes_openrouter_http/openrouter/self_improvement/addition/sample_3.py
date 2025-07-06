import tenseal as ts

context = ts.context(
    scale=2**14, 
    poly_modulus_degree=4096, 
    mode=ts.ContextMode.GF2^2
)

context.global_scale = 2**14

a = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = ts.ckks_vector(context, [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

a.add_(b)
c = a.decrypt()

print(c)