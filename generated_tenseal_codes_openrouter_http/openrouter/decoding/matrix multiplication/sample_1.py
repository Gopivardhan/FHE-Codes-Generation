
import tenseal as ts

context = ts.context(
    scheme=ts.SCHEME CKKS,
    poly_mods=[256, 257, 257, 257],
    plaintext_mod=257,
    plaintext_window=128,
    num_galois_tables=32,
    security=128
)

public_key = context.create_public_key()
secret_key = context.create_secret_key()

vector1 = ts.ckks_vector(context, [1, 2, 3])
vector2 = ts.ckks_vector(context, [4, 5, 6])

encrypted_vector1 = vector1.encrypt(public_key)
encrypted_vector2 = vector2.encrypt(public_key)

result = encrypted_vector1 * encrypted_vector2
decrypted_result = result.decrypt(secret_key)

print(decrypted_result)