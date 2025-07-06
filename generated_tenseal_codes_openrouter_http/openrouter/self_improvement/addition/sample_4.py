```
import tenseal as ts

# Initialize CKKS context
context = ts.CKKSContext(
    poly_modulus_degree=4096,
    scale=2**15,
    precision=25,
    coeff_mod_bit_sizes=[30, 62]
)

# Create a CKKS context
context.gen_keys()

# Create a CKKS vector
a = ts.ckks_vector(context, [1, 2, 3, 4, 5])
b = ts.ckks_vector(context, [5, 4, 3, 2, 1])

# Perform operation
result = a + b

# Decrypt
decrypted_result = result.decrypt()

# Print the result
print(decrypted_result)