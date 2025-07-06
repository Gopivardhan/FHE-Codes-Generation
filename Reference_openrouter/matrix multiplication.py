import numpy as np
import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2 ** 40

matrix = np.array([[1.0, 2.0], [3.0, 4.0]])
vector = [5.0, 6.0]

enc_vector = ts.ckks_vector(context, vector)
result = [np.dot(row, enc_vector.decrypt()) for row in matrix]
print(result)
