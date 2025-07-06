```
import tenseal as ts

# Initialize CKKS context
context = ts.context(
    ts.lwe_public_key_bits=2048,
    ts.lwe_secret_key_bits=2048,
    poly_modulus_degree=4096,
    scale=2**40,
    mode=ts.ContextMode.GPU
)

# Create CKKS vector
plaintext = ts.ckks_vector(context, 10)
plaintext.values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create CKKS vector
other = ts.ckks_vector(context, 10)
other.values = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Encrypt
encrypted = plaintext.encrypt()
other_encrypted = other.encrypt()

# Perform convolution
convolved = ts.ckks_vector(context, 100)
for i in range(10):
    for j in range(10):
        convolved.values[i*10+j] = encrypted.values[i] * other_encrypted.values[j]

# Decrypt
decrypted = convolved.decrypt()

# Print the result
print(decrypted.values)