import tenseal as ts
context = ts.context(ts.cpu_context(), poly_modulus_degree=4096, coeff_modulus=[2**61-1, 2**61-1], scale=1.0)
context.global_scale = 2**61
context.set_schedule()
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = [ts.ckks_vector.from_py(row, context) for row in data]
encrypted_data = [x.encrypt(context) for x in data]
result = ts.ckks_vector.zero_like(data[0])
for i in range(len(data)):
    for j in range(len(data[0])):
        for k in range(len(data[0])):
            result[j] += encrypted_data[i][k] * encrypted_data[k][j]
decrypted_result = result.decrypt()
print(decrypted_result.to_py())