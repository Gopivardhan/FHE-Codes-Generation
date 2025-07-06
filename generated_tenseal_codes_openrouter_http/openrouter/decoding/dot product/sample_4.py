
import tenseal as ts
context = ts.context(scheme=ts.Scheme.FHE, poly_modulus_degree=[4096, 8192], coeff_mod_bit_sizes=[30, 30], scale=2**30)
context.generate_galois_keys()
context.generate_public_eval_key()
context.generate_private_eval_key()
context.generate_gaussian_noise(stddev=3.2)

a = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0, 5.0])
b = ts.ckks_vector(context, [6.0, 7.0, 8.0, 9.0, 10.0])

a_encrypted = a.encrypt()
b_encrypted = b.encrypt()

dot_product = a_encrypted * b_encrypted
dot_product_decrypted = dot_product.decrypt()

print(dot_product_decrypted.get_plain())
