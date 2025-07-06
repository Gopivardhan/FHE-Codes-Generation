
import tenseal as ts

# Create CKKS context
context = ts.context(
    ts.dpn_ops=ts.DPNOps(),
    poly_mod_ops=ts.PolyModOps(),
    scale=2**30,
    precision_bits=30,
    party_size=2
)

# Generate public and secret keys
public_key, secret_key = context.keygen()

# Create two CKKS vectors
vec1 = ts.ckks_vector(context, [1, 2, 3, 4, 5])
vec2 = ts.ckks_vector(context, [6, 7, 8, 9, 10])

# Encrypt CKKS vectors
encrypted_vec1 = vec1.encrypt(public_key)
encrypted_vec2 = vec2.encrypt(public_key)

# Perform CKKS addition
result = encrypted_vec1 + encrypted_vec2

# Decrypt the result
decrypted_result = result.decrypt(secret_key)

print(decrypted_result)