```
import tenseal as ts

# Initialize CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096, 
    scale=2**30, 
    precision=30, 
    coeff_mod_bit_sizes=[30, 30]
)

# Encrypt numbers
plaintext1 = ts.ckks_vector(context, [1.0, 0.0, 0.0])
plaintext2 = ts.ckks_vector(context, [0.0, 1.0, 0.0])

# Perform multiplication
encrypted_result = plaintext1 * plaintext2

# Decrypt the result
decrypted_result = encrypted_result.decrypt()

# Print the result
print(decrypted_result)