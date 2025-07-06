
import tenseal as ts

# Create a CKKS context
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    security=128,
    mode=ts.MODE.GALGAL,
    max_depth=3,
    coeff_mod_bit_count=60,
    num_gal=4,
    scale=1 << 30,
    min_poly_size=0
)

# Generate secret key and public key
context.generate_galois_keys()
secret_key = context.secret_key
public_key = context.public_key

# Create a plaintext vector
x = ts.ckks_vector(context, [1, 2, 3, 4])

# Encrypt the plaintext vector
encrypted_x = x.encrypt(secret_key)

# Create another plaintext vector
y = ts.ckks_vector(context, [4, 3, 2, 1])

# Encrypt the second plaintext vector
encrypted_y = y.encrypt(secret_key)

# Perform CKKS convolution
encrypted_result = encrypted_x.convolution(encrypted_y)

# Decrypt the result
decrypted_result = encrypted_result.decrypt(secret_key)

# Print the decrypted result
print(decrypted_result.to_array())
