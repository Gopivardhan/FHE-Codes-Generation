
import tenseal as ts

context = ts.context(ts.context.CKKS, poly_modulus_degree=4096, scale=2**22, precision=22)
context.generate_galois_keys()
context.generate_public_key()
context.generate_secret_key()

a = ts.ckks_vector.from_py(context, [1, 2, 3, 4])
b = ts.ckks_vector.from_py(context, [5, 6, 7, 8])

encrypted_a = a.encrypt()
encrypted_b = b.encrypt()

c = encrypted_a * encrypted_b

decrypted_c = c.decrypt()

print(decrypted_c.to_py())
