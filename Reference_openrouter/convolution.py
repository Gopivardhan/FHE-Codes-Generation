import tenseal as ts
import numpy as np

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.generate_galois_keys()
context.global_scale = 2 ** 40

signal = [1.0, 2.0, 3.0, 4.0]
kernel = [0.25, 0.5, 0.25]

enc_signal = ts.ckks_vector(context, signal)
conv_result = np.convolve(enc_signal.decrypt(), kernel, mode="valid")
print(conv_result)
