import tenseal as ts
context = ts.context(scheme=ts.scheme.fhe, poly_mod_params=ts.modulus_params(2**14), plaintext_modulus=2**14, scale=2**20, precision=30)
context.generate_galois_keys()
context.generate_public_eval_key()
context.generate_secret_key()
public_key = context.secret_key()
coeff_modulus = [2**14, 2**14, 2**14, 2**14, 2**14]
plaintext = ts.ckks_vector(context, coeff_modulus, [1, 2, 3, 4, 5])
ciphertext = plaintext.encrypt(public_key)
coeff_modulus = [2**14, 2**14, 2**14, 2**14, 2**14]
plaintext2 = ts.ckks_vector(context, coeff_modulus, [1, 2, 3, 4, 5])
ciphertext2 = plaintext2.encrypt(public_key)
result = ciphertext.convolve(ciphertext2, public_key)
decrypted = result.decrypt(public_key)
print(decrypted)