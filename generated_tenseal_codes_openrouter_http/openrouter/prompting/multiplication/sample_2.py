import tenseal as ts

context = ts.context(
    scale=2**14,
    poly_modulus_degree=4096,
    mode=ts.ContextMode.GFWHM
)

context.generate_galois_keys()
context.generate_pck_keys()

x = ts.ckks_vector(context, [1.0, 2.0, 3.0, 4.0, 5.0])
y = ts.ckks_vector(context, [2.0, 3.0, 4.0, 5.0, 6.0])

encrypted_x = x.encrypt()
encrypted_y = y.encrypt()

encrypted_result = encrypted_x * encrypted_y

decrypted_result = encrypted_result.decrypt()

print(decrypted_result)