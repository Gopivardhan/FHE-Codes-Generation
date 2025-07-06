
import tenseal as ts

context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_mod_count=4096,
    poly_mod_degree=8192,
    plaintext_mod_count=256,
    plaintext_mod_prime=257,
    plaintext_mod_size=8,
    scale=1 << 40
)

context.relinearize = True
context.rescale_inplace = False
context.key_gen()

public_key = context.public_key
secret_key = context.secret_key

vector1 = ts.ckks_vector(context, [1, 2, 3])
vector2 = ts.ckks_vector(context, [4, 5, 6])

encrypted_vector1 = public_key.encrypt(vector1)
encrypted_vector2 = public_key.encrypt(vector2)

encrypted_sum = encrypted_vector1 + encrypted_vector2

decrypted_sum = secret_key.decrypt(encrypted_sum)

print(decrypted_sum)
