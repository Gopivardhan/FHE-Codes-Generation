
import tenseal as ts

# Context setup
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=4096,
    security_level=ts.SECURITY_LEVEL.SL_S128,
    mode=ts.MODE.GALOIS
)

# Key generation
context.generate_galois_keys()

# Encryption
x = ts.ckks_vector(context, [1, 2, 3])
y = ts.ckks_vector(context, [4, 5, 6])

# CKKS operation
encrypted_product = ts.ckks_vector(context)
encrypted_product.add(x).add(y)

# Decryption
result = encrypted_product.decrypt()

# Print the result
print(result)
