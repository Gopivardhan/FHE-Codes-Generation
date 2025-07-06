
import tenseal as ts

# Create CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=[4096, 4096],
    coeff_modulus=[8192, 8192, 8192],
    scale=2**23
)

# Create CKKS context
context.generate_galois_keys()
context.generate_zk_keys()

# Encrypt data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encrypted_data = [ts.ckks_vector.from_py(x, context) for x in data]

# Perform CKKS convolution
encrypted_convolved = ts.ckks_vector.zero_like(encrypted_data[0])
for i in range(len(encrypted_data)):
    for j in range(len(encrypted_data)):
        encrypted_convolved += encrypted_data[i] * encrypted_data[j]

# Decrypt
decrypted_convolved = [x.to_py() for x in encrypted_convolved]

print(decrypted_convolved)