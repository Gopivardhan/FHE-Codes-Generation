import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

vec1 = [1, 2, 3, 4, 5]
vec2 = [5, 4, 3, 2, 1]

encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

dot_product = encrypted_vec1 * encrypted_vec2
decrypted_dot_product = dot_product.decrypt()

print(decrypted_dot_product)
