
import tenseal as ts

context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    plaintext_modulus=2**64,
    scale=1 << 40,
    seed=0
)

context.relinearize = False
context.rescale_inplace = False
context.generate_galois_keys()

vector1 = ts.ckks_vector(context, [1, 2, 3])
vector2 = ts.ckks_vector(context, [4, 5, 6])

encrypted_vector1 = vector1.encrypt()
encrypted_vector2 = vector2.encrypt()

result = encrypted_vector1.dot(encrypted_vector2)

decrypted_result = result.decrypt()

print(decrypted_result)