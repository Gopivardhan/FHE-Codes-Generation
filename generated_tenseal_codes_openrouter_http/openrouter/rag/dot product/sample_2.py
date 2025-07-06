
import tenseal as ts

# Create a CKKS context
context = ts.CKKS(
    poly_mods=[ts.PolyModulus.from_degree(2048, ts.MPIR8),
              ts.PolyModulus.from_degree(2048, ts.MPIR8),
              ts.PolyModulus.from_degree(2048, ts.MPIR8)],
    scheme=ts.SCHEME_TYPE.BFV,
    galois_size=256,
    plaintext_modulus=257,
    sec_level=128,
    mode=ts.SCHEME_TYPE.CKKS,
    eval_depth=3)

# Generate two random plaintexts
x = ts.ckks_vector([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], context)
y = ts.ckks_vector([11, 12, 13, 14, 15, 16, 17, 18, 19, 20], context)

# Encrypt the plaintexts
x_enc = context.encrypt(x)
y_enc = context.encrypt(y)

# Perform CKKS dot product
x_enc.dot_product(y_enc)

# Decrypt the result
x_dec = context.decrypt(x_enc.dot_product(y_enc))

# Print the result
print(x_dec.decrypt())
