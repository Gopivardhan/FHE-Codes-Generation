import tenseal as ts

context = ts.context(scheme=ts.scheme.fhe, poly_mod_degree=4096, plaintext_modulus=65537, scale=2**30)
context.global_scale = 2**30
context.set_relin_degree(12)

params = context.params
params.scale = 2**30

plain_vector = ts.ckks_vector(context, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
encrypted_vector = plain_vector.encrypt()

encrypted_vector1 = ts.ckks_vector(context, [2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
encrypted_vector1 = encrypted_vector1.encrypt()

result = encrypted_vector.dot(encrypted_vector1)
decrypted_result = result.decrypt()

print(decrypted_result)