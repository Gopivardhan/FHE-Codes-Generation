
import tenseal as ts

# Create CKKS context
context = ts.context(
    scheme=ts.SCHEME_TYPE.CKKS,
    poly_modulus_degree=8192,
    security=128,
    mode=ts.SCHEME_TYPE.HE Standard,
)

# Generate public key and secret key
public_key = context.keygen()
secret_key = public_key.secret_key()

# Create CKKS encryptor
encryptor = ts.ckks_vector(
    context,
    public_key,
)

# Create CKKS decryptor
decryptor = ts.ckks_vector(
    context,
    secret_key,
)

# Encrypt a value
encrypted_value = encryptor.encrypt([1, 2, 3])

# Perform CKKS addition
encrypted_value += encryptor.encrypt([4, 5, 6])

# Decrypt the result
decrypted_value = decryptor.decrypt(encrypted_value)

# Print the result
print(decrypted_value)
