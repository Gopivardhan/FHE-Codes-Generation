import tenseal as ts
context = ts.context(ts.SCHEME_TYPE.CKKS, 12, 128)
context.global_scale = 2**20
ckks_vector1 = ts.ckks_vector(context, [1.0, 2.0, 3.0])
ckks_vector2 = ts.ckks_vector(context, [4.0, 5.0, 6.0])
encrypted_vector1 = ckks_vector1.encrypt()
encrypted_vector2 = ckks_vector2.encrypt()
result = encrypted_vector1 + encrypted_vector2
decrypted_result = result.decrypt()
print(decrypted_result)