
import tenseal as ts

context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    degree=8192,
    plaintext_modulus=257,
    modulus_bit_size=30,
    precision=30,
    security_level=128
)

context.generate_galois_keys()

plain = [1, 2, 3, 4]
encrypted = ts.ckks_vector(context, plain)
encrypted.multiply(encrypted)
decrypted = encrypted.decrypt()
print(decrypted)
