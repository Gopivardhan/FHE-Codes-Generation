
import tenseal as ts

context = ts.context(
    scheme=ts.scheme.CKKS,
    poly_mod_degree=8192,
    poly_mod_count=256,
    plaintext_mod_count=256,
    plaintext_mod_size=28,
    sec_level=128,
    seed=0
)

context.generate_galois_keys()

x = ts.ckks_vector(context, [1, 2, 3])
y = ts.ckks_vector(context, [4, 5, 6])

encrypted_x = x.encrypt()
encrypted_y = y.encrypt()

dot_product = encrypted_x.dot(encrypted_y)

decrypted_dot_product = dot_product.decrypt()

print(decrypted_dot_product)