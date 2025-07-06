
import tenseal as ts

context = ts.context(
    scale=2**14,
    poly_mod_degree=256,
    precision=64,
    noise_stddev=3.2e-5
)

context.set_party_vector()

enc_a = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
enc_b = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

context.eval_set_global_scale(2**14)

conv = ts.ckks_vector(context)
for i in range(8):
    for j in range(8):
        if i == j:
            conv[i] += enc_a[j]

decrypted = conv.decrypt()

print(decrypted)