
import tenseal as ts

# Context setup
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    security_level=128,
    mode=ts.MODE.GALois,
    degree=30,
    modulus_bits=8192,
    plaintext_modulus=257,
    min_poly_modulus_degree=30,
    coeff_modulus=[257, 257, 257, 257, 257],
    precision=30,
    basecase_level=30,
    scale=2**40
)

# Key generation
public_key = context.create_public_key()
secret_key = context.create_secret_key()

# Encrypting input vectors
x = ts.ckks_vector(context, [1, 2, 3])
y = ts.ckks_vector(context, [4, 5, 6])

# Encrypting public key
public_key_enc = public_key.encrypt(context)

# Encrypting input vectors
x_enc = x.encrypt(public_key_enc)
y_enc = y.encrypt(public_key_enc)

# Perform CKKS operation
result_enc = x_enc.dot(y_enc)

# Decrypt the result
result_dec = result_enc.decrypt(secret_key)

# Print the result
print(result_dec.decrypt(secret_key))