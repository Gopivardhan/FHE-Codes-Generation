import tenseal as ts

context = ts.context(
    ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    coeff_mod_bit_sizes=[60, 40, 40, 60]
)
context.global_scale = 2**40
context.generate_galois_keys()

vec1 = [1, 2, 3]
vec2 = [4, 5, 6]

encrypted_vec1 = ts.ckks_vector(context, vec1)
encrypted_vec2 = ts.ckks_vector(context, vec2)

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]

encrypted_matrix1 = ts.ckks_matrix(context, matrix1)
encrypted_matrix2 = ts.ckks_matrix(context, matrix2)

encrypted_result = encrypted_matrix1 @ encrypted_matrix2

decrypted_result = encrypted_result.decrypt().values

print(decrypted_result)
