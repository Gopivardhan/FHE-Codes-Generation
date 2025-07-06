import tenseal as ts
context = ts.context(scheme=ts.scheme_ckks, poly_mod_degree=4096, scale=2**30)
context.global_scale = 2**30
context.set-party-view(0)
a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [6, 7, 8, 9, 10])
a_encrypted = a.encrypt()
b_encrypted = b.encrypt()
result = a_encrypted.dot(b_encrypted)
decrypted_result = result.decrypt()
print(decrypted_result)